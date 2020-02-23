import pytest
import time


@pytest.mark.usefixtures('setup')
class TestShoppingCart:

    def test_shopping_cart_empty_not_logged(self, setup):
        # check whether 'Sign in' button is displayed
        assert self.shoppingCart.login_button_exists() is True
        # check the contents of the cart visible on the main page - it should be empty
        assert self.shoppingCart.main_page_cart_status() == '(empty)', 'Cart content should be empty -> ' + self.\
            shoppingCart.main_page_cart_status()
        self.shoppingCart.select_cart()
        time.sleep(2)
        # check that 'Your shopping cart is empty.' alert is displayed when you enter the shopping cart
        assert self.shoppingCart.check_no_contents() == 'Your shopping cart is empty.'

    def test_shopping_cart_empty_logged_in(self, setup):
        time.sleep(2)
        self.shoppingCart.log_in('mobiy43403@cityroyal.org', 'qwerty123')
        self.shoppingCart.go_back_to_main_page()
        # check the contents of the cart visible on the main page - it should be empty
        assert self.shoppingCart.main_page_cart_status() == '(empty)'
        self.shoppingCart.select_cart()
        time.sleep(2)
        # check that 'Your shopping cart is empty.' alert is displayed when you enter the shopping cart
        assert self.shoppingCart.check_no_contents() == 'Your shopping cart is empty.'

    def test_add_to_shopping_cart_logged_in(self, setup):
        time.sleep(2)
        self.shoppingCart.log_in('mobiy43403@cityroyal.org', 'qwerty123')
        self.shoppingCart.go_back_to_main_page()
        time.sleep(2)
        self.shoppingCart.select_item()
        time.sleep(2)
        self.shoppingCart.add_to_cart()
        time.sleep(2)
        self.shoppingCart.continue_shopping()
        self.shoppingCart.hover_over_cart()
        # check that 1 item was added to the shopping cart and is displayed on main page
        assert self.shoppingCart.check_item_in_cart_main_page() == '1'
        self.shoppingCart.select_cart()
        time.sleep(2)
        # check that 1 item was added to the shopping cart and is displayed in summary
        assert self.shoppingCart.check_item_in_cart_summary() == '1 Product'

    def test_add_to_shopping_cart_logged_out(self, setup):
        time.sleep(2)
        self.shoppingCart.select_item()
        time.sleep(2)
        self.shoppingCart.add_to_cart()
        time.sleep(2)
        self.shoppingCart.continue_shopping()
        self.shoppingCart.hover_over_cart()
        # check that 1 item was added to the shopping cart and is displayed on main page
        assert self.shoppingCart.check_item_in_cart_main_page() == '1'
        self.shoppingCart.select_cart()
        time.sleep(2)
        # check that 1 item was added to the shopping cart and is displayed in summary
        assert self.shoppingCart.check_item_in_cart_summary() == '1 Product'

    def test_remove_item_from_shopping_cart_logged_in(self, setup):
        time.sleep(2)
        self.shoppingCart.log_in('mobiy43403@cityroyal.org', 'qwerty123')
        self.shoppingCart.go_back_to_main_page()
        time.sleep(2)
        self.shoppingCart.select_item()
        time.sleep(2)
        self.shoppingCart.add_to_cart()
        time.sleep(2)
        self.shoppingCart.continue_shopping()
        self.shoppingCart.hover_over_cart()
        self.shoppingCart.remove_from_cart_main_page()
        time.sleep(2)
        # check the contents of the cart visible on the main page - it should be empty
        assert self.shoppingCart.main_page_cart_status() == '(empty)'
        self.shoppingCart.select_cart()
        time.sleep(2)
        # check that 'Your shopping cart is empty.' alert is displayed when you enter the shopping cart
        assert self.shoppingCart.check_no_contents() == 'Your shopping cart is empty.'

    def test_remove_item_from_shopping_cart_logged_out(self, setup):
        time.sleep(2)
        self.shoppingCart.select_item()
        time.sleep(2)
        self.shoppingCart.add_to_cart()
        time.sleep(2)
        self.shoppingCart.continue_shopping()
        self.shoppingCart.hover_over_cart()
        self.shoppingCart.remove_from_cart_main_page()
        time.sleep(2)
        # check the contents of the cart visible on the main page - it should be empty
        assert self.shoppingCart.main_page_cart_status() == '(empty)'
        self.shoppingCart.select_cart()
        time.sleep(2)
        # check that 'Your shopping cart is empty.' alert is displayed when you enter the shopping cart
        assert self.shoppingCart.check_no_contents() == 'Your shopping cart is empty.'
