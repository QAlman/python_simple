import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 24')
class TestEcom_24(WebBase):

    @allure.title('Смок 24 Ганзель и Гретта')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_24(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_24()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        city = "Санкт-Петербург и ЛО"
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        ecom.select_address_self_any(address_market, city, sw)
        ecom.open_catalog()
        ecom.open_noda_milk()
        ecom.select_cheese()
        ecom.select_cheese_milk()






