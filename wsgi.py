"""
Used to run the application on production
"""
from flask_restplus_app import create_app

application = create_app()

if __name__ == "__main__":
    application.run()
