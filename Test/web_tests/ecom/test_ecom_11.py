import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 11')
class TestEcom_11(WebBase):

    @allure.title('Смок 11 Подборка все акционные товары проверка  неавторизованным пользователем)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_11(self):
        ecom = self.APP.web_activity.button_to_ecom_11()
        self.APP.web_steps.step_test_11()
        self.APP.web_any_page.close_cookie()
        city = "Санкт-Петербург и ЛО"
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        ecom.select_address_self_any(address_market, city, sw)
        ecom.page_up_local()
        ecom.check_items()
        ecom.sort_items()
        ecom.send_range_left()
        ecom.send_range_right()
        ecom.sort_brand()
        ecom.sort_noda()




