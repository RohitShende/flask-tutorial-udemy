"""
Contains API routes from main flask_restplus_app
"""
from flask import Blueprint
from flask import redirect
from flask import send_file
from flask import url_for

main = Blueprint("main", __name__)


@main.route("/favicon.ico")
def favicon():
    """
    Returns the favicon image
    :return:
    The favicon image
    """

    return send_file("static/favicon.ico", mimetype="image/vnd.microsoft.icon")


@main.route("/api")
def api():
    """
    Redirect to /api.doc
    """

    return redirect(url_for("api.doc"))


@main.route("/")
def index():
    """
    Redirect to /api.doc
    """

    return redirect(url_for("api.doc"))
