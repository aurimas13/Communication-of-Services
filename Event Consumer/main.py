import os
from routes import routes

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.config.from_pyfile("config.py") # +

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run()
