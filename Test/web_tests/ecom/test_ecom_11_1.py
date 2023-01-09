import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 11')
class TestEcom_11_1(WebBase):

    @allure.title('Смок 11_1 Подборка все акционные товары проверка авторизованным пользователем)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_11_1(self):
        ecom = self.APP.web_activity.button_to_ecom_11()
        self.APP.web_steps.step_test_11_1()
        #ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_any_page.close_cookie()
        ecom.click_btn_registration()
        ecom.click_phone()
        txt_phone = "9883237989"
        ecom.send_phone(txt_phone)
        ecom.click_next_button()
        arg = [0]
        self.APP.web_any_page.send_sms_code_phone(*arg)
        ecom.small_wait()
        city = "Санкт-Петербург и ЛО"
        sw = "1"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        ecom.select_address_self_any(address_market, city, sw)
        ecom.small_wait()

        ecom = self.APP.web_activity.button_to_ecom_11()
        ecom.check_items()
        ecom.sort_items()
        ecom.send_range_left()
        ecom.send_range_right()
        ecom.sort_brand()
        ecom.sort_noda()




