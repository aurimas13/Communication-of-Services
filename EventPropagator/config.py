"""Configuration file"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

WAIT_SECONDS = environ.get('WAIT_SECONDS')
ENDPOINT = environ.get('ENDPOINT')
INPUT_FILE_LOCATION =\
environ.get("INPUT_FILE_LOCATION") if\
environ.get("INPUT_FILE_LOCATION") != '' else\
path.dirname(path.abspath(__file__)) + '/events.json'
