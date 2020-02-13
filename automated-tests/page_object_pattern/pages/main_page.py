class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.cart_layer_checkout_button = 'a[title="Proceed to checkout"]'
        self.product_faded_short_tshirt = 'Faded Short Sleeve T-shirts'
        self.product_printed_chiffon_dress = '#homefeatured img[title="Printed Chiffon Dress"] , quick-view'
        self.product_iframe = '.fancybox-iframe'
        self.product_iframe_button = '#add_to_cart button[type="submit"]'

    def click_on_product_tshirt(self):
        self.driver.find_element_by_link_text(self.product_faded_short_tshirt).click()

    def click_on_product_dress(self):
        self.driver.find_element_by_css_selector(self.product_printed_chiffon_dress).click()

    def switch_to_product_iframe(self):
        iframe = self.driver.find_element_by_css_selector(self.product_iframe)
        self.driver.switch_to.frame(iframe)

    def click_on_add_to_cart_button_product_iframe(self):
        self.driver.find_element_by_css_selector(self.product_iframe_button).click()

    def switch_to_page(self):
        self.driver.switch_to.default_content()

    def click_on_checkout_button_cart_layer(self):
        self.driver.find_element_by_css_selector(self.cart_layer_checkout_button).click()
