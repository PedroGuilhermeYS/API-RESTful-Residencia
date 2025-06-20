from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Princial Teste"

@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify ({"mensagem": "Bem-vindo à API de exemplo"})

if __name__ == "__main__":
    app.run(port=3000)