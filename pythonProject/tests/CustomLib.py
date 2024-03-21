from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Credentials and URLs
USERNAME = "test.user.girish@gmail.com"
PASSWORD = "test"
GMAIL_SIGN_URL = r"https://mail.google.com/"

# Path to Chromedriver
CHROMEDRIVER_PATH = r"C:\Users\eltsin\chromediver\chromedriver-win64\chromedriver"

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

def enter_username():
    """
    Function to navigate to Gmail sign-in page and maximize the window.
    """
    driver.get(GMAIL_SIGN_URL)
    driver.maximize_window()
