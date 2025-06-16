import tkinter as tk
from tkinter import messagebox
from Controller import devolucao_controller
from View.Menus import tela_menu_admin

def abrir_tela_devolucao_admin():
    janela = tk.Tk()
    janela.title("Devolução de Livro - Administrador")
    janela.geometry("400x300")

    tk.Label(janela, text="Matrícula do Usuário:").pack(pady=5)
    entrada_matricula = tk.Entry(janela, width=40)
    entrada_matricula.pack()

    tk.Label(janela, text="ISBN do Livro:").pack(pady=5)
    entrada_isbn = tk.Entry(janela, width=40)
    entrada_isbn.pack()

    def confirmar_devolucao():
        matricula = entrada_matricula.get().strip()
        isbn = entrada_isbn.get().strip()

        if not matricula or not isbn:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        sucesso = devolucao_controller.realizar_devolucao(matricula, isbn)

        if sucesso:
            messagebox.showinfo("Sucesso", "Devolução registrada com sucesso.")
            janela.destroy()
            tela_menu_admin.abrir_menu_admin()
        else:
            messagebox.showerror("Erro", "Não foi possível registrar a devolução.\nVerifique a matrícula, o ISBN ou se o livro já foi devolvido.")

    tk.Button(janela, text="Registrar Devolução", width=25, command=confirmar_devolucao).pack(pady=10)
    tk.Button(janela, text="Voltar", width=25, command=lambda: voltar(janela)).pack()

    janela.mainloop()

def voltar(janela):
    janela.destroy()
    tela_menu_admin.abrir_menu_admin()