import pytest
import allure


@allure.description('Testing Checkout Feature')
@pytest.mark.usefixtures('setup')
class TestCheckoutFeature:

    def test_checkout_2_items_pay_by_bank_wire(self, setup):
        product_name = 'Faded Short Sleeve T-shirts'
        product_price = '$16.51'
        shipping_cost = '$2.00'
        get_h1, get_price, get_quantity = self.checkout_feature.click_on_faded_tshirt()
        assert product_name in self.driver.title, 'Page title must contain ' + product_name
        assert product_name == get_h1, 'H1 must contain ' + product_name
        assert product_price == get_price, 'Price must be ' + product_price
        assert '1' == get_quantity, 'Default quantity must be ' + '1'
        get_heading_counter, get_product_name, get_product_size, get_product_unit_price, get_cart_shipping_cost, \
            get_cart_total_cost = self.checkout_feature.add_to_cart_size_l(2)
        assert '2 Products' in get_heading_counter, 'Heading counter must contain 2 Products'
        assert product_name == get_product_name, 'Product name must be ' + product_name
        assert 'Size : L' in get_product_size, 'Product size must be L'
        assert product_price == get_product_unit_price, 'Product unit price must be ' + product_price
        assert shipping_cost == get_cart_shipping_cost, 'Total shipping cost must be ' + shipping_cost
        assert '$35.02' == get_cart_total_cost, 'Cart total cost must be $35.02'
        self.checkout_feature.proceed_to_checkout_registered_user('varihig924@era7mail.com', '12345', 'check')
        assert 'You have chosen to pay by check.' in self.driver.page_source, 'Page title must be Order - My Store'


    def test_search_bar_is_displayed(self, setup):
        assert self.searching_produtcs.search_bar_is_displayed() is True, 'Search bar is not displayed'

    def test_empty_search_query(self, setup):
        assert '0 results' in self.searching_produtcs.enter_query_to_search_bar(''), 'Empty query should return no prod'
        assert self.searching_produtcs.search_alert_is_displayed() is True, 'Search alert bar should be displayed'

    @pytest.mark.parametrize('query', ['t-shirt', 'blouse', 'dress'])
    def test_search_tshirt_blouse_query(self, setup, query):
        assert '0 results' not in self.searching_produtcs.enter_query_to_search_bar(query), '0 result must not displ.'
        product_lst = self.searching_produtcs.list_of_products()
        assert len(product_lst) >= 1, 'Lenght of product list should greater or equal to 1'
