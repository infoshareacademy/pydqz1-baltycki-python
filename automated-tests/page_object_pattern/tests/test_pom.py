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
        self.home.click(CommonPageLocators.PRODUCT_FADED_TSHIRTS)
        self.home.switch_to(CommonPageLocators.PRODUCT_QUICKVIEW)
        self.home.click(CommonPageLocators.PRODUCT_QUICKVIEW_ADD_QTY)
        self.home.click(CommonPageLocators.PRODUCT_QUICKVIEW_SIZE_DROPX_L)
        self.home.click(CommonPageLocators.PRODUCT_QUICKVIEW_COLOR_BLUE)
        self.home.click(CommonPageLocators.ADD_TO_CART_BUTTON)
        self.home.switch_to_default()

        sleep(2)
        self.home.search_for('tshirts')
        sleep(1)
        self.home.click(CommonPageLocators.PAGE_LOGO)
        sleep(1)

