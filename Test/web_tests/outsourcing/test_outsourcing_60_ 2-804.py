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
@allure.story('60: 2-804 : Проверка формирования отчета 97 - Версия1')
class TestOutsourcing_60(WebBase):

    @allure.title('60: 2-804 : Проверка формирования отчета 97 - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-804 : Проверка формирования отчета 97 - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-804")
    @allure.description('Позитивный тест 2-804 : Проверка формирования отчета 97 - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_804
    #@pytest.mark.skip
    def test_outsourcing_60(self):
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
        z = '97. Выгрузка СЗ вместе со ссылками на AMO'
        outsourcing.send_login(z)
        outsourcing.click_search_celery()

        sp = "a"
        tx = "97. Выгрузка СЗ вместе со ссылками на AMO"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "li"
        tx = "Параметры"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        pr = 'value'
        fin = outsourcing.outsourcing_get_queryset(pr)
        fin_ex = json.loads(fin)
        scr = FW.WEB.outsourcing.data_test.DataTest.txt_script_804
        fin_int = json.loads(scr)
        assert fin_ex == fin_int, "Скрипт для 804 не корректен"

        sp = "input"
        tx = 'value'
        txx = "Запустить экспорт"
        outsourcing.click_only_class(sp, tx, txx)
        outsourcing.small_time()

        dt_1 = outsourcing.get_time_only()

        sp = "a"
        tx = "[↗]"
        txx = "1"
        outsourcing.click_only_txt_next(sp, tx, txx)

        outsourcing.switch_to_new_tab()
        time.sleep(2200)
        outsourcing.ex_refresh()
        outsourcing.small_time()

        sp = "div"
        tx = "class"
        txx = "readonly"
        txxx = "5"
        st = "Готов"
        fin = outsourcing.get_text_only(sp, tx, txx, txxx)
        assert fin == st, "Статус не корректен"

        sp = "a"
        tx = "Скачать"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        fl = "export_selfemployed_amo_"
        c1 = "Имя"
        c2 = "Дата приёма в агентство"
        c3 = "Телефон"
        c4 = "Дата рождения"
        c5 = "Гражданство"
        c6 = "Города"
        c7 = "Адрес"
        c8 = "Ближайшее метро"
        c9 = "Ветка метро"
        c10 = "Статус СЗ"
        c11 = "Статус в Альфа"
        c12 = "Пол"
        c13 = "Ограничение по сетям"
        c14 = "Количество блокировок"
        c15 = "Описание статуса"
        # c16 = "Дата выдачи"
        # c17 = "Дата окончания"
        # c18 = "Описание статуса"
        # c19 = "ФИО"
        # c20 = ""
        # c21 = ""
        # c22 = ""
        # c23 = ""
        # c24 = ""

        outsourcing.get_xlsxfile_only(fl, dt_1, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15)