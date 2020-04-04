# Automated tests using Selenium, Python and PyTest

This is a project for automated E2E tests for shopping app: http://automationpractice.com/index.php using Selenium, Python,
Pytest, allure reports and page object model.

## Visuals

Project include screenshots of failed tests using allure report (https://docs.qameta.io/allure/).

## Installation

git clone https://github.com/infoshareacademy/pydqz1-baltycki-python.git

## Usage
1. Requirements:
    * pip==20.0.2
    * setuptools==46.1.3
    * pytest==5.4.1
    * selenium==3.141.0
    * webdriver-manager==2.3.0
    * allure-pytest==2.8.12
    * assertpy==1.0
    * pytest-xdist==1.31.0
2. Tests execution: $ pytest --alluredir=/tmp/my_allure_results
3. Generating report to temp directory: $ allure serve /tmp/my_allure_results

## Test features and strategy

Test strategy - we focused on happy paths and added a few negative paths for functional tests on the Chrome browser.
We have tested the most basic test cases.
We tested the following features:
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

