import tkinter as tk
from tkinter import messagebox
from Controller import devolucao_controller
from View.Menus import tela_menu_usuario

def abrir_tela_devolucao_usuario(matricula, nome):
    janela = tk.Tk()
    janela.title("Devolução de Livro - Usuário")
    janela.geometry("400x250")

    tk.Label(janela, text=f"Usuário: {nome}").pack(pady=10)
    tk.Label(janela, text="ISBN do Livro a Devolver:").pack(pady=5)
    entrada_isbn = tk.Entry(janela, width=40)
    entrada_isbn.pack()

    def confirmar_devolucao():
        isbn = entrada_isbn.get().strip()

        if not isbn:
            messagebox.showerror("Erro", "Por favor, informe o ISBN do livro.")
            return

        sucesso = devolucao_controller.realizar_devolucao(matricula, isbn)

        if sucesso:
            messagebox.showinfo("Sucesso", "Devolução registrada com sucesso.")
            janela.destroy()
            tela_menu_usuario.abrir_menu_usuario(matricula, nome)
        else:
            messagebox.showerror("Erro", "Nenhum empréstimo ativo encontrado para esse livro.")

    tk.Button(janela, text="Confirmar Devolução", width=25, command=confirmar_devolucao).pack(pady=10)
    tk.Button(janela, text="Voltar", width=25, command=lambda: voltar(janela, matricula, nome)).pack()

    janela.mainloop()

def voltar(janela, matricula, nome):
    janela.destroy()
    tela_menu_usuario.abrir_menu_usuario(matricula, nome)
