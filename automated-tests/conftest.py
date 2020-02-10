import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(request):
# te akcje zostsaną wykonane przed testem:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    """It's easy - request.cls is the test class using the fixture, so request.cls.driver = ...
    is essentially the same as MyTestClass.driver = ... if MyTestClass uses the fixture.
    https://pytest.readthedocs.io/en/2.8.7/builtin.html"""

# te akcje zostaną po wykonaniu akcji z plików z testami:
    yield
    driver.quit()

