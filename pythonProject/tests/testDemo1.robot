*** Settings ***
Documentation    To validate the login form
Library    SeleniumLibrary
#Resource

*** Test Cases ***
Validate UnSuccessful Login
    open the browser with mortgage payment with url
    Fill the login form
    wait until it checks and display error message
    verify error message is correct

*** Keywords ***
open the browser with mortgage payment with url
    
