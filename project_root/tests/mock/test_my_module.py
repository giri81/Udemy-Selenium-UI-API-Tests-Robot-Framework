# test_my_module.py

import unittest
from unittest.mock import patch
import my_module
import logging

# Set up logging configuration for tests
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestFetchData(unittest.TestCase):
    """
    Unit tests for the fetch_data function in my_module.
    """

    @patch('my_module.requests.get')
    def test_fetch_data_success(self, mock_get):
        """
        Test fetch_data returns the correct data on a successful API call.

        Parameters:
        mock_get (Mock): The mock object for requests.get.

        Returns:
        None
        """
        logger.info("Starting test_fetch_data_success")

        # Create a mock response object with the expected properties
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}

        url = "http://example.com/api"
        result = my_module.fetch_data(url)

        # Assertions
        mock_get.assert_called_once_with(url)
        logger.debug(f"mock_get called with URL: {url}")
        self.assertEqual(result, {"key": "value"})
        logger.debug(f"Expected result received: {result}")

    @patch('my_module.requests.get')
    def test_fetch_data_failure(self, mock_get):
        """
        Test fetch_data returns None on a failed API call.

        Parameters:
        mock_get (Mock): The mock object for requests.get.

        Returns:
        None
        """
        logger.info("Starting test_fetch_data_failure")

        # Create a mock response object with the expected properties
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        url = "http://example.com/api"
        result = my_module.fetch_data(url)

        # Assertions
        mock_get.assert_called_once_with(url)
        logger.debug(f"mock_get called with URL: {url}")
        self.assertIsNone(result)
        logger.debug("Expected result received: None")


if __name__ == '__main__':
    unittest.main()
