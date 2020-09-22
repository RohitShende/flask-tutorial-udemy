"""
Initializing the flask app
"""
from flask import Flask

from app.apis_v1 import blueprint as v1_blueprint
from app.views import main as main_blueprint


def create_app():
    """
    Create app is used to create the flask app and return the app object
    Returns:
        flask app object
    """
    app = Flask(__name__)

    # register the blueprints
    app.register_blueprint(main_blueprint, url_prefix="/")
    app.register_blueprint(v1_blueprint)

    return app
