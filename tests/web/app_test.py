# tests/web/app_test.py
import unittest
from src.web.app import create_app


class AppTest(unittest.TestCase):

    def setUp(self):
        # Set up a testing configuration and create a test app
        self.app, _, _, _ = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass  # Clean up if needed

    def test_home_endpoint(self):
        # Test the home endpoint
        response = self.client.get("/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("message", data)
        self.assertIn("application", data)
        self.assertIn("environment", data)
        self.assertIn("paths", data)


if __name__ == "__main__":
    unittest.main()
