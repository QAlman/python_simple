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
@allure.story('59: 2-805 : Проверка формирования отчета 119 ')
class TestOutsourcing_59(WebBase):

    @allure.title('59:2-805 : Проверка формирования отчета 119 - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-805 : Проверка формирования отчета 119 - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-805")
    @allure.description('Позитивный тест 2-805 : Проверка формирования отчета 119 - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_805
    #@pytest.mark.skip
    def test_outsourcing_59(self):
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
        z = '119. Документы СЗ (Моя смена)'
        outsourcing.send_login(z)
        outsourcing.click_search_celery()

        sp = "a"
        tx = "119. Документы СЗ (Моя смена)"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "li"
        tx = "Параметры"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        pr = 'value'
        fin = outsourcing.outsourcing_get_queryset(pr)
        fin_ex = json.loads(fin)
        scr = FW.WEB.outsourcing.data_test.DataTest.txt_script_805
        fin_int = json.loads(scr)
        assert fin_ex == fin_int, "Скрипт для 805 не корректен"

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

        # time.sleep(22222)

