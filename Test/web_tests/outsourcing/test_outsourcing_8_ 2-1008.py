import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 8    Статус уволен у сотрудника с прошедшей, текущей и будущей датой увольнения')
class TestOutsourcing_8(WebBase):

    @allure.title('1: 2-1009 :   Статус уволен у сотрудника с прошедшей, текущей и будущей датой увольнения - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1008 :   Статус уволен у сотрудника с прошедшей, текущей и будущей датой увольнения - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-1008 :   Статус уволен у сотрудника с прошедшей, текущей и будущей датой увольнения - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_8(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/agency-employees-list/"
        # outsourcing.goto_employees_all_page(ur)
        nb = "2"
        outsourcing.outsourcing_click_cell(nb)

        outsourcing.click_shifts_toolbar()

        fd = "Выберите дату увольнения..."
        outsourcing.click_textarea(fd)

        outsourcing.send_bcs_textarea(fd)

        fdd = "08.02.2024"
        outsourcing.send_textarea(fd, fdd)

        ap = " Сохранить изменения "
        outsourcing.click_button(ap)

        outsourcing.click_shifts_toolbar()
        fd = "Выберите дату увольнения..."
        outsourcing.click_textarea(fd)
        outsourcing.send_bcs_textarea(fd)
        fdd = "31.01.2023"
        outsourcing.send_textarea(fd, fdd)
        ap = " Сохранить изменения "
        outsourcing.click_button(ap)
        al = "Дата увольнения не может быть ранее сегодняшней даты"
        outsourcing.check_alert(al)







