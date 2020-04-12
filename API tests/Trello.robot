*** Settings ***
Documentation       Trello API tests
Library             RequestsLibrary
Library             String
Suite Setup         Create Trello Session

*** Variables ***
${URL}                         https://api.trello.com
${API_KEY}                     1
${TOKEN}                       2

*** Test Cases ***
Get All Boards
    [Tags]                          Boards
    ${resp}     Get Request         trello      /1/members/me/boards?key=${API_KEY}&token=${TOKEN}
    Request Should Be Successful    ${resp}

Create Board
    [Tags]                                            Boards
    ${board_name}           Generate Random String    8           [LETTERS][NUMBERS]
    ${resp}                 Post Request              trello      /1/boards/?name=${board_name}&key=${API_KEY}&token=${TOKEN}
    Request Should Be Successful                      ${resp}
    Validate Board Name In The Response               ${resp}     ${board_name}
    ${existing_board_id}    Collect Board Id          ${resp}
    Set Suite Variable      ${BOARD_ID}               ${existing_board_id}

Get Board With Valid Id
    [Tags]                              Boards
    ${resp}     Get Request             trello              /1/boards/${BOARD_ID}?key=${API_KEY}&token=${TOKEN}
    Request Should Be Successful        ${resp}
    Validate Board Id In The Response   ${resp}             ${BOARD_ID}

Get Board With Invalid Id
    [Tags]                          Boards
    ${invalid_board_id}             Generate Random String    24           [LETTERS][NUMBERS]
    ${resp}     Get Request         trello          /1/boards/${invalid_board_id}?key=${API_KEY}&token=${TOKEN}
    Validate Bad Status Code        ${resp.status_code}
    Validate "Invalid id" Response  ${resp.content}

Create New List
    [Tags]                                            Lists
    ${list_name}            Generate Random String    8           [LETTERS][NUMBERS]
    ${resp}                 Post Request              trello      /1/lists?name=${list_name}&idBoard=${BOARD_ID}&key=${API_KEY}&token=${TOKEN}
    Request Should Be Successful                      ${resp}
    ${existing_list_id}     Collect List Id           ${resp}
    Set Suite Variable      ${LIST_ID}                ${existing_list_id}

Update List
    [Tags]                                            Lists
    ${new_list_name}        Generate Random String    8           [LETTERS][NUMBERS]
    ${resp}                 Put Request               trello      /1/lists/${LIST_ID}?name=${new_list_name}&key=${API_KEY}&token=${TOKEN}
    Request Should Be Successful                      ${resp}

Delete Existing Board
    [Tags]                          Boards
    ${resp}     Delete Request      trello            /1/boards/${BOARD_ID}?key=${API_KEY}&token=${TOKEN}
    Request Should Be Successful    ${resp}

*** Keywords ***
Create Trello Session
    Create Session      trello                  ${URL}

Validate Bad Status Code
    [Arguments]         ${resp.status_code}
    Log                 ${resp.status_code}
    ${status}           Convert To String       ${resp.status_code}
    Should Be Equal     ${status}               400

Validate "Invalid id" Response
    [Arguments]         ${resp.content}
    ${response}         Convert To String       ${resp.content}
    Should Be Equal     ${response}             invalid id

Validate Board Name In The Response
    [Arguments]          ${resp}               ${board_name}
    ${resp_dict}         Set Variable          ${resp.json()}
    Should Be Equal As Strings                 ${resp_dict}[name]   ${board_name}

Validate Board Id In The Response
    [Arguments]          ${resp}               ${BOARD_ID}
    ${resp_dict}         Set Variable          ${resp.json()}
    Should Be Equal As Strings                 ${resp_dict}[id]   ${BOARD_ID}

Collect Board Id
    [Arguments]          ${resp}
    ${resp_dict}         Set Variable          ${resp.json()}
    ${board_id}          Set Variable          ${resp_dict}[id]
    Log                  ${board_id}
    [Return]             ${board_id}

Collect List Id
    [Arguments]          ${resp}
    ${resp_dict}         Set Variable          ${resp.json()}
    ${list_id}           Set Variable          ${resp_dict}[id]
    Log                  ${list_id}
    [Return]             ${list_id}

*** Comments ***

