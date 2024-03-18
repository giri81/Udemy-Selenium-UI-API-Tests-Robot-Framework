*** Settings ***
Documentation    To validate the login form
Library    SeleniumLibrary
Test Setup    open the browser with gmail signin url
Test Teardown    Close Browser Session
Resource    resource.robot

*** Variables ***
${error_web_element}    class:error

*** Test Cases ***
Validate Gmail Successful Login
     Fill the gmail signin form and click    ${user_name}
#    wait until it checks and display error message
#    verify error message is correct

*** Keywords ***
Fill the gmail signin form and click
    [Arguments]    ${username}
    Sleep    5
    Input Text    id:identifierId    ${username}



