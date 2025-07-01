import json

CAMINHO_ARQUIVO = 'usuarios.json'

def salvar_em_json(lista_usuarios):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump([u.to_dict() for u in lista_usuarios], arquivo, ensure_ascii=False, indent=4)