import pytest
import allure
from allure_commons.types import AttachmentType
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.checkout_feature import CheckoutFeature
from page_object_pattern.pages.searching_products import SearchingProducts
from page_object_pattern.pages.shopping_cart_page import ShoppingCart
from page_object_pattern.pages.register_page import RegisterPage
from page_object_pattern.pages.login_page import LoginPage


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://automationpractice.com/index.php')
    request.cls.driver = driver
    request.cls.checkout_feature = CheckoutFeature(driver)
    request.cls.searching_products = SearchingProducts(driver)
    request.cls.shoppingCart = ShoppingCart(driver)
    request.cls.register_page = RegisterPage(driver)
    request.cls.login_page = LoginPage(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    sleep(2)
    driver.quit()
