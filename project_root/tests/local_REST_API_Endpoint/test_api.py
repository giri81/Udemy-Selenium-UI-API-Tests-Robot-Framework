import os
import requests
import unittest
import subprocess
import time
import logging
from datetime import datetime

# Create a logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Get the path to the api_server.py script
        script_path = os.path.join('utils', 'api_server.py')
        # Start the API server as a subprocess
        cls.server_process = subprocess.Popen(['python', script_path])
        # Wait for the server to start
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # Stop the API server
        cls.server_process.terminate()

    def setUp(self):
        # Define the base URL for the local API endpoint
        self.base_url = 'http://localhost:8000'

    def test_get_request(self):
        # Send a GET request to the API endpoint
        response = requests.get(self.base_url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        self.log_assert("Response status code", 200, response.status_code)

        # Assert that the response content type is JSON
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.log_assert("Response content type", 'application/json', response.headers['Content-Type'])

        # Assert that the response body contains the expected message
        expected_message = {'message': 'Hello, this is your REST API response!'}
        self.assertEqual(response.json(), expected_message)
        self.log_assert("Response body", expected_message, response.json())

    def log_assert(self, message, expected, actual):
        # Generate a log file name with timestamp
        log_file = os.path.join('logs', f'test_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt')
        # Configure logging to write to the new log file
        logging.basicConfig(filename=log_file, filemode='a', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        # Log the assert message along with expected and actual values
        logging.info(f"{message}: Expected - {expected}, Actual - {actual}")


if __name__ == '__main__':
    unittest.main()
