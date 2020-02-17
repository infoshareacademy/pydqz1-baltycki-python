from ..pages.locators import CommonPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """

    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://automationpractice.com/index.php')

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def search_for(self, search_string):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(CommonPageLocators.SEARCH_BAR))\
            .send_keys(search_string + Keys.ENTER)

    def switch_to(self, by_locator):
        iframe = WebDriverWait(self.driver, 10).until((ec.visibility_of_element_located
                                                       (CommonPageLocators.PRODUCT_QUICKVIEW)))
        self.driver.switch_to.frame(iframe)

    def switch_to_default(self):
        self.driver.switch_to.default_content()
