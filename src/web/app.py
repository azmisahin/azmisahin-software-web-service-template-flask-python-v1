# src/web/app.py
import os
from flask import Flask
from .api import blueprint as api_blueprint

# Get environment variables
APP_ENV = os.environ.get("APP_ENV")
APP_NAME = os.environ.get("APP_NAME")

# Create Flask app instance
app = Flask(__name__)

# Register the API Blueprint
app.register_blueprint(api_blueprint, url_prefix="/api")


# Get API paths from the request object
paths = [
    rule.rule for rule in app.url_map.iter_rules() if rule.endpoint.startswith("api.")
]


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
        "paths": paths,
    }


if __name__ == "__main__":
    app.run()
