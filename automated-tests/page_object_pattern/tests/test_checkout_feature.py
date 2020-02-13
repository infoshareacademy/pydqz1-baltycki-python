from time import sleep
import pytest
from ..pages.main_page import MainPage
from ..pages.product_page import ProductPage
from ..pages.cart_page_summary import CartPageSummary
from ..pages.cart_page_sign_in import CartPageSignIn
from ..pages.cart_page_addresses import CartPageAddresses
from ..pages.cart_page_shipping import CartPageShipping
from ..pages.cart_page_payment import CartPagePayment
from ..pages.cart_page_order_summary import CartPageOrderSummary
from ..pages.cart_page_order_confirmation import CartPageOrderConfirmation


@pytest.mark.usefixtures('setup')
class TestCheckoutFeature:

    def test_registered_user_pay_by_bank_wire(self):
        """Happy path: registered user with one item in cart paid by bank wire"""
        self.driver.get('http://automationpractice.com/index.php')
        main_page = MainPage(self.driver)
        main_page.click_on_product()
        product_page = ProductPage(self.driver)
        product_page.add_product_to_cart()
        cart_summary = CartPageSummary(self.driver)
        cart_summary.click_checkout_button()
        cart_sigin = CartPageSignIn(self.driver)
        cart_sigin.login_as_registered_user()
        cart_address = CartPageAddresses(self.driver)
        cart_address.click_checkout_button()
        cart_shipping = CartPageShipping(self.driver)
        cart_shipping.enable_checkbox()
        cart_shipping.click_checkout_button()
        cart_payment = CartPagePayment(self.driver)
        cart_payment.click_pay_by_bank_wire()
        cart_order_summary = CartPageOrderSummary(self.driver)
        cart_order_summary.click_order_confirmation_buton()
        cart_order_confirmation = CartPageOrderConfirmation(self.driver)
        order_complete = cart_order_confirmation.get_order_confiramation_text()
        sleep(2)
        assert 'Your order on My Store is complete.' == order_complete, 'No order complete text on page'
        sleep(2)
