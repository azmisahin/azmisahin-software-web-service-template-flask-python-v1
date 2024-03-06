# src/web/app.py
import os
from flask import Flask

# Get environment variables
APP_ENV = os.environ.get("APP_ENV")
APP_NAME = os.environ.get("APP_NAME")

# Create Flask app instance
app = Flask(__name__)


@app.route("/")
def home():
    """API Gateway Home

    Returns:
        dict: JSON response containing welcome message, application name, and environment.
    """
    return {
        "message": "Welcome to the API Gateway!",
        "application": APP_NAME,
        "environment": APP_ENV,
    }


if __name__ == "__main__":
    app.run()
