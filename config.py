import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql:///warcraft_logs')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql:///warcraft_logs_test')
    SECRET_KEY = 'testing'
