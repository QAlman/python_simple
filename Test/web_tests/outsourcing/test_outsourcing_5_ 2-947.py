import time
from random import random
import datetime
import allure
import pytest
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Outsourcing')
@allure.story('Test 5   Передавать в карточку сотрудника Адрес фактического проживания  ')
class TestOutsourcing_4(WebBase):

    @allure.title('5: 2-947 :   Передавать в карточку сотрудника Адрес фактического проживания - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-947 :    Передавать в карточку сотрудника Адрес фактического проживания - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-947")
    @allure.description('Позитивный тест 2-947 :    Передавать в карточку сотрудника Адрес фактического проживания - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_5(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-employees-list/"
        outsourcing.goto_employees_all_page(ur)

        ch = "Моя Смена" # можно менять
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        # #time.sleep(22222)
        #
        # sp = "button"
        # tx = "Действия"
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "span"
        # tx = "Статус по табелям"
        # outsourcing.click_only_txt(sp, tx)
        #
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/outsource-reports/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # outsourcing.click_only_download()

        # time.sleep(22222)
        #
        # ch = "Моя Смена"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # outsourcing.small_time()
        # nb = "2"
        # outsourcing.outsourcing_click_cell(nb)
        # outsourcing.click_only_menu()
        #
        # sp = "span"
        # tx = "Создать сотрудника"
        # outsourcing.click_only_txt(sp, tx)

        """
        Необходимо детализировать шаги теста

        """

