from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'chave_segura')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@localhost/p1_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'outra_chave_secreta_segura')
    


print(Config.SQLALCHEMY_DATABASE_URI)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)

    jwt = JWTManager(app)
    
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_SECURE'] = False  # Deve ser True em produção
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    print(os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@localhost/p1_db'))

    from .views import api_bp
    print('hi, this is the uri:', Config.SQLALCHEMY_DATABASE_URI)
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app