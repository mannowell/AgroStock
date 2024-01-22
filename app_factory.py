# app_factory.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    
    with app.app_context():
        db.create_all()

    return app, db
