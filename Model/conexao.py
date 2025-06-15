import sqlite3
import os

# Caminho do arquivo do banco de dados
CAMINHO_BANCO = os.path.join(os.path.dirname(__file__), '..', 'Dados', 'biblioteca.db')

def conectar():
    """Abrindo a conexão com o banco SQLite."""
    conexao = sqlite3.connect(CAMINHO_BANCO)
    return conexao