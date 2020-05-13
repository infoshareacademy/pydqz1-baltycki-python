*** Settings ***
Documentation       Trello API tests
Library             RequestsLibrary
Library             String
Library             Collections
Library             SeleniumLibrary
Suite Setup         Create Session For Endpoint


*** Variables ***
${URL}                         https://api.trello.com
${API_KEY}                     368d48aa730effc645b49fb64ba9b0fd
${TOKEN}                       d8a6adf89ba3e29f33f93c0c2b0f2f589dc6705bfa6ebdcbb7b9a836c856cc19


*** Test Cases ***
Valid Create Board Request
    [Tags]                          Boards
    ${board_name}                   Generate Random String  8             [LETTERS][NUMBERS]
    ${resp}                         Create Board Request                  ${board_name}
    ${existing_board_id}            Get Id                                ${resp}
    Set Suite Variable              ${BOARD_ID}                           ${existing_board_id}
    Request Should Be Successful    ${resp}
    Validate Response Field         ${resp}                 name          ${board_name}

Valid Create New List Request
    [Tags]                          Lists
    ${list_name}                    Generate Random String     8                   [LETTERS][NUMBERS]
    ${resp}                         Create New List Request    ${list_name}        ${BOARD_ID}
    ${existing_list_id}             Get Id                     ${resp}
    Set Suite Variable              ${LIST_ID}                 ${existing_list_id}
    Request Should Be Successful    ${resp}
    Validate Response Field         ${resp}      name          ${list_name}
    Validate Response Field         ${resp}      idBoard       ${BOARD_ID}

Create New List Request With Invalid Board Id
    [Tags]                          Lists
    ${list_name}                    Generate Random String     8                   [LETTERS][NUMBERS]
    ${invalid_board_id}             Generate Random String     24                  [LETTERS][NUMBERS]
    ${resp}                         Create New List Request    ${list_name}        ${invalid_board_id}
    Status Should Be                400                        ${resp}             msg=invalid value for idBoard

Valid Create New Card Request
    [Tags]                          Cards
    ${card_name}                    Generate Random String     8                   [LETTERS][NUMBERS]
    ${resp}                         Create New Card Request    ${LIST_ID}          ${card_name}
    ${existing_card_id}             Get Id                     ${resp}
    Set Suite Variable              ${CARD_ID}                 ${existing_card_id}
    Request Should Be Successful    ${resp}
    Validate Response Field         ${resp}                    idList               ${LIST_ID}
    Validate Response Field         ${resp}                    name                 ${card_name}

Create New Card Request With Invalid List Id
    [Tags]                          Cards
    ${card_name}                    Generate Random String     8                    [LETTERS][NUMBERS]
    ${invalid_list_id}              Generate Random String     24                   [LETTERS][NUMBERS]
    ${resp}                         Create New Card Request                         ${invalid_list_id}             ${card_name}
    Status Should Be                400                        ${resp}              msg=invalid value for idList

Valid Get Card Request
    [Tags]                             Cards
    ${resp}                            Get Card Request                             ${CARD_ID}
    Request Should Be Successful       ${resp}
    Validate Response Field            ${resp}                 id                   ${CARD_ID}

Get Card Request With Invalid Card Id
    [Tags]                             Cards
    ${invalid_card_id}                 Generate Random String              24                  [LETTERS][NUMBERS]
    ${resp}                            Get Card Request                    ${invalid_card_id}
    Status Should Be                   400                                 ${resp}             msg=invalid id

Valid Delete Card Request
    [Tags]                             Cards
    ${resp}                            Delete Card Request                 ${CARD_ID}
    Request Should Be Successful       ${resp}
    Validate Response Field            ${resp}                 limits      {}

Delete Card Request With Invalid Id
    [Tags]                             Cards
    ${invalid_card_id}                 Generate Random String              24                  [LETTERS][NUMBERS]
    ${resp}                            Delete Card Request                 ${invalid_card_id}
    Status Should Be                   400                                 ${resp}             msg=invalid id

Delete Card Request with Already Deleted Card Id
    [Tags]                             Cards
    ${deleted_card_id}                 Set Variable                        ${CARD_ID}
    ${resp}                            Delete Card Request                 ${deleted_card_id}
    Status Should Be                   404                                 ${resp}             msg=The requested resource was not found.

*** Keywords ***
Create Session For Endpoint
    Create Session      trello                  ${URL}

Get Id
    [Arguments]          ${resp}
    ${resp_dict}         Set Variable           ${resp.json()}
    ${object_id}         Set Variable           ${resp_dict}[id]
    Log                  ${object_id}
    [Return]             ${object_id}

Delete Card Request
    [Arguments]          ${card_id}
    ${params}            Create Dictionary      key=${API_KEY}       token=${TOKEN}
    ${resp}              Delete Request         trello               /1/cards/${card_id}/   params=${params}
    [Return]             ${resp}

Get Card Request
    [Arguments]          ${card_id}
    ${params}            Create Dictionary      key=${API_KEY}       token=${TOKEN}
    ${resp}              Get Request            trello               /1/cards/${card_id}/   params=${params}
    [Return]             ${resp}

Create New Card Request
    [Arguments]          ${list_id}             ${card_name}
    ${params}            Create Dictionary      idList=${list_id}    key=${API_KEY}          token=${TOKEN}      name=${card_name}
    ${resp}              Post Request           trello               /1/cards/               params=${params}
    [Return]             ${resp}

Create New List Request
    [Arguments]          ${list_name}           ${board_id}
    ${params}            Create Dictionary      name=${list_name}    idBoard=${board_id}        key=${API_KEY}   token=${TOKEN}
    ${resp}              Post Request           trello               /1/lists/                  params=${params}
    [Return]             ${resp}

Create Board Request
    [Arguments]          ${board_name}
    ${params}            Create Dictionary      name=${board_name}   key=${API_KEY}          token=${TOKEN}
    ${resp}              Post Request           trello               /1/boards/              params=${params}
    [Return]             ${resp}

Validate Response Field
    [Arguments]                                 ${resp}              ${key}                   ${expected_value}
    ${resp_dict}                                Set Variable         ${resp.json()}
    Dictionary Should Contain Item              ${resp_dict}         ${key}                   ${expected_value}



