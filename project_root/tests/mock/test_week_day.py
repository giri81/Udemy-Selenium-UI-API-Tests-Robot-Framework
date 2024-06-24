import datetime
import logging
import unittest
from unittest.mock import patch

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_weekday():
    """
    Determines if today is a weekday.

    Returns:
        bool: True if today is a weekday (Monday to Friday), False otherwise.
    """
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5

class MockDateTime(datetime.datetime):
    """
    Custom mock class for datetime.datetime to override the today() method.

    This class inherits from datetime.datetime and overrides the today() method
    to return a predefined date for testing purposes.
    """
    @classmethod
    def today(cls):
        """
        Override the today() method to return a predefined date.

        Returns:
            datetime: The mocked current date.
        """
        return cls._today

class TestIsWeekday(unittest.TestCase):
    """
    Test case for the is_weekday function.
    """
    def setUp(self):
        """
        Set up the test case with predefined dates.
        """
        self.june_18_2024 = datetime.datetime(year=2024, month=6, day=18)  # Tuesday
        self.june_17_2024 = datetime.datetime(year=2024, month=6, day=17)  # Monday
        self.june_16_2024 = datetime.datetime(year=2024, month=6, day=16)  # Sunday

    def test_june_18_2024_is_weekday(self):
        """
        Test that June 18, 2024 is a weekday.
        """
        with patch('datetime.datetime', MockDateTime):
            MockDateTime._today = self.june_18_2024
            result = is_weekday()
            logging.info("June 18, 2024 is a weekday: %s", result)
            self.assertTrue(result, "June 18, 2024 should be a weekday")

    def test_june_17_2024_is_weekday(self):
        """
        Test that June 17, 2024 is a weekday.
        """
        with patch('datetime.datetime', MockDateTime):
            MockDateTime._today = self.june_17_2024
            result = is_weekday()
            logging.info("June 17, 2024 is a weekday: %s", result)
            self.assertTrue(result, "June 17, 2024 should be a weekday")

    def test_june_16_2024_is_not_weekday(self):
        """
        Test that June 16, 2024 is not a weekday.
        """
        with patch('datetime.datetime', MockDateTime):
            MockDateTime._today = self.june_16_2024
            result = is_weekday()
            logging.info("June 16, 2024 is a weekday: %s", result)
            self.assertFalse(result, "June 16, 2024 should not be a weekday")

if __name__ == "__main__":
    unittest.main()
