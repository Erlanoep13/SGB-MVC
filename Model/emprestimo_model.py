from Model.conexao import conectar
from datetime import datetime, timedelta

# Função para registrar um novo empréstimo
def registrar_emprestimo(usuario_id, livro_id):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        data_emprestimo = datetime.now().date()
        data_prevista = data_emprestimo + timedelta(days=7)

        cursor.execute("""
            INSERT INTO emprestimos (usuario_id, livro_id, data_emprestimo, data_prevista, status)
            VALUES (?, ?, ?, ?, ?)
        """, (usuario_id, livro_id, data_emprestimo.isoformat(), data_prevista.isoformat(), 'ativo'))

        conexao.commit()
        print("Empréstimo registrado com sucesso.")
    except Exception as e:
        print(f"Erro ao registrar empréstimo: {e}")
    finally:
        conexao.close()

# Função para listar empréstimos ativos de um usuário
def listar_emprestimos_ativos_por_usuario(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id, livro_id, data_emprestimo, data_prevista
        FROM emprestimos
        WHERE usuario_id = ? AND status = 'ativo'
    """, (usuario_id,))
    emprestimos = cursor.fetchall()
    conexao.close()
    return emprestimos

# Função para marcar a devolução de um livro
def registrar_devolucao(emprestimo_id):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        # Obter data prevista
        cursor.execute("""
            SELECT data_prevista FROM emprestimos WHERE id = ?
        """, (emprestimo_id,))
        resultado = cursor.fetchone()
        if not resultado:
            print("Empréstimo não encontrado.")
            return

        data_prevista = datetime.strptime(resultado[0], "%Y-%m-%d").date()
        data_devolucao = datetime.now().date()

        # Determina o status final
        if data_devolucao > data_prevista:
            status_final = 'atrasado'
        else:
            status_final = 'devolvido'

        cursor.execute("""
            UPDATE emprestimos
            SET data_devolucao = ?, status = ?
            WHERE id = ?
        """, (data_devolucao.isoformat(), status_final, emprestimo_id))

        conexao.commit()
        print(f"Devolução registrada. Status: {status_final}")
    except Exception as e:
        print(f"Erro ao registrar devolução: {e}")
    finally:
        conexao.close()

# Função para listar todos os empréstimos ativos
def listar_emprestimos_ativos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT usuario_id, livro_id, data_emprestimo, data_prevista
        FROM emprestimos
        WHERE status = 'ativo'
    """)
    emprestimos = cursor.fetchall()
    conexao.close()
    return emprestimos

# Função para listar usuários com devoluções atrasadas
def listar_usuarios_atrasados():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT usuario_id, livro_id, data_prevista
        FROM emprestimos
        WHERE status = 'atrasado'
    """)
    atrasados = cursor.fetchall()
    conexao.close()
    return atrasados