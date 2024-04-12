*** Settings ***
Library    SeleniumLibrary
Library    TestPage.py
Variables  ../pages/variables.py
Resource    resource.txt
# Suite Setup
# Suite Teardown

*** Test Cases ***
File download Test Page
    [Documentation]    Test the download functionality
    [Tags]    Integration
    Log    open home url
    Open Homepage    ${BROWSER}    ${HOMEPAGE_URL}
    Log    Click on link
    Click With Xpath    //*[@id="content"]/ul/li[17]/a
    Sleep    2s
    Log    Click to download file
    Click With Xpath    //*[@id="content"]/div/a[1]
    Sleep    10s
    Verify File Exists    ${folder_path}    ${filename}
    Close Browser Session



