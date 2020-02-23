import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from page_object_pattern.pages.shopping_cart import ShoppingCart


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://automationpractice.com/index.php')
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)
    request.cls.shoppingCart = ShoppingCart(driver)
    yield
    before_failed = request.session.testsfailed
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    driver.quit()
