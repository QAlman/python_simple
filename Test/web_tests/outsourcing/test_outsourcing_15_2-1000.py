import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase



@allure.feature('Web - Outsourcing')
@allure.story('Test 15   Тестирование создания сотрудника')
class TestOutsourcing_15(WebBase):

    @allure.title('15: 2-1000 :  Тестирование создания сотрудника - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1000 :  Тестирование создания сотрудника - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-1000 :  Тестирование создания сотрудника - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_15(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/agency-employees-list/"
        # outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        nb = "2"
        outsourcing.outsourcing_click_cell(nb)
        outsourcing. click_only_menu()

        sp = "span"
        tx = "Создать сотрудника"
        outsourcing.click_only_txt(sp, tx)


        outsourcing.agency_create_employee()

        # time.sleep(22222)
        # """
        # Необходимо добавить смены
        #
        # """

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




