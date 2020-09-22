"""
Initializing the flask app
"""
import werkzeug
from flask import Flask

from .apis_v1 import blueprint as v1_blueprint
from .views import main as main_blueprint

werkzeug.cached_property = werkzeug.utils.cached_property


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
