class CartPagePayment:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.pay_by_bank_button = '.bankwire'
        self.pay_by_check_button = '.cheque'

    def action_on_page(self):
        self.driver.find_element_by_css_selector(self.pay_by_bank_button).click()
