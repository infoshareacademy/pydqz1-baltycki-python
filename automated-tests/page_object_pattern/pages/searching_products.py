import allure
from ..pages.locators import CommonPageLocators as Locators


class SearchingProducts:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Looking for search bar')
    def search_bar_is_displayed(self):
        search_bar = self.driver.find_element(*Locators.SEARCH_BAR)
        return search_bar.is_displayed()

    @allure.step('Enter a query in search bar')
    def enter_query_to_search_bar(self, query):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys(query)
        self.driver.find_element(*Locators.SEARCH_GO_BUTTON).click()
        search_counter = self.driver.find_element(*Locators.SEARCH_COUNTER)
        return search_counter.text

    def get_search_counter(self):
        return self.driver.find_element(*Locators.SEARCH_COUNTER).text

    def search_alert_is_displayed(self):
        search_alert = self.driver.find_element(*Locators.SEARCH_ALERT)
        return search_alert.is_displayed()

    def list_of_products(self):
        products_list = self.driver.find_elements_by_css_selector('div.product-container')
        return products_list
