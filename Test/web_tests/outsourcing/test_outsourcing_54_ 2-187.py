import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('54: 2-187 :   Проверка развёртывания документов - Версия1')
class TestOutsourcing_54(WebBase):

    @allure.title('54: 2-187 :   Проверка развёртывания документов - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-187 :   Проверка развёртывания документов - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-187")
    @allure.description("Позитивный тест 2-187 :   Проверка развёртывания документов - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_187
    #@pytest.mark.skip
    def test_outsourcing_54(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-employees-list/"
        outsourcing.goto_employees_all_page(ur)

        ch = "ИП Могилева"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        cell = "2"
        outsourcing.outsourcing_click_cell(cell)
        outsourcing.small_time()

        sp = "span"
        tx = "Документы"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        """
        Необходимо актуализировать шаги

        """


        #
        # ur = "https://outsourcing-auto.verme.ru/shifts-list/"
        # outsourcing.goto_employees_all_page(ur)
        # ch = "ИП Могилева"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # ur = "https://outsourcing-auto.verme.ru/client-requests-list/"
        # outsourcing.goto_employees_all_page(ur)
        # ch = "Эльдорадо а442"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # ur = "https://outsourcing-auto.verme.ru/client-shifts-list/"
        # outsourcing.goto_employees_all_page(ur)
        # ch = "Эльдорадо а442"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        #
        # outsourcing.small_time()
        #
        # ur = "https://outsourcing-auto.verme.ru/promo-timesheets-list/"
        # outsourcing.goto_employees_all_page(ur)
        # ch = "Директ кредит 113"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # ur = "https://outsourcing-auto.verme.ru/promo-reports/"
        # outsourcing.goto_employees_all_page(ur)
        # ch = "Директ кредит 113"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()




