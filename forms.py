from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class OrcamentoForm(FlaskForm):
    nome_empresa = StringField('Nome da Empresa', validators=[DataRequired()])
    alimento = StringField('Alimento', validators=[DataRequired()])
    valor_alimento = FloatField('Valor do Alimento', validators=[
        DataRequired(),
        NumberRange(min=0, message='Valor deve ser maior ou igual a zero')
    ])


class AlimentoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    quantidade = IntegerField('Quantidade', validators=[
        DataRequired(),
        NumberRange(min=0, message='Quantidade deve ser maior ou igual a zero')
    ])
    tipo_animal = StringField('Tipo de Animal', validators=[DataRequired()])
    reserva = IntegerField('Reserva', validators=[
        NumberRange(min=0, message='Reserva deve ser maior ou igual a zero')
    ], default=0)
