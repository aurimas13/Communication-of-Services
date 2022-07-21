"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

TESTING = False
DEBUG = False
FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY')
SERVER_NAME = environ.get('SERVER_NAME')
TARGET_FILE_LOCATION = path.dirname(path.abspath(__file__))
