# base_page.py

class BasePage:
    """
    Base class representing a generic page.
    """

    def __init__(self, driver):
        """
        Constructor for BasePage.

        Args:
            driver: WebDriver instance used to interact with the web page.
        """
        self.driver = driver
