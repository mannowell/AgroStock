# 🌾 AgroStock — Sistema de Controle de Estoque e Orçamentos

> Solução moderna para gestão de insumos agrícolas e geração automatizada de orçamentos e pedidos de compra. Desenvolvido com **Python + Flask**.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-333333.svg)](https://www.sqlalchemy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 Funcionalidades

| Feature | Descrição |
|---------|-----------|
| 📊 **Dashboard de Estoque** | Visualização do estado atual com alertas automáticos para itens baixos |
| 🐄 **Gestão de Alimentos** | Cadastro e monitoramento de insumos por tipo de animal |
| 📄 **Geração de Orçamentos** | Criação de orçamentos formatados em Word (.docx) |
| 🛒 **Pedidos de Compra** | Geração automática de listas de reposição baseadas no estoque crítico |
| 📥 **Importação/Exportação** | Suporte completo para arquivos CSV |
| 🌙 **Modo Escuro** | Interface responsiva com Dark Mode |

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|--------|------------|
| Backend | Python, Flask, SQLAlchemy, Flask-Migrate, Flask-WTF |
| Frontend | HTML5, CSS3 (CSS Variables), JavaScript |
| Documentos | Python-docx (geração de Word) |
| Editor | TinyMCE (edição rica) |

---

## 📦 Instalação

### Pré-requisitos
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

# 3. Dependências
pip install flask flask-sqlalchemy flask-migrate flask-wtf python-docx pandas beautifulsoup4

# 4. Executar
python app.py
```

Acesse: `http://127.0.0.1:5000`

---

## 📂 Estrutura do Projeto

```
AgroStock/
├── app.py                 # Ponto de entrada
├── app_factory.py         # Application Factory
├── models.py              # Modelos do banco de dados
├── routes/                # Blueprints (rotas)
│   ├── auth.py
│   ├── dashboard.py
│   ├── estoque.py
│   └── orcamentos.py
├── templates/             # Jinja2 templates
│   ├── base.html
│   ├── dashboard.html
│   └── ...
├── static/                # CSS, JS, imagens
│   ├── css/
│   └── js/
├── requirements.txt       # Dependências
└── README.md
```

---

## 📊 Modelo de Dados

| Tabela | Descrição |
|--------|-----------|
| `insumos` | Cadastro de insumos agrícolas |
| `estoque` | Controle de estoque atual |
| `animais` | Tipos de animais |
| `orcamentos` | Orçamentos gerados |
| `pedidos` | Pedidos de compra |

---

## 📄 Licença

Distribuído sob licença **MIT**.

---

## 👤 Autor

**Wellison Oliveira (Mannowell)**

- 🌐 [GitHub](https://github.com/mannowell)
- 💼 [LinkedIn](https://linkedin.com/in/wellison-nascimento-79ba6b65/)
- 📧 [Email](mailto:manofama@gmail.com)
- 🔗 [Portfolio](https://mannowell.github.io/Portifolio/)

---

> 📌 **Projeto de portfólio** — Demonstração de habilidades em Python/Flask, modelagem de dados e automação de documentos.
