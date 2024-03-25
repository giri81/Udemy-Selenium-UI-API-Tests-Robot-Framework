# login_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """
    Class representing the login page of the website.
    """

    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    login_button = (By.CSS_SELECTOR, '#login > button')

    def enter_credentials(self, username, password):
        """
        Enters the provided username and password into the respective input fields.

        Args:
            username: The username to be entered.
            password: The password to be entered.
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        """
        Clicks on the login button.
        """
        self.driver.find_element(*self.login_button).click()
