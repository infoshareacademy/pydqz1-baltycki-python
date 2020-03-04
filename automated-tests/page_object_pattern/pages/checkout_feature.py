import allure
from ..pages.locators import CommonPageLocators as Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class CheckoutFeature:
    def __init__(self, driver):
        self.driver = driver

    # @allure.step('Looking for search bar')
    def click_on_faded_tshirt(self):
        element = self.driver.find_element(*Locators.PRODUCT_FADED_TSHIRTS)
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_element(*Locators.PRODUCT_HOVER_MORE_BUTTON_FADED_TSHIRTS).click()
        product_h1 = self.driver.find_element(*Locators.PRODUCT_H1).text
        product_price = self.driver.find_element(*Locators.PRODUCT_PRICE).text
        product_quantity = self.driver.find_element(*Locators.QUANTITY_INPUT).get_attribute('value')
        return product_h1, product_price, product_quantity

    def add_to_cart_size_l(self, quantity):
        self.driver.find_element(*Locators.QUANTITY_INPUT).clear()
        self.driver.find_element(*Locators.QUANTITY_INPUT).send_keys(quantity)
        self.driver.find_element(*Locators.PRODUCT_SIZE_DROPX_L).click()
        self.driver.find_element(*Locators.ADD_TO_CART_BUTTON).click()
        self.driver.find_element(*Locators.CART_LAYER_PROCEED_BUTTON).click()
        heading_counter = self.driver.find_element(*Locators.SEARCH_COUNTER).text
        return heading_counter
