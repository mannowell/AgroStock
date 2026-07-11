from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class OrcamentoForm(FlaskForm):
    nome_empresa = StringField('Nome da Empresa', validators=[DataRequired()])
    alimento = StringField('Alimento', validators=[DataRequired()])
    valor_alimento = StringField('Valor do Alimento', validators=[DataRequired()])
