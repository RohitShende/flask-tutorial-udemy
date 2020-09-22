"""
common functions needed by different modules
"""
from functools import wraps

from flask import current_app as app
from flask import request

valid_tokens = ["my_token1", "my_token2"]


# ######################### Check token #######################
def check_token(supplied_token):
    """
    Checks the token is valid or not
    Args:
        supplied_token (str): token supplied by the user

    Returns:
        True / False
    """
    return supplied_token in valid_tokens


def token_required(func):
    """
    Decorator to be used with API's which need token for authorization
    """

    @wraps(func)
    def decorated(*args, **kwargs):

        token = None

        if "X-API-KEY" in request.headers:
            token = request.headers["X-API-KEY"]

        if not token:
            return {"message": "Token is missing."}, 401

        if not check_token(token):
            return {"message": "Your token is wrong !!!"}, 401

        app.logger.info("Authenticated Using TOKEN: {}".format(token))
        return func(*args, **kwargs)

    return decorated

# #############################################################################
