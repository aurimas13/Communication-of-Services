"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

PORT = environ.get('PORT')
TARGET_FILE_LOCATION = environ.get("TARGET_FILE_LOCATION") if environ.get("TARGET_FILE_LOCATION") != '' else path.dirname(path.abspath(__file__)) + '/output/events.json'
FLASK_APP = 'main.py'
