import os
from routes import routes

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

api = Flask(__name__)
api.config.from_pyfile("config.py") # +

api.register_blueprint(routes)

if __name__ == "__main__":
    api.run()
