# app_factory.py
from flask import Flask
from config import Config
from models import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from routes.rotas import rotas_blueprint
    app.register_blueprint(rotas_blueprint)
    
    with app.app_context():
        db.create_all()

    return app
