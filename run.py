"""
run.py used to run the application locally
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()