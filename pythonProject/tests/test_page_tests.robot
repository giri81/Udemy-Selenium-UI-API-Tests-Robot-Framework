*** Settings ***
Library    SeleniumLibrary
Library    TestPage.py
Resource   resource.txt
Variables  pages/variables.py

*** Test Cases ***
Test Page Functionality
    [Documentation]    Test the functionality of the website in the specified browser. Available browser options:\n
    ...                `${BROWSER}`: Default browser value (chrome).
    ...                `${BROWSER_FIREFOX}`: Firefox browser.
    ...                `${BROWSER_EDGE}`: Edge browser.
    Open Browser To Homepage    ${BROWSER_EDGE}
    Log    Maximizes the browser window
    Maximize Browser Window
    Sleep    4s
    Close Browser Session
