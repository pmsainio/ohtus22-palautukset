*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallo  kallo123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kallo123
    Output Should Contain  Too short a username

Register With Valid Username And Too Short Password
    Input Credentials  kallo  kallo1
    Output Should Contain  Too short a password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallo  salasana
    Output Should Contain  Password too simple

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input New Command

