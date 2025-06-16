import tkinter as tk
from tkinter import messagebox
from Controller import emprestimo_controller
from View.Menus import tela_menu_usuario

def abrir_tela_emprestimo_usuario(matricula, nome):
    janela = tk.Tk()
    janela.title("Empréstimo de Livro - Usuário")
    janela.geometry("400x250")

    tk.Label(janela, text=f"Usuário: {nome}").pack(pady=10)
    tk.Label(janela, text="ISBN do Livro:").pack(pady=5)
    entrada_isbn = tk.Entry(janela, width=40)
    entrada_isbn.pack()

    def confirmar_emprestimo():
        isbn = entrada_isbn.get()
        if not isbn:
            messagebox.showerror("Erro", "Digite o ISBN do livro.")
            return

        sucesso = emprestimo_controller.realizar_emprestimo(matricula, isbn)

        if sucesso:
            messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso.")
            janela.destroy()
            tela_menu_usuario.abrir_menu_usuario(matricula, nome)
        else:
            messagebox.showerror("Erro", "Não foi possível realizar o empréstimo.\nVerifique as regras e tente novamente.")

    tk.Button(janela, text="Confirmar Empréstimo", width=25, command=confirmar_emprestimo).pack(pady=10)
    tk.Button(janela, text="Voltar", width=25, command=lambda: voltar(janela, matricula, nome)).pack()

    janela.mainloop()

def voltar(janela, matricula, nome):
    janela.destroy()
    tela_menu_usuario.abrir_menu_usuario(matricula, nome)