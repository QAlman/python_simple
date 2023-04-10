import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('37: 2-859 :   Назначение сотрудников на смены - Версия1')
class TestOutsourcing_37(WebBase):

    @allure.title('37: 2-859 :   Назначение сотрудников на смены - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-859 :   Назначение сотрудников на смены - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-859")
    @allure.description("Позитивный тест 2-859 :   Назначение сотрудников на смены - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_37(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/shifts-list"
        outsourcing.goto_employees_all_page(ur)

        ch = "Аркадия"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)

        # yr = "2023"
        # nb = "2"  # март
        # mn = "1"
        # wk = "3"
        # outsourcing.click_datapicker(yr, nb, mn, wk)

        st = "не назначен"
        outsourcing.click_list_status(st)

        fd = "Выберите сотрудника..."
        outsourcing.click_textarea(fd)
        wr = " Абдуал Хур Ам "
        outsourcing.select_list_status(wr)
        ap = "Назначить"
        outsourcing.click_button(ap)

        """
        Необходимо всегда иметь магазин с сменами и сотрудниками
        на данный момент этого нет
    
    
        """