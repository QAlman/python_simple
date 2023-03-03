import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 14  Тестирование модальных фильтров')
class TestOutsourcing_14(WebBase):

    @allure.title('14: 2-1001 :  Тестирование модальных фильтров - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1001 :  Тестирование модальных фильтров - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-1001 :  Тестирование модальных фильтров - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_14(self):
        time.sleep(3)
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/promo-schedule/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Computers_Acer"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)

        sp = "button"
        tx = "Фильтры"
        outsourcing.click_only_txt(sp, tx)

        ap = "Применить"
        outsourcing.click_button(ap)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/shifts-list"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/shifts-list"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
