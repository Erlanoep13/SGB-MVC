from Model.conexao import conectar

# Função para inserir um novo usuário
def inserir_usuario(matricula, nome, curso):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO usuarios (matricula, nome, curso)
            VALUES (?, ?, ?)
        """, (matricula, nome, curso))
        conexao.commit()
        print("Usuário cadastrado com sucesso.")
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        conexao.close()

# Função para listar todos os usuários
def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT matricula, nome, curso FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

# Função para buscar um usuário por matrícula
def buscar_usuario_por_matricula(matricula):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT matricula, nome, curso FROM usuarios WHERE matricula = ?", (matricula,))
    usuario = cursor.fetchone()
    conexao.close()
    return usuario