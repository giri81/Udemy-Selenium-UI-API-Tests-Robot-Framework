*** Settings ***
Documentation    A resource file with reusable keywords and variables.
...              three dots enable multiple lines documentation.
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${user_name}            test@gmail.com
${invalid_password}     test
${url}                  https://rahulshettyacademy.com/locatorspractice/            

*** Keywords ***
open the browser with mortgage payment with url
    Create Webdriver    Chrome
    Go To               ${url}

Close Browser Session
    Close Browser