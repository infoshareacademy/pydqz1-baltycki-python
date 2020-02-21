from time import sleep
import pytest
import allure
from faker import Faker
from ..pages.page import BasePage
from ..pages.locators import CommonPageLocators, OrderPageLocators

faker = Faker()
f_email = faker.email()


@allure.description('Testing checkout feature')
@pytest.mark.usefixtures('setup')
class TestCheckoutFeature:
    """

    """
    @allure.title('Registered user with 2 items in cart, paid by bank wire')
    @pytest.mark.parametrize('user, password', [('varihig924@era7mail.com', '12345')])
    def test_buying001(self, user, password):
        self.home = BasePage(self.driver)
        empty_cart = self.home.get_the_value(CommonPageLocators.CART_AJAX_EMPTY)
        assert '(empty)' == empty_cart, 'Cart is not empty, must contain (empty)'
        self.home.click(CommonPageLocators.PRODUCT_FADED_TSHIRTS)
        self.home.switch_to(CommonPageLocators.PRODUCT_QUICKVIEW)
        self.home.click(CommonPageLocators.PRODUCT_QUICKVIEW_ADD_QTY)
        self.home.click(CommonPageLocators.PRODUCT_SIZE_DROPX_L)
        self.home.click(CommonPageLocators.PRODUCT_COLOR_BLUE)
        self.home.click(CommonPageLocators.ADD_TO_CART_BUTTON)
        self.home.switch_to_default()
        self.home.click(CommonPageLocators.CART_LAYER_PROCEED_BUTTON)
        self.home.click(CommonPageLocators.CHECKOUT_BUTTON)
        self.home.enter_to_input(OrderPageLocators.EMAIL_INPUT, user)
        self.home.enter_to_input(OrderPageLocators.PASSWORD_INPUT, password)
        self.home.click(OrderPageLocators.SIGN_IN)
        self.home.click(OrderPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        self.home.click(OrderPageLocators.TERMS_CHECK_BOX)
        self.home.click(OrderPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        self.home.click(OrderPageLocators.PAY_BY_BANK_WIRE)
        self.home.click(OrderPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        assert 'Order confirmation - My Store' == self.driver.title, 'Page title should be "Order confirmation - ' \
                                                                     'My Store"'
        assert 'Your order on My Store is complete.' in self.driver.page_source, 'Page should have "Your order on ' \
                                                                                 'My Store is complete."'
        sleep(4)

    @pytest.mark.skip
    def test_buying002(self):
        self.home = BasePage(self.driver)
        empty_cart = self.home.get_the_value(CommonPageLocators.CART_AJAX_EMPTY)
        assert '(empty)' == empty_cart, 'Cart is not empty, must contain (empty)'
        self.home.hover_to(CommonPageLocators.PRODUCT_PRINTED_DRESS)
        self.home.click(CommonPageLocators.PRODUCT_HOVER_ADD_TO_CART_BUTTON)
        self.home.click(CommonPageLocators.CART_LAYER_CONTINUE_BUTTON)
        self.home.hover_to(CommonPageLocators.MENU_WOMEN)
        self.home.click(CommonPageLocators.MENU_WOMEN_DRESSES)
        self.home.hover_to(CommonPageLocators.PRODUCT_SUMMER_DRESS)
        self.home.click(CommonPageLocators.PRODUCT_HOVER_MORE_BUTTON)
        self.home.click(CommonPageLocators.PRODUCT_SIZE_DROPX_L)
        self.home.enter_to_input(CommonPageLocators.QUANTITY_INPUT, '100')
        self.home.click(CommonPageLocators.PRODUCT_COLOR_ORANGE)
        self.home.click(CommonPageLocators.ADD_TO_CART_BUTTON)
        self.home.click(CommonPageLocators.CART_LAYER_CONTINUE_BUTTON)
        self.home.click(CommonPageLocators.PAGE_LOGO)
        # self.home.search_for('blouse')
        # self.home.click(CommonPageLocators.PRODUCT_BLOUSE)
        # self.home.switch_to(CommonPageLocators.PRODUCT_QUICKVIEW)
        # self.home.click(CommonPageLocators.PRODUCT_COLOR_WHITE)
        # self.home.enter_to_input(CommonPageLocators.QUANTITY_INPUT, '3')
        # self.home.click(CommonPageLocators.ADD_TO_CART_BUTTON)
        # self.home.switch_to_default()
        # self.home.click(CommonPageLocators.CART_LAYER_PROCEED_BUTTON)
        self.home.click(CommonPageLocators.SHOPPING_CART)
        self.home.click(CommonPageLocators.CHECKOUT_BUTTON)

    @pytest.mark.skip
    @pytest.mark.parametrize('user, password', [('varihig924@era7mail.com', '12345')])
    def test_login_full_shopping_cart(self, user, password):
        self.home = BasePage(self.driver)
        self.home.click(CommonPageLocators.SHOPPING_CART)
        self.home.enter_to_input(OrderPageLocators.EMAIL_INPUT, user)
        self.home.enter_to_input(OrderPageLocators.PASSWORD_INPUT, password)
        self.home.click(OrderPageLocators.SIGN_IN)
        self.home.click(OrderPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        self.home.click(OrderPageLocators.TERMS_CHECK_BOX)
        self.home.click(OrderPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        sleep(3)
