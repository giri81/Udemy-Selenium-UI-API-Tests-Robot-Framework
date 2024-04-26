*** Settings ***
Library    SeleniumLibrary
Library    TestPage.py
Variables  ../pages/variables.py
Resource   resource.txt

*** Test Cases ***
Form Authentication
    [Documentation]    Test for Geolocation using Edge browser
    [Tags]    Integration
    Open Homepage    ${BROWSER}    ${HOMEPAGE_URL}
    Log    Click web element "Geolocation"
    Click With Xpath    //*[@id="content"]/ul/li[23]/a
    Sleep    2s
    Log    Verifying the page is loaded
    Verify Page Contains Element    content    Geolocation
    Sleep    2s
    Log    clicking the location button.
    Click With Xpath    //*[@id="content"]/div/button
    Sleep    5s
    Click Allow On Popup
    Sleep    2s
    Close Browser Session


