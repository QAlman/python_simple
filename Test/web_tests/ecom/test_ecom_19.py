import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 19')
class TestEcom_19(WebBase):

    @allure.title('Смок 19 Товар закончился, выбрать другой')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_19(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_19
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        city = "Санкт-Петербург и ЛО"
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        ecom.select_address_self_any(address_market, city, sw)
        ecom.open_catalog()
        ecom.open_noda_coffee()
        ecom.select_tee()
        ecom.basket_add()
        ecom.basket_move()
        city = "Санкт-Петербург и ЛО"
        sw = "1"
        address_market = "Малый пр. ВО, д. 54, лит"
        ecom.select_address_self_any(address_market, city, sw)
        # address_market = "г. Ломоносов, ул. Михайловская, д. 40/7"
        c = "Товар закончился"
        ecom.basket_check_delivery(c)
        ecom.click_next_item()
        ecom.switch_to_new_tab()
        ecom.check_noda_black_tee()







