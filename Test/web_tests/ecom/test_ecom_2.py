import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 2')
class TestEcom_2(WebBase):

    @allure.title('Смок 2 Сортировка по бренду')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_ecom_2(self):
        ecom = self.APP.web_activity.button_to_ecom_2()
        self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        ecom.move_to_enterprise()
        ecom.show_next()
        b = "365"
        ecom.select_brand_all(b)
        ecom.check_select_brand_all(b)

