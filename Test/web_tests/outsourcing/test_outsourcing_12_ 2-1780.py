import time
from random import random
import datetime
import allure
import pytest
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Outsourcing')
@allure.story('Test 12  Тестирование страницы "Квоты" ')
class TestOutsourcing_12(WebBase):

    @allure.title('12: 2-1780 :   Тестирование страницы "Квоты" - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-1780 :    Тестирование страницы "Квоты" - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1780")
    @allure.description('Позитивный тест 2-1780 :    Тестирование страницы "Квоты" - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_12(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/client-quotas-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.small_time()

        ch = "SPAR" # можно менять
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        sp = "button"
        tx = "Действия"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "span"
        tx = "Выгрузить в Excel"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()
        #
        # ur = "https://outsourcing-auto.verme.ru/client-reports/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.more_time()
        # outsourcing.ex_refresh()
        # outsourcing.small_time()
        # outsourcing.click_only_download()

        """
        Необходимо уточнить по экспорту квот

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
