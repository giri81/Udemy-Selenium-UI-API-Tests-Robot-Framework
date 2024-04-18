*** Settings ***
Library    SeleniumLibrary
Library    TestPage.py
Variables  ../pages/variables.py
Resource   resource.txt

*** Test Cases ***
Form Authentication
    [Documentation]    Test for FormAuthentication
    [Tags]    Smoke
    Open Homepage    ${BROWSER}    ${HOMEPAGE_URL}
    Log    Click web element "Form Authentication"
    Click With Xpath    //*[@id="content"]/ul/li[21]/a
    Sleep    2s
    Log    Verifying the page is loaded
    Verify Page Contains Element    content    Login Page
    Log    Performs Form Authentication by entering the provided username and password and clicking the login button.
    Perform Form Authentication    ${FORM_USERNAME}    ${FORM_PASSWORD}    //*[@id="login"]/button/i
    Log    Verify if login is successful
    Verify Page Contains Element    content    Secure Area
    Sleep    2s
    Close Browser Session


