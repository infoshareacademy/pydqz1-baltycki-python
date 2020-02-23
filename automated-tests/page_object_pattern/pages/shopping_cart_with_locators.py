from selenium.webdriver import ActionChains
from ..pages.locators import CommonPageLocators as Locators


class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver

    def login_button_exists(self):
        sign_in_btn = self.driver.find_element(*Locators.LOGIN_BUTTON)
        return sign_in_btn.is_displayed()

    def main_page_cart_status(self):
        cart_status = self.driver.find_element(*Locators.CART_WIDGET_EMPTY)
        return cart_status.text

    def select_cart(self):
        self.driver.find_element(*Locators.CART_WIDGET).click()

    def check_no_contents(self):
        alert = self.driver.find_element(*Locators.CART_PAGE_ALERT)
        return alert.text

    def select_item(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        shop_item = self.driver.find_element(*Locators.PRODUCT_BLOUSE)
        ActionChains(self.driver).move_to_element(shop_item).perform()

    def add_to_cart(self):
        self.driver.find_element(*Locators.HOVER_ADD_TO_CART_BUTTON_BLOUSE).click()

    def log_in(self, user, password):
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(user)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.SIGN_IN_BUTTON).click()

    def go_back_to_main_page(self):
        self.driver.find_element(*Locators.PAGE_LOGO).click()

    def continue_shopping(self):
        self.driver.find_element(*Locators.CART_LAYER_CONTINUE_BUTTON).click()

    def hover_over_cart(self):
        cart_main_page = self.driver.find_element(*Locators.CART_WIDGET)
        ActionChains(self.driver).move_to_element(cart_main_page).perform()

    def check_item_in_cart_main_page(self):
        quantity = self.driver.find_element(*Locators.CART_MAIN_QUANTITY)
        return quantity.text

    def check_item_in_cart_summary(self):
        quantity_summary = self.driver.find_element(*Locators.CART_MAIN_SUMMARY)
        return quantity_summary.text

    def remove_from_cart_main_page(self):
        self.driver.find_element(*Locators.CART_MAIN_REMOVE_ITEM).click()


