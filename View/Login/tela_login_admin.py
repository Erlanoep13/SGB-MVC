import tkinter as tk
from tkinter import messagebox
from Controller import login_controller
from View import tela_principal
from View.Menus import tela_menu_admin

def abrir_tela_login_admin():
    janela = tk.Tk()
    janela.title("Login - Administrador")
    janela.geometry("300x200")

    tk.Label(janela, text="Nome do Administrador:").pack(pady=5)
    entrada_nome = tk.Entry(janela)
    entrada_nome.pack(pady=5)

    tk.Label(janela, text="Senha:").pack(pady=5)
    entrada_senha = tk.Entry(janela, show="*")
    entrada_senha.pack(pady=5)

    def fazer_login():
        nome = entrada_nome.get()
        senha = entrada_senha.get()

        if login_controller.validar_login_admin(nome, senha):
            messagebox.showinfo("Login", f"Bem-vindo, {nome}!")
            janela.destroy()
            tela_menu_admin.abrir_menu_admin()
        else:
            messagebox.showerror("Erro", "Senha incorreta!")

    tk.Button(janela, text="Entrar", width=15, command=fazer_login).pack(pady=5)
    tk.Button(janela, text="Voltar", width=15, command=lambda: voltar(janela)).pack(pady=5)

    janela.mainloop()

def voltar(janela):
    janela.destroy()
    tela_principal.abrir_tela_principal()