import os.path
import json
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

my_path = os.path.abspath(os.path.dirname(__file__))
json_file_path = os.path.join(my_path, '../Helpers/user.json')


class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver
        self.my_shopping_cart_css = 'div.shopping_cart [title="View my shopping cart"]'
        self.shopping_cart_no_items_css = '.ajax_cart_no_product'
        self.empty_shopping_cart_alert_css = '.alert.alert-warning'
        self.shopping_cart_summary_css = 'h1#cart_title.page-heading'
        self.sign_in_button_css = '.login'
        self.quick_view_btn_css = '.quick-view'
        self.shop_item_css = 'ul#homefeatured li:nth-child(2) > div > div.left-block > div > a.product_img_link [' \
                             'title="Blouse"] '
        self.add_to_cart_btn_css = 'ul#homefeatured li:nth-child(2) > div > div.right-block > div.button-container > ' \
                                   'a.button.ajax_add_to_cart_button.btn.btn-default[title="Add to cart"][' \
                                   'data-id-product="2"] '
        self.proceed_to_checkout_btn_css = '.btn.btn-default.button.button-medium'
        self.email_field_css = 'email'
        self.password_field_css = 'passwd'
        self.sign_in_btn_css = '#SubmitLogin'
        self.logo_css = '.logo.img-responsive'
        self.continue_shopping_btn_css = '.continue.btn.btn-default.button.exclusive-medium[title="Continue shopping"]'
        self.cart_quantity_main_page_css = '.ajax_cart_quantity.unvisible'
        self.cart_quantity_summary_css = '#summary_products_quantity'
        self.remove_from_cart_btn_css = 'header#header span > a'
        self.log_me_out_button_css = '.logout'
        self.quick_view_btn_css = 'ul#homefeatured li:nth-child(2) > div > div.left-block > div > a.quick-view > span'
        self.add_to_cart_quick_view_css = 'ul#homefeatured li:nth-child(2) > div > div.left-block > div > a.quick-view'
        self.wishlist_btn_css = '#wishlist_button'
        self.add_to_cart_btn_details_view_css = 'p#add_to_cart span'
        self.plus_btn_detail_view_css = 'p#quantity_wanted_p a.btn.btn-default.button-plus.product_quantity_up > span'
        self.size_dropdown_css = 'select#group_1'
        self.color_btn_css = 'a#color_8'
        self.total_price_css = '#total_product_price_2_12_0'
        self.size_and_color_css = 'table#cart_summary small:nth-child(3) > a'

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
        self.driver.execute_script("window.scrollTo(0, 1000)")
        shop_item = self.driver.find_element_by_css_selector(self.shop_item_css)
        ActionChains(self.driver).move_to_element(shop_item).perform()

    def add_to_cart(self):
        self.driver.find_element_by_css_selector(self.add_to_cart_btn_css).click()

    def log_in(self):
        with open(json_file_path) as f:
            data = json.load(f)
        self.driver.find_element_by_css_selector(self.sign_in_button_css).click()
        self.driver.find_element_by_id(self.email_field_css).send_keys(data['Id'])
        self.driver.find_element_by_id(self.password_field_css).send_keys(data['Password'])
        self.driver.find_element_by_css_selector(self.sign_in_btn_css).click()

    def go_back_to_main_page(self):
        self.driver.find_element_by_css_selector(self.logo_css).click()

    def continue_shopping(self):
        self.driver.find_element_by_css_selector(self.continue_shopping_btn_css).click()

    def hover_over_cart(self):
        cart_main_page = self.driver.find_element_by_css_selector(self.my_shopping_cart_css)
        ActionChains(self.driver).move_to_element(cart_main_page).perform()

    def check_item_in_cart_main_page(self):
        quantity = self.driver.find_element_by_css_selector(self.cart_quantity_main_page_css)
        return quantity.text

    def check_item_in_cart_summary(self):
        quantity_summary = self.driver.find_element_by_css_selector(self.cart_quantity_summary_css)
        return quantity_summary.text

    def remove_from_cart_main_page(self):
        self.driver.find_element_by_css_selector(self.remove_from_cart_btn_css).click()

    def proceed_to_checkout_from_main_page(self):
        self.driver.find_element_by_css_selector(self.proceed_to_checkout_btn_css).click()

    def log_me_out_button_exists(self):
        sign_out_btn = self.driver.find_element_by_css_selector(self.log_me_out_button_css)
        return sign_out_btn.is_displayed()

    def select_quick_view(self):
        self.driver.find_element_by_css_selector(self.quick_view_btn_css).click()

    def add_to_cart_quick_view(self):
        self.driver.find_element_by_css_selector(self.add_to_cart_quick_view_css).click()

    def add_to_wish_list(self):
        self.driver.find_element_by_css_selector(self.wishlist_btn_css).click()

    def add_to_cart_details_view(self):
        self.driver.find_element_by_css_selector(self.add_to_cart_btn_details_view_css).click()

    def move_to_details_view(self):
        self.driver.find_element_by_css_selector(self.shop_item_css).click()

    def add_additional_item(self):
        self.driver.find_element_by_css_selector(self.plus_btn_detail_view_css).click()

    def change_size(self):
        dropdown = Select(self.driver.find_element_by_css_selector(self.size_dropdown_css))
        dropdown.select_by_index(2)

    def change_color(self):
        self.driver.find_element_by_css_selector(self.color_btn_css).click()

    def check_total_price(self):
        total_price = self.driver.find_element_by_css_selector(self.total_price_css)
        return total_price.text

    def check_size_and_color(self):
        size_color = self.driver.find_element_by_css_selector(self.size_and_color_css)
        return size_color.text
