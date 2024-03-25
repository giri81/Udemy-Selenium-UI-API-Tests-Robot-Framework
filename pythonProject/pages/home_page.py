# home_page.py

from .base_page import BasePage


class HomePage(BasePage):
    """
    Class representing the home page of the website.
    """

    url = "https://the-internet.herokuapp.com/"

    def open(self):
        """
        Opens the home page in the browser.
        """
        self.driver.get(self.url)
