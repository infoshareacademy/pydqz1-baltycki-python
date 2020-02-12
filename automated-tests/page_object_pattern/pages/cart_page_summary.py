class CartPageSummary:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.checkout_button = '.standard-checkout'

    def action_on_page(self):
        self.driver.find_element_by_css_selector(self.checkout_button).click()
