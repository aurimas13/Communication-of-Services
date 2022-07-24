import os
from config import PORT
from routes import routes

# from dotenv import load_dotenv
from flask import Flask


# load_dotenv()
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py") # +
    app.register_blueprint(routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=PORT)
