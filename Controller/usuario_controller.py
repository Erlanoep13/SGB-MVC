from Model import usuario_model

def cadastrar_usuario(matricula, nome, curso):
    # Verifica se a matrícula já existe
    existente = usuario_model.buscar_usuario_por_matricula(matricula)
    if existente:
        return False, "Já existe um usuário com essa matrícula."

    try:
        usuario_model.inserir_usuario(matricula, nome, curso)
        return True, "Usuário cadastrado com sucesso."
    except Exception as e:
        return False, f"Erro ao cadastrar usuário: {e}"