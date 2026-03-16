from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class DocumentForm(FlaskForm):
    documento = FileField('Documento', validators=[FileRequired()])

class OrcamentoForm(FlaskForm):
    nome_empresa = StringField('Nome da Empresa', validators=[DataRequired()])
    alimento = StringField('Alimento', validators=[DataRequired()])
    valor_alimento = StringField('Valor do Alimento', validators=[DataRequired()])
