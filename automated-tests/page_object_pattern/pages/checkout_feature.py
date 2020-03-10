import allure
from ..pages.locators import CommonPageLocators as Locators
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class CheckoutFeature:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('On main page click on Blouse - add 1 to cart')
    def add_one_blouse_to_cart(self):
        element = self.driver.find_element(*Locators.PRODUCT_BLOUSE)
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_element(*Locators.HOVER_ADD_TO_CART_BUTTON_BLOUSE).click()
        self.driver.find_element(*Locators.CART_LAYER_PROCEED_BUTTON).click()

    @allure.step('On main page click on Faded tshirts')
    def click_on_faded_tshirt(self):
        element = self.driver.find_element(*Locators.PRODUCT_FADED_TSHIRTS)
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_element(*Locators.PRODUCT_HOVER_MORE_BUTTON_FADED_TSHIRTS).click()
        product_h1 = self.driver.find_element(*Locators.PRODUCT_H1).text
        product_price = self.driver.find_element(*Locators.PRODUCT_PRICE).text
        product_quantity = self.driver.find_element(*Locators.QUANTITY_INPUT).get_attribute('value')
        return product_h1, product_price, product_quantity

    @allure.step('Login as registered user')
    def login_as_registered_user(self, mail, password):
        self.driver.find_element(*Locators.PROCEED_TO_CHECKOUT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(mail)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.SIGN_IN_BUTTON).click()

    @allure.step('Proceed to shipping options')
    def proceed_to_shipping_options(self):
        for click in range(2):
            self.driver.find_element(*Locators.PROCEED_TO_CHECKOUT_BUTTON).click()
        notify = self.driver.find_element(*Locators.FANCYBOX_NOTIFY)
        return notify.is_displayed(), notify.text

    @allure.step('Add to cart Faded tshirts size L quantity 2')
    def add_to_cart_size_l(self, quantity):
        self.driver.find_element(*Locators.QUANTITY_INPUT).clear()
        self.driver.find_element(*Locators.QUANTITY_INPUT).send_keys(quantity)
        self.driver.find_element(*Locators.PRODUCT_SIZE_DROPX_L).click()
        self.driver.find_element(*Locators.ADD_TO_CART_BUTTON).click()
        self.driver.find_element(*Locators.CART_LAYER_PROCEED_BUTTON).click()
        heading_counter = self.driver.find_element(*Locators.SEARCH_COUNTER).text
        product_name = self.driver.find_element(*Locators.CART_PRODUCT_NAME).text
        product_size = self.driver.find_element(*Locators.CART_PRODUCT_COLOR_SIZE).text
        product_unit_price = self.driver.find_element(*Locators.CART_PRODUCT_UNIT_PRICE).text
        cart_shipping_cost = self.driver.find_element(*Locators.CART_TOTAL_SHIPPING).text
        cart_total_cost = self.driver.find_element(*Locators.CART_TOTAL_COST).text
        return heading_counter, product_name, product_size, product_unit_price, cart_shipping_cost, cart_total_cost

    @allure.step('Proceed to checkout as registered user pay by {1}')
    def proceed_to_checkout_registered_user(self, payment_option):
        self.driver.find_element(*Locators.PROCEED_TO_CHECKOUT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys('varihig924@era7mail.com')
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys('12345')
        self.driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        self.driver.find_element(*Locators.PROCEED_TO_CHECKOUT_BUTTON).click()
        self.driver.find_element(*Locators.TERMS_CHECK_BOX).click()
        self.driver.find_element(*Locators.PROCEED_TO_CHECKOUT_BUTTON).click()
        if payment_option == 'bank wire':
            self.driver.find_element(*Locators.PAY_BY_BANK_WIRE).click()
        elif payment_option == 'check':
            self.driver.find_element(*Locators.PAY_BY_CHECK).click()
        self.driver.find_element(*Locators.PROCEED_TO_CHECKOUT_BUTTON).click()
