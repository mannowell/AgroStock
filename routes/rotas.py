import os
import re
from io import BytesIO

from flask import (
    Blueprint,
    jsonify,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
)
from docx import Document
from werkzeug.utils import secure_filename
import pandas as pd

from forms import OrcamentoForm
from models import Alimento, db

rotas_blueprint = Blueprint('rotas', __name__)


@rotas_blueprint.route('/')
def index():
    alimentos = Alimento.query.all()
    return render_template('index.html', alimentos=alimentos)


@rotas_blueprint.route('/add', methods=['POST'])
def add():
    nome = request.form.get('nome', '').strip()
    quantidade_raw = request.form.get('quantidade', '')
    tipo_animal = request.form.get('tipo_animal', '').strip()

    if not nome or not tipo_animal:
        return redirect(url_for('rotas.index'))

    try:
        quantidade = int(quantidade_raw)
    except (ValueError, TypeError):
        return redirect(url_for('rotas.index'))

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
    if not file or not file.filename or not file.filename.endswith('.csv'):
        return redirect(url_for('rotas.index'))

    try:
        df = pd.read_csv(file)
    except Exception:
        return redirect(url_for('rotas.index'))

    for _, row in df.iterrows():
        nome = str(row.get('nome', '')).strip()
        if not nome:
            continue
        try:
            quantidade = int(row.get('quantidade', 0))
        except (ValueError, TypeError):
            quantidade = 0
        tipo_animal = str(row.get('tipo_animal', '')).strip()
        reserva = row.get('reserva')
        if reserva is not None:
            try:
                reserva = int(reserva)
            except (ValueError, TypeError):
                reserva = None

        alimento = Alimento(
            nome=nome,
            quantidade=quantidade,
            tipo_animal=tipo_animal,
            reserva=reserva,
        )
        db.session.add(alimento)

    db.session.commit()
    return redirect(url_for('rotas.index'))


@rotas_blueprint.route('/orcamento', methods=['GET', 'POST'])
def orcamento():
    form = OrcamentoForm()
    if form.validate_on_submit():
        return redirect(url_for('rotas.gerar_orcamento'))
    return render_template('orcamento.html', form=form)


@rotas_blueprint.route('/gerar_orcamento', methods=['POST'])
def gerar_orcamento():
    nome_empresa = request.form.get('nome_empresa', '').strip()
    alimento = request.form.get('alimento', '').strip()
    try:
        valor_alimento = float(request.form.get('valor_alimento', 0))
    except (ValueError, TypeError):
        valor_alimento = 0.0

    if not nome_empresa or not alimento:
        return redirect(url_for('rotas.orcamento'))

    doc = Document()
    doc.add_heading(f'Orcamento - {nome_empresa}', 0)
    doc.add_paragraph(f'Produto: {alimento}')
    doc.add_paragraph(f'Valor: R$ {valor_alimento:.2f}')

    output = BytesIO()
    doc.save(output)
    output.seek(0)

    filename = re.sub(r'[^\w\-]', '_', nome_empresa)
    return send_file(output, as_attachment=True, download_name=f'orcamento_{filename}.docx')


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
    content = request.form.get('tinymce', '')
    doc = Document()
    doc.add_heading('Documento Editado', 0)

    if content:
        clean_text = re.sub(r'<[^>]+>', '', content)
        doc.add_paragraph(clean_text)

    output = BytesIO()
    doc.save(output)
    output.seek(0)

    return send_file(output, as_attachment=True, download_name='documento_editado.docx')


@rotas_blueprint.route('/api/alimentos', methods=['GET'])
def obter_alimentos():
    alimentos = Alimento.query.all()
    return jsonify([a.to_dict() for a in alimentos])
