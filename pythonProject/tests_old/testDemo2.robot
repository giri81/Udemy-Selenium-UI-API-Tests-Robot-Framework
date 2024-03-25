*** Settings ***
Documentation    To validate the login form
Library    SeleniumLibrary
Test Setup    open the browser with mortgage payment with url
Test Teardown    Close Browser Session
Resource    resource.robot

*** Variables ***
${error_web_element}    class:error

*** Test Cases ***
Validate UnSuccessful Login
    Fill the login form
    wait until it checks and display error message
    verify error message is correct

*** Keywords ***
Fill the login form
    Input Text    id:inputUsername    ${username}
    Input Password    name:inputPassword    ${invalid_password}
    Click Button    class:submit

wait until it checks and display error message
    Wait Until Element Is Visible    ${error_web_element}

verify error message is correct
    ${result}=    Get Text    ${error_web_element}
    Should Be Equal As Strings    ${result}     * Incorrect username or password
