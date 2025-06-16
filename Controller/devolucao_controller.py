from Model import emprestimo_model, livro_model

def realizar_devolucao(matricula, isbn):
    # Busca todos os empréstimos ativos do usuário
    emprestimos_ativos = emprestimo_model.listar_emprestimos_ativos_por_usuario(matricula)

    # Filtra o empréstimo ativo desse livro específico
    emprestimo_encontrado = next((e for e in emprestimos_ativos if e[1] == isbn), None)  # e[1] = livro_id (ISBN)

    if not emprestimo_encontrado:
        return False  # Nenhum empréstimo ativo desse livro para esse usuário

    emprestimo_id = emprestimo_encontrado[0]  # Coluna 0 = ID do empréstimo
    sucesso = emprestimo_model.registrar_devolucao(emprestimo_id)

    if sucesso:
        livro = livro_model.buscar_livro_por_isbn(isbn)
        if livro:
            nova_quantidade = livro[4] + 1  # Posição 4 = quantidade disponível
            livro_model.atualizar_quantidade(isbn, nova_quantidade)

    return sucesso
