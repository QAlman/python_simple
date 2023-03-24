import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 24   Тестирование смены орг. единиц - Версия1')
class TestOutsourcing_24(WebBase):

    @allure.title('24: 2-991 :  Тестирование смены орг. единиц - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-991 :  Тестирование смены орг. единиц - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-991 :  Тестирование смены орг. единиц - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def test_outsourcing_24(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-requests-list/"
        outsourcing.goto_employees_all_page(ur)

        ch = "ИП Могилева"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/shifts-list/"
        outsourcing.goto_employees_all_page(ur)
        ch = "ИП Могилева"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/client-requests-list/"
        outsourcing.goto_employees_all_page(ur)
        ch = "Эльдорадо а442"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/client-shifts-list/"
        outsourcing.goto_employees_all_page(ur)
        ch = "Эльдорадо а442"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)

        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/promo-timesheets-list/"
        outsourcing.goto_employees_all_page(ur)
        ch = "Директ кредит 113"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/promo-reports/"
        outsourcing.goto_employees_all_page(ur)
        ch = "Директ кредит 113"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()





