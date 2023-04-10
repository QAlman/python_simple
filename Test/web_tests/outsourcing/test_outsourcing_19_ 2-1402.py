import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('19: 2-1402 :  Тестирование сохранения фильтров страницы - Версия1')
class TestOutsourcing_19(WebBase):

    @allure.title('19: 2-1402 :  Тестирование сохранения фильтров страницы - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1402 :  Тестирование сохранения фильтров страницы - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1402")
    @allure.description("Позитивный тест 2-1402 :  Тестирование сохранения фильтров страницы - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_19(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()

        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-requests-list/"
        outsourcing.goto_employees_all_page(ur)

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)

        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/shifts-list/"
        outsourcing.goto_employees_all_page(ur)

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)

        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/client-claims-list/"
        outsourcing.goto_employees_all_page(ur)

        ch = "М-Видео"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)

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




