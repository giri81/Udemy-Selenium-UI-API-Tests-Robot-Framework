*** Settings ***
Library    SeleniumLibrary
Library    TestPage.py
Variables  ../pages/variables.py
Resource   resource.txt

*** Test Cases ***
Check First Checkbox
    [Documentation]    Test to check the first checkbox
    Open Homepage    ${BROWSER}    ${HOMEPAGE_URL}
    Log    Click web element "Checkboxes"
    Click With Xpath    //*[@id="content"]/ul/li[6]/a
    Verify Page Contains Element    content    Checkboxes
    Check Checkbox With Xpath    //input[@type='checkbox'][1]
    Sleep    2s
    Close Browser Session

Uncheck Second Checkbox
    [Documentation]    Test to uncheck the second checkbox
    Open Homepage    ${BROWSER}    ${HOMEPAGE_URL}
    Log    Click web element "Checkboxes"
    Click With Xpath    //*[@id="content"]/ul/li[6]/a
    Verify Page Contains Element    content    Checkboxes
    Uncheck Checkbox With Xpath    //input[@type='checkbox'][2]
    Sleep    2s
    Close Browser Session
