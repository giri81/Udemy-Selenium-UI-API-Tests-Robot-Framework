*** Settings ***
Library    SeleniumLibrary
Library    test_page.py

*** Test Cases ***
Test Page Functionality
    [Documentation]    Test the functionality of the website
    Open Browser And Navigate To Homepage
    Close the Browser Session

*** Keywords ***
Open Browser And Navigate To Homepage
    [Documentation]    Open the browser and navigate to the homepage
    Open Browser To Homepage

Close the Browser Session
    [Documentation]    Close the browser
    Close Browser Session