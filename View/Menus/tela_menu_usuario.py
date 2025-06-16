import tkinter as tk
from View import tela_principal
from View.FuncUser import tela_emprestimo_user, tela_devolucao_user

def abrir_menu_usuario(matricula, nome):
    janela = tk.Tk()
    janela.title("Menu - Usuário Comum")
    janela.geometry("300x250")

    tk.Label(janela, text=f"Bem-vindo, {nome}!", font=("Arial", 14)).pack(pady=10)

    # Botões para as ações permitidas ao usuário comum
    tk.Button(janela, text="Realizar Empréstimo", width=25, command=lambda: abrir_tela_emprestimo(janela, matricula, nome)).pack(pady=5)
    tk.Button(janela, text="Realizar Devolução", width=25, command=lambda: abrir_tela_devolucao(janela, matricula, nome)).pack(pady=5)
    tk.Button(janela, text="Voltar ao Início", width=25, command=lambda: voltar(janela)).pack(pady=10)
    tk.Button(janela, text="Sair", width=25, command=janela.destroy).pack(pady=5)

    janela.mainloop()

def abrir_tela_emprestimo(janela, matricula, nome):
    janela.destroy()
    tela_emprestimo_user.abrir_tela_emprestimo_usuario(matricula, nome)

def abrir_tela_devolucao(janela, matricula, nome):
    janela.destroy()
    tela_devolucao_user.abrir_tela_devolucao_usuario(matricula, nome)

def voltar(janela):
    janela.destroy()
    tela_principal.abrir_tela_principal()