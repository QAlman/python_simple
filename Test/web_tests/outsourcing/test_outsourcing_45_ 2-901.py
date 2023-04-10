import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('45: 2-901 :  Снятие со смен (Аутсорсинг и Агенства) - Версия1')
class TestOutsourcing_45(WebBase):

    @allure.title('45: 2-901 :  Снятие со смен (Аутсорсинг и Агенства) - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-901 :  Снятие со смен (Аутсорсинг и Агенства) - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-901")
    @allure.description("Позитивный тест 2-901 :  Снятие со смен (Аутсорсинг и Агенства) - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_45(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/promo-schedule/"
        outsourcing.goto_employees_all_page(ur)

        ch = "Computers_Acer"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)

        yr = "2023"
        nb = "2" # март
        mn = "1"
        wk = "3"
        outsourcing.click_datapicker(yr, nb, mn, wk)

        nb = "3"
        ev = " Удалить смену "
        outsourcing.check_mutation(nb, ev)

        nm = " К Де Валер " # К Де Валер Гал Алек Витал
        outsourcing.add_shifts_in_agency(nb, nm)

        mu = ' Добавить '
        outsourcing.click_mutation(mu)

        outsourcing.small_time()

        # outsourcing.click_shifts_in_agency(nb)

        st = ' Не назначен '
        outsourcing.get_shifts_agency(nb, st)

        mu = ' Изменить '
        outsourcing.click_mutation(mu)

        """

        Необходимо детализировать шаги теста

        """




