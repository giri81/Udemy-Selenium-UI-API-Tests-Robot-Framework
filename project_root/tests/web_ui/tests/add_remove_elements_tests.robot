*** Settings ***
Library    SeleniumLibrary
Library    TestPage.py
Variables  ../pages/variables.py
Resource    resource.txt
# Suite Setup
# Suite Teardown

*** Test Cases ***
Add Remove Elements
    [Documentation]    Test Add/Remove Elements
    [Tags]    Smoke
    Log    open home url
    Open Homepage    ${BROWSER}    ${HOMEPAGE_URL}
    Log    click web element "Add/Remove Elements"
    Click With Xpath    //*[@id="content"]/ul/li[2]/a
    Log    verify the Add/Remove Elements page loaded by checking for the Text
    Verify Page Contains element    content    Add/Remove Elements
    Log    Click Add Element Button 
    Click With XPath    //*[@id="content"]/div/button
    Sleep    2s
    Verify Page Contains Element    elements    Delete
    Log    Add Element Button clicked successfully
    Sleep    2s
    Close Browser Session



