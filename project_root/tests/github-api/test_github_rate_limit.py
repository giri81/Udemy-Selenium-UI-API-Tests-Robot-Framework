import unittest
import requests
import logging  # Importing the logging module for logging test results
import os  # Importing the os module for file operations
from datetime import datetime  # Importing datetime module to generate timestamp
from utils.github_api_utils import GitHubAPIUtils  # Importing the GitHubAPIUtils class for constructing GitHub API URLs

# Create a logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Generate a new log file name with timestamp
log_file = os.path.join('logs', f'test_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt')

# Configure logging to write to the new log file
logging.basicConfig(filename=log_file, filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class GitHubRateLimitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class by defining common test data and resources.
        """
        cls.rate_limit_endpoint = GitHubAPIUtils.fetch_rate_limit_endpoint()
        logging.info(f"rate limit end point: {cls.rate_limit_endpoint}")

    def test_fetch_rate_limit(self):
        """Tests fetching and logging the current rate limit."""

        url = self.rate_limit_endpoint  # Rate limit endpoint

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)  # Assert successful response

        if response.json():  # Check for successful JSON parsing
            data = response.json()
            # Access specific rate limit information from the response data
            # (e.g., core.limit, core.remaining)
            logging.info(f"Rate Limit Information:")
            logging.info(f"- Limit: {data['resources']['core']['limit']}")
            logging.info(f"- Remaining: {data['resources']['core']['remaining']}")
        else:
            logging.info("Error: Failed to parse response as JSON")


if __name__ == '__main__':
    unittest.main()
