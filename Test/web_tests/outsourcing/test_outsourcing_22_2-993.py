import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 22   Тестирование страницы - Версия1')
class TestOutsourcing_22(WebBase):

    @allure.title('22: 2-993 :  Тестирование страницы - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-993 :  Тестирование страницы - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-993 :  Тестирование страницы - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def test_outsourcing_22(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/outsource/orglinks/client/"
        outsourcing.goto_employees_all_page(ur)

        ch = "SPAR"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)

        outsourcing.small_time()





