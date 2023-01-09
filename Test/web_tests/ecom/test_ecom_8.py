import time
from random import random
import allure
import pytest
import FW.WEB.ecom.ecom_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 8')
class TestEcom_8(WebBase):

    @allure.title('Смок 8 Подборки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_8(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_8()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        ecom.select_address_self_any(address_market, city, sw)
        time.sleep(4)
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
        ecom.page_down_local()
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_8)
        oo = "Подpобнее"
        ecom.click_button_all(oo)
        ecom.click_container_address()

