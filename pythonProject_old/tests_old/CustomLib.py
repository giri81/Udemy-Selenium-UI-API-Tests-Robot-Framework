from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Credentials and URLs
USERNAME = "mock.user.girish@gmail.com"
PASSWORD = "mock"
GMAIL_SIGN_URL = r"https://mail.google.com/"

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

def enter_username():
    """
    Function to navigate to Gmail sign-in page and maximize the window.
    """
    driver.get(GMAIL_SIGN_URL)
    driver.maximize_window()
