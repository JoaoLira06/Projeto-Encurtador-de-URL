# URL Shortener

API de encurtamento de URLs desenvolvida com Python e FastAPI, com frontend integrado.

## 🚀 Tecnologias

- **Python 3.14**
- **FastAPI** — framework web moderno e de alta performance
- **SQLAlchemy** — ORM para comunicação com o banco de dados
- **SQLite** — banco de dados local
- **Pydantic** — validação de dados
- **Uvicorn** — servidor ASGI
- **HTML/CSS/JavaScript** — frontend integrado

## 📁 Estrutura do Projeto

```
Projeto/
├── app/
│   ├── __init__.py
│   ├── database.py    # configuração do banco de dados
│   ├── models.py      # modelo da tabela URLs
│   ├── schemas.py     # validação de dados com Pydantic
│   ├── utils.py       # geração de códigos curtos
│   └── routes.py      # endpoints da API
├── static/
│   ├── style.css      # estilos do frontend
│   └── script.js      # lógica do frontend
├── templates/
│   └── index.html     # página principal
├── main.py            # ponto de entrada da aplicação
└── requirements.txt
```

## ⚙️ Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/url-shortener.git
cd url-shortener
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate.bat  # Windows
```

**3. Instale as dependências**
```bash
python -m pip install fastapi uvicorn sqlalchemy python-dotenv jinja2 python-multipart
```

**4. Rode o servidor**
```bash
python -m uvicorn main:app --reload
```

**5. Acesse**
- Frontend: http://localhost:8000
- Documentação da API: http://localhost:8000/docs

## 📡 Endpoints da API

### POST /shorten
Encurta uma URL longa.

**Request:**
```json
{
  "original_url": "https://www.google.com"
}
```

**Response (201):**
```json
{
  "short_code": "aB3xZ9",
  "original_url": "https://www.google.com/",
  "short_url": "http://localhost:8000/aB3xZ9"
}
```

---

### GET /{short_code}
Redireciona para a URL original e incrementa o contador de acessos.

**Exemplo:** `GET /aB3xZ9`

**Response:** Redirecionamento 302 para a URL original.

---

### GET /stats/{short_code}
Retorna as estatísticas de acesso de uma URL encurtada.

**Exemplo:** `GET /stats/aB3xZ9`

**Response (200):**
```json
{
  "short_code": "aB3xZ9",
  "original_url": "https://www.google.com/",
  "access_count": 5,
  "created_at": "2026-04-28T12:00:00"
}
```

## 🖥️ Frontend

A aplicação possui um frontend integrado acessível em `http://localhost:8000`. Permite encurtar URLs, copiar o link gerado e visualizar o número de acessos em tempo real.
