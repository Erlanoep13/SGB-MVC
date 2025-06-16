import tkinter as tk
from tkinter import messagebox
from Controller import usuario_controller
from View.Menus import tela_menu_admin

def abrir_tela_cadastro_usuario():
    janela = tk.Tk()
    janela.title("Cadastro de Usuário")
    janela.geometry("400x350")

    # Labels e entradas
    tk.Label(janela, text="Nome:").pack(pady=5)
    entrada_nome = tk.Entry(janela, width=40)
    entrada_nome.pack()

    tk.Label(janela, text="Matrícula:").pack(pady=5)
    entrada_matricula = tk.Entry(janela, width=40)
    entrada_matricula.pack()

    tk.Label(janela, text="Curso:").pack(pady=5)
    entrada_curso = tk.Entry(janela, width=40)
    entrada_curso.pack()

    def salvar_usuario():
        nome = entrada_nome.get()
        matricula = entrada_matricula.get()
        curso = entrada_curso.get()

        if not nome or not matricula or not curso:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        sucesso, mensagem = usuario_controller.cadastrar_usuario(matricula, nome, curso)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            janela.destroy()
            tela_menu_admin.abrir_menu_admin()
        else:
            messagebox.showerror("Erro", mensagem)

    tk.Button(janela, text="Salvar", width=20, command=salvar_usuario).pack(pady=10)
    tk.Button(janela, text="Voltar", width=20, command=lambda: voltar(janela)).pack()

    janela.mainloop()

def voltar(janela):
    janela.destroy()
    tela_menu_admin.abrir_menu_admin()