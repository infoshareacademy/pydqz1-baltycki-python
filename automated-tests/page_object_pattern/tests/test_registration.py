import pytest
import time
from selenium.webdriver.support.ui import Select

from ..pages.base_page import BasePage
from ..pages.register_page import RegisterPage


@pytest.mark.usefixtures('setup')
class TestSignupPage:

    def register_setup(self):
        self.driver.get('http://automationpractice.com/index.php')
        register_page = RegisterPage(self.driver)
        # time.sleep(2)
        register_page.get_navigation_bar_sign_in().click()
        # time.sleep(2)
        return register_page

    def test_valid_data(self):
        """Register with valid data"""

        register_page = self.register_setup()

        email_for_register = "gikesi5378@nwesmail.com"
        BasePage.slow_typing(register_page.get_register_page_email_create_input(), email_for_register)

        register_page.get_register_page_create_an_account_button().click()
        time.sleep(2)

        BasePage.slow_typing(register_page.get_register_page_first_name_input(), 'Jan')

        BasePage.slow_typing(register_page.get_register_page_last_name_input(), 'Kowalski')

        BasePage.slow_typing(register_page.get_register_page_password_input(), 'LubiePlacki123')

        BasePage.slow_typing(register_page.get_register_page_address_input(), 'World Newsagency Pavilon ParcelPoint')

        BasePage.slow_typing(register_page.get_register_page_address_city(), 'Spinalonga')

        selected_state_for_register = Select(register_page.get_register_page_state())
        selected_state_for_register.select_by_value('1')

        BasePage.slow_typing(register_page.get_register_page_postal_code(), '80254')

        BasePage.slow_typing(register_page.get_get_register_page_mobile_phone(), '695826584')

        register_page.get_register_page_register_button().click()
        time.sleep(2)

        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=my-account"


    def test_invalid_email_format(self):

        """Register with invalid email format in CREATE AN ACCOUNT section"""
        register_page = self.register_setup()
        email_for_register = "tifak72483xmailsme.com"
        BasePage.slow_typing(register_page.get_register_page_email_create_input(), email_for_register)

        register_page.get_register_page_create_an_account_button().click()
        time.sleep(5)
        alert = self.driver.find_element_by_id('create_account_error').text
        assert 'Invalid email address.' in alert

    def test_email_empty(self):

        """Register with email adress empty in CREATE AN ACCOUNT section"""
        register_page = self.register_setup()

        email_for_register = ""
        BasePage.slow_typing(register_page.get_register_page_email_create_input(), email_for_register)

        register_page.get_register_page_create_an_account_button().click()
        time.sleep(5)
        alert = self.driver.find_element_by_id('create_account_error').text
        assert 'Invalid email address.' in alert

    def test_email_registered(self):

        """Register with email associated with already existing account"""
        register_page = self.register_setup()


        email_for_register = "gikesi5319@nwesmail.com"
        BasePage.slow_typing(register_page.get_register_page_email_create_input(), email_for_register)

        register_page.get_register_page_create_an_account_button().click()
        time.sleep(5)
        alert = self.driver.find_element_by_id('create_account_error').text
        assert 'An account using this email address has already been registered. Please enter a valid password or request a new one.' in alert

    def test_all_fields_empty(self):

        """Register with all Fields Empty in Your Personal Information Section"""
        register_page = self.register_setup()

        email_for_register = "gikesi5366@nwesmail.com"
        BasePage.slow_typing(register_page.get_register_page_email_create_input(), email_for_register)

        register_page.get_register_page_create_an_account_button().click()
        time.sleep(2)

        register_page.get_register_page_email_input().clear()
        time.sleep(2)

        register_page.get_register_page_register_button().click()
        time.sleep(2)

        alert = self.driver.find_element_by_css_selector('#center_column > div').text
        assert 'There are 9 errors' in alert

# self.driver.find_element_by_css_selector(self.nav_bar_css).text
# assert 'Wylogowanie' in self.nav.get_nav_bar_content(), 'Wylogowanie was not displayed'
