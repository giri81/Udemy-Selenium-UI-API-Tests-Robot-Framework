*** Settings ***
Library    SeleniumLibrary
Library    TestPage.py
Variables  ../pages/variables.py
# Suite Setup
# Suite Teardown

*** Test Cases ***
Add Remove Elements Test Page Functionality (Chrome Browser)
    [Documentation]    Test the functionality of the-internet.herokuapp.com's Add/Remove Elements page using Chrome browser
    Open Homepage    ${BROWSER}    ${ADD_REMOVE_ELEMENTS_URL}
    Verify Page Contains Text    Add/Remove Elements
    Click Button With XPath    //*[@id="content"]/div/button
    Sleep    2s
    Log    Add Element Button clicked successfully
    Sleep    2s
    Close Browser Session

*** Keywords ***
Open Homepage
    [Arguments]    ${browser}   ${url}
    Log    Open URL and maximize the window
    Open Browser To Homepage    ${browser}  ${url}

Close Browser Session
    Close All Browsers

