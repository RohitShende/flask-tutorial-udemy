"""
Initializing the flask flask_restplus_app
"""
from flask import Flask

from flask_restplus_app.apis_v1 import blueprint as v1_blueprint
from flask_restplus_app.views import main as main_blueprint


def create_app():
    """
    Create flask_restplus_app is used to create the flask flask_restplus_app and return
    the flask_restplus_app object
    Returns:
        flask flask_restplus_app object
    """
    app = Flask(__name__)

    # register the blueprints
    app.register_blueprint(main_blueprint, url_prefix="/")
    app.register_blueprint(v1_blueprint)

    return app
