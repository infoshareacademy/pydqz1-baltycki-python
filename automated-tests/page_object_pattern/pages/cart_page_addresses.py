class CartPageAddresses:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.create_account_email_text_box = '#email_create'
        self.checkout_button = 'button[name="processAddress"]'

    def action_on_page(self):
        self.driver.find_element_by_css_selector(self.checkout_button).click()
