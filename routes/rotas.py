from flask import Blueprint, render_template, redirect, request, send_file, jsonify, url_for
from models import db, Alimento
from forms import DocumentForm, OrcamentoForm
from docx import Document
from io import BytesIO
import pandas as pd
from werkzeug.utils import secure_filename
import os

rotas_blueprint = Blueprint('rotas', __name__)

@rotas_blueprint.route('/')
def index():
    alimentos = Alimento.query.all()
    return render_template('index.html', alimentos=alimentos)

@rotas_blueprint.route('/add', methods=['POST'])
def add():
    nome = request.form.get('nome')
    quantidade = int(request.form.get('quantidade'))
    tipo_animal = request.form.get('tipo_animal')

    alimento = Alimento(nome=nome, quantidade=quantidade, tipo_animal=tipo_animal)
    db.session.add(alimento)
    db.session.commit()
    return redirect(url_for('rotas.index'))

@rotas_blueprint.route('/export')
def export():
    alimentos = Alimento.query.all()
    df = pd.DataFrame([a.to_dict() for a in alimentos])
    
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return send_file(output, mimetype='text/csv', as_attachment=True, download_name='estoque.csv')

@rotas_blueprint.route('/import', methods=['POST'])
def import_data():
    file = request.files.get('file')
    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        for _, row in df.iterrows():
            # Basic import logic - could be improved with checks
            alimento = Alimento(
                nome=row.get('nome'), 
                quantidade=row.get('quantidade'), 
                tipo_animal=row.get('tipo_animal'),
                reserva=row.get('reserva')
            )
            db.session.add(alimento)
        db.session.commit()
        return redirect(url_for('rotas.index'))
    return "Arquivo inválido", 400

@rotas_blueprint.route('/orcamento', methods=['GET', 'POST'])
def orcamento():
    form = OrcamentoForm()
    if form.validate_on_submit():
        # logic handled by gerar_orcamento via post, or we can unify
        pass
    return render_template('orcamento.html', form=form)

@rotas_blueprint.route('/gerar_orcamento', methods=['POST'])
def gerar_orcamento():
    nome_empresa = request.form.get('nome_empresa')
    alimento = request.form.get('alimento')
    try:
        valor_alimento = float(request.form.get('valor_alimento'))
    except (ValueError, TypeError):
        valor_alimento = 0.0

    doc = Document()
    doc.add_heading(f'Orçamento - {nome_empresa}', 0)
    doc.add_paragraph(f'Produto: {alimento}')
    doc.add_paragraph(f'Valor: R$ {valor_alimento:.2f}')
    
    output = BytesIO()
    doc.save(output)
    output.seek(0)
    
    return send_file(output, as_attachment=True, download_name=f'orcamento_{nome_empresa}.docx')

@rotas_blueprint.route('/generate_document')
def generate_document():
    alimentos = Alimento.query.all()
    document = Document()
    document.add_heading('Pedido de Novo Estoque', level=1)

    for alimento in alimentos:
        document.add_paragraph(f'{alimento.nome}: {alimento.quantidade} para {alimento.tipo_animal}')

    output = BytesIO()
    document.save(output)
    output.seek(0)

    return send_file(output, download_name='pedido_estoque.docx', as_attachment=True)

@rotas_blueprint.route('/create_document', methods=['POST'])
def create_document():
    content = request.form.get('tinymce')
    doc = Document()
    doc.add_heading('Documento Editado', 0)
    
    if content:
        import re
        clean_text = re.sub('<[^<]+?>', '', content)
        doc.add_paragraph(clean_text)

    output = BytesIO()
    doc.save(output)
    output.seek(0)
    
    return send_file(output, as_attachment=True, download_name='documento_editado.docx')

@rotas_blueprint.route('/api/alimentos', methods=['GET'])
def obter_alimentos():
    alimentos = Alimento.query.all()
    return jsonify([a.to_dict() for a in alimentos])

