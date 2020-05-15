*** Settings ***
Documentation       Trello API tests
Library             RequestsLibrary
Library             String
Library             Collections
Library             SeleniumLibrary
Suite Setup         Create Session For Endpoint
Suite Teardown      Close Browser


*** Variables ***
${URL}                         https://trello.com
${BROWSER}                     chrome
${EMAIL}                       ratodi1378@zaelmo.com
${DOMAIN}                      trello.com
${PASSWORD}                    AnnaKowalskaratodi1378
${USERNAME}                    annakowalska69
${LOG_IN}                      //a[@class='_2ZNy4w8Nfa58d1 _1_raGOZzcyjACT']
${INPUT_USER}                  //input[@id='user']
${INPUT_PASSWORD}              //input[@id='password']
${LOGIN_BTN}                   //input[@id='login']
${SUBMIT_BTN}                  //button[@id='login-submit']//span[@class='css-t5emrf']
${BOARD_TITLE1}                //li[.//text() = 'GUI_test_monika1']
${BOARD_TITLE2}                //li[.//text() = 'GUI_test_monika2']

*** Test Cases ***
Check given board name exists_1
    [Tags]                           Validation
    ${board_title}                   Get Text           ${BOARD_TITLE1}
    Should Be Equal As Strings       ${board_title}     GUI_test_monika1

Check given board name exists_2
    [Tags]                           Validation
    ${board_title}                   Get Text           ${BOARD_TITLE2}
    Should Be Equal As Strings       ${board_title}     GUI_test_monika2

*** Keywords ***
Create Session For Endpoint
    Create Session      trello                  ${URL}
    Open Browser
    ...                                   https://trello.com/login?returnUrl=%2Fannakowalska69%2Fboards
    ...                                   ${BROWSER}
    Log In

Log In
    Input Text                            ${INPUT_USER}         ${EMAIL}
    Click Element                         ${LOGIN_BTN}
    Wait Until Page Contains Element      ${SUBMIT_BTN}
    Input Text                            ${INPUT_PASSWORD}     ${PASSWORD}
    Click Element                         ${SUBMIT_BTN}
    Wait Until Page Contains Element       //*[@id="header"]/div[2]/button[4]/div/span
    ${token}        Get Cookie            token
    Log To Console                        ${token}

