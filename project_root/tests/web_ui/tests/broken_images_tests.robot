*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    TestPage.py
Resource    resource.txt
Variables  ../pages/variables.py
# Suite Setup
# Suite Teardown

*** Test Cases ***
Check for Broken Images
    [Documentation]    Verify that there are broken images
    Log    open home url
    Open Homepage    ${BROWSER}    ${HOMEPAGE_URL}
    Log    xpath to test 'broken image' //*[@id="content"]/ul/li[4]/a
    Log    xpath to test 'no broken image' //*[@id="content"]/ul/li[2]/a
    Click With Xpath    //*[@id="content"]/ul/li[4]/a
    Sleep    2s
    Log    using custom keyword check for broken images, Pass for broken img found else error
    Check For Broken Images
    Sleep    2s
    Close Browser Session


