# src/web/app.py
import os
from flask import Flask
from .api import blueprint as api_blueprint
from gevent.pywsgi import WSGIServer  # Import the WSGIServer from gevent

# Get environment variables
APP_ENV = os.environ.get("APP_ENV")
APP_NAME = os.environ.get("APP_NAME")
HOST_IP = os.environ.get("HOST_IP")
TCP_PORT = os.environ.get("TCP_PORT")


def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Register the API Blueprint with a URL prefix
    app.register_blueprint(api_blueprint, url_prefix="/api")

    # Get API paths from the request object
    paths = [
        rule.rule
        for rule in app.url_map.iter_rules()
        if rule.endpoint.startswith("api.")
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

    return app


# Build Flask app to migrate to Gunicorn
app = create_app()

if __name__ == "__main__":
    # Run the Flask app using Gunicorn
    http_server = WSGIServer((HOST_IP, TCP_PORT), app)
    http_server.serve_forever()
