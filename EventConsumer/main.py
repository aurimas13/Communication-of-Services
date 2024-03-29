from config import PORT
from src.routes import routes
from flask import Flask


def create_app():
    '''
    Creating a Flask API, loading a configuration file and
    registering API endpoints
    :return: <class 'flask.app.Flask'>
    '''
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.register_blueprint(routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=False, port=PORT)
