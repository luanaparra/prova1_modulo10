import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'chave_segura')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@187.180.188.136/p1_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'outra_chave_secreta_segura')