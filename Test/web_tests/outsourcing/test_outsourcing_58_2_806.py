import time
import json
from random import random
import datetime
import allure
import pytest
from Test.web_tests.WebBase import WebBase
import FW.WEB.outsourcing.data_test
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Outsourcing')
@allure.story('58: 2-806 : Проверка формирования отчета 101')
class TestOutsourcing_58(WebBase):

    @allure.title('58:2-806 : Проверка формирования отчета 101 - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-806 : Проверка формирования отчета 101 - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-806")
    @allure.description('Позитивный тест 2-806 : Проверка формирования отчета 101 - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_806
    #@pytest.mark.skip
    def test_outsourcing_58(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/admin"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        outsourcing.page_down_once()

        sp = "a"
        tx = "Виды отчётов"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        outsourcing.click_search_celery()
        z = '101. Статус регистрации в АБ'
        outsourcing.send_login(z)
        outsourcing.click_search_celery()

        sp = "a"
        tx = "101. Статус регистрации в АБ"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "li"
        tx = "Параметры"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        pr = 'value'
        fin = outsourcing.outsourcing_get_queryset(pr)
        fin_ex = json.loads(fin)
        scr = FW.WEB.outsourcing.data_test.DataTest.txt_script_806
        fin_int = json.loads(scr)
        assert fin_ex == fin_int, "Скрипт для 806 не корректен"

        sp = "input"
        tx = 'value'
        txx = "Запустить экспорт"
        outsourcing.click_only_class(sp, tx, txx)
        outsourcing.small_time()

        sp = "a"
        tx = "[↗]"
        txx = "1"
        outsourcing.click_only_txt_next(sp, tx, txx)

        outsourcing.switch_to_new_tab()
        outsourcing.more_time()

        sp = "div"
        tx = "class"
        txx = "readonly"
        txxx = "5"
        st = "Готов"
        fin = outsourcing.get_text_only(sp, tx, txx, txxx)
        assert fin == st, "Статус не корректен"

        dt_1 = outsourcing.get_time_only()

        sp = "a"
        tx = "Скачать"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        c1 = "Онбординг АБ"
        c2 = "ИНН"
        c3 = "Фамилия"
        c4 = "Имя"
        c5 = "Отчество"
        #c6 = "Дата рождения"
        #c7 = "Место рождения"
        #c8 = "Гражданство"
        #c9 = "Паспорт серия"
        #c10 = "Паспорт номер"
        #c11 = "Кем выдан паспорт"
        #c12 = "Код подразделения"
        c13 = "Номер телефона"
        #c14 = "Адрес проживания"
        #c15 = "Email"
        #c16 = "Дата выдачи"
        #c17 = "Дата окончания"
        #c18 = "Описание статуса"
        c19 = "ФИО"
        # c20 = ""
        # c21 = ""
        # c22 = ""
        # c23 = ""
        # c24 = ""

        outsourcing.get_xlsxfile_only(dt_1, c1, c2, c3, c4, c5, c13, c19)

        # time.sleep(22222)