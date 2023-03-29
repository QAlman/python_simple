import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 41   Тестирование отправки оповещений - Версия1 ')
class TestOutsourcing_41(WebBase):

    @allure.title('41: 2-1072 :  Тестирование отправки оповещений - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1072 :  Тестирование отправки оповещений - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1072")
    @allure.description("Позитивный тест 2-1072 :  Тестирование отправки оповещений - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def test_outsourcing_41(self):


        """
        Необходимо расписать шаги подробно и разбить тест на несколько
        с использованием  заранее подготовленных пользователнй

        """

