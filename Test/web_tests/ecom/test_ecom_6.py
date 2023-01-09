import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 6')
class TestEcom_6(WebBase):

    @allure.title('Смок 6 Сортировка в нодах каталога')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_6(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_6()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        ecom.select_address_self_any(address_market, city, sw)
        ecom.open_noda_coffee()
        ecom.sort_items_pop()
        item = "Кофе зерновой EGOISTE Noir, 1кг"
        ecom.get_items_one(item)
        ecom.sort_items()






