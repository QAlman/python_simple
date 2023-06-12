import time
from random import random
import datetime
import allure
import pytest
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Outsourcing')
@allure.story('6: 2-930 :   Некорректная ошибка при загрузке дополнительного фото - Версия1')
class TestOutsourcing_6(WebBase):

    @allure.title('6: 2-930 :   Некорректная ошибка при загрузке дополнительного фото - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-930 :    Некорректная ошибка при загрузке дополнительного фото - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-930")
    @allure.description('Позитивный тест 2-930 :    Некорректная ошибка при загрузке дополнительного фото - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_930
    #@pytest.mark.skip
    def test_outsourcing_6(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/agency-employees-list/"
        # outsourcing.goto_employees_all_page(ur)

        ch = "Моя Смена" # можно менять
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        outsourcing.small_time()
        nb = "2"

        outsourcing.outsourcing_click_cell(nb)
        outsourcing.small_time()

        sp = "span"
        tx = "Лицевая биометрия"
        outsourcing.click_only_txt(sp, tx)

        outsourcing.small_time()
        file = "02.jpg"
        outsourcing.send_photo_agency_all(file)
        outsourcing.small_time()
        sp = "button"
        tx = " Кадрировать и отправить "
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        # sp = "span"
        # tx = "Клиенты"
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "span"
        # tx = "Мероприятия"
        # outsourcing.click_only_txt(sp, tx)
        #
        """
        Необходимо детализировать шаги теста

        """

