from Model import livro_model

def cadastrar_livro(isbn, titulo, autor, ano, quantidade):
    sucesso = livro_model.inserir_livro(isbn, titulo, autor, ano, quantidade)
    if sucesso:
        return True, "Livro cadastrado com sucesso!"
    else:
        return False, "Erro ao cadastrar livro."

def listar_livros():
    return livro_model.listar_livros()

def buscar_livro_por_isbn(isbn):
    return livro_model.buscar_livro(isbn)

def atualizar_livro(isbn, titulo, autor, ano, quantidade):
    return livro_model.atualizar_livro(isbn, titulo, autor, ano, quantidade)

def deletar_livro(isbn):
    return livro_model.deletar_livro(isbn)