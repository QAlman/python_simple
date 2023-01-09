import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 4')
class TestEcom_4(WebBase):

    @allure.title('Смок 4 Акции , выпадающее меню')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_4(self):
        ecom = self.APP.web_activity.button_to_ecom()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        ecom.move_to_actions()
        z = "Акции для спб"
        ecom.select_actions(z)


