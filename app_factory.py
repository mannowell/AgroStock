from flask import Flask
from flask_wtf.csrf import CSRFProtect

from config import Config
from models import db, migrate

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from routes.rotas import rotas_blueprint
    app.register_blueprint(rotas_blueprint)

    return app
