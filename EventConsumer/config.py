"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

PORT = environ.get('PORT')
TARGET_FILE_LOCATION = path.dirname(path.abspath(_file_)) + '/output/events.json'

if environ.get("TARGET_FILE_LOCATION") != '':
    TARGET_FILE_LOCATION = environ.get("TARGET_FILE_LOCATION")
