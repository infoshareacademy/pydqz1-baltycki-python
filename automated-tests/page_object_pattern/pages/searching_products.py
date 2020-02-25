from selenium.webdriver import ActionChains
from ..pages.locators import CommonPageLocators as Locators


class SearchingProducts:
    def __init__(self, driver):
        self.driver = driver

    def search_box_is_empty(self):
        search_bar = self.driver.find_element(*Locators.SEARCH_BAR).text
        return search_bar

    def enter_query_to_search_input(self, query):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys(query)
        self.driver.find_element(*Locators.SEARCH_GO_BUTTON).click()
