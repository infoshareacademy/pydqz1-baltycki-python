import time
import pytest
from ..pages.locators import CommonPageLocators as Locators

from ..pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver8):
        super(RegisterPage, self).__init__(driver8) #wywołanie konstruktora klasy bazowej

    def get_navigation_bar_sign_in(self):
        return self.driver.find_element(*Locators.LOGIN_BUTTON)

    def get_register_page_email_create_input(self):
        return self.driver.find_element(*Locators.EMAIL_CREATE_INPUT)

    def get_register_page_create_an_account_button(self):
        return self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON)

    def get_register_page_first_name_input(self):
        return self.driver.find_element(*Locators.CREATE_ACC_FIRST_NAME_INPUT)

    def get_register_page_last_name_input(self):
        return self.driver.find_element(*Locators.CREATE_ACC_LAST_NAME_INPUT)

    # def get_register_page_email_input(self):
    #     return self.driver.find_element_by_id('email')

    def get_register_page_password_input(self):
        return self.driver.find_element(*Locators.CREATE_ACC_PASSWORD_INPUT)

    # def get_register_page_address_first_name_input(self):
    #     return self.driver.find_element_by_id('firstname')
    #
    # def get_register_page_address_last_name_input(self):
    #     return self.driver.find_element_by_id('lastname')

    def get_register_page_address_input(self):
        return self.driver.find_element(*Locators.CREATE_ACC_PASSWORD_INPUT)

    def get_register_page_address_city(self):
        return self.driver.find_element(*Locators.CREATE_ACC_CITY_INPUT)

    def get_register_page_state(self):
        return self.driver.find_element(*Locators.CREATE_ACC_STATE_DROPBOX)

    def get_register_page_postal_code(self):
        return self.driver.find_element(*Locators.CREATE_ACC_POST_CODE)

    def get_get_register_page_mobile_phone(self):
        return self.driver.find_element(*Locators.CREATE_ACC_MOBILE_PHONE_INPUT)

    def get_register_page_register_button(self):
        return self.driver.find_element(*Locators.CREATE_ACC_REGISTER_BUTTON)
