# test_page.py

from selenium.webdriver import Chrome
from robot.api.deco import keyword
from pages.home_page import HomePage
from time import sleep


class test_page():
    """
    Class containing test cases for the website.
    """

    def __init__(self):
        """
        Constructor for TestPage.
        """
        self.driver = Chrome()

    @keyword
    def open_browser_to_homepage(self):
        """
        Opens the browser and navigates to the home page.
        """
        homepage = HomePage(self.driver)
        homepage.open()
        sleep(3)

    @keyword
    def close_browser_session(self):
        """
        Closes the browser.
        """
        self.driver.quit()