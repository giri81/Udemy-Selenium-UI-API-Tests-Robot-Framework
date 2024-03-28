# WebDriverFactory.py

from selenium.webdriver import Chrome, Firefox, Edge


class WebDriverFactory:
    """
    Factory class for creating WebDriver instances.
    """

    @staticmethod
    def create_driver(browser):
        """
        Create a WebDriver instance based on the specified browser.

        Args:
            browser: The name of the browser to use.

        Returns:
            WebDriver instance.
        """
        if browser.lower() == 'chrome':
            return Chrome()
        elif browser.lower() == 'firefox':
            return Firefox()
        elif browser.lower() == 'edge':
            return Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
