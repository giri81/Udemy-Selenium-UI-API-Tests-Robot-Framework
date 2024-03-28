*** Settings ***
Library    SeleniumLibrary
Library    TestPage.py
Variables  pages/variables.py

*** Test Cases ***
Test Page Functionality
    [Documentation]    Test the functionality of the website in the specified browser. Available browser options:\n
    ...                `${BROWSER}`: Default browser value (chrome).
    ...                `${BROWSER_FIREFOX}`: Firefox browser.
    ...                `${BROWSER_EDGE}`: Edge browser.
    Open Homepage    ${BROWSER_EDGE}    ${HOMEPAGE_URL}
    Sleep    2s
    Close Browser Session

*** Keywords ***
Open Homepage
    [Arguments]    ${browser}   ${url}
    Log    open url and maximize the window
    open browser to homepage    ${browser}  ${url}

Close Browser Session
    Close All Browsers
