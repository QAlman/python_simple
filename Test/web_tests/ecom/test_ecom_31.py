import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 31')
class TestEcom_31(WebBase):

    @allure.title('Смок 31 Страница бренда неавторизованный ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_31(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_31()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()

        city = "Санкт-Петербург и ЛО"
        sw = "2"
        address_market = "ш. Выборгское, д. 11, лит. А"
        ecom.select_address_self_any(address_market, city, sw)
        ecom.open_catalog()
        ecom.open_noda_coffee()
        ecom.select_tee()
        ecom.move_to_brand()
        ecom.select_brand()
        b = "Страница RICHARD"
        ecom.page_brand(b)
        ecom.go_to_brand()
        ecom.page_brand(b)



