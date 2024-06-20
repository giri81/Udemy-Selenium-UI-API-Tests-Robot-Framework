# my_module.py

import requests
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_data(url):
    """
    Fetch data from the given URL.

    Parameters:
    url (str): The URL to fetch data from.

    Returns:
    dict: The JSON response if the status code is 200.
    None: If the status code is not 200.
    """
    logger.info(f"Fetching data from URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        logger.info("Data fetched successfully.")
        return response.json()
    else:
        logger.warning(f"Failed to fetch data. Status code: {response.status_code}")
        return None
