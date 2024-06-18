import datetime
import logging
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


# Test dates
june_18_2024 = datetime.datetime(year=2024, month=6, day=18)  # Tuesday
june_17_2024 = datetime.datetime(year=2024, month=6, day=17)  # Monday
june_16_2024 = datetime.datetime(year=2024, month=6, day=16)  # Sunday


def test_is_weekday():
    """
    Test the is_weekday function with predefined dates.
    """
    # Test June 18, 2024 is a weekday
    with patch('datetime.datetime', MockDateTime):
        MockDateTime._today = june_18_2024
        result = is_weekday()
        logging.info("June 18, 2024 is a weekday: %s", result)
        assert result, "June 18, 2024 should be a weekday"

    # Test June 17, 2024 is a weekday
    with patch('datetime.datetime', MockDateTime):
        MockDateTime._today = june_17_2024
        result = is_weekday()
        logging.info("June 17, 2024 is a weekday: %s", result)
        assert result, "June 17, 2024 should be a weekday"

    # Test June 16, 2024 is not a weekday
    with patch('datetime.datetime', MockDateTime):
        MockDateTime._today = june_16_2024
        result = is_weekday()
        logging.info("June 16, 2024 is a weekday: %s", result)
        assert not result, "June 16, 2024 should not be a weekday"


if __name__ == "__main__":
    test_is_weekday()
    print("All tests passed.")
