import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Verme')
@allure.story('Test 2  Регистрации')
class TestVerme_2(WebBase):

    @allure.title('2:  Регистрации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-967 : Регистрации на Shifts-dev - Version 1", url="https://testlink.verme.ru/index.php?caller=login&viewer=")

    @allure.description("Позитивный тест 2-967 : Регистрации на Shifts-dev - Version 1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def test_verme_2(self):

        verme = self.APP.web_activity.button_to_verme()
        time.sleep(222222)
        self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        verme.send_range_left()
        verme.send_range_right()
        verme.compare_all()


