import pytest
import allure
from assertpy import assert_that


@allure.parent_suite('Checkout Feature')
@allure.description("Tests validating proper Checkout Feature behaviour")
@pytest.mark.usefixtures('setup')
class TestCheckoutFeature:
    @allure.title('Can\'t checkout with unchecked Terms of Service checkbox')
    @allure.description_html("""<h2>Customer must not checkout when Terms of Service checkbox is unchecked</h2>""")
    @pytest.mark.parametrize('mail, password', [('varihig924@era7mail.com', '12345'),
                                                ('varihig924@era7mail.com', '1234')])
    def test_terms_checkbox(self, setup, mail, password):
        notify_text = 'You must agree to the terms of service before continuing.'
        self.checkout_feature.add_one_blouse_to_cart()
        self.checkout_feature.login_as_registered_user(mail, password)
        get_notify_is_displayed, get_notify_text = self.checkout_feature.proceed_to_shipping_options()
        assert_that(get_notify_is_displayed).is_true(), 'Notify must be displayed'
        assert_that(notify_text).is_equal_to(get_notify_text), 'Notify text must be ' + notify_text

    @allure.title('Checkout and pay by {payment_option}')
    @allure.description_html("""<h2>Test checkout and check product name, price, shipping cost, total cost
                            on product page then on cart page and finally on order confirmation page</h2>""")
    @pytest.mark.parametrize('payment_option', ['bank wire', 'check'])
    @pytest.mark.parametrize('mail, password', [('varihig924@era7mail.com', '12345')])
    def test_checkout_2_items(self, setup, payment_option, mail, password):
        product_name = 'Faded Short Sleeve T-shirts'
        product_price = '$16.51'
        shipping_cost = '$2.00'
        total_cost = '$35.02'
        get_h1, get_price, get_quantity = self.checkout_feature.click_on_faded_tshirt()
        assert_that(self.driver.title).contains(product_name), 'Page title must contain ' + product_name
        assert_that(product_name).is_equal_to(get_h1), 'H1 must contain ' + product_name
        assert_that(product_price).is_equal_to(get_price), 'Price must be ' + product_price
        assert_that('1').is_equal_to(get_quantity), 'Default quantity must be ' + '1'
        get_heading_counter, get_product_name, get_product_size, get_product_unit_price, get_cart_shipping_cost, \
                                                    get_cart_total_cost = self.checkout_feature.add_to_cart_size_l(2)
        assert_that(get_heading_counter).contains('2 Products'), 'Heading counter must contain 2 Products'
        assert_that(product_name).is_equal_to(get_product_name), 'Product name must be ' + product_name
        assert_that(get_product_size).contains('Size : L'), 'Product size must be L'
        assert_that(product_price).is_equal_to(get_product_unit_price), 'Product unit price must be ' + product_price
        assert_that(shipping_cost).is_equal_to(get_cart_shipping_cost), 'Total shipping cost must be ' + shipping_cost
        assert_that(total_cost).is_equal_to(get_cart_total_cost), 'Cart total cost must be ' + total_cost
        self.checkout_feature.login_as_registered_user(mail, password)
        self.checkout_feature.proceed_to_checkout_registered_user(payment_option)
        assert_that('Order confirmation - My Store').is_equal_to(self.driver.title), 'Page title must be Order - My'
        if payment_option == 'bank wire':
            assert_that(self.driver.page_source).contains('Please send us a bank wire'), \
                                                                                'Page must contain info about bank wire'
            assert_that(self.driver.page_source).contains(total_cost), 'Page must contain final amount ' + total_cost
        elif payment_option == 'check':
            assert_that(self.driver.page_source).contains('Your check must include:'), \
                                                                                'Page must contain info about bank wire'
            assert_that(self.driver.page_source).contains(total_cost), 'Page must contain final amount ' + total_cost

    @allure.title('Checkout 1_000_000 of tshirts and pay by {payment_option}')
    @allure.description_html("""<h2>Test checkout 1_000_000 of tshirts and pay by {payment_option}.
                            Test must fail.</h2>""")
    @pytest.mark.parametrize('payment_option', ['bank wire'])
    @pytest.mark.parametrize('mail, password', [('varihig924@era7mail.com', '12345')])
    @pytest.mark.xfail(reason='It must not be possible to buy 1 milion of one product')
    def test_checkout1000000_items(self, setup, payment_option, mail, password):
        self.checkout_feature.click_on_faded_tshirt()
        self.checkout_feature.add_to_cart_size_l(1_000_000)
        self.checkout_feature.login_as_registered_user(mail, password)
        self.checkout_feature.proceed_to_checkout_registered_user(payment_option)
        assert_that('Order confirmation - My Store').is_equal_to(self.driver.title), 'Page title must be Order - My'
