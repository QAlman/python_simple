import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 34')
class TestEcom_34(WebBase):

    @allure.title('Смок 34 Создание заказа с примененным промокодом на доставку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_34(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_34()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        ecom.click_phone()
        num = "9407718110"
        ecom.send_phone(num)
        ecom.click_next_button()
        arg = [0]
        self.APP.web_any_page.send_sms_code_phone(*arg)
        ecom.small_wait()
        ecom.basket_move()
        ecom.clear_basket()
        sw = "1"
        address_market = "г Новосибирск, Гусинобродское шоссе, д 64"
        city = "Новосибирск"
        ecom.select_address_delivery_any(address_market, city, sw)
        ecom.add_basket()
        pr = "Тест11"
        ecom.add_promocode(pr)
        p = ecom.get_price()
        z = " 10%"
        ecom.click_apply(z)
        pt = ecom.get_price_tips()
        pf = ecom.get_price_final()
        ecom.continue_next()
        d = 100
        ecom.check_price(p, pf, d)
        ecom.check_price_basket(pf)
        ecom.select_flat()
        ecom.click_delivery()
        ecom.click_other_card()
        ecom.select_card()
        ecom.send_pay()
        ecom.click_success()
        ecom.final_table()
        ecom.check_final(pf)


