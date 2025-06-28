from app.construtor import Usuario
from app.banco import banco_usuarios

def adicionar(nome, email):
    contadorID = len(banco_usuarios) + 1
    novo_usuario = Usuario(contadorID, nome, email)
    banco_usuarios.append(novo_usuario)
    return novo_usuario

def listar_usuarios():
    return [usuario.to_dict() for usuario in banco_usuarios]

def atualizar(id, nome, email):
    for usuario in usuario:
        if usuario.id == id:
            usuario.nome = nome
            usuario.email = email
            return usuario
    return None

def deletar(id):
    for indice, usuario in enumerate(banco_usuarios):
        if usuario.id == id:
            banco_usuarios.pop(indice)
            return True
    return None
            