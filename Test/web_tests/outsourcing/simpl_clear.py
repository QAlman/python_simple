import time
from random import random
import datetime
import allure
import pytest
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Outsourcing')
@allure.story('59: 2-805 : Проверка формирования отчета 119 ')

class  TestOutsourcing_clear(WebBase):

    @pytest.mark.test2_clear
    @pytest.mark.skip()
    def  test_outsourcing_clear(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/admin/payments/paymentdoc/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        #time.sleep(22222)

        for i in range(60):
            sp = "input"
            tx = "type"
            txx = "checkbox"
            txxx = "1"
            outsourcing.click_only_class_next(sp, tx, txx, txxx)

            sp = "select"
            tx = "name"
            txx = "action"
            outsourcing.move_to_class(sp, tx, txx)
            outsourcing.small_time()

            sp = "option"
            tx = "---------"
            outsourcing.click_only_txt(sp, tx)
            outsourcing.small_time()

            sp = "option"
            tx = "Удалить выбранные документы об оплате"
            outsourcing.click_only_txt(sp, tx)
            outsourcing.small_time()

            sp = "button"
            tx = "Выполнить"
            outsourcing.click_only_txt(sp, tx)
            outsourcing.small_time()

            outsourcing.move_to_item()

            sp = "input"
            tx = "value"
            txx = "Да, я уверен"
            outsourcing.click_only_class(sp, tx, txx)
            outsourcing.small_time()




        time.sleep(22222)

        # fin = outsourcing.check_field()
        # assert fin == 0, "Список документов не очищен"

        # https://outsourcing-auto.verme.ru/admin/payments/paymentdoc/? 19:52
        # sp = "select"
        # tx = "name"
        # txx = "action"
        # outsourcing.click_only_class(sp, tx, txx)
        # outsourcing.small_time()

        # outsourcing.small_time()
        # sp = "option"
        # tx = "---------"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()

        # time.sleep(5)
        #
        # sp = "select"
        # tx = "name"
        # txx = "action"
        # outsourcing.click_only_class(sp, tx, txx)
        # outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/agency-timesheets-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        # outsourcing.big_time()
        # outsourcing.big_time()
        # outsourcing.big_time()

        # 1111111111111111111111111111111

        sp = "div"
        tx = "id"
        txx = "__BVID__46"
        outsourcing.click_only_class(sp, tx, txx)

        sp = "td"
        tx = "data-month"
        txx = "3"
        outsourcing.click_only_class(sp, tx, txx)

        sp = "button"
        tx = "Фильтры"
        outsourcing.click_only_txt(sp, tx)

        sp = "span"
        tx = "Выберите сотрудника"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "Поиск..."
        tx = "Рутилова"
        outsourcing.send_textarea(sp, tx)
        outsourcing.small_time()
        sp = "li"
        tx = "Рутилова Марина Марина"
        outsourcing.click_only_txt(sp, tx)

        sp = "button"
        tx = "Применить"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        # outsourcing.check_mutation_on()

        # выбор апреля
        # фильтры - компания- пятерочка - сотрудники -т Рутилова Мирина
        # применить
        # банк - выбрать все - сформировать
        # админка- отчетность-документы об оплате
        # галочка - затем- действия- выбрать - выгрузить платежные документы(Все)- выполнить
        # кнопочка х для перехода на страницу отчета

        # статус -готов
        # скачать
        # проверить к-во табелей

        sp = "button"
        tx = "Действия"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "span"
        tx = "Платёжные поручения"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "input"
        tx = "placeholder"

        txx = "начало"
        txxx = "01.04.2023"

        txxxx = "окончание"
        txxxxx = "01.05.2023"

        outsourcing.send_datepicker(sp, tx, txx, txxx, txxxx, txxxxx)

        sp = "span"
        tx = "Выберите банк..."
        outsourcing.click_only_txt(sp, tx)

        sp = "li"
        tx = "Альфа Банк (Инвент сервис)"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "button"
        tx = "Сформировать"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        # --------------------------
        # self.verme.goto_celery_page()
        # v = "asdsadsfdvg@asdsffrgt.com"
        # self.verme.send_login(v)
        # v = "freftTRHTRH!@#13564"
        # self.verme.send_password(v)
        # self.verme.click_signin_celery()
        # self.verme.send_login(z)
        # self.verme.click_signin_celery()
        # ----------------------------

        ur = "https://outsourcing-auto.verme.ru/admin/payments/paymentdoc/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        time.sleep(22222)
        #
        #
        #
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
