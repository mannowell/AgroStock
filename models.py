from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Alimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    tipo_animal = db.Column(db.String(20), nullable=False)
    reserva = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'quantidade': self.quantidade,
            'tipo_animal': self.tipo_animal,
            'reserva': self.reserva
        }
