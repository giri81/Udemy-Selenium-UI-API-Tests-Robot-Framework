from robot.api.deco import keyword
from pages.home_page import HomePage
from pages.WebDriverFactory import WebDriverFactory
from time import sleep
import pages.variables as variables  # Import variables.py module


class TestPage:
    """
    Class containing test cases for the website.
    """

    def __init__(self):
        """
        Constructor for TestPage.
        """
        self.driver = None

    @keyword
    def open_browser_to_homepage(self, browser='chrome', url=None):  # Accept 'url' as argument
        """
        Opens the browser and navigates to the home page.

        Args:
            browser: The name of the browser to use (default: 'chrome').
            url: The URL of the home page.
        """
        self.driver = WebDriverFactory.create_driver(browser)
        self._navigate_to_homepage(url)  # Pass 'url' to _navigate_to_homepage

    @keyword
    def _navigate_to_homepage(self, url=None):  # Accept 'url' as argument
        """
        Navigates to the home page.

        Args:
            url: The URL of the home page.
        """
        homepage = HomePage(self.driver, url)  # Pass 'url' to HomePage instance
        homepage.open()
        sleep(2)

    @keyword
    def open_add_remove_elements_page(self):
        """
        Opens the 'Add/Remove Elements' page in the browser.
        """
        add_remove_elements_url = variables.ADD_REMOVE_ELEMENTS_URL
        self.driver.get(add_remove_elements_url)
        sleep(2)

    @keyword
    def close_browser_session(self):
        """
        Closes the browser session.
        """
        if self.driver:
            try:
                self.driver.quit()
            except Exception as e:
                print(f"An error occurred while closing the browser: {e}")

