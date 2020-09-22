"""
This is a conftest file needed for pytest
"""
import pytest

from app import create_app

print("Creating app...")
application = create_app()


@pytest.fixture
def app():
    """
    This is a fixture that returns the application which is
    then used by pytest with the name 'client' to test the application

    Returns:

    """
    return application
