# features/steps/web/api/v1/time_service_steps.py

from behave import given, when, then

from src.web.api.v1.time_service import TimeService
from datetime import datetime

from src.web.app import (
    create_app,
)  # Update this import according to your project structure

client = create_app().test_client()

# Let's create the TimeService object
time_service = TimeService()


@given("the Time Service API is running")
def step_given_time_service_api_running(context):
    # If you do not need to make any additional configuration here, you do not need to do anything.
    pass


@when("I request the current time")
def step_when_request_current_time(context):
    # Make a GET request to the /api/v1/time endpoint
    context.response = context.client.get("/api/v1/time")

    # Check if the response status code is 200
    assert context.response.status_code == 200


@then("the response should contain the current time in string format")
def step_then_response_contains_current_time(context):
    assert context.response.status_code == 200
    assert "current_time" in context.response.json

    # Let's get the current time and check if it is in the expected format
    current_time = datetime.now()
    expected_time_format = current_time.strftime("%Y-%m-%d %H:%M:%S")
    assert context.response.json["current_time"] == expected_time_format
