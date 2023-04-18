import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('25: 2-1411 :   Тестирование страницы Супервайзеры - Версия1')
class TestOutsourcing_25(WebBase):

    @allure.title('25: 2-1411 :   Тестирование страницы Супервайзеры - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1411 :   Тестирование страницы Супервайзеры - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1411")
    @allure.description("Позитивный тест 2-1411 :   Тестирование страницы Супервайзеры - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_1411
    #@pytest.mark.skip
    def test_outsourcing_25(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/employees/supervisors/agency/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()


        ap = "Действия"
        outsourcing.click_button(ap)

        sp = "span"
        tx = "Добавить супервайзера"
        outsourcing.click_only_txt(sp, tx)


        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/employees/supervisors/hq/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = 'Группа "М.Видео-Эльдорадо"'
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()


        ap = "Действия"
        outsourcing.click_button(ap)

        sp = "span"
        tx = "Добавить супервайзера"
        outsourcing.click_only_txt(sp, tx)

        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/employees/supervisors/promo/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = 'Директ Кредит_РГКП113'
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()


        ap = "Действия"
        outsourcing.click_button(ap)

        sp = "span"
        tx = "Добавить супервайзера"
        outsourcing.click_only_txt(sp, tx)

        """
        Необходимо актуализировать шаги
        в частности в М Видео нет поля добавить супервайзера
        """

        #time.sleep(222222)

        # sp = "span"
        # tx = "Выгрузить в Excel"
        # outsourcing.click_only_txt(sp, tx)
        #
        # tx = "Отчёты формируются в фоновом режиме! Перейдите на страницу отчётов"
        # outsourcing.click_only_txt(sp, tx)
        #
        # ur = "https://outsourcing-auto.verme.ru/admin/reports/reportitem/"
        # outsourcing.goto_employees_all_page(ur)
        #
        # d = outsourcing.datetime_only_data()
        # us = None
        # st = "Готов"
        # outsourcing.check_excel_ui(ch, us, st, d)
