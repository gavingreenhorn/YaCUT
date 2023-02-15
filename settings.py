# import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # не проходит не-локальный pytest
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    # SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SECRET_KEY = 'whatever'
