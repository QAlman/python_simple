import time
from random import random
import allure
import pytest
import FW.WEB.ecom.ecom_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 15')
class TestEcom_15(WebBase):

    @allure.title('Смок 15 Избранное товары, списки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_15(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_15()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        ecom.select_address_self_any(address_market, city, sw)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_15)
        ecom.click_favorites_small()
        ecom.click_favorites_small()
        ecom.click_favorites_small()
        ecom.basket_add_small()
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_15_1)
        ecom.click_favorites_remove()
        ecom.add_basket()
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_15_2)
        v = "Список"
        ecom.click_tab_tab(v)
        ecom.click_manual_send()
        vv = "cok"
        ecom.send_manual_send(vv)
        ecom.send_enter_now()
        vvv = "Кола"
        ecom.send_manual_send(vvv)
        ecom.send_enter_now()
        n = 4
        ecom.click_button_delete(n)
        ecom.click_button_repair()
        m = 3
        ecom.click_button_delete(m)
        #assert n == m , "Нет страницы поиска "







