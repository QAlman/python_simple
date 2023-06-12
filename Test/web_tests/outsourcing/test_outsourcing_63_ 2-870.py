import time
from random import random
import datetime
import allure
import pytest
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Outsourcing')
@allure.story('63: 2-870 :  Проверка формирования отчета Выгрузка орг.структуры ')
class TestOutsourcing_63(WebBase):

    @allure.title('63:2-870 :  Проверка формирования отчета Выгрузка орг.структуры - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-870 :  Проверка формирования отчета Выгрузка орг.структуры - Версия1',
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-870")
    @allure.description('Позитивный тест  Проверка формирования отчета Выгрузка орг.структуры - Версия1')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_870
    #@pytest.mark.skip
    def test_outsourcing_63(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/client-quotas-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Магазин A442"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()


        # sp = "div"
        # tx = "id"
        # txx = "__BVID__47"
        # outsourcing.click_only_class(sp, tx, txx)
        #
        sp = "span"
        tx = "2023 г."
        outsourcing.click_only_txt(sp, tx)

        sp = "td"
        tx = "data-month"
        txx = "4"
        outsourcing.click_only_class(sp, tx, txx)
        outsourcing.small_time()

        sp = "button"
        tx = "Действия"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "span"
        tx = "Справочник орг. структуры"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        dt_1 = outsourcing.get_time_only()

        ur = "https://outsourcing-auto.verme.ru/client-reports/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        outsourcing.click_only_download()
        outsourcing.small_time()
        outsourcing.small_time()


        fl = "export_org_references_"
        c1 = "Код"
        c2 = "Название"
        # c3 = "Клиент"
        # c4 = "Макрорегион"
        # c5 = "Дивизион"
        # c6 = "Кластер"
        # c7 = "Магазин"
        # c8 = "Адрес магазина"
        # c9 = "Сотрудник"
        # c10 = "Телефон"
        # c11 = "Адрес фактического проживания СЗ"
        # c12 = "Ближайшее метро"
        # c13 = "Статус"
        # c14 = "Дата смены"
        # c15 = "Функция"
        # c16 = "Стоимость Клиент"
        # c17 = "Начало смены"
        # c18 = "Конец смены"
        # c19 = "Стоимость Сотрудник"
        # c20 = "Рабочее время в минутах"
        # c21 = "Задача"
        # c22 = "Часовой план"
        # c23 = "Рабочий план"
        # c24 = "ФИО менеджера"
        # c25 = "Кол-во часов с момента заказа до старта смены"
        # c26 = "Цвет функции"
        # c27 = "Внешний ID"
        # c28 = "Код завода"
        # c29 = "Дата последнего назначения"
        # c30 = "Адм. территориальная единица"
        # c31 = "Дата создания торговой точки"
        # c32 = "Дата создания первой смены"
        # c32 = "ФИО менеджера"
        # c33 = "ФИО менеджера"

        outsourcing.get_xlsxfile_only(fl, dt_1, c1, c2)




        #time.sleep(22222)




        # outsourcing.page_down_once()
        #
        # sp = "a"
        # tx = "Виды отчётов"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # outsourcing.click_search_celery()
        # z = '119. Документы СЗ (Моя смена)'
        # outsourcing.send_login(z)
        # outsourcing.click_search_celery()
        #
        #
        #
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
