import pytest
import allure
from assertpy import assert_that


@allure.parent_suite('Searching Products Feature - HEADLESS 1920x1080')
@allure.description("Tests validating proper Searching Products behaviour")
@pytest.mark.usefixtures('headless_1920_1080')
class TestSearchingProducts:

    @allure.title('Check if search bar is displayed')
    @allure.description_html("""<h2>Search bar must be displayed</h2>""")
    def test_search_bar_is_displayed(self, headless_1920_1080):
        assert_that(self.searching_products.search_bar_is_displayed()).is_true()

    @allure.title('Enter empty query to search bar')
    @allure.description_html("""<h2>Search bar alert must be displayed</h2>""")
    def test_empty_search_query(self, headless_1920_1080):
        assert_that(self.searching_products.search_bar_is_displayed()).is_true()
        assert_that(self.searching_products.enter_query_to_search_bar('')).contains('0 results')
        assert_that(self.searching_products.search_alert_is_displayed()).is_true()

    @allure.title('Enter t-shirt query to search bar')
    @allure.description_html("""<h2>Page should display at least one product</h2>""")
    def test_search_tshirt_query(self, headless_1920_1080):
        assert_that(self.searching_products.enter_query_to_search_bar('t-shirt')).contains('1 result')
        assert_that(len(self.searching_products.list_of_products())).is_greater_than(0)

    @allure.title('Enter dress query to search bar')
    @allure.description_html("""<h2>Page should display at least one product</h2>""")
    def test_search_dress_query(self, headless_1920_1080):
        assert_that(self.searching_products.search_bar_is_displayed()).is_true()
        assert_that(len(self.searching_products.list_of_products())).is_greater_than(0)
        assert_that(self.searching_products.enter_query_to_search_bar('dress')).contains('7 result')
        assert_that(self.driver.title).is_equal_to('Search - My Store')
