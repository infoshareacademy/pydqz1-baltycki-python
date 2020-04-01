import pytest
import allure
from allure_commons.types import AttachmentType
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.checkout_feature import CheckoutFeature
from page_object_pattern.pages.searching_products import SearchingProducts
from page_object_pattern.pages.shopping_cart_page import ShoppingCart


@pytest.fixture()
def setup(request):
    # options = webdriver.ChromeOptions()
    # options.set_capability('browserName', 'chrome')
    # options.add_argument('headless')
    # options.add_argument('start-maximized')
    # driver = webdriver.Remote('http://localhost:4444/wd/hub', options=options)
    # options.add_argument("--window-size=2000,1000")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://automationpractice.com/index.php')
    request.cls.driver = driver
    request.cls.checkout_feature = CheckoutFeature(driver)
    request.cls.searching_products = SearchingProducts(driver)
    request.cls.shoppingCart = ShoppingCart(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    sleep(2)
    driver.quit()
