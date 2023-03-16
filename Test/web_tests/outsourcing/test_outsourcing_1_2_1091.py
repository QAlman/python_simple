import datetime
import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 1    Не отображаются отметки в отчете')
class TestOutsourcing_1(WebBase):

    @allure.title('1: 2-1091 :   Не отображаются отметки в отчете - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1091 :   Не отображаются отметки в отчете - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1091")
    @allure.description("Позитивный тест 2-1091 :   Не отображаются отметки в отчете - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_1(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()
        # test_outsourcing_2_ 2-950.py
        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/timesheets-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()



        sp = "button"
        tx = "Действия"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()
        """
        Необходимо актуализировать шаги

        """

        # time.sleep(22222)
        #
        #
        # ch = "Тестовое агентство М.Видео"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # cell = "2"
        # outsourcing.outsourcing_click_cell(cell)
        # outsourcing.small_time()
        #
        # sp = "span"
        # tx = "Файлы"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # outsourcing.outsourcing_click_cell(cell)
        # outsourcing.small_time()
        # tx = "Сообщения"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # sp = "button"
        # tx = "Добавить "
        # outsourcing.click_only_txt(sp, tx)
        #
        # ta = "Введите сообщение..."
        # outsourcing.click_textarea(ta)
        # ts = datetime.datetime.now()
        # outsourcing.send_textarea(ta, str(ts))
        #
        # file = "02.jpg"
        # outsourcing.send_photo_agency_all(file)
        #
        # sp = "button"
        # tx = "Отправить"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # sp = "span"
        # tx = "Основная"
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "button"
        # tx = "К списку обращений "
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        #
        # ur = "https://outsourcing-auto.verme.ru/client-claims-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        #
        # ch = 'Группа "М.Видео-Эльдорадо"'
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # cell = "2"
        # outsourcing.outsourcing_click_cell(cell)
        # outsourcing.small_time()
        #
        # sp = "span"
        # tx = "Файлы"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # outsourcing.outsourcing_click_cell(cell)
        # outsourcing.small_time()
        # tx = "Сообщения"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # sp = "button"
        # tx = "Добавить "
        # outsourcing.click_only_txt(sp, tx)
        #
        # ta = "Введите сообщение..."
        # outsourcing.click_textarea(ta)
        # ts = datetime.datetime.now()
        # outsourcing.send_textarea(ta, str(ts))
        #
        # file = "02.jpg"
        # outsourcing.send_photo_agency_all(file)
        #
        # sp = "button"
        # tx = "Отправить"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # sp = "span"
        # tx = "Основная"
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "button"
        # tx = "К списку обращений "
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # ur = "https://outsourcing-auto.verme.ru/promo-claims-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        #
        # ch = "Директ Кредит"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # cell = "2"
        # outsourcing.outsourcing_click_cell(cell)
        # outsourcing.small_time()
        #
        # sp = "span"
        # tx = "Файлы"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # outsourcing.outsourcing_click_cell(cell)
        # outsourcing.small_time()
        # tx = "Сообщения"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # sp = "button"
        # tx = "Добавить "
        # outsourcing.click_only_txt(sp, tx)
        #
        # ta = "Введите сообщение..."
        # outsourcing.click_textarea(ta)
        # ts = datetime.datetime.now()
        # outsourcing.send_textarea(ta, str(ts))
        #
        # file = "02.jpg"
        # outsourcing.send_photo_agency_all(file)
        #
        # sp = "button"
        # tx = "Отправить"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # sp = "span"
        # tx = "Основная"
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "button"
        # tx = "К списку обращений "
        # outsourcing.click_only_txt(sp, tx)


