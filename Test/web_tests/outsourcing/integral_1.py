import time
from random import random
import datetime
import pandas as pd
import openpyxl
import allure
import pytest
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Integral')
@allure.story('64: 2-1149 : Экспорт отчета ')
class TestIntegral_1(WebBase):

    @allure.title('64: 2-1149 : Экспорт отчета ')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-1149 : Экспорт отчета ',
                 url="https://")
    @allure.description('Позитивный тест ')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_1000
    #@pytest.mark.skip
    def test_integral_1(self):
        outsourcing = self.APP.web_activity.button_to_integral_wb()


        sp = "a"
        tx = "Войти"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        v = "9261530351"
        outsourcing.send_only(v)
        outsourcing.small_time()

        sp = "button"
        tx = "Получить код"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.more_time()

        sp = "input"
        tx = "id"
        txx = "searchInput"
        outsourcing.click_only_class(sp, tx, txx)
        outsourcing.small_time()

        dt = "Kenko Бинокль"
        outsourcing.send_only_class(dt, sp, tx, txx)

        sp = "span"
        tx = "Kenko Бинокль"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.more_time()



        time.sleep(22222)


        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/admin/payments/paymentdoc/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        el = outsourcing.check_field()

        if el >= 1:

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

        fin = outsourcing.check_field()
        assert fin < 1, "Список документов не очищен"


        #https://outsourcing-auto.verme.ru/admin/payments/paymentdoc/? 19:52
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

        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-timesheets-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()


        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        # sp = "div"
        # tx = "id"
        # txx = "__BVID__46"
        # outsourcing.click_only_class(sp, tx, txx)

        sp = "span"
        tx = "2023 г."
        outsourcing.click_only_txt(sp, tx)

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

        #outsourcing.check_mutation_on()

        #выбор апреля
        #фильтры - компания- пятерочка - сотрудники -т Рутилова Мирина
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
        txxx ="01.04.2023"

        txxxx = "окончание"
        txxxxx = "01.05.2023"

        outsourcing.send_datepicker(sp, tx, txx, txxx, txxxx, txxxxx)


        sp = "span"
        tx = "Выберите банк..."
        outsourcing.click_only_txt(sp, tx)

        # sp = "li"
        # tx = "Альфа Банк (Моя смена)"
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        sp = "div"
        tx = "class"
        txx = "list-item"
        outsourcing.click_only_class(sp, tx, txx)

        sp = "button"
        tx = "Сформировать"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        outsourcing.ex_refresh()
        outsourcing.more_time()
        outsourcing.more_time()
        #--------------------------
        # self.verme.goto_celery_page()
        # v = "asdsadsfdvg@asdsffrgt.com"
        # self.verme.send_login(v)
        # v = "freftTRHTRH!@#13564"
        # self.verme.send_password(v)
        # self.verme.click_signin_celery()
        # self.verme.send_login(z)
        # self.verme.click_signin_celery()
        #----------------------------

        ur = "https://outsourcing-auto.verme.ru/admin/payments/paymentdoc/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()


        #
        #
        #
        # outsourcing.page_down_once()
        #



        nb= "3"
        sp = "td"
        tx = "class"
        txx = "field-count_row"
        txxx = "1"
        sd = outsourcing.get_text_only(sp, tx, txx, txxx)
        outsourcing.small_time()
        assert sd == nb, "Колличество смен не корректно"

        sp = "input"
        tx = "type"
        txx = "checkbox"
        txxx = "1"
        outsourcing.click_only_class_next(sp, tx, txx, txxx)

        sp = "option"
        tx = "---------"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "option"
        tx = "Выгрузить платежные документы(Все)"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "button"
        tx = "Выполнить"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        dt_1 = outsourcing.get_time_only()

        sp = "a"
        tx = "[↗]"
        txx = "1"
        outsourcing.click_only_txt_next(sp, tx, txx)
        outsourcing.small_time()

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

        print(dt_1)

        outsourcing.get_zipfile_only(dt_1)




