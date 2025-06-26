from flask import Flask, jsonify, request
usuarios = []

app = Flask(__name__)

@app.route("/")
def home():
    return "Princial Teste"

@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify ({"mensagem": "Bem-vindo à API de exemplo"})

@app.route("/usuarios", methods=['POST'])
def adicionar_usuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    if not nome or not email:
        return jsonify({"erro": "Campos 'nome' e 'email' são obrigatórios"}), 400

    novo_usuario = {"nome": nome, "email": email}
    usuarios.append(novo_usuario)

    return jsonify(novo_usuario), 201

if __name__ == "__main__":
    app.run(port=3000)