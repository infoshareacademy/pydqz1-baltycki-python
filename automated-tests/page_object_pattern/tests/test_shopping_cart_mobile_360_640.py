import pytest
import allure
from assertpy import assert_that


@allure.parent_suite('Shopping Cart - MOBILE 360x640')
@allure.description("Tests validating proper shopping cart behaviour")
@pytest.mark.usefixtures('mobile_360_640')
class TestShoppingCart:
    @pytest.mark.skip(reason="Problem wit javascript error: Failed to execute 'elementsFromPoint'")
    @allure.title('Add item to shopping cart from main menu - logged in')
    def test_add_to_shopping_cart_logged_in(self, mobile_360_640):
        self.shoppingCart.log_in()
        self.shoppingCart.go_back_to_main_page()
        # check the contents of the cart visible on the main page - it should be empty
        assert_that(self.shoppingCart.main_page_cart_status()).contains('(empty)')
        self.shoppingCart.select_cart()
        # check that 'Your shopping cart is empty.' alert is displayed when you enter the shopping cart
        assert_that(self.shoppingCart.check_no_contents()).contains('Your shopping cart is empty.')
        self.shoppingCart.go_back_to_main_page()
        self.shoppingCart.select_item()
        self.shoppingCart.add_to_cart()
        self.shoppingCart.continue_shopping()
        self.shoppingCart.hover_over_cart()
        # check that 1 item was added to the shopping cart and is displayed on main page
        assert_that(self.shoppingCart.check_item_in_cart_main_page()).contains('1')
        self.shoppingCart.select_cart()
        # check that 1 item was added to the shopping cart and is displayed in summary
        assert_that(self.shoppingCart.check_item_in_cart_summary()).contains('1 Product')

    @allure.title('Add item to shopping cart from main menu - not logged')
    def test_add_to_shopping_cart_logged_out(self, mobile_360_640):
        # check the contents of the cart visible on the main page - it should be empty
        assert_that(self.shoppingCart.main_page_cart_status()).contains('(empty)')
        self.shoppingCart.select_cart()
        # check that 'Your shopping cart is empty.' alert is displayed when you enter the shopping cart
        assert_that(self.shoppingCart.check_no_contents()).contains('Your shopping cart is empty.')
        self.shoppingCart.go_back_to_main_page()
        self.shoppingCart.select_item()
        self.shoppingCart.add_to_cart()
        self.shoppingCart.continue_shopping()
        self.shoppingCart.hover_over_cart()
        # check that 1 item was added to the shopping cart and is displayed on main page
        assert_that(self.shoppingCart.check_item_in_cart_main_page()).contains('1')
        self.shoppingCart.select_cart()
        # check that 1 item was added to the shopping cart and is displayed in summary
        assert_that(self.shoppingCart.check_item_in_cart_summary()).contains('1 Product')

    @allure.title('Remove item from the shopping cart in main menu - logged in')
    def test_remove_item_from_shopping_cart_logged_in(self, mobile_360_640):
        self.shoppingCart.log_in()
        self.shoppingCart.go_back_to_main_page()
        self.shoppingCart.select_item()
        self.shoppingCart.add_to_cart()
        self.shoppingCart.continue_shopping()
        self.shoppingCart.hover_over_cart()
        self.shoppingCart.remove_from_cart_main_page()
        # check the contents of the cart visible on the main page - it should be empty
        assert_that(self.shoppingCart.main_page_cart_status()).does_not_contain('1')
        self.shoppingCart.select_cart()
        # check that 'Your shopping cart is empty.' alert is displayed when you enter the shopping cart
        assert_that(self.shoppingCart.check_no_contents()).contains('Your shopping cart is empty.')

    @allure.title('Add item to the shopping cart and proceed to checkout - not logged')
    def test_proceed_to_checkout_logged_out(self, mobile_360_640):
        self.shoppingCart.select_item()
        self.shoppingCart.add_to_cart()
        self.shoppingCart.proceed_to_checkout_from_main_page()
        # check that 1 item was added to the shopping cart and is displayed in summary
        assert_that(self.shoppingCart.check_item_in_cart_summary()).contains('1 Product')

    @allure.title('Add item to the shopping cart and proceed to checkout - logged in')
    def test_proceed_to_checkout_logged_in(self, mobile_360_640):
        self.shoppingCart.log_in()
        self.shoppingCart.go_back_to_main_page()
        self.shoppingCart.select_item()
        self.shoppingCart.add_to_cart()
        self.shoppingCart.proceed_to_checkout_from_main_page()
        # check that 1 item was added to the shopping cart and is displayed in summary
        assert_that(self.shoppingCart.check_item_in_cart_summary()).contains('1 Product')

    @allure.title('Add item to the shopping cart in details view - not logged')
    def test_details_view_logged_out(self, mobile_360_640):
        self.shoppingCart.select_item()
        self.shoppingCart.move_to_details_view()
        self.shoppingCart.add_to_cart_details_view()
        self.shoppingCart.continue_shopping()
        self.shoppingCart.hover_over_cart()
        # check that 1 item was added to the shopping cart and is displayed on main page
        assert_that(self.shoppingCart.check_item_in_cart_main_page()).contains('1')
        self.shoppingCart.select_cart()
        # check that 1 item was added to the shopping cart and is displayed in summary
        assert_that(self.shoppingCart.check_item_in_cart_summary()).contains('1 Product')

    @allure.title('Add item to the shopping cart in details view - logged in')
    def test_details_view_logged_in(self, mobile_360_640):
        self.shoppingCart.log_in()
        self.shoppingCart.go_back_to_main_page()
        self.shoppingCart.select_item()
        self.shoppingCart.move_to_details_view()
        self.shoppingCart.add_to_cart_details_view()
        self.shoppingCart.continue_shopping()
        self.shoppingCart.hover_over_cart()
        # check that 1 item was added to the shopping cart and is displayed on main page
        assert_that(self.shoppingCart.check_item_in_cart_main_page()).contains('1')
        self.shoppingCart.select_cart()
        # check that 1 item was added to the shopping cart and is displayed in summary
        assert_that(self.shoppingCart.check_item_in_cart_summary()).contains('1 Product')

    @allure.title('Add item to the shopping cart - check contents')
    def test_add_to_cart_check_contents(self, mobile_360_640):
        self.shoppingCart.select_item()
        self.shoppingCart.move_to_details_view()
        self.shoppingCart.add_additional_item()
        self.shoppingCart.change_color()
        self.shoppingCart.change_size()
        self.shoppingCart.add_to_cart_details_view()
        self.shoppingCart.proceed_to_checkout_from_main_page()
        # check that 2 items were added to the shopping cart and are displayed in summary
        assert_that(self.shoppingCart.check_item_in_cart_summary()).contains('2 Products'),
        # check that selected size is L and color is 'White'
        assert_that(self.shoppingCart.check_size_and_color()).contains('Color : White, Size : L'),
        # check that selected total price is 54$'
        assert_that(self.shoppingCart.check_total_price()).contains('$54.00')
