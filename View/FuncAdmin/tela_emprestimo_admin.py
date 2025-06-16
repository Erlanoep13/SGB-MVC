import tkinter as tk
from tkinter import messagebox
from Controller import emprestimo_controller
from View.Menus import tela_menu_admin

def abrir_tela_emprestimo_admin():
    janela = tk.Tk()
    janela.title("Empréstimo de Livro - Administrador")
    janela.geometry("400x300")

    tk.Label(janela, text="Matrícula do Usuário:").pack(pady=5)
    entrada_matricula = tk.Entry(janela, width=40)
    entrada_matricula.pack()

    tk.Label(janela, text="ISBN do Livro:").pack(pady=5)
    entrada_isbn = tk.Entry(janela, width=40)
    entrada_isbn.pack()

    def realizar_emprestimo():
        matricula = entrada_matricula.get()
        isbn = entrada_isbn.get()

        if not matricula or not isbn:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        sucesso = emprestimo_controller.realizar_emprestimo(matricula, isbn)

        if sucesso:
            messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso.")
            janela.destroy()
            tela_menu_admin.abrir_menu_admin()
        else:
            messagebox.showerror("Erro", "Não foi possível realizar o empréstimo.\nVerifique as regras de empréstimo.")

    tk.Button(janela, text="Confirmar Empréstimo", width=25, command=realizar_emprestimo).pack(pady=10)
    tk.Button(janela, text="Voltar", width=25, command=lambda: voltar(janela)).pack()

    janela.mainloop()

def voltar(janela):
    janela.destroy()
    tela_menu_admin.abrir_menu_admin()