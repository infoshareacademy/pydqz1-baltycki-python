# Automated tests using Selenium, Python and PyTest

This is a project for automated E2E tests for shopping app: http://automationpractice.com/index.php using Selenium, Python,
Pytest, allure reports and page object model.

## Visuals

Project include screenshots of failed tests using allure report (https://docs.qameta.io/allure/).

## Installation

git clone https://github.com/infoshareacademy/pydqz1-baltycki-python.git

## Usage

1. Tests execution: $ pytest --alluredir=/tmp/my_allure_results
2. Generating report to temp directory: $ allure serve /tmp/my_allure_results

## Test features and strategy

Test strategy - functional tests on the Chrome browser:
1. Searching products
2. Basket feature (including Shopping-Cart Summary)
3. Checkout feature (from checkout to finish) 
4. Registration feature

## Authors and acknowledgment
This project wouldn't be in the current stage without the hard work of the following individuals:
* **Agnieszka**
* **Monika**
* **Mateusz**
* **Marcin**

We would also like to thank Jacek for his guidance and support.

## Project status
The project is still in the development phase. 

