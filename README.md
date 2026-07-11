# AgroStock — Sistema de Controle de Estoque e Orcamentos

> Solucao moderna para gestao de insumos agricolas e geracao automatizada de orcamentos e pedidos de compra. Desenvolvido com **Python + Flask**.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-333333.svg)](https://www.sqlalchemy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## Funcionalidades

| Feature | Descricao |
|---------|-----------|
| **Dashboard de Estoque** | Visualizacao do estado atual com alertas automaticos para itens baixos |
| **Gestao de Alimentos** | Cadastro e monitoramento de insumos por tipo de animal |
| **Geracao de Orcamentos** | Criacao de orcamentos formatados em Word (.docx) |
| **Pedido de Compra** | Geracao automatica de listas de reposicao baseadas no estoque critico |
| **Importacao/Exportacao** | Suporte completo para arquivos CSV |
| **Modo Escuro** | Interface responsiva com Dark Mode |
| **Editor de Documentos** | Edicao rica de documentos com TinyMCE, exportacao para .docx |

---

## Tecnologias

| Camada | Tecnologia |
|--------|------------|
| Backend | Python, Flask, SQLAlchemy, Flask-Migrate, Flask-WTF |
| Frontend | HTML5, CSS3 (CSS Variables), JavaScript |
| Documentos | python-docx (geracao de Word) |
| Editor | TinyMCE (edicao rica) |
| Seguranca | Flask-WTF CSRF Protection |

---

## Instalacao

### Pre-requisitos
- Python 3.10+
- pip

### Passo a Passo

```bash
# 1. Clone
git clone https://github.com/mannowell/AgroStock.git
cd AgroStock

# 2. Ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Dependencias
pip install -r requirements.txt

# 4. Executar
python app.py
```

Acesse: `http://127.0.0.1:5000`

---

## Estrutura do Projeto

```
AgroStock/
├── app.py                 # Ponto de entrada
├── app_factory.py         # Application Factory + CSRF setup
├── config.py              # Configuracoes (DB, secret key)
├── models.py              # Modelos do banco de dados
├── forms.py               # Formularios WTForms
├── routes/
│   ├── __init__.py
│   └── rotas.py           # Blueprint principal (rotas + API)
├── templates/             # Jinja2 templates
│   ├── layout.html        # Layout base (nav, dark mode, TinyMCE)
│   ├── index.html         # Dashboard de estoque
│   └── orcamento.html     # Geracao de orcamentos
├── static/
│   └── css/
│       └── style.css      # Estilos globais + dark mode
├── data/                  # Banco de dados SQLite (local)
├── requirements.txt       # Dependencias
└── README.md
```

---

## Modelo de Dados

| Tabela | Descricao |
|--------|-----------|
| `alimento` | Cadastro de insumos agricolas com nome, quantidade, tipo de animal e reserva |

---

## Rotas

| Rota | Metodo | Descricao |
|------|--------|-----------|
| `/` | GET | Dashboard de estoque |
| `/add` | POST | Adicionar item ao estoque |
| `/export` | GET | Exportar estoque como CSV |
| `/import` | POST | Importar estoque de arquivo CSV |
| `/orcamento` | GET/POST | Formulario de geracao de orcamentos |
| `/gerar_orcamento` | POST | Gerar documento .docx do orcamento |
| `/generate_document` | GET | Gerar pedido de reposicao em .docx |
| `/create_document` | POST | Gerar documento editado via TinyMCE |
| `/api/alimentos` | GET | API JSON com todos os alimentos |

---

## Licenca

Distribuido sob licenca **MIT**.

---

## Autor

**Wellison Oliveira (Mannowell)**

- [GitHub](https://github.com/mannowell)
- [LinkedIn](https://linkedin.com/in/wellison-nascimento-79ba6b65/)
- [Email](mailto:manofama@gmail.com)
- [Portfolio](https://mannowell.github.io/Portifolio/)

---

> **Projeto de portfolio** — Demonstracao de habilidades em Python/Flask, modelagem de dados e automacao de documentos.
