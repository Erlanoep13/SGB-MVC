import tkinter as tk
from View import tela_principal
from View.FuncAdmin import (
    tela_cadastro_livro,
    tela_cadastro_usuario,
    tela_emprestimo_admin,
    tela_devolucao_admin,
    tela_relatorios
)

def abrir_menu_admin():
    janela = tk.Tk()
    janela.title("Menu - Administrador")
    janela.geometry("300x350")

    tk.Label(janela, text="Menu do Administrador", font=("Arial", 14)).pack(pady=10)

    tk.Button(janela, text="Cadastrar Livro", width=25,
              command=lambda: chamar_funcao(janela, tela_cadastro_livro.abrir_tela_cadastro_livro)).pack(pady=5)

    tk.Button(janela, text="Cadastrar Usuário", width=25,
              command=lambda: chamar_funcao(janela, tela_cadastro_usuario.abrir_tela_cadastro_usuario)).pack(pady=5)

    tk.Button(janela, text="Realizar Empréstimo", width=25,
              command=lambda: chamar_funcao(janela, tela_emprestimo_admin.abrir_tela_emprestimo_admin)).pack(pady=5)

    tk.Button(janela, text="Realizar Devolução", width=25,
              command=lambda: chamar_funcao(janela, tela_devolucao_admin.abrir_tela_devolucao_admin)).pack(pady=5)

    tk.Button(janela, text="Relatórios", width=25,
              command=lambda: chamar_funcao(janela, tela_relatorios.abrir_tela_relatorios)).pack(pady=5)

    tk.Button(janela, text="Voltar ao Início", width=25,
              command=lambda: voltar(janela)).pack(pady=10)

    tk.Button(janela, text="Sair", width=25, command=janela.destroy).pack(pady=5)

    janela.mainloop()

def chamar_funcao(janela_atual, funcao):
    janela_atual.destroy()
    funcao()

def voltar(janela):
    janela.destroy()
    tela_principal.abrir_tela_principal()