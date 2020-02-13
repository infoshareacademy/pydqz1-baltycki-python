class CartPageOrderConfirmation:

    def __init__(self, driver):
        self.driver = driver
        self.order_confirmation_text = '//*[contains(text(), "Your order on My Store is complete.")]'

    def get_order_confiramation_text(self):
        order_complete = self.driver.find_element_by_xpath(self.order_confirmation_text).text
        return order_complete
