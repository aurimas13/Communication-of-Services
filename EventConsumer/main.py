# Created by Aurimas A. Nausedas on 07/23/22.
# Updated by Aurimas A. Nausedas on 07/26/22.

from config import PORT
from src.routes import routes
from flask import Flask


def create_app():
    '''

    :return:
    '''
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.register_blueprint(routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=False, port=PORT)
