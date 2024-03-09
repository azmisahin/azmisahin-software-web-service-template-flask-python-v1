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

    def test_server_via_http(self):
        # Must be able to connect to the server via http
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("message", data)
        self.assertIn("application", data)
        self.assertIn("environment", data)
        self.assertIn("paths", data)

    def test_server_via_https(self):
        # Must be able to connect to the server via https
        response = self.client.get("/", environ_base={"wsgi.url_scheme": "https"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("message", data)
        self.assertIn("application", data)
        self.assertIn("environment", data)
        self.assertIn("paths", data)

    def test_server_via_socket(self):
        # Must be able to connect to the server via socket
        pass

    def test_server_via_web_socket(self):
        # Must be able to connect to the server via web socket
        pass


if __name__ == "__main__":
    unittest.main()
