class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.product_add_to_cart_button = '#add_to_cart button[type="submit"]'
        self.cart_layer_checkout_button = 'a[title="Proceed to checkout"]'

    def action_on_page(self):
        self.driver.find_element_by_css_selector(self.product_add_to_cart_button).click()
        self.driver.find_element_by_css_selector(self.cart_layer_checkout_button).click()
