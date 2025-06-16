# Sistema de Gestão de Biblioteca 📚

## Introdução

Este projeto tem como objetivo desenvolver um sistema de gestão de biblioteca com interface gráfica utilizando Python, Tkinter e banco de dados SQLite.

O sistema segue a arquitetura **MVC (Model-View-Controller)**, promovendo uma separação clara entre:

- Lógica de interface (View)
- Regras de negócio (Controller)
- Persistência de dados (Model)

O sistema permite o gerenciamento de livros, usuários e empréstimos, com diferentes níveis de acesso para administradores e usuários comuns.

## Tecnologias utilizadas

- **Python** (Linguagem utilizada para a programação)
- **Tkinter** (Interface gráfica)
- **SQLite** (Banco de dados local)
- Arquitetura **MVC**


## Manual de uso

### Como executar o sistema:

1. Certifique-se de ter o **Python 3 instalado** em sua máquina.
2. Para iniciar o sistema, execute o arquivo principal:

```
python main.py
```

### Fluxo inicial:

Ao iniciar o sistema, o usuário verá a tela de seleção de perfil com duas opções:

- **Login como Administrador**
- **Login como Usuário Comum**

### Acesso como Administrador:

- **Senha padrão:** `123`
- Funcionalidades disponíveis:
  - Cadastro de livros
  - Cadastro de usuários
  - Realização de empréstimos
  - Realização de devoluções
  - Emissão de relatórios

### Acesso como Usuário Comum:

- O usuário precisa informar uma **matrícula existente no sistema**.
- Caso a matrícula não exista, o sistema informa que o usuário não está cadastrado.
- Funcionalidades disponíveis:
  - Realizar empréstimos
  - Realizar devoluções

### Funcionalidades principais:

✅ Cadastro de livros  
✅ Cadastro de usuários  
✅ Realização de empréstimos (limite de 3 livros por usuário)  
✅ Controle de devoluções (com verificação de atraso)  
✅ Relatórios administrativos:
- Empréstimos ativos
- Usuários com devoluções atrasadas


# Informações já inseridas no banco de dados

## Alunos:
- Rafael - Matrícula: 1 - Curso: ADS
- Erlano - Matrícula: 2 - Curso: ADS
- Celso - Matrícula: 3 - Curso: ADS

## Livros:
- O pequeno príncipe - Autor: Antoine de Saint-Exupéry - Ano de publicação: 1943 - Quantidade disponível: 1
- Divina comédia - Autor: Dante Allighiere - Ano de publicação: 1304 - Quantidade disponível: 9

## Empréstimos:
- Celso - Divina Comédia