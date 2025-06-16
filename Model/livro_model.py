from Model.conexao import conectar

def inserir_livro(isbn, titulo, autor, ano_publicacao, quantidade_disponivel):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO livros (isbn, titulo, autor, ano_publicacao, quantidade_disponivel)
            VALUES (?, ?, ?, ?, ?)
        """, (isbn, titulo, autor, ano_publicacao, quantidade_disponivel))
        conexao.commit()
        return True  # Se der tudo certo
    except Exception as e:
        print(f"Erro ao inserir livro: {e}")
        return False  # Se der algum erro (ex: ISBN duplicado)
    finally:
        conexao.close()

# Função para listar todos os livros
def listar_livros():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT isbn, titulo, autor, ano_publicacao, quantidade_disponivel FROM livros")
    livros = cursor.fetchall()
    conexao.close()
    return livros

# Função para buscar um livro por ISBN
def buscar_livro_por_isbn(isbn):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT isbn, titulo, autor, ano_publicacao, quantidade_disponivel FROM livros WHERE isbn = ?", (isbn,))
    livro = cursor.fetchone()
    conexao.close()
    return livro

# Função para atualizar a quantidade disponível de exemplares (usado no empréstimo e devolução)
def atualizar_quantidade(isbn, nova_quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE livros
            SET quantidade_disponivel = ?
            WHERE isbn = ?
        """, (nova_quantidade, isbn))
        conexao.commit()
    except Exception as e:
        print(f"Erro ao atualizar quantidade: {e}")
    finally:
        conexao.close()