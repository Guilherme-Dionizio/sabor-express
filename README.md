# sabor-express

## O que é?

`sabor-express` é uma API simples em **FastAPI** que consome uma fonte externa de dados de restaurantes (um JSON público) e expõe endpoints para:

- consultar todos os restaurantes disponíveis
- consultar o cardápio de um restaurante específico

---

## Endpoints principais

### ✅ `GET /api/hello`

Retorna um JSON de saudação simples:

```json
{ "Hello": "World" }
```

### ✅ `GET /api/restaurantes/`

Busca dados de restaurantes em:
`https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json`

#### 🔸 Sem query string

Retorna todos os dados recebidos:

```json
{ "Dados": [ ... ] }
```

#### 🔸 Com `?restaurante=Nome`

Filtra o cardápio do restaurante e retorna:

```json
{
  "Restaurante": "Nome",
  "Cardapio": [
    { "item": "...", "price": "...", "description": "..." },
    ...
  ]
}
```

---

## Comportamento em caso de falha na fonte externa

Se a requisição ao JSON externo falhar, retorna um JSON com um campo `Erro`:

```json
{ "Erro": "status - mensagem" }
```

---

## Como rodar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicie a API com o Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
3. Acesse:
   - `http://127.0.0.1:8000/api/hello`
   - `http://127.0.0.1:8000/api/restaurantes/`

---

## Conteúdo do projeto

- `main.py` → API FastAPI
- `app.py` → script que baixa o JSON externo e gera arquivos `.json` por restaurante
- `requirements.txt` → dependências do projeto
