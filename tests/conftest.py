"""
This is a conftest file needed for pytest
"""
import pytest

from flask_restplus_app import create_app

print("Creating flask_restplus_app...")
application = create_app()


@pytest.fixture
def app():
    """
    This is a fixture that returns the application which is
    then used by pytest with the name 'client' to test the application

    Returns:

    """
    return application
