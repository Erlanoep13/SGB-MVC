import tkinter as tk
from tkinter import messagebox
from Controller import livro_controller
from View.Menus import tela_menu_admin

def abrir_tela_cadastro_livro():
    janela = tk.Tk()
    janela.title("Cadastro de Livro")
    janela.geometry("400x400")

    # Labels e Entradas
    tk.Label(janela, text="Título:").pack(pady=5)
    entrada_titulo = tk.Entry(janela, width=40)
    entrada_titulo.pack()

    tk.Label(janela, text="Autor:").pack(pady=5)
    entrada_autor = tk.Entry(janela, width=40)
    entrada_autor.pack()

    tk.Label(janela, text="ISBN:").pack(pady=5)
    entrada_isbn = tk.Entry(janela, width=40)
    entrada_isbn.pack()

    tk.Label(janela, text="Ano de Publicação:").pack(pady=5)
    entrada_ano = tk.Entry(janela, width=40)
    entrada_ano.pack()

    tk.Label(janela, text="Quantidade Disponível:").pack(pady=5)
    entrada_quantidade = tk.Entry(janela, width=40)
    entrada_quantidade.pack()

    # Função interna para salvar o livro
    def salvar_livro():
        titulo = entrada_titulo.get()
        autor = entrada_autor.get()
        isbn = entrada_isbn.get()
        ano = entrada_ano.get()
        quantidade = entrada_quantidade.get()

        # Validação simples
        if not titulo or not autor or not isbn or not ano or not quantidade:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            ano = int(ano)
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showerror("Erro", "Ano e quantidade devem ser números.")
            return

        # Chama o Controller
        sucesso, mensagem = livro_controller.cadastrar_livro(isbn, titulo, autor, ano, quantidade)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            janela.destroy()
            tela_menu_admin.abrir_menu_admin()
        else:
            messagebox.showerror("Erro", mensagem)

    # Botões
    tk.Button(janela, text="Salvar", width=20, command=salvar_livro).pack(pady=10)
    tk.Button(janela, text="Voltar", width=20, command=lambda: voltar(janela)).pack()

    janela.mainloop()

def voltar(janela):
    janela.destroy()
    tela_menu_admin.abrir_menu_admin()