from time import sleep
import pytest
from ..pages.page import BasePage
from ..pages.locators import CommonPageLocators


@pytest.mark.usefixtures('setup')
class TestCheckoutFeature:
    """

    """
    def test_TC001(self):
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
        self.home.click(CommonPageLocators.CART_LAYER_CONTINUE_BUTTON)
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
        self.home.search_for('blouse')
        self.home.click(CommonPageLocators.PRODUCT_BLOUSE)
        self.home.switch_to(CommonPageLocators.PRODUCT_QUICKVIEW)
        self.home.click(CommonPageLocators.PRODUCT_COLOR_WHITE)
        self.home.enter_to_input(CommonPageLocators.QUANTITY_INPUT, '3')
        self.home.click(CommonPageLocators.ADD_TO_CART_BUTTON)
        self.home.switch_to_default()
        self.home.click(CommonPageLocators.CART_LAYER_PROCEED_BUTTON)
        sleep(3)
