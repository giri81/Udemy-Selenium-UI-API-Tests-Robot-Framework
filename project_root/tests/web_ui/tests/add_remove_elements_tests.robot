*** Settings ***
Library    SeleniumLibrary
Library    TestPage.py
Variables  ../pages/variables.py
Suite Setup     Open Homepage    ${BROWSER}    ${HOMEPAGE_URL}
Suite Teardown  Close Browser Session

*** Test Cases ***
Add Remove Elements Test Page Functionality (Chrome Browser)
    [Documentation]    Test the functionality of the-internet.herokuapp.com's Add/Remove Elements page using Chrome browser
    Log    This is your test case steps...
    Sleep    2s

*** Keywords ***
Open Homepage
    [Arguments]    ${browser}   ${url}
    Log    open url and maximize the window
    open browser to homepage    ${browser}  ${url}

Close Browser Session
    Close All Browsers
