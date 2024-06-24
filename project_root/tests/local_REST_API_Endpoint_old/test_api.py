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

    def test_get_request_1(self):
        # Send a GET request to the API endpoint
        response = requests.get(self.base_url)

        try:
            # Assert that the response status code is 200 (OK)
            self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")

            # Assert that the response content type is JSON
            self.assertEqual(response.headers.get('Content-Type'), 'application/json',
                             f"Expected content type 'application/json' but got {response.headers.get('Content-Type')}")

            # Assert that the response body contains the expected message
            expected_message = {'message': 'Hello, this is your REST API response!'}
            self.assertEqual(response.json(), expected_message,
                             f"Expected response body {expected_message} but got {response.json()}")

            # Log mock pass status
            self.log_test_status("test_get_request_1", "PASS")
        except AssertionError as e:
            # Log the failure details
            self.log_test_failure("test_get_request_1", str(e))

    def test_get_request_2(self):
        # Send a GET request to the API endpoint
        response = requests.get(self.base_url)

        try:
            # Assert that the response status code is 200 (OK)
            self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")

            # Assert that the response content type is JSON
            self.assertEqual(response.headers.get('Content-Type'), 'application/json',
                             f"Expected content type 'application/json' but got {response.headers.get('Content-Type')}")

            # Assert that the response body contains the expected message
            expected_message = {'message': 'Welcome to the API!'}
            self.assertEqual(response.json(), expected_message,
                             f"Expected response body {expected_message} but got {response.json()}")

            # Log mock pass status
            self.log_test_status("test_get_request_2", "PASS")
        except AssertionError as e:
            # Log the failure details
            self.log_test_failure("test_get_request_2", str(e))

    def log_test_status(self, test_name, status):
        # Generate a log file name with timestamp
        log_file = os.path.join('logs', f'test_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt')
        # Configure logging to write to the new log file
        logging.basicConfig(filename=log_file, filemode='a', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        # Log the mock status
        logging.info(f"{test_name} - {status}")

    def log_test_failure(self, test_name, failure_details):
        # Generate a log file name with timestamp
        log_file = os.path.join('logs', f'test_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt')
        # Configure logging to write to the new log file
        logging.basicConfig(filename=log_file, filemode='a', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        # Log the mock failure details along with expected and actual values
        logging.info(f"{test_name} - FAILED: {failure_details}")


if __name__ == '__main__':
    unittest.main()
