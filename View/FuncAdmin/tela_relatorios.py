import tkinter as tk
from tkinter import ttk
from Model import emprestimo_model, livro_model
from View.Menus import tela_menu_admin

def abrir_tela_relatorios():
    janela = tk.Tk()
    janela.title("Relatórios - Administrador")
    janela.geometry("600x500")

    aba = ttk.Notebook(janela)
    aba.pack(expand=True, fill='both')

    # Abas
    frame_ativos = ttk.Frame(aba)
    frame_atrasados = ttk.Frame(aba)
    frame_livros = ttk.Frame(aba)

    aba.add(frame_ativos, text="Empréstimos Ativos")
    aba.add(frame_atrasados, text="Empréstimos Atrasados")
    aba.add(frame_livros, text="Livros Disponíveis")

    # Função auxiliar para criar área de texto com scrollbar
    def criar_area_texto(frame):
        texto = tk.Text(frame, wrap="word")
        scroll = ttk.Scrollbar(frame, orient="vertical", command=texto.yview)
        texto.configure(yscrollcommand=scroll.set)
        texto.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        return texto

    # Empréstimos ativos
    texto_ativos = criar_area_texto(frame_ativos)
    ativos = emprestimo_model.listar_emprestimos_ativos()
    if ativos:
        for emp in ativos:
            texto_ativos.insert(tk.END, f"Matrícula: {emp[0]} | Livro: {emp[1]} | Empréstimo: {emp[2]} | Previsto: {emp[3]}\n")
    else:
        texto_ativos.insert(tk.END, "Nenhum empréstimo ativo encontrado.")

    # Empréstimos atrasados
    texto_atrasados = criar_area_texto(frame_atrasados)
    atrasados = emprestimo_model.listar_usuarios_atrasados()
    if atrasados:
        for atr in atrasados:
            texto_atrasados.insert(tk.END, f"Matrícula: {atr[0]} | Livro: {atr[1]} | Previsto para: {atr[2]}\n")
    else:
        texto_atrasados.insert(tk.END, "Nenhum empréstimo atrasado.")

    # Livros disponíveis
    texto_livros = criar_area_texto(frame_livros)
    livros = livro_model.listar_livros()
    livros_disponiveis = [l for l in livros if l[4] > 0]  # posição 4: quantidade disponível
    if livros_disponiveis:
        for livro in livros_disponiveis:
            texto_livros.insert(tk.END, f"{livro[1]} | ISBN: {livro[0]} | Autor: {livro[2]} | Quantidade: {livro[4]}\n")
    else:
        texto_livros.insert(tk.END, "Nenhum livro disponível no momento.")

    # Botão voltar
    tk.Button(janela, text="Voltar ao menu", command=lambda: voltar(janela)).pack(pady=10)

    janela.mainloop()

def voltar(janela):
    janela.destroy()
    tela_menu_admin.abrir_menu_admin()