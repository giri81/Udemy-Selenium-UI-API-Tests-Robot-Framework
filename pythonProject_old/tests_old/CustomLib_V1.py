from selenium import webdriver


class CustomLib_V1(object):

    def __init__(self):
        self.USERNAME = "mock.user.girish@gmail.com"
        self.PASSWORD = "mock"
        self.GMAIL_SIGN_URL = r"https://mail.google.com/"

        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome()

    def enter_username(self):
        """
        Function to navigate to Gmail sign-in page and maximize the window.
        """
        self.driver.get(self.GMAIL_SIGN_URL)
        self.driver.maximize_window()
