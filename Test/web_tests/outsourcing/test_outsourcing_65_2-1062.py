import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('49: 2-1062 :  Снятие со смен (Аутсорсинг и Агенства) - Версия1')
class TestOutsourcing_65(WebBase):

    @allure.title('49: 2-1062 :  Снятие со смен (Аутсорсинг и Агенства) - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1062 :  Снятие со смен (Аутсорсинг и Агенства) - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-1062 :  Снятие со смен (Аутсорсинг и Агенства) - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_1062
    @pytest.mark.skip
    def test_outsourcing_65(self):
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
        """
        Необходимо добавить смены

        """

        # c = "9"
        # outsourcing.outsourcing_click_cell(c)

        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # #outsourcing.click_sort_fio()
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/employees/supervisors/agency/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/client-employees-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/client-shifts-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/client-reports/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/promo-employees-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/promo-reports/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)



