import pytest
import allure


@allure.description('Testing search feature')
@pytest.mark.usefixtures('setup')
class TestSearchingProducts:

    def test_search_bar_is_displayed(self, setup):
        assert self.searching_produtcs.search_bar_is_displayed() is True

    def test_empty_search_query(self, setup):
        assert self.searching_produtcs.search_bar_is_displayed() is True
        assert '0 results' in self.searching_produtcs.enter_query_to_search_bar('')
        assert self.searching_produtcs.search_alert_is_displayed() is True

    def test_search_tshirt_query(self, setup):
        assert '1 result' in self.searching_produtcs.enter_query_to_search_bar('t-shirt')
        assert len(self.searching_products.list_of_products()) > 0

    # def test_search_dress_query(self, setup):
    #     assert self.searching_produtcs.search_bar_is_displayed() is True
    #     product_counter = str(len(self.searching_produtcs.list_of_products()))
    #     assert '7 result' in self.searching_produtcs.enter_query_to_search_bar('dress')
    #     assert 'Search - My Store' == self.driver.title
    #     assert '7' == product_counter
