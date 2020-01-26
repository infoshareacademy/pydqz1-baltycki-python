import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# zaimportowana strona z lokatorami do użycia wewną†rz medoty selenium select...():
from locators import main_page


# klasa z testami dotyczącymi jednej funkcjonalności:
@pytest.mark.usefixtures('setup')
class TestPageFeature:

# pojedyńczy test odnośnie danej funkcjonalności np. czy jak wpiszę w wyszukiwarkę tekst to mi wyskoczy dobry wynik?
    def test_name(self):
        """opis co robi test"""
        """test powinien: otworzyć stronę, wykonać akcje i zakończyć się assercją"""
