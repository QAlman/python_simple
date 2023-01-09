import time
from random import random
import allure
import pytest
import FW.WEB.ecom.ecom_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 12')
class TestEcom_12(WebBase):

    @allure.title('Смок 12 Наличие в других ТК')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_12(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_12()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А" #ул.  Савушкина, д. 112, лит. А
        city = "Санкт-Петербург и ЛО"
        ecom.select_address_self_any(address_market, city, sw)
        #time.sleep(4)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_12)
        address = "ул. Савушкина, д. 112, лит. А"
        ecom.check_container(address)
        ecom.click_container_address()
        ecom.click_container_search()
        address = "выборгское, д. 11"
        ecom.send_container_search(address)
        stock = "Товара много"
        ecom.check_container_search_address(stock)
        address = "ш. Выборгское, д. 11, лит. А"
        ecom.click_container_search_address(address)
        ecom.page_up_local()
        z = ecom.check_address_location()
        assert address in z, "We have problem"

        sw = "1"
        address_market = "ш. Кирилловское, д. 50А"
        city = "Кострома"
        ecom.select_address_self_any(address_market, city, sw)






