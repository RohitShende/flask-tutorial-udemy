"""
run.py used to run the application locally
"""
from flask_restplus_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=5000)
