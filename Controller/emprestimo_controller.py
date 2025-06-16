from Model import usuario_model, livro_model, emprestimo_model

def realizar_emprestimo(usuario_id, livro_id):
    # Regra 1: Verificar se o usuário existe
    usuario = usuario_model.buscar_usuario_por_matricula(usuario_id)
    if not usuario:
        print("Usuário não encontrado.")
        return False

    # Regra 2: Verificar se o livro existe
    livro = livro_model.buscar_livro_por_isbn(livro_id)
    if not livro:
        print("Livro não encontrado.")
        return False

    # Regra 3: Verificar se o livro tem exemplares disponíveis
    quantidade_disponivel = livro[4]  # posição 4 = quantidade_disponivel
    if quantidade_disponivel <= 0:
        print("Livro sem exemplares disponíveis.")
        return False

    # Regra 4: Verificar se o usuário já tem 3 empréstimos ativos
    emprestimos_ativos = emprestimo_model.listar_emprestimos_ativos_por_usuario(usuario_id)
    if len(emprestimos_ativos) >= 3:
        print("O usuário já atingiu o limite de 3 empréstimos.")
        return False

    # Tudo certo, realizar o empréstimo
    emprestimo_model.registrar_emprestimo(usuario_id, livro_id)

    # Atualizar a quantidade de exemplares disponíveis
    livro_model.atualizar_quantidade(livro_id, quantidade_disponivel - 1)

    print("Empréstimo realizado com sucesso.")
    return True
