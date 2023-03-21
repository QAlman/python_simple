import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Outsourcing')
@allure.story('Test 34    Страница для вывода BI отчетов')
class TestOutsourcing_34(WebBase):

    @allure.title('34: 2-981 :   Страница для вывода BI отчетов - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-981 :   Страница для вывода BI отчетов - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-981 :   Страница для вывода BI отчетов - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def test_outsourcing_34(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/client-shifts-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        outsourcing.small_time()

        """
        Необходимо уточнить по поводу наличия страницы  PowerBI

        """

