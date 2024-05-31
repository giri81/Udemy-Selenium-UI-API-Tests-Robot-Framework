*** Settings ***
Library           Process
Library           SeleniumLibrary

*** Variables ***
${MANAGE.PY}      simplesocial/manage.py
${PORT}           8000

*** Keywords ***
Start Django Server
    Start Process    python    ${MANAGE.PY}    runserver    ${PORT}    shell=True
    Sleep            5s

Stop Django Server
    Terminate All Processes
