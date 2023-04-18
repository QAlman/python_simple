import time
from random import random
import datetime
import allure
import pytest
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Outsourcing')
@allure.story('7: 2-929 :   Страница для вывода BI отчетов - Версия1')
class TestOutsourcing_7(WebBase):

    @allure.title('7: 2-929 :   Страница для вывода BI отчетов - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-929 :    Страница для вывода BI отчетов - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-929")
    @allure.description('Позитивный тест 2-929 :    Страница для вывода BI отчетов - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_929
    #@pytest.mark.skip
    def test_outsourcing_7(self):
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

