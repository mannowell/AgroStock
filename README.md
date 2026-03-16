# AgroStock - Sistema de Controle de Estoque e Orçamentos

AgroStock é uma solução moderna para gestão de insumos agrícolas e geração automatizada de orçamentos e pedidos de compra. Desenvolvido com Flask, o sistema oferece uma interface intuitiva e recursos de automação.

## 🚀 Funcionalidades

- **Dashboard de Estoque**: Visualize o estado atual do seu estoque com alertas automáticos para itens baixos.
- **Gestão de Alimentos**: Adicione e monitore insumos por tipo de animal.
- **Geração de Orçamentos**: Crie orçamentos formatados em Word (.docx) rapidamente.
- **Pedidos de Compra**: Editor integrado que gera automaticamente listas de reposição baseadas no estoque crítico.
- **Importação/Exportação**: Suporte completo para arquivos CSV, facilitando a migração de dados.
- **Design Moderno**: Interface responsiva com suporte a **Modo Escuro (Dark Mode)**.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python, Flask, SQLAlchemy, Flask-Migrate, Flask-WTF.
- **Frontend**: HTML5, CSS3 Moderno (CSS Variables), JavaScript.
- **Documentação**: Python-docx para geração de arquivos Word.
- **Editor**: TinyMCE para edição rica de documentos.

## 📦 Como Instalar

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd Projeto
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   # ou
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install flask flask-sqlalchemy flask-migrate flask-wtf python-docx pandas beautifulsoup4
   ```

4. Execute a aplicação:
   ```bash
   python app.py
   ```

O sistema estará disponível em `http://127.0.0.1:5000`.

## 📂 Estrutura do Projeto

- `app.py`: Ponto de entrada da aplicação.
- `app_factory.py`: Configuração do padrão Application Factory.
- `models.py`: Definições de banco de dados.
- `routes/`: Módulos de rotas (Blueprints).
- `templates/`: Arquivos HTML com Jinja2.
- `static/`: Arquivos CSS, Imagens e JavaScript.
