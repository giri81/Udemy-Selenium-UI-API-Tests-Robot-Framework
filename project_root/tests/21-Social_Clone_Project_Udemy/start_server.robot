*** Settings ***
Resource          common.robot
Suite Setup       Start Django Server
Suite Teardown    Stop Django Server

*** Test Cases ***
Example Test
    [Documentation]    This is an example test case to ensure the server is running.
    Open Browser    http://localhost:${PORT}    Chrome
    Sleep    5s
    [Teardown]    Close Browser
