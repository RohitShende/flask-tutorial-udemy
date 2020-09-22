"""
This module contains version 1 APIs
"""
from flask import Blueprint
from flask_restplus import Api

from .apis.student import api as student_api

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

authorizations = {"apikey": {"type": "apiKey",
                             "in": "header", "name": "X-API-KEY"}}

api = Api(
    blueprint,
    title="Flask REST API",
    version="1.0",
    description="Version 1 of Flask REST API",
    ordered=True,
    authorizations=authorizations,
    contact_email="rohitshende16@gmail.com",
    validate=True,
)

api.add_namespace(student_api, path="/student")
