class CartPageShipping:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.terms_of_service_checkbox = '#cgv'
        self.checkout_button = 'button[name="processCarrier"]'

    def enable_checkbox(self):
        self.driver.find_element_by_css_selector(self.terms_of_service_checkbox).click()

    def click_checkout_button(self):
        self.driver.find_element_by_css_selector(self.checkout_button).click()
