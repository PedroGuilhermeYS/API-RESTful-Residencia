# API-RESTful-Residencia

# 📄 Documentação - API com Python (Flask) - Residência (ATIVIDADE)

## 🗂️ Organização:
```
API-RESTful-Residencia/
│
├── app/
│   ├── __init__.py
│   ├── banco.py
│   ├── construtor.py
│   ├── controladores.py
│   ├── routes.py
│
├── .gitignore
├── README.md
├── requirements.txt
```

## 🚀 URL da API

- Local: `http://localhost:5000`  

## 📦 Detalhes dos Endpoints

### 🔸 GET `/saudacao`
Retorna uma mensagem de boas-vindas.

**Exemplo de resposta:**
```json
{
  "mensagem": "Bem-vindo a API de exemplo"
}
```

---

### 🔸 POST `/usuarios`
Cadastra um novo usuário.

---

### 🔸 GET `/usuarios`
Lista todos os usuários cadastrados.

**Exemplo de resposta:**
```json
[
  {
    "id": 1,
    "nome": "Marca Passo",
    "email": "MarcaPasso@email.com"
  }

```

---

### 🔸 PUT `/usuarios/:id`
Atualiza um usuário existente.

**Body (JSON):**
```json
{
    "nome": "Marca Passo",
    "email": "MarcaPasso@email.com"
  }
```

**Resposta (sucesso):**
```json
{
    "id": 1,
    "nome": "Marca Passo",
    "email": "MarcaPasso@email.com"
  }
```

**Resposta (erro):**
```json
{
  "Usuário não encontrado, tente novamente"
}
```

---

### 🔸 DELETE `/usuarios/:id`
Deleta um usuário pelo ID.

**Exemplo de resposta:**
```json
{
  ""Usuario deletado""
}
```

---

## ⚠️ Observações Importantes

- Os dados são armazenados **em memória**, então são resetados quando o servidor reinicia.
- Todos os dados devem ser enviados em **formato JSON**.
- Funciona localmente na porta **5000**.
