import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 27   Тестирование пагинации страницы')
class TestOutsourcing_27(WebBase):

    @allure.title('27: 2-1401 :  Тестирование пагинации страницы - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1401 :  Тестирование пагинации страницы - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1401")
    @allure.description("Позитивный тест 2-1401 :  Тестирование пагинации страницы - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_27(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()

        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-requests-list/"
        outsourcing.goto_employees_all_page(ur)

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.outsourcing_click_pagination()
        v = "20"
        outsourcing.outsourcing_click_pagination_value(v)

        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/shifts-list/"
        outsourcing.goto_employees_all_page(ur)

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.outsourcing_click_pagination()
        v = "20"
        outsourcing.outsourcing_click_pagination_value(v)

        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/client-claims-list/"
        outsourcing.goto_employees_all_page(ur)

        ch = "МВидео"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.outsourcing_click_pagination()
        v = "20"
        outsourcing.outsourcing_click_pagination_value(v)






