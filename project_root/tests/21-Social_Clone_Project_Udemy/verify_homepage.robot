*** Settings ***
Resource          common.robot
Suite Setup       Start Django Server
Suite Teardown    Stop Django Server

*** Test Cases ***
Verify homepage loaded
    [Documentation]    Verify home page contains the expected text.
    Open Browser    http://localhost:${PORT}    Chrome
    Wait Until Page Contains Element    xpath=/html/body/div/h1    10s
    Element Text Should Be    xpath=/html/body/div/h1    Welcome to Star Social!
    Sleep    5s
    [Teardown]    Close Browser
