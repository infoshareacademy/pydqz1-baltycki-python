# Automated Trello API test using Postman & Robot Framework

This is a project for automated tests for API app: https://api.trello.com/ using Postman and Robot Framework.

## Visuals

Project includes screenshots of passed and failed tests using Postman report (https://learning.postman.com/docs/postman/design-and-develop-apis/view-and-analyze-api-reports/)
and Robot Framework report (http://robotframework.org/QuickStartGuide/report.html).

## Installation

Open terminal and run following commands:
```console
user@machine:~$ git clone https://github.com/infoshareacademy/pydqz1-baltycki-python.git
user@machine:~$ cd pydqz1-baltycki-python/
user@machine:~/pydqz1-baltycki-python$ python3 -m venv venv
user@machine:~/pydqz1-baltycki-python$ source venv/bin/activate
user@machine:~/pydqz1-baltycki-python$ pip install -r requirements.txt 
```

## Usage
1. Requirements:
    * pip==20.1
    * setuptools==46.3.1
    * robotframework==3.2.1
    * robotframework-requests==0.7.0
    * robotframework-seleniumlibrary==4.4.0
2. Tests execution and reports using Postman:
    1. open terminal and run following command:
    
        ```console
          user@machine:~$ postman
        ```
    2. In Postman go to File and Import test files from /api-test directory.
    3. Click Run button to start tests.
3. Tests execution and reports using Robot Framework:
    1.  open terminal and run following command:
    
        ```console
          user@machine:~$ robot api-tests/
        ```
    2. After tests were finished in api-tests/ directory there should be files:
        * report.html
        * log.html
        * output.xml
        
## Test features and strategy

Test strategy - we focused on happy paths and added a few negative paths for API tests.
We have tested the most basic test cases.
We tested the following Trello API features:
1. Get a List, Get Cards on Boards, Update a Card
2. Create a List on Board, Create a new Card, Delete a Card, Get a Card
3. Update a List, Create a Board, Delete a Board, Get a Board
4. Get Cards in a List, Get the Board a List is On, Create a new List, Get a Lists of Cards

## Authors and acknowledgment

This project wouldn't be in the current stage without the hard work of the following individuals:
* **Agnieszka**
* **Monika**
* **Mateusz**
* **Marcin**

We would also like to thank Jacek for his guidance and support.

## Project status

The project is still in the development phase.
