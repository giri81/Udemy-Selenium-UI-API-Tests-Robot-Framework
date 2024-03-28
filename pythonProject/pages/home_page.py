from .base_page import BasePage
from time import sleep


class HomePage(BasePage):
    """
    Class representing the home page of the website.
    """

    def __init__(self, driver, url):
        """
        Constructor for HomePage.

        Args:
            driver: WebDriver instance.
            url: URL of the home page.
        """
        super().__init__(driver)
        self.url = url

    def open(self):
        """
        Opens the home page in the browser.
        """
        self.driver.get(self.url)
        sleep(2)
        self.maximize_browser_window_custom()

    def maximize_browser_window_custom(self):
        """
        Maximizes the browser window using WebDriver's built-in method.
        """
        self.driver.maximize_window()
