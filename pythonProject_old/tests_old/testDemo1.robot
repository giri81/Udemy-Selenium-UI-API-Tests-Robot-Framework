*** Settings ***
Documentation    To validate the login form
Library    SeleniumLibrary
Test Teardown    Close Browser
#Resource

*** Variables ***
${error_web_element}    class:error

*** Test Cases ***
Validate UnSuccessful Login
    open the browser with mortgage payment with url
    Fill the login form
    wait until it checks and display error message
    verify error message is correct

*** Keywords ***
open the browser with mortgage payment with url
    Create Webdriver    Chrome
    Go To    https://rahulshettyacademy.com/locatorspractice/

Fill the login form
    Input Text    id:inputUsername    test@gmail.com
    Input Password    name:inputPassword    test
    Click Button    class:submit

wait until it checks and display error message
    Wait Until Element Is Visible    ${error_web_element}

verify error message is correct
    ${result}=    Get Text    ${error_web_element}
    Should Be Equal As Strings    ${result}     * Incorrect username or password
    