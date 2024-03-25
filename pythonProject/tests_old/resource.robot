*** Settings ***
Documentation    A resource file with reusable keywords and variables.
...              three dots enable multiple lines documentation.
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${user_name}            test@gmail.com
${invalid_password}     test
${password}             test
${url}                  https://rahulshettyacademy.com/locatorspractice/
${gmail-sign-url}       https://mail.google.com/

*** Keywords ***
open the browser with mortgage payment with url
    Create Webdriver    Chrome
    Go To               ${url}

Close Browser Session
    Close Browser
    
open the browser with gmail signin url
    Create Webdriver    Chrome
    Go To               ${gmail-sign-url}
    Maximize Browser Window
