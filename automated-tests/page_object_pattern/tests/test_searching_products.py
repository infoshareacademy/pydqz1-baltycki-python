import pytest


@pytest.mark.usefixtures('setup')
class TestSearchingProducts:

    def test_search_empty_query(self, setup):
        assert '' == self.searching_products.search_box_is_empty()
