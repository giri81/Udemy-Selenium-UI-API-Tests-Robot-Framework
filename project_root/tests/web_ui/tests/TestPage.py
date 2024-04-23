from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.WebDriverFactory import WebDriverFactory
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException

from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.keys import Keys
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
    def open_the_homepage(self, browser='chrome', url=None):
        """
        Opens the browser and navigates to the home page.
        """
        self.driver = WebDriverFactory.create_driver(browser)
        self._navigate_to_homepage(url)

    @keyword
    def _navigate_to_homepage(self, url=None):
        """
        Navigates to the home page.
        """
        homepage = HomePage(self.driver, url)
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
    def verify_page_contains_element(self, byid, text):
        """
        Verifies that the page contains the specified text.
        """
        locator = (By.ID, byid)
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            element = self.driver.find_element(*locator)
            assert text in element.text, f"Expected text '{text}' not found on the page. Actual text: '{element.text}'"
        except Exception as e:
            raise AssertionError(f"Failed to verify page contains text: {e}")

    @keyword
    def click_with_xpath(self, xpath):
        """
        Clicks the button using the provided XPath.
        """
        try:
            # Wait for the button to be clickable
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            # Ensure button is visible and enabled
            if button.is_displayed() and button.is_enabled():
                button.click()
            else:
                raise AssertionError("Button is not visible or enabled")
        except Exception as e:
            raise AssertionError(f"Failed to click button with XPath '{xpath}': {e}")

    @keyword
    def check_for_broken_images(self):
        """
        Checks for broken images on the page.
        """
        try:
            images = self.driver.find_elements(By.TAG_NAME, 'img')
            broken_images = []
            for image in images:
                src = image.get_attribute('src')
                response = requests.head(src)
                if response.status_code != 200:
                    broken_images.append(src)

            if broken_images:
                print(f"Broken images found: {', '.join(broken_images)}")
            else:
                raise AssertionError("No broken images found on the page.")

        except NoSuchElementException:
            raise AssertionError("No images found on the page.")

        except TimeoutException:
            raise TimeoutException("Page did not load in time.")

    @keyword
    def check_checkbox_with_xpath(self, checkbox_xpath):
        """
        Checks the checkbox with the specified XPath.
        """
        try:
            checkbox = self.driver.find_element(By.XPATH, checkbox_xpath)
            if not checkbox.is_selected():
                checkbox.click()
        except Exception as e:
            raise AssertionError(f"Failed to check checkbox with XPath '{checkbox_xpath}': {e}")


    @keyword
    def uncheck_checkbox_with_xpath(self, checkbox_xpath):
        """
        Unchecks the checkbox with the specified XPath.
        """
        try:
            checkbox = self.driver.find_element(By.XPATH, checkbox_xpath)
            if checkbox.is_selected():
                checkbox.click()
        except Exception as e:
            raise AssertionError(f"Failed to uncheck checkbox with XPath '{checkbox_xpath}': {e}")

    @keyword
    def verify_file_exists(self, folder_path, filename):
        """
        Verifies if the file exists in the given folder path.

        Arguments:
        - folder_path: The absolute path of the folder where the file is expected to exist.
        - filename: The name of the file to be checked.
        """
        import os

        file_path = os.path.join(folder_path, filename)
        if os.path.exists(file_path):
            print(f"File '{filename}' exists in the folder '{folder_path}'.")
        else:
            raise AssertionError(f"File '{filename}' does not exist in the folder '{folder_path}'.")

    @keyword
    def perform_form_authentication(self, username, password, login_button_xpath):
        """
        Performs Form Authentication by entering the provided username and password,
        and clicking the login button.

        Arguments:
        - username: The username to be entered in the form.
        - password: The password to be entered in the form.
        - login_button_xpath: The XPath of the login button.
        """
        try:
            # Enter username
            username_field = self.driver.find_element(By.ID, 'username')
            username_field.clear()
            username_field.send_keys(username)

            # Enter password
            password_field = self.driver.find_element(By.ID, 'password')
            password_field.clear()
            password_field.send_keys(password)

            # Click login button
            login_button = self.driver.find_element(By.XPATH, login_button_xpath)
            login_button.click()
        except Exception as e:
            raise AssertionError(f"Failed to perform form authentication: {e}")

    @keyword
    def click_allow_on_popup(self):
        """
        Clicks the 'Allow' button on a popup window.
        """
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("No popup alert found or unable to switch to alert.")

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
