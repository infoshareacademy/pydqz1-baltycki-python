import pytest
import allure


@allure.description('Testing Checkout Feature')
@pytest.mark.usefixtures('setup')
class TestCheckoutFeature:
    @allure.title('Try to place order with unchecked Terms of Service checkbox')
    @pytest.mark.parametrize('mail, password', [('varihig924@era7mail.com', '12345')])
    def test_terms_checkbox(self, setup, mail, password):
        notify_text = 'You must agree to the terms of service before continuing.'
        self.checkout_feature.add_one_blouse_to_cart()
        self.checkout_feature.login_as_registered_user(mail, password)
        get_notify_is_displayed, get_notify_text = self.checkout_feature.proceed_to_shipping_options()
        assert True == get_notify_is_displayed, 'Notify must be displayed'
        assert notify_text == get_notify_text, 'Notify text must be ' + notify_text

    @allure.title('Checkout Product')
    @pytest.mark.parametrize('payment_option', ['bank wire', 'check'])
    def test_checkout_2_items(self, setup, payment_option):
        product_name = 'Faded Short Sleeve T-shirts'
        product_price = '$16.51'
        shipping_cost = '$2.00'
        total_cost = '$35.02'
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
        assert total_cost == get_cart_total_cost, 'Cart total cost must be ' + total_cost
        self.checkout_feature.proceed_to_checkout_registered_user(payment_option)
        assert 'Order confirmation - My Store' == self.driver.title, 'Page title must be Order - My'
        if payment_option == 'bank wire':
            assert 'Please send us a bank wire' in self.driver.page_source, 'Page must contain info about bank wire'
            assert total_cost in self.driver.page_source, 'Page must contain final amount ' + total_cost
        elif payment_option == 'check':
            assert 'Your check must include:' in self.driver.page_source, 'Page must contain info about bank wire'
            assert total_cost in self.driver.page_source, 'Page must contain final amount ' + total_cost
