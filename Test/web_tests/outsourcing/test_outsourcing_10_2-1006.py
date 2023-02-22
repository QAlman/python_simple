import time
from random import random
import allure
import pytest


from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 10   Не удаляются несколько смен сразу ')
class TestOutsourcing_10(WebBase):

    @allure.title('10: 2-1006 :  Не удаляются несколько смен сразу - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1006 :  Не удаляются несколько смен сразу - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-1006 :  Не удаляются несколько смен сразу - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def test_outsourcing_10(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/promo-schedule/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Computers_Acer"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        nb = "3"
        ev = " Удалить смену "
        outsourcing.check_mutation(nb, ev)


        nm = "2" # К Де Валер
        outsourcing.add_shifts_in_agency_by_num(nb, nm)

        mu = ' Добавить '
        outsourcing.click_mutation(mu)

        outsourcing.small_time()

        nb = "4"
        outsourcing.add_shifts_in_agency_by_num(nb, nm)

        mu = ' Добавить '
        outsourcing.click_mutation(mu)

        nb = "5"
        outsourcing.add_shifts_in_agency_by_num(nb, nm)

        mu = ' Добавить '
        outsourcing.click_mutation(mu)


        #outsourcing.check_mutation_all()

