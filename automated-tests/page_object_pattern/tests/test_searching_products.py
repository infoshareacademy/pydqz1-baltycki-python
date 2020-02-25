import pytest
import allure


@allure.description('Testing search feature')
@pytest.mark.usefixtures('setup')
class TestSearchingProducts:

    def test_search_bar_is_displayed(self, setup):
        assert self.searching_produtcs.search_bar_is_displayed() is True, 'Search bar is not displayed'

    def test_empty_search_query(self, setup):
        assert '0 results' in self.searching_produtcs.enter_query_to_search_bar(''), 'Empty query should return no prod'
        assert self.searching_produtcs.search_alert_is_displayed() is True, 'Search alert bar should be displayed'

    @pytest.mark.parametrize('query', ['t-shirt', 'blouse', 'dress'])
    def test_search_tshirt_blouse_query(self, setup, query):
        assert '0 results' not in self.searching_produtcs.enter_query_to_search_bar(query), '0 result must not displ.'
        product_lst = self.searching_produtcs.list_of_products()
        assert len(product_lst) >= 1, 'Lenght of product list should greater or equal to 1'
