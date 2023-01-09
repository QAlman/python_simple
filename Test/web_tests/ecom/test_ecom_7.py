import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 7')
class TestEcom_7(WebBase):

    @allure.title('Смок 7 Просмотр большой и маленькой карточки SKU (Тест не готов - с лупой не работает)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_7(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_7()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        ecom.select_address_self_any(address_market, city, sw)

        ecom.open_noda_coffee()







