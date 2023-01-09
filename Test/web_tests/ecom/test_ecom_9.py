import time
from random import random
import allure
import pytest
import FW.WEB.ecom.ecom_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 9')
class TestEcom_9(WebBase):

    @allure.title('Смок 9 Корзина, чекаут, спасибо за заказ Самовывоз (Тест не доделан полсностью)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_9(self):
        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_9()
        # self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        ecom.click_phone()
        num = "9407718110"
        ecom.send_phone(num)
        ecom.click_next_button()
        arg = [0]
        self.APP.web_any_page.send_sms_code_phone(*arg)
        time.sleep(4)
        ecom.refresh()
        sw = "1"
        address_market = "г Новосибирск, Гусинобродское шоссе, д 64"
        city = "Новосибирск"
        ecom.select_address_self_any(address_market, city, sw)
        ecom.small_wait()
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_9)
        ecom.small_wait()
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_9_1)

        ecom.page_up_local()
        ecom.move_to_actions()
        z = "СУПЕРСКИДКИ"
        ecom.select_actions(z)
        ecom.move_to_actions()
        z = "Товары недели"
        ecom.select_actions(z)
        o = "bigmedia карусель"
        ecom.get_header_title(o)
        ecom.move_to_carousel()
        ecom.click_carousel_left()
        ecom.click_carousel_right()
        ecom.move_to_actions()
        z = "Подборка Ленточка"
        ecom.select_actions(z)
        ecom.move_to_actions()
        z = "landing page"
        ecom.select_actions(z)
        ecom.move_to_actions()
        z = "Безумные скидки"
        ecom.select_actions(z)

