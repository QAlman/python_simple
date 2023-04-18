import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('29: 2-813 :  Ошибка при выгрузке супервайзеров - Версия1')
class TestOutsourcing_29(WebBase):

    @allure.title('29: 2-813 :  Ошибка при выгрузке супервайзеров - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-813 :   Ошибка при выгрузке супервайзеров - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-813")
    @allure.description("Позитивный тест 2-813:   Ошибка при выгрузке супервайзеров - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_813
    @pytest.mark.skip
    def test_outsourcing_29(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/employees/supervisors/promo/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Computers_Acer"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()
        ap= "Действия"
        outsourcing.click_button(ap)
        sp = "span"
        tx = "Выгрузить в Excel"
        outsourcing.click_only_txt(sp, tx)
        tx = "Отчёты формируются в фоновом режиме! Перейдите на страницу отчётов"
        outsourcing.click_only_txt(sp, tx)

        ur = "https://outsourcing-auto.verme.ru/admin/reports/reportitem/"
        outsourcing.goto_employees_all_page(ur)

        d = outsourcing.datetime_only_data()
        us = None
        st = "Готов"
        outsourcing.check_excel_ui(ch, us, st, d)



