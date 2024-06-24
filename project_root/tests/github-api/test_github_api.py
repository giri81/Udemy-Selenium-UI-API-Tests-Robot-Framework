import unittest  # Importing the unittest module for creating mock cases
import requests  # Importing the requests module for making HTTP requests
import logging  # Importing the logging module for logging mock results
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


class TestGitHubAPI(unittest.TestCase):
    """
    A mock case class for testing GitHub API functionality.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the mock class by defining common mock data and resources.
        """
        cls.owner = 'giri81'
        cls.repo_name = 'Udemy-Selenium-UI-API-Tests-Robot-Framework'
        cls.url = GitHubAPIUtils.create_repo_url(cls.owner, cls.repo_name)
        logging.info(f"Setting up class: Owner - {cls.owner}, Repo Name - {cls.repo_name}, URL - {cls.url}")

    def test_response_code(self):
        """
        Test the response code of the GitHub API request.
        """
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)
        logging.info(f"Response code mock passed for URL: {self.url}")

    def test_user_information(self):
        """
        Test the user information retrieved from the GitHub API response.
        """
        response = requests.get(self.url)
        repo_info = response.json()
        self.assertEqual(repo_info['owner']['login'], self.owner)
        self.assertEqual(repo_info['name'], self.repo_name)
        logging.info(f"User information mock passed for URL: {self.url}")


if __name__ == '__main__':
    unittest.main()
