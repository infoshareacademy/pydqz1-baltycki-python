from selenium.webdriver import ActionChains


class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver
        self.my_shopping_cart_css = 'div.shopping_cart [title="View my shopping cart"]'
        self.shopping_cart_no_items_css = '.ajax_cart_no_product'
        self.empty_shopping_cart_alert_css = '.alert.alert-warning'
        self.shopping_cart_summary_css = 'h1#cart_title.page-heading'
        self.sign_in_button_css = '.login'
        self.quick_view_btn_css = '.quick-view'
        self.shop_item_css = '.product-name [title*="T-shirts"]'
        self.add_to_cart_btn_css = '#add_to_cart'
        self.proceed_to_checkout_btn_css = '.btn.btn-default.button.button-medium'
        self.continue_shopping_btn_css = '.continue.btn.btn-default.button.exclusive-medium'
        self.email_field_css = 'email'
        self.password_field_css = 'passwd'
        self.sign_in_btn_css = '#SubmitLogin'
        self.logo_css = '.logo.img-responsive'

    def login_button_exists(self):
        sign_in_btn = self.driver.find_element_by_css_selector(self.sign_in_button_css)
        return sign_in_btn.is_displayed()

    def main_page_cart_status(self):
        cart_status = self.driver.find_element_by_css_selector(self.shopping_cart_no_items_css)
        return cart_status.text

    def select_cart(self):
        self.driver.find_element_by_css_selector(self.my_shopping_cart_css).click()

    def check_no_contents(self):
        alert = self.driver.find_element_by_css_selector(self.empty_shopping_cart_alert_css)
        return alert.text

    def select_item(self):
        # self.driver.execute_script("window.scrollTo(0, 900)")
        self.driver.find_element_by_css_selector(self.shop_item_css)

    def add_to_cart(self):
        self.driver.find_element_by_css_selector(self.add_to_cart_btn_css).click()

    def log_in(self):
        self.driver.find_element_by_css_selector(self.sign_in_button_css).click()
        self.driver.find_element_by_id(self.email_field_css).send_keys('mobiy43403@cityroyal.org')
        self.driver.find_element_by_id(self.password_field_css).send_keys('qwerty123')
        self.driver.find_element_by_css_selector(self.sign_in_btn_css).click()

    def go_back_to_main_page(self):
        self.driver.find_element_by_css_selector(self.logo_css).click()
