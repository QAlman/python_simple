import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 1')
class TestEcom_1(WebBase):

    @allure.title('Смок 1 Фильтр по цене')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_1(self):

        ecom = self.APP.web_activity.button_to_ecom_1()
        self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        ecom.send_range_left()
        ecom.send_range_right()
        ecom.compare_all()


