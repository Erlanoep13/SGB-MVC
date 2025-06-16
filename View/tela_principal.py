import tkinter as tk
from tkinter import messagebox
from Controller import login_controller
from View import tela_menu_admin, tela_menu_usuario  # vamos criar depois

def abrir_login_admin():
    login_window = tk.Toplevel()
    login_window.title("Login Administrador")

    tk.Label(login_window, text="Nome:").grid(row=0, column=0)
    tk.Label(login_window, text="Senha:").grid(row=1, column=0)

    nome_entry = tk.Entry(login_window)
    senha_entry = tk.Entry(login_window, show="*")

    nome_entry.grid(row=0, column=1)
    senha_entry.grid(row=1, column=1)

    def autenticar():
        nome = nome_entry.get()
        senha = senha_entry.get()

        if login_controller.validar_login_admin(nome, senha):
            messagebox.showinfo("Sucesso", f"Bem-vindo, {nome}!")
            login_window.destroy()
            tela_menu_admin.abrir_tela_admin()
        else:
            messagebox.showerror("Erro", "Senha incorreta.")

    tk.Button(login_window, text="Entrar", command=autenticar).grid(row=2, column=0, columnspan=2)

def abrir_login_usuario():
    login_window = tk.Toplevel()
    login_window.title("Login Usuário")

    tk.Label(login_window, text="Matrícula:").grid(row=0, column=0)
    entrada = tk.Entry(login_window)
    entrada.grid(row=0, column=1)

    def autenticar():
        matricula = entrada.get()
        usuario = login_controller.validar_login_usuario(matricula)

        if usuario:
            messagebox.showinfo("Bem-vindo", f"{usuario['nome']}")
            login_window.destroy()
            tela_menu_usuario.abrir_tela_usuario(usuario)
        else:
            messagebox.showwarning("Não encontrado", "Usuário não encontrado.")
            # Podemos perguntar se deseja se cadastrar, ou redirecionar.

    tk.Button(login_window, text="Entrar", command=autenticar).grid(row=1, column=0, columnspan=2)

def iniciar_tela_principal():
    root = tk.Tk()
    root.title("Sistema de Biblioteca")

    tk.Label(root, text="Bem-vindo ao Sistema de Biblioteca").pack(pady=10)

    tk.Button(root, text="Login como Administrador", command=abrir_login_admin, width=30).pack(pady=5)
    tk.Button(root, text="Login como Usuário", command=abrir_login_usuario, width=30).pack(pady=5)

    root.mainloop()
