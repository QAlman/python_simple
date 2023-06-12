import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('26: 2-1414 :   Тестирование работы формы "Заявки" - Версия1')
class TestOutsourcing_26(WebBase):

    @allure.title('26: 2-1414 :   Тестирование работы формы "Заявки" - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1414 :   Тестирование работы формы Заявки - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1414")
    @allure.description("Позитивный тест 2-1414 :   Тестирование работы формы Заявки - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_1414
    #@pytest.mark.skip
    def test_outsourcing_26(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-requests-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/client-requests-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = 'Группа "М.Видео-Эльдорадо"'
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        #
        # cell = "2"
        # outsourcing.outsourcing_click_cell(cell)
        # outsourcing.small_time()
        #
        # sp = "span"
        # tx = "Документы"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()

        """
        Необходимо актуализировать шаги 
        по отклонению заявки и верстке
        и наличию заявок у М Видео

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

