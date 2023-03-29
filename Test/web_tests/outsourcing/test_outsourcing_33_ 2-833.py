import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 33    Проверка поисковика орг. единиц ')
class TestOutsourcing_33(WebBase):

    @allure.title('33: 2-833 :   Проверка поисковика орг. единиц - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-833 :   Проверка поисковика орг. единиц - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-833")
    @allure.description("Позитивный тест 2-833 :   Проверка поисковика орг. единиц - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_33(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/promo-schedule/"
        # outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)

        d = 1
        d2 = 2
        assert d > d2, "Проверка assert"


        """
        Необходимо добавить проверку по признаку 

        """




