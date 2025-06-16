import tkinter as tk
from tkinter import messagebox
from View.Login import tela_login_admin, tela_login_usuario

def abrir_tela_principal():
    janela = tk.Tk()
    janela.title("Sistema de Biblioteca - Login")
    janela.geometry("300x200")

    # Texto inicial
    label = tk.Label(janela, text="Fazer login como:", font=("Arial", 14))
    label.pack(pady=20)

    # Botão para login de Aluno (Usuário comum)
    botao_aluno = tk.Button(janela, text="Aluno", width=20, command=lambda: abrir_login_usuario(janela))
    botao_aluno.pack(pady=5)

    # Botão para login de Administrador
    botao_admin = tk.Button(janela, text="Administrador", width=20, command=lambda: abrir_login_admin(janela))
    botao_admin.pack(pady=5)

    janela.mainloop()

def abrir_login_admin(janela_atual):
    janela_atual.destroy()
    tela_login_admin.abrir_tela_login_admin()

def abrir_login_usuario(janela_atual):
    janela_atual.destroy()
    tela_login_usuario.abrir_tela_login_usuario()