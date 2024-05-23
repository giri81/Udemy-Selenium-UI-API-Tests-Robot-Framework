*** Settings ***
Library           Process
Library           SeleniumLibrary
Suite Setup       Start Django Server
Suite Teardown    Stop Django Server

*** Variables ***
${MANAGE.PY}      simplesocial/manage.py
${PORT}           8000

*** Keywords ***
Start Django Server
    Start Process    python    ${MANAGE.PY}    runserver    ${PORT}    shell=True
    Sleep            5s

Stop Django Server
    Terminate All Processes

*** Test Cases ***
Example Test
    [Documentation]    This is an example test case to ensure the server is running.
    Open Browser    http://localhost:${PORT}    Chrome
    Sleep    5s
    Close Browser
