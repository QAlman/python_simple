import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 5   Копирование назначений на смены Аутсорсинга ')
class TestOutsourcing_5(WebBase):

    @allure.title('1: 2-1012 :  Копирование назначений на смены Аутсорсинга - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1012 :  Копирование назначений на смены Агенств - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-1013 :  Копирование назначений на смены Агенств - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    # @pytest.mark.skip
    def test_outsourcing_5(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/outsource-schedule/"
        outsourcing.goto_employees_all_page(ur)

        ch = "НьюСтафф"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)


        wr = "Сотрудник не назначен"
        outsourcing.click_shifts_in_shedule(wr)

        """
        Необходимо детализировать шаги теста

        """


        # time.sleep(22222)

        # yr = "2023"
        # nb = "2"  # март
        # mn = "1"
        # wk = "3"
        # outsourcing.click_datapicker(yr, nb, mn, wk)

        # nb = "3"
        # ev = " Удалить смену "
        # outsourcing.check_mutation(nb, ev)
        #
        # nm = " К Де Валер "  # К Де Валер Гал Алек Витал
        # outsourcing.add_shifts_in_agency(nb, nm)
        #
        # mu = ' Добавить '
        # outsourcing.click_mutation(mu)





