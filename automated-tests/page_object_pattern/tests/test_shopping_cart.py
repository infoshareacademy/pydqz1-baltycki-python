import pytest
import time


@pytest.mark.usefixtures('setup')
class TestShoppingCart:

    def test_shopping_cart_empty(self, setup):
        self.shoppingCart.select_cart()
        time.sleep(2)
        assert self.shoppingCart.check_no_contents() == 'Your shopping cart is empty.'
