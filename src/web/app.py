# src/web/app.py
import os

from flask import Flask
from flask_cors import CORS

from .socket import initialize
from .api import blueprint as api_blueprint, api


# Get environment variables
APP_ENV = os.environ.get("APP_ENV")
APP_NAME = os.environ.get("APP_NAME")
HOST_IP = os.environ.get("HOST_IP")
HTTP_PORT = os.environ.get("HTTP_PORT")
HTTPS_PORT = os.environ.get("HTTPS_PORT")
TCP_PORT = os.environ.get("TCP_PORT")
SOCKET_PORT = os.environ.get("SOCKET_PORT")

httpPortNumber = int(HTTP_PORT)
httpsPortNumber = int(HTTPS_PORT)
tcpPortNumber = int(TCP_PORT)
socketPortNumber = int(SOCKET_PORT)


def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Cross-Origin Resource Sharing
    CORS(app, origins="*")

    # This can help the application run in an optimized manner.
    app.config["ENV"] = APP_ENV

    # Register the API Blueprint with a URL prefix
    app.register_blueprint(api_blueprint, url_prefix="/api")

    # Get API paths from the request object
    paths = [
        rule.rule
        for rule in app.url_map.iter_rules()
        if rule.endpoint.startswith("api.")
    ]

    # Ability to access endpoints via socket.
    io = initialize(app, api, paths)

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

    print(
        "app start",
        {
            "APP_ENV": APP_ENV,
            "HOST_IP": HOST_IP,
            "httpPortNumber": httpPortNumber,
        },
    )

    return app, io, None, None


# Listen for HTTP and WebSocket connections on the same port
app, io, _, _ = create_app()
