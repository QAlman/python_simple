import time
from random import random
import datetime
import allure
import pytest
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Outsourcing')
@allure.story('14: 2-1804 :   Тестирование работы страницы претензии - Версия1')
class TestOutsourcing_14(WebBase):

    @allure.title('14: 2-1804 :   Тестирование работы страницы претензии - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-1804 :    Тестирование работы страницы претензии - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1804")
    @allure.description('Позитивный тест 2-1804 :    Тестирование работы страницы претензии - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_14(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-claims-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Тестовое агентство М.Видео" # можно менять
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        cell = "2"
        outsourcing.outsourcing_click_cell(cell)
        outsourcing.small_time()

        sp = "span"
        tx = "Файлы"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        outsourcing.outsourcing_click_cell(cell)
        outsourcing.small_time()
        tx = "Сообщения"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "button"
        tx = "Добавить "
        outsourcing.click_only_txt(sp, tx)

        ta = "Введите сообщение..."
        outsourcing.click_textarea(ta)
        ts = datetime.datetime.now()
        outsourcing.send_textarea(ta, str(ts))

        file = "02.jpg"
        outsourcing.send_photo_agency_all(file)

        sp = "button"
        tx = "Отправить"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "span"
        tx = "Основная"
        outsourcing.click_only_txt(sp, tx)

        sp = "button"
        tx = "К списку обращений "
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/client-claims-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = 'Группа "М.Видео-Эльдорадо"' # можно менять
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        cell = "2"
        outsourcing.outsourcing_click_cell(cell)
        outsourcing.small_time()

        sp = "span"
        tx = "Файлы"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        outsourcing.outsourcing_click_cell(cell)
        outsourcing.small_time()
        tx = "Сообщения"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "button"
        tx = "Добавить "
        outsourcing.click_only_txt(sp, tx)

        ta = "Введите сообщение..."
        outsourcing.click_textarea(ta)
        ts = datetime.datetime.now()
        outsourcing.send_textarea(ta, str(ts))

        file = "02.jpg"
        outsourcing.send_photo_agency_all(file)

        sp = "button"
        tx = "Отправить"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "span"
        tx = "Основная"
        outsourcing.click_only_txt(sp, tx)

        sp = "button"
        tx = "К списку обращений "
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/promo-claims-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Директ Кредит" # можно менять
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        cell = "2"
        outsourcing.outsourcing_click_cell(cell)
        outsourcing.small_time()

        sp = "span"
        tx = "Файлы"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        outsourcing.outsourcing_click_cell(cell)
        outsourcing.small_time()
        tx = "Сообщения"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "button"
        tx = "Добавить "
        outsourcing.click_only_txt(sp, tx)

        ta = "Введите сообщение..."
        outsourcing.click_textarea(ta)
        ts = datetime.datetime.now()
        outsourcing.send_textarea(ta, str(ts))

        file = "02.jpg"
        outsourcing.send_photo_agency_all(file)

        sp = "button"
        tx = "Отправить"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "span"
        tx = "Основная"
        outsourcing.click_only_txt(sp, tx)

        sp = "button"
        tx = "К списку обращений "
        outsourcing.click_only_txt(sp, tx)
