*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle2
    Set Passwords  kalle123  kalle123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Passwords  kalle123  kalle123
    Submit Credentials
    Registration Should Fail With Message  Username too short

Register With Taken Username
    Set Username  kalle
    Set Passwords  kalle123  kalle123
    Submit Credentials
    Registration Should Fail With Message  User with username kalle already exists

Register With Valid Username And Too Short Password
    Set Username  kalle2
    Set Passwords  kalle1  kalle1
    Submit Credentials
    Registration Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle2
    Set Passwords  kalle123  kalle321
    Submit Credentials
    Registration Should Fail With Message  Nonmatching passwords

Password only contains letters
    set Username  kalle2
    Set Passwords  kallekalle  kallekalle
    Submit Credentials
    Registration Should Fail With Message  Password too simple

Login After Successful Registration
    Set Username  kalle2
    Set Passwords  kalle123  kalle123
    Submit Credentials
    Go To Login Page
    Input Text  username  kalle2
    Input Password  password  kalle123
    Click Button  Login
    Login Should Succeed


Login After Failed Registration
    Set Username  kalle3
    Set Passwords  kallekalle  kallekalle
    Submit Credentials
    Go To Login Page
    Input Text  username  kalle3
    Input Password  password  kallekalle
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Passwords
    [Arguments]  ${password1}  ${password2}
    Input Password  password  ${password1}
    Input Password  password_confirmation  ${password2}

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}
