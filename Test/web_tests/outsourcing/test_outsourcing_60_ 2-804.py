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
class TestOutsourcing_60(WebBase):

    @allure.title('59:2-805 : Проверка формирования отчета 119 - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-805 : Проверка формирования отчета 119 - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-805")
    @allure.description('Позитивный тест 2-805 : Проверка формирования отчета 119 - Версия1')
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

        #time.sleep(22222)

        # ch = "Директ Кредит_РГКП24"
        # nb = "1"
        # outsourcing.click_field_agency(ch, nb)
        # outsourcing.small_time()
        #
        # sp = "button"
        # tx = "Действия"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # sp = "span"
        # tx = "Расширенный отчёт"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # ur = "https://outsourcing-auto.verme.ru/admin/reports/reportitem/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.more_time()
        # outsourcing.ex_refresh()
        # outsourcing.small_time()
        # outsourcing.click_only_download()
        #
        # """
        # Необходимо уточнить по выгрузке отчета и полям
        #
        # """

        # c = "9"
        # outsourcing.outsourcing_click_cell(c)

        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # #outsourcing.click_sort_fio()
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/employees/supervisors/agency/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/client-employees-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/client-shifts-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/client-reports/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/promo-employees-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/promo-reports/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
