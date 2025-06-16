from Model import usuario_model

# Login do administrador com senha fixa
def validar_login_admin(nome_digitado, senha_digitada):
    senha_correta = "123"  # Senha fixa

    if senha_digitada == senha_correta:
        return True
    else:
        return False

# Login de usuário comum: verifica se a matrícula existe no banco
def validar_login_usuario(matricula_digitada):
    usuario = usuario_model.buscar_usuario_por_matricula(matricula_digitada)
    if usuario:
        return usuario  # Retorna o usuário encontrado
    else:
        return None