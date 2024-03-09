import os
import unittest
import threading
import time
import json
from src.web.app import create_app
import websocket
from dotenv import load_dotenv


class WebSocketTest(unittest.TestCase):
    def setUp(self):
        try:
            load_dotenv(".env")
            # Get environment variables
            SOCKET_PORT = os.environ.get("SOCKET_PORT")
            self.server_host = "localhost"
            self.server_socketPortNumber = int(SOCKET_PORT)

        except Exception as e:
            raise Exception(f"Failed to set up the test environment: {e}")

        # Create a separate thread for the Flask app
        self.thread = threading.Thread(target=self.start_flask_app)
        self.thread.start()

        # Wait for the Flask app to start
        time.sleep(1)

    def tearDown(self):
        # Stop the Flask app and join the thread
        self.io.stop()  # Flask-SocketIO kullanılıyorsa bu şekilde durdurulmalı
        self.thread.join()

    def start_flask_app(self):
        # Start the Flask app in a separate thread
        app, self.io, _, _ = create_app()
        self.app_ctx = app.app_context()
        self.app_ctx.push()
        self.io.run(app, host=f"{self.server_host}", port=self.server_socketPortNumber)

    def test_websocket_connection(self):
        # Replace 'your_host_ip' and 'your_socket_port' with the actual values
        socket_url = f"ws://{self.server_host}:{self.server_socketPortNumber}/socket"

        def on_message(ws, message):
            # Define your expected message handling logic here
            expected_response = {"type": "response", "content": "Expected response"}
            self.assertEqual(json.loads(message), expected_response)

        # Create a WebSocket connection
        ws = websocket.WebSocketApp(socket_url, on_message=on_message)
        ws.run_forever()


if __name__ == "__main__":
    unittest.main()
