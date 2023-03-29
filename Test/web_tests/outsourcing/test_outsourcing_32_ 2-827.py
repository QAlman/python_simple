import time

import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 32 Ошибка получения orgUnit\pageParty ')
class TestOutsourcing_32(WebBase):

    @allure.title('32: 2-827 :  Ошибка получения orgUnit\pageParty - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-827 :  Ошибка получения orgUnit\pageParty - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-827")
    @allure.description("Позитивный тест 2-827 :  Ошибка получения orgUnit\pageParty - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_32(self):

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

        ch = 'Биржа М.Видео-Эльдорадо'
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()


        """
        Необходимо актуализировать шаги 
        с существующими супервайзерами


        """
        #
        # sp = "button"
        # tx = "Табели"
        # outsourcing.click_only_txt(sp, tx)
        #
        # ap = "Применить"
        # outsourcing.click_button(ap)
        # outsourcing.small_time()
        #
        # ur = "https://outsourcing-auto.verme.ru/timesheets-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        #
        #
        #
        # ch = "ИП Могилева"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # sp = "button"
        # tx = "Фильтры"
        # outsourcing.click_only_txt(sp, tx)
        #
        # ap = "Применить"
        # outsourcing.click_button(ap)
        # outsourcing.small_time()
        #
        #
        # ur = "https://outsourcing-auto.verme.ru/promo-schedule/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        #
        #
        # ch = "Директ Кредит"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # sp = "button"
        # tx = "Фильтры"
        # outsourcing.click_only_txt(sp, tx)
        #
        # ap = "Применить"
        # outsourcing.click_button(ap)
        # outsourcing.small_time()
        #
        # ur = "https://outsourcing-auto.verme.ru/promo-timesheets-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        #
        #
        # ch = "Директ Кредит"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # sp = "button"
        # tx = "Фильтры"
        # outsourcing.click_only_txt(sp, tx)
        #
        # ap = "Применить"
        # outsourcing.click_button(ap)
        # outsourcing.small_time()

