from ..pages.locators import CommonPageLocators as Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_btn(self):
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

    def get_email_create_input(self):
        return self.driver.find_element(*Locators.EMAIL_CREATE_INPUT)

    def get_create_an_account_button(self):
        return self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON)

    def fill_create_account_email(self, email):
        self.get_email_create_input().send_keys(email)
        self.get_create_an_account_button().click()

