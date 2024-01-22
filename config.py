# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/estoque.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'sua_chave_secreta'
