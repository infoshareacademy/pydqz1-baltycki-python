from time import sleep
import pytest
import json
from ..utils.read_json import JsonReader
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

    def test_unregistered_user_happy_path(self):
        """Happy path: unregistered user with one item in cart paid by bank wire"""
        user_data = JsonReader.get_user_data()
        random_number = randint(1, 1000)
        self.driver.get('http://automationpractice.com/index.php')
        main_page = MainPage(self.driver)
        main_page.action_on_page()
        product_page = ProductPage(self.driver)
        product_page.action_on_page()
        cart_summary = CartPageSummary(self.driver)
        cart_summary.action_on_page()
        cart_sigin = CartPageSignIn(self.driver)

        # cart_sigin.action_on_page()
        # cart_address = CartPageAddresses(self.driver)
        # cart_address.action_on_page()
        # cart_shipping = CartPageShipping(self.driver)
        # cart_shipping.action_on_page()
        # cart_payment = CartPagePayment(self.driver)
        # cart_payment.action_on_page()
        # cart_order_summary = CartPageOrderSummary(self.driver)
        # cart_order_summary.action_on_page()
        # cart_order_confirmation = CartPageOrderConfirmation(self.driver)
        # order_complete = cart_order_confirmation.action_on_page()
        sleep(2)
        # assert 'Your order on My Store is complete.' == order_complete, 'No order complete text on page'
