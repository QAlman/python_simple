import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 32   Проверка отображения ссылки в карточке сотрудника')
class _TestOutsourcing_32(WebBase):

    @allure.title('32: 2-983 :  Проверка отображения ссылки в карточке сотрудника - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-983 :  Проверка отображения ссылки в карточке сотрудника - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-983 :  Проверка отображения ссылки в карточке сотрудника - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def _test_outsourcing_32(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-employee/127635"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "1.1"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        """
        Необходимо уточнить про кнопку  AMO CRM

        """

