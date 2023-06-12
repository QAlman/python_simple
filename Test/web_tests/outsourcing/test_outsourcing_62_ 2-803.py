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
@allure.story('62: 2-803 : Проверка формирования отчета 53 ')
class TestOutsourcing_62(WebBase):

    @allure.title('62: 2-803 : Проверка формирования отчета 53 - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-803 : Проверка формирования отчета 53 - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-803")
    @allure.description('Позитивный тест 2-803 : Проверка формирования отчета 53 - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_803
    #@pytest.mark.skip
    def test_outsourcing_62(self):
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
        z = '53. Смены аутсорсинга импорт-экспорт (моя смена)'
        outsourcing.send_login(z)
        outsourcing.click_search_celery()

        sp = "a"
        tx = "53. Смены аутсорсинга импорт-экспорт (моя смена)"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "li"
        tx = "Параметры"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        pr = 'value'
        fin = outsourcing.outsourcing_get_queryset(pr)
        fin_ex = json.loads(fin)
        scr = FW.WEB.outsourcing.data_test.DataTest.txt_script_803
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
        time.sleep(150)
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

        fl = "export_shifts.outsourcingshift_"
        c1 = "Дата заказа смены"
        c2 = "ID смены"
        c3 = "Клиент"
        c4 = "Макрорегион"
        c5 = "Дивизион"
        c6 = "Кластер"
        c7 = "Магазин"
        c8 = "Адрес магазина"
        c9 = "Сотрудник"
        c10 = "Телефон"
        c11 = "Адрес фактического проживания СЗ"
        c12 = "Ближайшее метро"
        c13 = "Статус"
        c14 = "Дата смены"
        c15 = "Функция"
        c16 = "Стоимость Клиент"
        c17 = "Начало смены"
        c18 = "Конец смены"
        c19 = "Стоимость Сотрудник"
        c20 = "Рабочее время в минутах"
        c21 = "Задача"
        c22 = "Часовой план"
        c23 = "Рабочий план"
        c24 = "ФИО менеджера"
        c25 = "Кол-во часов с момента заказа до старта смены"
        c26 = "Цвет функции"
        c27 = "Внешний ID"
        c28 = "Код завода"
        c29 = "Дата последнего назначения"
        c30 = "Адм. территориальная единица"
        c31 = "Дата создания торговой точки"
        c32 = "Дата создания первой смены"
        #c32 = "ФИО менеджера"
        #c33 = "ФИО менеджера"

        outsourcing.get_xlsxfile_only(fl, dt_1, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16,
                                      c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32)


