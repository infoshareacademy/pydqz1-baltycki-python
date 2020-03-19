import pytest
import time
from selenium.webdriver.support.ui import Select

from page_object_pattern.Helpers import registration_data
from page_object_pattern.pages.register_page import RegisterPage
from page_object_pattern.Helpers.Data_generator import *
import random
import allure
from assertpy import assert_that
from page_object_pattern.Helpers.registration_data import *


@allure.description('Testing register feature')
@allure.parent_suite('TestSignupPage')
@pytest.mark.usefixtures('setup')
class TestSignupPage:

    def register_setup(self):
        self.driver.get('http://automationpractice.com/index.php')
        register_page = RegisterPage(self.driver)
        register_page.get_navigation_bar_sign_in().click()
        return register_page

    @allure.title('Register with valid data')
    def test_valid_data(self):
        """Register with valid data"""

        register_page = self.register_setup()
        registration_data = RegistrationData()
        register_page.first_step(registration_data.email_input)
        register_page.last_step(registration_data)
        info_account = register_page.get_info_account_text()
        customer_account_name = register_page.get_customer_button_name_text()
        nav_bar_content = register_page.get_navigation_bar_sign_out_text()
        # check if url has been changed
        assert_that(self.driver.current_url).is_equal_to("http://automationpractice.com/index.php?controller=my-account")
        # check if Welcome-info_account was displayed
        assert_that(info_account).contains('Welcome to your account. Here you can manage all of your personal '
                                           'information and orders.')
        # check if customer name was displayed
        assert_that(customer_account_name).contains(registration_data.first_name_input + " " + registration_data.last_name_input)
        # check if 'Sign out' was displayed in navbar
        assert_that(nav_bar_content).contains('Sign out')

    @allure.title('Register with invalid email format in CREATE AN ACCOUNT section')
    @pytest.mark.parametrize("email", [generate_email().replace("@", ""), generate_email().split('.')[0]])
    def test_invalid_email_format(self, email):
        """Register with invalid email format in CREATE AN ACCOUNT section"""

        register_page = self.register_setup()
        register_page.first_step(email)
        time.sleep(2)# MUST be 2s!
        alert = register_page.get_alert_account_text()
        # check if alert was displayed for email adress without @ and domain
        assert_that(alert).contains("Invalid email address.")

    @allure.title('Register with empty email in CREATE AN ACCOUNT section')
    def test_email_empty(self):
        """Register with email adress empty in CREATE AN ACCOUNT section"""

        register_page = self.register_setup()
        register_page.get_email_create_input().clear()
        register_page.get_create_an_account_button().click()
        time.sleep(2)# MUST be 2s!
        alert = register_page.get_alert_account_text()
        # check if alert was displayed for empty email
        assert_that(alert).contains('Invalid email address.')

    @allure.title('Register with email associated with already existing account')
    def test_email_registered(self):

        """Register with email associated with already existing account"""
        register_page = self.register_setup()
        email_input = "gikesi5319@nwesmail.com"
        register_page.first_step(email_input)
        time.sleep(2)# MUST be 2s!
        alert = register_page.get_alert_account_text()
        # check if alert about already used email was displayed
        assert_that(alert).contains('An account using this email address has already been registered.'
                                    ' Please enter a valid password or request a new one.')

    @allure.title('Register with all Fields Empty')
    def test_all_fields_empty(self):
        """Register with all Fields Empty in Your Personal Information Section"""

        register_page = self.register_setup()
        registration_data = RegistrationData()
        register_page.first_step(registration_data.email_input)
        time.sleep(2)# MUST be 2s!
        register_page.get_email_input().clear()
        register_page.get_register_button().click()
        alert = register_page.get_alert_account_all_text()
        # check if alert about required fields was displayed
        assert_that(alert).contains('There are 9 errors')

    @allure.title('Register with invalid password format')
    @pytest.mark.parametrize("password", [generate_nick()[0], 123])
    def test_invalid_password_format(self, password):
        """Register with invalid password format"""

        register_page = self.register_setup()
        registration_data = RegistrationData()
        register_page.first_step(registration_data.email_input)
        registration_data.password_input = password
        register_page.last_step(registration_data)
        time.sleep(2)
        alert = register_page.get_alert_account_password()
        # check if alert 'passwd is invalid' was displayed
        assert_that(alert).contains('passwd is invalid.')
