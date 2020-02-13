import time
import pytest

from page_object_pattern.pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver8):
        super(RegisterPage, self).__init__(driver8) #wywołanie konstruktora klasy bazowej

    def get_navigation_bar_sign_in(self):
        return self.driver.find_element_by_class_name('header_user_info')

    def get_register_page_email_create_input(self):
        return self.driver.find_element_by_id('email_create')

    def get_register_page_create_an_account_button(self):
        return self.driver.find_element_by_id('SubmitCreate')

    def get_register_page_first_name_input(self):
        return self.driver.find_element_by_id('customer_firstname')

    def get_register_page_last_name_input(self):
        return self.driver.find_element_by_id('customer_lastname')

    def get_register_page_email_input(self):
        return self.driver.find_element_by_id('email')

    def get_register_page_password_input(self):
        return self.driver.find_element_by_id('passwd')

    def get_register_page_address_first_name_input(self):
        return self.driver.find_element_by_id('firstname')

    def get_register_page_address_last_name_input(self):
        return self.driver.find_element_by_id('lastname')

    def get_register_page_address_input(self):
        return self.driver.find_element_by_id('address1')

    def get_register_page_address_city(self):
        return self.driver.find_element_by_id('city')

    def get_register_page_state(self):
        return self.driver.find_element_by_id('id_state')

    def get_register_page_postal_code(self):
        return self.driver.find_element_by_id('postcode')

    def get_get_register_page_mobile_phone(self):
        return self.driver.find_element_by_id('phone_mobile')

    def get_register_page_register_button(self):
        return self.driver.find_element_by_id('submitAccount')

