class CartPageOrderSummary:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.confirm_order_button = '#cart_navigation button[type="submit"]'

    def action_on_page(self):
        self.driver.find_element_by_css_selector(self.confirm_order_button).click()