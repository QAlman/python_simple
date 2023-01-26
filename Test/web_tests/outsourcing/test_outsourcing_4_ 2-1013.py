import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 4   Копирование назначений на смены Агенств ')
class TestOutsourcing_4(WebBase):

    @allure.title('1: 2-1013 :  Копирование назначений на смены Агенств - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1013 :  Копирование назначений на смены Агенств - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-1013 :  Копирование назначений на смены Агенств - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_4(self):
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

        nb = "3"
        nm = " Гал Алек Витал "
        outsourcing.add_shifts_in_agency(nb, nm)

        #time.sleep(22222)

        nb = "21"
        st = ' Не назначен '
        outsourcing.get_shifts_agency(nb, st)

        # mu = ' Изменить '
        # outsourcing.click_mutation(mu)

        outsourcing.check_mutation()

