import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 30   Не открываются ячейки табелей ')
class TestOutsourcing_30(WebBase):

    @allure.title('30: 2-816 :  Не открываются ячейки табелей - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-816 :  Не открываются ячейки табелей - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-816")
    @allure.description("Позитивный тест 2-816 :  Не открываются ячейки табелей - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def test_outsourcing_30(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/promo-timesheets-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Computers_Acer"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()
        outsourcing.check_mutation_on()






