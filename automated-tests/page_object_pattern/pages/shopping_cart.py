class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver
        self.basket_css = 'div.shopping_cart [title="View my shopping cart"]'
        self.empty_basket_alert_css = '.alert.alert-warning'

    def select_cart(self):
        self.driver.find_element_by_css_selector(self.basket_css).click()
        self.driver.find_element_by_css_selector(self.empty_basket_alert_css)

    def check_no_contents(self):
        alert = self.driver.find_element_by_css_selector(self.empty_basket_alert_css)
        return alert.text
