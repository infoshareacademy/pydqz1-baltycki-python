
from selenium.webdriver.support.select import Select
from ..pages.locators import CommonPageLocators as Locators
from page_object_pattern.Helpers.user_data import *


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, personal_data):
        self.driver.find_element(*Locators.CREATE_ACC_CITY_INPUT).send_keys(
            personal_data.city_name)  # must be first
        self.driver.find_element(*Locators.CREATE_ACC_FIRST_NAME_INPUT).send_keys(personal_data.first_name_input)
        self.driver.find_element(*Locators.CREATE_ACC_LAST_NAME_INPUT).send_keys(personal_data.last_name_input)
        self.driver.find_element(*Locators.CREATE_ACC_PASSWORD_INPUT).send_keys(personal_data.password_input)
        self.driver.find_element(*Locators.CREATE_ACC_ADDRESS_INPUT).send_keys(
            personal_data.city_street + " " + str(random.randint(1, 100)))
        Select(self.driver.find_element(*Locators.CREATE_ACC_STATE_DROPBOX)).select_by_value(
            personal_data.state_value_input)
        self.driver.find_element(*Locators.CREATE_ACC_POST_CODE).send_keys(personal_data.city_code_format)
        self.driver.find_element(*Locators.CREATE_ACC_MOBILE_PHONE_INPUT).send_keys(personal_data.mobile_phone_input)
        self.register_submit_btn()

    def clear_email(self):
        self.driver.find_element(*Locators.EMAIL_INPUT).clear()

    def register_submit_btn(self):
        self.driver.find_element(*Locators.CREATE_ACC_REGISTER_BUTTON).click()

    def get_alert_account_text(self):
        return self.driver.find_element(*Locators.CREATE_ACC_ALERT).text

    def get_create_acc_text(self):
        return self.driver.find_element(*Locators.CREATE_ACC_INFO).text

    def get_customer_button_name_text(self):
        return self.driver.find_element(*Locators.CUSTOMER_NAME_ACC_BUTTON).text

    def get_alert_account_all_text(self):
        return self.driver.find_element(*Locators.CREATE_ACC_ALERT_ALL).text

    def get_alert_account_password_text(self):
        return self.driver.find_element(*Locators.CREATE_ACC_ALERT_PASSWORD).text

    def get_navigation_bar_sign_out_text(self):
        return self.driver.find_element(*Locators.LOGOUT_BUTTON).text
