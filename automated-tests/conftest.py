import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from page_object_pattern.pages.shopping_cart import ShoppingCart


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://automationpractice.com/index.php')
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 15)
    request.cls.shoppingCart = ShoppingCart(driver)
    yield
    time.sleep(2)
    driver.quit()