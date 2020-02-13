class CartPagePayment:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.pay_by_bank_button = '.bankwire'
        self.pay_by_check_button = '.cheque'

    def click_pay_by_bank_wire(self):
        self.driver.find_element_by_css_selector(self.pay_by_bank_button).click()

    def click_pay_by_check(self):
        self.driver.find_element_by_css_selector(self.pay_by_check_button).click()
