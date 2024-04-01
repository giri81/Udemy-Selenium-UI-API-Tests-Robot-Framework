from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    def open_browser_to_homepage(self, browser='chrome', url=None):
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
    def close_browser_session(self):
        """
        Closes the browser session.
        """
        if self.driver:
            try:
                self.driver.quit()
            except Exception as e:
                print(f"An error occurred while closing the browser: {e}")
