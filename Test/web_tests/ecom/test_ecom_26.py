import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 26')
class TestEcom_26(WebBase):

    @allure.title('Смок 26 Товар недоступен для доставки,выбрать другой')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_26(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_26()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        #ecom.click_btn_registration()
        ecom.click_phone()
        txt_phone = "9945274140"
        ecom.send_phone(txt_phone)
        ecom.click_next_button()
        arg = [0]
        self.APP.web_any_page.send_sms_code_phone(*arg)
        ecom.small_wait()
        ecom.basket_move()
        ecom.clear_basket()
        city = "Новосибирск" #г. Новосибирск, гусинобродское шоссе 64
        sw = "1"
        address_market = "ш. Гусинобродское, д. 64"
        ecom.select_address_self_any(address_market, city, sw)
        time.sleep(6)
        ecom.open_catalog()
        #ecom.open_noda_alco()
        ecom.open_noda_forhome()
        #ecom.select_alco_item()
        ecom.basket_add()
        ecom.basket_move()
        # city = "Санкт-Петербург и ЛО"
        #sw = "1"
        address_market = "г Новосибирск, Гусинобродское шоссе, д 64" #г Санкт-Петербург, Выборгское шоссе, д 11 литера А
        ecom.select_address_delivery_any(address_market, city, sw)
        ecom. small_wait()
        c = "Товар недоступен для доставки" #овар доступен в других магазинах "Лента"
        ecom.basket_check_delivery(c)
        # ecom.click_next_item()
        # ecom.switch_to_new_tab()
        # ecom.check_noda_alco()






