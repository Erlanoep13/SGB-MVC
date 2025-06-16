import tkinter as tk
from tkinter import messagebox
from Controller import login_controller
from View import tela_principal
from View.Menus import tela_menu_usuario

def abrir_tela_login_usuario():
    janela = tk.Tk()
    janela.title("Login - Usuário Comum")
    janela.geometry("300x200")

    tk.Label(janela, text="Matrícula do Usuário:").pack(pady=10)
    entrada_matricula = tk.Entry(janela)
    entrada_matricula.pack(pady=5)

    def fazer_login():
        matricula = entrada_matricula.get()

        usuario = login_controller.validar_login_usuario(matricula)
        if usuario:
            messagebox.showinfo("Login", f"Bem-vindo, {usuario[1]}!")
            janela.destroy()
            tela_menu_usuario.abrir_menu_usuario(usuario[0], usuario[1])  # Passa matrícula e nome
        else:
            messagebox.showerror("Erro", "Usuário não encontrado.\nConsulte o administrador para cadastro.")

    tk.Button(janela, text="Entrar", width=15, command=fazer_login).pack(pady=5)
    tk.Button(janela, text="Voltar", width=15, command=lambda: voltar(janela)).pack(pady=5)

    janela.mainloop()

def voltar(janela):
    janela.destroy()
    tela_principal.abrir_tela_principal()