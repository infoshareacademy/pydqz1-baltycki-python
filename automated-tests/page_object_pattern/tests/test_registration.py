import pytest
import time
from selenium.webdriver.support.ui import Select
from page_object_pattern.pages.register_page import RegisterPage
from page_object_pattern.Helpers.Data_generator import *
import random


@pytest.mark.usefixtures('setup')
class TestSignupPage:

    def register_setup(self):
        self.driver.get('http://automationpractice.com/index.php')
        register_page = RegisterPage(self.driver)
        register_page.get_navigation_bar_sign_in().click()
        return register_page

    def test_valid_data(self):
        """Register with valid data"""

        register_page = self.register_setup()
        email_input = generate_email()
        first_name_input = generate_name()
        last_name_input = generate_surname()
        password_input = generate_nick()
        city_code, city_name, city_street = generate_addr_components()
        city_code_format = city_code.replace("-", "")
        mobile_phone_input = random.randint(1, 1000)
        state_value_input = str(random.randint(1, 51))
        register_page.get_email_create_input().send_keys(email_input)
        register_page.get_create_an_account_button().click()
        register_page.get_address_city().send_keys(city_name) # must be first - bug?
        register_page.get_first_name_input().send_keys(first_name_input)
        register_page.get_last_name_input().send_keys(last_name_input)
        register_page.get_password_input().send_keys(password_input)
        register_page.get_address_input().send_keys(city_street + " " + str(random.randint(1, 100)))
        Select(register_page.get_state()).select_by_value(state_value_input)
        register_page.get_postal_code().send_keys(city_code_format)
        register_page.get_get_mobile_phone().send_keys(mobile_phone_input)
        register_page.get_register_button().click()
        info_account = register_page.get_info_account_text()
        customer_account_name = register_page.get_customer_button_name_text()
        nav_bar_content = register_page.get_navigation_bar_sign_out_text()

        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=my-account",\
            "url has not changed"
        assert 'Welcome to your account. Here you can manage all of your personal information and orders.'\
               in info_account, "Welcome-info_account wasn't displayed"
        assert first_name_input + " " + last_name_input in customer_account_name, "Customer name wasn't displayed"
        assert 'Sign out' in nav_bar_content, "Sign out wasn't displayed"

    def test_invalid_email_format(self):
        """Register with invalid email format in CREATE AN ACCOUNT section"""

        register_page = self.register_setup()
        email_input = generate_email().replace("@", "")
        register_page.get_email_create_input().send_keys(email_input)
        register_page.get_create_an_account_button().click()
        time.sleep(2)# MUST be 2s!
        alert = register_page.get_alert_account_text()

        assert "Invalid email address." in alert, "Invalid email address alert wasn't displayed"

    def test_email_empty(self):
        """Register with email adress empty in CREATE AN ACCOUNT section"""

        register_page = self.register_setup()
        register_page.get_email_create_input().clear()
        register_page.get_create_an_account_button().click()
        time.sleep(2)# MUST be 2s!
        alert = register_page.get_alert_account_text()

        assert 'Invalid email address.' in alert

    def test_email_registered(self):
        """Register with email associated with already existing account"""

        register_page = self.register_setup()
        email_input = "gikesi5319@nwesmail.com"
        register_page.get_email_create_input().send_keys(email_input)
        register_page.get_create_an_account_button().click()
        time.sleep(2)# MUST be 2s!
        alert = register_page.get_alert_account_text()

        assert 'An account using this email address has already been registered. Please enter a valid password or ' \
               'request a new one.'\
               in alert, "Alert about already used email wasn't displayed"

    def test_all_fields_empty(self):
        """Register with all Fields Empty in Your Personal Information Section"""

        register_page = self.register_setup()
        email_input = generate_email()
        register_page.get_email_create_input().send_keys(email_input)
        register_page.get_create_an_account_button().click()
        time.sleep(2)# MUST be 2s!
        register_page.get_email_input().clear()
        register_page.get_register_button().click()
        alert = register_page.get_alert_account_all_text()

        assert 'There are 9 errors' in alert, "Alert about required fields wasn't displayed "

    def test_invalid_password_format(self):
        """Register with invalid password format"""

        register_page = self.register_setup()
        email_input = generate_email()
        first_name_input = generate_name()
        last_name_input = generate_surname()
        password_input = generate_nick()
        password_input_wrong_format = password_input[0]
        city_code, city_name, city_street = generate_addr_components()
        city_code_format = city_code.replace("-", "")
        mobile_phone_input = random.randint(1, 1000)
        state_value_input = str(random.randint(1, 51))
        register_page.get_email_create_input().send_keys(email_input)
        register_page.get_create_an_account_button().click()
        time.sleep(2)
        register_page.get_address_city().send_keys(city_name)  # must be first - bug?
        register_page.get_first_name_input().send_keys(first_name_input)
        register_page.get_last_name_input().send_keys(last_name_input)
        register_page.get_password_input().send_keys(password_input_wrong_format)
        register_page.get_address_input().send_keys(city_street + " " + str(random.randint(1, 100)))
        Select(register_page.get_state()).select_by_value(state_value_input)
        register_page.get_postal_code().send_keys(city_code_format)
        register_page.get_get_mobile_phone().send_keys(mobile_phone_input)
        register_page.get_register_button().click()
        alert = register_page.get_alert_account_password()

        assert 'passwd is invalid.' in alert
