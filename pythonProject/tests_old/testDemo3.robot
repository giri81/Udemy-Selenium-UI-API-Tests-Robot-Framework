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
     Sleep    2s    # Wait for loading
#    wait until it checks and display error message
#    verify error message is correct

*** Keywords ***
Press Tab and Hit Enter
    [Documentation]    Executes JavaScript to remove the focus from the currently focused element.
    ...                 Then, simulates pressing the Tab and Enter keys without specifying any element locator.
    Execute JavaScript    document.activeElement.blur()
    Press Keys    None    \\9    # Press Tab key (ASCII code for Tab is 9)
    Press Keys    None    \\13   # Press Enter key (ASCII code for Enter is 13)




Fill the gmail signin form and click
    [Arguments]    ${username}
    Sleep    2s
    Input Text    id:identifierId    ${username}
    Sleep    2s
    Press Tab and Hit Enter
    Sleep    2s    # Wait for page to load



