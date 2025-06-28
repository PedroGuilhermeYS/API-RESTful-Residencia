from flask import jsonify, request
from app import app
from app.controladores import adicionar, listar_usuarios, atualizar, deletar
@app.route("/")
def home():
    return "Principal Teste"

@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify ({"mensagem": "Bem-vindo a API de exemplo"})

@app.route("/usuarios", methods=['POST'])
def adicionar_usuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    if not nome or not email:
        return jsonify({"erro: Nome e Email são obrigatorios"}), 400

    novo_usuario = adicionar(nome, email)
    return jsonify(novo_usuario.to_dict()), 201

@app.route("/usuarios", methods=['GET'])
def listagem_de_usuarios():
    return jsonify(listar_usuarios())

@app.route("/usuarios/<int:id_usuario>", methods=['PUT'])
def atualizar_usuario(id_usuario):
    data= request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    if not nome or not email:
        return jsonify({"Nome e email são obrigatorios"}), 400

    novo_usuario = atualizar(id_usuario, nome, email)
    if novo_usuario == None:
        return jsonify(novo_usuario.to_dict())
    else:
        return jsonify({"Usuário não encontrado, tente novamente"}), 404

@app.route("/usuarios/<int:id_usuario>", methods=['DELETE'])
def deletar_usuario(id_usuario):

    usuario_deletado = deletar(id_usuario)

    if usuario_deletado == True:
        return jsonify("Usuario deletado")
    else:
        return jsonify({"Usuário não encontrado, tente novamente"}), 404
