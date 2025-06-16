from Model import emprestimo_model, livro_model

def realizar_devolucao(emprestimo_id):
    # Primeiro, buscar os dados do empréstimo
    emprestimos_ativos = emprestimo_model.listar_emprestimos_ativos()

    emprestimo = next((e for e in emprestimos_ativos if e[0] == emprestimo_id), None)
    if not emprestimo:
        print("Empréstimo não encontrado ou já devolvido.")
        return False

    livro_id = emprestimo[1]  # Coluna 1 é o livro_id

    # Registrar devolução (a model já atualiza o status e a data de devolução)
    emprestimo_model.registrar_devolucao(emprestimo_id)

    # Atualizar quantidade de exemplares disponíveis
    livro = livro_model.buscar_livro_por_isbn(livro_id)
    if livro:
        nova_quantidade = livro[4] + 1  # Posição 4 = quantidade_disponivel
        livro_model.atualizar_quantidade(livro_id, nova_quantidade)

    print("Devolução realizada com sucesso.")
    return True
