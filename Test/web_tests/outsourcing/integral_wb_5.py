import time
from random import random
import datetime
import pandas as pd
import openpyxl
import allure
import pytest

import FW.WEB.outsourcing.url_test
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys


@allure.feature('Web - Integral')
@allure.story('64: 2-1149 : Экспорт отчета ')
class TestIntegral_5(WebBase):

    @allure.title('64: 2-1149 : Экспорт отчета ')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name='2-1149 : Экспорт отчета ',
                 url="https://")
    @allure.description('Позитивный тест ')
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_1000
    # @pytest.mark.skip
    def test_integral_5(self):
        outsourcing = self.APP.web_activity.button_to_integral_wb()
        outsourcing.small_time()
        ur = FW.WEB.outsourcing.url_test.UrlTest.url_2
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        sp = "h1"
        tx = "data-link"
        txx = "text{:selectedNomenclature^goodsName}"
        txxx = "1"
        fin = outsourcing.get_text_only(sp, tx, txx, txxx)

        sp = "span"
        tx = "class"
        txx = "price-block__price"
        txxx = "2"
        fin_1 = outsourcing.get_text_only(sp, tx, txx, txxx)

        outsourcing.small_time()

        sp = "span"
        tx = "Добавить в корзину"
        txx = "2"
        outsourcing.click_only_txt_next(sp, tx, txx)
        outsourcing.small_time()

        sp = "span"
        tx = "class"
        txx = "basket"
        txxx = "1"
        outsourcing.click_only_class_next(sp, tx, txx, txxx)
        outsourcing.small_time()
        # -----------------------------
        sp = "div"
        tx = "class"
        txx = "j-btn-choose-address"
        txxx = "1"
        outsourcing.click_only_class_next(sp, tx, txx, txxx)  # выбор адреса доставки
        outsourcing.small_time()

        zz = outsourcing.load_city_txt()
        print(zz)

        for i in zz:
            print("zz = " + str(i))

            dt = str(i)

            sp = "input"
            tx = "placeholder"
            txx = "Введите адрес"
            txxx = "1"
            outsourcing.click_only_class_next(sp, tx, txx, txxx)
            outsourcing.small_time()

            # dt = "Петропавловск-Камчатский "
            sp = "input"
            tx = "placeholder"
            txx = "Введите адрес"
            txxx = "1"
            outsourcing.send_only_class_next(dt, sp, tx, txx, txxx)
            outsourcing.small_time()

            sp = "ymaps"
            tx = "class"
            txx = "searchbox__button-cell"
            txxx = "1"
            outsourcing.click_only_class_next(sp, tx, txx, txxx)  # Кнопка Найти
            outsourcing.small_time()
            outsourcing.click_only_class_next(sp, tx, txx, txxx)  # Кнопка Найти
            outsourcing.small_time()

            # sp = "div"
            # tx = "class"
            # txx = "address-item__wrap"
            # txxx = "1"
            # outsourcing.click_only_class_next(sp, tx, txx, txxx)
            # outsourcing.small_time()

            sp = "ymaps"
            tx = "class"
            txx = "islets__first"
            txxx = "1"
            outsourcing.click_only_class_next(sp, tx, txx, txxx)  # активный город в единственном экземпляре
            outsourcing.small_time()

            sp = "span"
            tx = "class"
            txx = "address-item__name-text"
            txxx = "1"
            outsourcing.click_only_class_next(sp, tx, txx, txxx)
            outsourcing.small_time()

            sp = "button"
            tx = "class"
            txx = "details-self__btn"

            outsourcing.click_only_class(sp, tx, txx)
            outsourcing.small_time()

            # Камчатский край, Петропавловск-Камчатский

            sp = "h3"
            tx = "Недоступны для заказа"
            txx = "1"
            fin_3 = outsourcing.check_message_txt(sp, tx, txx)
            # assert fin == 0, "Товар - Недоступны для заказа"
            if fin_3 > 0:
                fin_3 = "Недоступны для заказа"
            else:
                fin_3 = "Доступны для заказа"

            outsourcing.small_time()

            zz = outsourcing.get_time_only_day()

            txt = fin
            txt_1 = fin_1
            txt_2 = fin_3
            txt_3 = zz

            outsourcing.write_xlsx_only(txt, txt_1, txt_2, dt, txt_3)

            sp = "button"
            tx = "class"
            txx = "btn-change"

            outsourcing.click_only_class(sp, tx, txx)
            outsourcing.small_time()

            sp = "button"
            tx = "class"
            txx = "address-item__btn-dots"

            outsourcing.click_only_class(sp, tx, txx)
            outsourcing.small_time()
            sp = "button"
            tx = "class"
            txx = "address-delete"

            outsourcing.click_only_class(sp, tx, txx)
            outsourcing.small_time()

            sp = "button"
            tx = "class"
            txx = "list-address__btn"
            txxx = "1"
            outsourcing.click_only_class_next(sp, tx, txx, txxx)  # выбрать адрес доставки
            outsourcing.small_time()
