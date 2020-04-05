import pytest
import allure
from allure_commons.types import AttachmentType
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from page_object_pattern.pages.register_page import RegisterPage
from page_object_pattern.pages.login_page import LoginPage
from page_object_pattern.pages.checkout_feature import CheckoutFeature
from page_object_pattern.pages.searching_products import SearchingProducts
from page_object_pattern.pages.shopping_cart_page import ShoppingCart


@pytest.fixture()
def desktop_1366_768(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://automationpractice.com/index.php')
    request.cls.driver = driver
    request.cls.register_page = RegisterPage(driver)
    request.cls.login_page = LoginPage(driver)
    request.cls.checkout_feature = CheckoutFeature(driver)
    request.cls.searching_products = SearchingProducts(driver)
    request.cls.shoppingCart = ShoppingCart(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    sleep(2)
    driver.quit()


@pytest.fixture()
def mobile_360_640(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(360, 640)
    driver.implicitly_wait(10)
    driver.get('http://automationpractice.com/index.php')
    request.cls.driver = driver
    request.cls.register_page = RegisterPage(driver)
    request.cls.login_page = LoginPage(driver)
    request.cls.checkout_feature = CheckoutFeature(driver)
    request.cls.searching_products = SearchingProducts(driver)
    request.cls.shoppingCart = ShoppingCart(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    sleep(2)
    driver.quit()


@pytest.fixture()
def mobile_414_896(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(414, 896)
    driver.implicitly_wait(10)
    driver.get('http://automationpractice.com/index.php')
    request.cls.driver = driver
    request.cls.register_page = RegisterPage(driver)
    request.cls.login_page = LoginPage(driver)
    request.cls.checkout_feature = CheckoutFeature(driver)
    request.cls.searching_products = SearchingProducts(driver)
    request.cls.shoppingCart = ShoppingCart(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    sleep(2)
    driver.quit()


@pytest.fixture()
def headless_1920_1080(request):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://automationpractice.com/index.php')
    request.cls.driver = driver
    request.cls.register_page = RegisterPage(driver)
    request.cls.login_page = LoginPage(driver)
    request.cls.checkout_feature = CheckoutFeature(driver)
    request.cls.searching_products = SearchingProducts(driver)
    request.cls.shoppingCart = ShoppingCart(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    sleep(2)
    driver.quit()
