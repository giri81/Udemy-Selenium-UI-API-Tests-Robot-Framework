*** Settings ***
Library    SeleniumLibrary
Library    TestPage.py
#Resource   resources.robot

*** Test Cases ***
Test Page Functionality in Chrome
    [Documentation]    Test the functionality of the website in Chrome
    Open Browser To Homepage    chrome
    # Add your test steps here
    Close Browser Session

Test Page Functionality in Firefox
    [Documentation]    Test the functionality of the website in Firefox
    Open Browser To Homepage    firefox
    # Add your test steps here
    Close Browser Session

Test Page Functionality in Edge
    [Documentation]    Test the functionality of the website in Edge
    Open Browser To Homepage    edge
    # Add your test steps here
    Close Browser Session
