import allure
from ..pages.locators import CommonPageLocators as Locators


class SearchingProducts:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Check if search bar is displayed')
    def search_bar_is_displayed(self):
        search_bar = self.driver.find_element(*Locators.SEARCH_BAR)
        return search_bar.is_displayed()

    @allure.step('Enter query to search bar')
    def enter_query_to_search_bar(self, query):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys(query)
        self.driver.find_element(*Locators.SEARCH_GO_BUTTON).click()
        search_counter = self.driver.find_element(*Locators.SEARCH_COUNTER)
        return search_counter.text

    @allure.step('Get the text content of search counter')
    def get_search_counter(self):
        return self.driver.find_element(*Locators.SEARCH_COUNTER).text

    @allure.step('Check if search alert is displayed')
    def search_alert_is_displayed(self):
        search_alert = self.driver.find_element(*Locators.SEARCH_ALERT)
        return search_alert.is_displayed()

    @allure.step('Get product list')
    def list_of_products(self):
        products_list = self.driver.find_elements_by_css_selector('div.product-container')
        return products_list
