import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('47: 2-1017 : Тестирование счетчика отображения сотрудников - Версия1')
class TestOutsourcing_47(WebBase):

    @allure.title('47: 2-1017 : Тестирование счетчика отображения сотрудников - Версия1 ')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1017 : Тестирование счетчика отображения сотрудников - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1017")
    @allure.description("Позитивный тест 2-1017 : Тестирование счетчика отображения сотрудников - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_outsourcing_47(self):

        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        # ur = "https://outsourcing-auto.verme.ru/agency-employees-list/"
        # outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        outsourcing.outsourcing_click_pagination()
        z = "20"
        e = "сотрудники"
        outsourcing.outsourcing_click_pagination_value(z)
        outsourcing.outsourcing_check_pagination_value(e, z)
        c = "9"
        outsourcing.outsourcing_click_cell(c)
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.outsourcing_check_pagination_value(e, z)

        ur = "https://outsourcing-auto.verme.ru/employees/supervisors/agency/"
        outsourcing.goto_employees_all_page(ur)
        z = "20"
        e = "супервайзеры"
        outsourcing.outsourcing_click_pagination_value(z)
        z = "2"
        outsourcing.outsourcing_check_pagination_value(e, z)
        ur = "https://outsourcing-auto.verme.ru/agency-requests-list/"
        outsourcing.goto_employees_all_page(ur)
        ur = "https://outsourcing-auto.verme.ru/shifts-list/"
        outsourcing.goto_employees_all_page(ur)
        ur = "https://outsourcing-auto.verme.ru/agency-claims-list/"
        outsourcing.goto_employees_all_page(ur)
        ur = "https://outsourcing-auto.verme.ru/outsource-reports/"
        outsourcing.goto_employees_all_page(ur)

        ur = "https://outsourcing-auto.verme.ru/outsource/orglinks/client/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.outsourcing_click_pagination()
        z = "20"
        e = "связи"
        outsourcing.outsourcing_click_pagination_value(z)
        outsourcing.outsourcing_check_pagination_value(e, z)
        c = "9"
        outsourcing.outsourcing_click_cell(c)
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/outsource/orglinks/client/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.outsourcing_check_pagination_value(e, z)

        ur = "https://outsourcing-auto.verme.ru/client-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.outsourcing_click_pagination()
        z = "20"
        e = "сотрудники"
        outsourcing.outsourcing_click_pagination_value(z)
        z = "16"
        outsourcing.outsourcing_check_pagination_value(e, z)
        c = "9"
        outsourcing.outsourcing_click_cell(c)
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/client-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.outsourcing_check_pagination_value(e, z)

        ur = "https://outsourcing-auto.verme.ru/employees/supervisors/hq/"
        outsourcing.goto_employees_all_page(ur)

        ur = "https://outsourcing-auto.verme.ru/client-reports/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.outsourcing_click_pagination()
        z = "20"
        e = "отчёты"
        outsourcing.outsourcing_click_pagination_value(z)
        z= "3"
        outsourcing.outsourcing_check_pagination_value(e, z)
        c = "9"
        outsourcing.outsourcing_click_cell(c)
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/client-reports/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.outsourcing_check_pagination_value(e, z)

        ur = "https://outsourcing-auto.verme.ru/promo-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.outsourcing_click_pagination()
        z = "20"
        e = "сотрудники"
        outsourcing.outsourcing_click_pagination_value(z)
        z = "9"
        outsourcing.outsourcing_check_pagination_value(e, z)
        c = "9"
        outsourcing.outsourcing_click_cell(c)
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/promo-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.outsourcing_check_pagination_value(e, z)

        ur = "https://outsourcing-auto.verme.ru/promo-reports/"
        outsourcing.goto_employees_all_page(ur)





