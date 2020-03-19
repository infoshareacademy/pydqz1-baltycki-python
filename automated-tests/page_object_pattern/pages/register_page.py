from selenium.webdriver.support.select import Select

from ..pages.locators import CommonPageLocators as Locators

from page_object_pattern.Helpers.helpers import Helpers
import allure
from page_object_pattern.Helpers.registration_data import *


class RegisterPage(Helpers):

    def __init__(self, driver):
        super(RegisterPage, self).__init__(driver) #wywołanie konstruktora klasy bazowej

    def get_navigation_bar_sign_in(self):
        return self.driver.find_element(*Locators.LOGIN_BUTTON)

    def get_email_create_input(self):
        return self.driver.find_element(*Locators.EMAIL_CREATE_INPUT)

    def get_create_an_account_button(self):
        return self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON)

    def get_first_name_input(self):
        return self.driver.find_element(*Locators.CREATE_ACC_FIRST_NAME_INPUT)

    def get_last_name_input(self):
        return self.driver.find_element(*Locators.CREATE_ACC_LAST_NAME_INPUT)

    # def get_email_input(self):
    #     return self.driver.find_element_by_id('email')

    def get_password_input(self):
        return self.driver.find_element(*Locators.CREATE_ACC_PASSWORD_INPUT)

    # def get_address_first_name_input(self):
    #     return self.driver.find_element_by_id('firstname')
    #
    # def get_address_last_name_input(self):
    #     return self.driver.find_element_by_id('lastname')

    def get_address_input(self):
        return self.driver.find_element(*Locators.CREATE_ACC_ADDRESS_INPUT)

    def get_address_city(self):
        return self.driver.find_element(*Locators.CREATE_ACC_CITY_INPUT)

    def get_state(self):
        return self.driver.find_element(*Locators.CREATE_ACC_STATE_DROPBOX)

    def get_postal_code(self):
        return self.driver.find_element(*Locators.CREATE_ACC_POST_CODE)

    def get_get_mobile_phone(self):
        return self.driver.find_element(*Locators.CREATE_ACC_MOBILE_PHONE_INPUT)

    def get_register_button(self):
        return self.driver.find_element(*Locators.CREATE_ACC_REGISTER_BUTTON)

    def get_alert_account_text(self):
        return self.driver.find_element(*Locators.CREATE_ACC_ALERT).text

    def get_info_account_text(self):
        return self.driver.find_element(*Locators.CREATE_ACC_INFO).text

    def get_customer_button_name_text(self):
        return self.driver.find_element(*Locators.CUSTOMER_NAME_ACC_BUTTON).text

    def get_email_input(self):
        return self.driver.find_element(*Locators.EMAIL_INPUT)

    def get_alert_account_all_text(self):
        return self.driver.find_element(*Locators.CREATE_ACC_ALERT_ALL).text

    def get_alert_account_password(self):
        return self.driver.find_element(*Locators.CREATE_ACC_ALERT_PASSWORD).text

    def get_navigation_bar_sign_out_text(self):
        return self.driver.find_element(*Locators.LOGOUT_BUTTON).text

    def first_step(self, email):
        self.get_email_create_input().send_keys(email)
        self.get_create_an_account_button().click()

    def last_step(self, personal_data):
        self.get_address_city().send_keys(personal_data.city_name) # must be first - bug?
        self.get_first_name_input().send_keys(personal_data.first_name_input)
        self.get_last_name_input().send_keys(personal_data.last_name_input)
        self.get_password_input().send_keys(personal_data.password_input)
        self.get_address_input().send_keys(personal_data.city_street + " " + str(random.randint(1, 100)))
        Select(self.get_state()).select_by_value(personal_data.state_value_input)
        self.get_postal_code().send_keys(personal_data.city_code_format)
        self.get_get_mobile_phone().send_keys(personal_data.mobile_phone_input)
        self.get_register_button().click()

