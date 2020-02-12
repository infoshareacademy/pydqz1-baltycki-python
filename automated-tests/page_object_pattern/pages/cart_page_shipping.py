class CartPageShipping:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.terms_of_service_checkbox = '#cgv'
        self.checkout_button = 'button[name="processCarrier"]'

    def action_on_page(self):
        self.driver.find_element_by_css_selector(self.terms_of_service_checkbox).click()
        self.driver.find_element_by_css_selector(self.checkout_button).click()

    def failed_action_on_page(self):
        self.driver.find_element_by_css_selector(self.checkout_button).click()
