# app.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from routes.rotas import rotas_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'data', 'estoque.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(16)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registre o Blueprint
app.register_blueprint(rotas_blueprint)

csrf = CSRFProtect(app)

if __name__ == '__main__':
    app.run(debug=True)
