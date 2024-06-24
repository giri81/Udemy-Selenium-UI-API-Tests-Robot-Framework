import requests
import unittest
import xmlrunner
import logging
import time
from api_helpers import authenticate_api

# Generate a unique timestamp to use in the log file name
timestamp = time.strftime("%Y%m%d_%H%M%S")

# Configure logging settings with a unique log file name
log_file = f"test_{timestamp}.log"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=log_file)


class TestAPI(unittest.TestCase):
    def setUp(self):
        logging.info("Starting mock case...")

    def tearDown(self):
        logging.info("Finishing mock case...")

    def test_authentication_success(self):
        logging.info("Executing test_authentication_success...")
        # Positive mock: Correct credentials
        response = requests.get("https://the-internet.herokuapp.com/digest_auth",
                                auth=authenticate_api("admin", "admin"))
        self.assertEqual(response.status_code, 200)
        # Log the outcome of the assertion
        if response.status_code == 200:
            logging.info("Assertion passed: Response status code is 200")
        else:
            logging.error("Assertion failed: Response status code is not 200")

    def test_authentication_failure(self):
        logging.info("Executing test_authentication_failure...")
        # Negative mock: Incorrect credentials
        response = requests.get("https://the-internet.herokuapp.com/digest_auth",
                                auth=authenticate_api("invalid_username", "invalid_password"))
        # Verify that the response status code indicates authentication failure
        self.assertNotEqual(response.status_code, 200)
        # Log the outcome of the assertion
        if response.status_code != 200:
            logging.info("Assertion passed: Response status code indicates authentication failure")
        else:
            logging.error("Assertion failed: Response status code does not indicate authentication failure")


if __name__ == "__main__":
    # Use XMLTestRunner to generate XML mock report
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='mock-reports'), exit=False)
