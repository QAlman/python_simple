import time
from random import random
import datetime
import allure
import pytest
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Outsourcing')
@allure.story('57: 2-807 : Проверка формирования отчета 74')
class TestOutsourcing_57(WebBase):

    @allure.title('57: 2-807 :  Проверка формирования отчета 74 - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-807 : Проверка формирования отчета 74 - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-807")
    @allure.description('Позитивный тест 2-807 : Проверка формирования отчета 74 - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_807
    @pytest.mark.skip
    def test_outsourcing_57(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/admin"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        outsourcing.page_down_once()

        sp = "a"
        tx = "Виды отчётов"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        outsourcing.click_search_celery()
        z = '74.Реестр кандидатов Моя Смена интеграция АльфаБанк'
        outsourcing.send_login(z)
        outsourcing.click_search_celery()

        sp = "a"
        tx = "74.Реестр кандидатов Моя Смена интеграция АльфаБанк"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "li"
        tx = "Исполняемый код"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        time.sleep(22222)





        sp = "li"
        tx = "74.Реестр кандидатов Моя Смена интеграция АльфаБанк"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        ch = "Директ Кредит_РГКП24"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        sp = "a"
        tx = "74.Реестр кандидатов Моя Смена интеграция АльфаБанк"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "span"
        tx = "Расширенный отчёт"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/admin/reports/reportitem/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.more_time()
        outsourcing.ex_refresh()
        outsourcing.small_time()
        outsourcing.click_only_download()

        """
        Необходимо уточнить по выгрузке отчета и полям

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
