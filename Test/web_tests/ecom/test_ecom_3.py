import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 3')
class TestEcom_3(WebBase):

    @allure.title('Смок 3 Фильтр по бренду и фабрике')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_3(self):
        ecom = self.APP.web_activity.button_to_ecom_2()
        self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        ecom.move_to_enterprise()
        b = "365"
        ecom.select_brand_all(b)
        ecom.show_next_2()
        ecom.select_fabric(b)
        ecom.check_select_brand_all(b)
