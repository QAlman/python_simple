import time
from random import random
import allure
import pytest
import FW.WEB.ecom.ecom_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 13')
class TestEcom_13(WebBase):

    @allure.title('Смок 13 Блок "Вы смотрели"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_13(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_13()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        ecom.select_address_self_any(address_market, city, sw)
        ecom.open_noda_milk()
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_13)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_13_1)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_13_2)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_13_3)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_13_4)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_13_5)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_13_6)
        ecom.page_down_local()
        ecom.move_to_carousel()

        ecom.click_carousel_left()
        ecom.click_carousel_right()








