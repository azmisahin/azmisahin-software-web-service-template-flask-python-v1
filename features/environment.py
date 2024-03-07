# features/environment.py
from src.web.app import create_app


def before_all(context):
    # Initialize Flask app and set the context.app variable
    context.app = create_app()
    context.client = context.app.test_client()


def after_all(context):
    # Teardown logic if needed
    pass


# Additional hooks and configurations can be added as needed
