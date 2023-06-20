import time
from random import random
import pyautogui as pyautogui
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Verme')
@allure.story('Test 1  Регистрации')
class TestIntegral_oz_1(WebBase):

    @allure.title('1: 2-964 : Регистрации на Shifts-dev ')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-964 : Регистрации на Shifts-dev - Version 1", url="https://testlink.verme.ru/index.php?caller=login&viewer=")

    @allure.description("Позитивный тест 2-964 : Регистрации на Shifts-dev - Version 1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_integral_oz_1(self):

        verme = self.APP.web_activity.button_to_integral_oz()
        # verme.small_time()
        verme.open_devtools()
        # verme.small_time()
        # #---------------
        # #time.sleep(22222)
        # pyautogui.keyDown('ctrl')
        # pyautogui.keyDown('shift')
        # pyautogui.keyDown('I')
        # pyautogui.keyUp('ctrl')
        # pyautogui.keyUp('shift')
        # pyautogui.keyUp('I')
        # verme.small_time()
        # pyautogui.keyDown('ctrl')
        # pyautogui.keyDown('shift')
        # pyautogui.keyDown('M')
        # pyautogui.keyUp('ctrl')
        # pyautogui.keyUp('shift')
        # pyautogui.keyUp('M')
        # verme.small_time()
        # #---------------

        verme.ex_refresh()
        # ur = "https://www.ozon.ru/cart"
        # verme.goto_employees_all_page(ur)
        time.sleep(2222222)
        verme.small_time()
        # verme.small_time()
        # verme.small_time()

        sp = "span"
        tx = "Укажите адрес доставки"
        txx = "1"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()

        sp = "span"
        tx = "Изменить"
        txx = "1"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()

        sp = "input"
        tx = "type"
        txx = "search"
        txxx = "1"
        verme.click_only_class_next(sp, tx, txx, txxx)

        dt = "Петропавловск-Камчатский"
        sp = "input"
        tx = "type"
        txx = "search"
        txxx = "1"
        verme.send_only_class_next(sp, tx, txx, txxx)

        time.sleep(55555)




        ur = "https://www.ozon.ru/product/kraska-tikkurila-44939-bystrosohnushchaya-do-85-akrilatno-lateksnaya-matovoe-pokrytie-9-kg-belyy-823085083/?avtc=1&avte=2&avts=1687291648&sh=QAyjYhW3vA"
        verme.goto_employees_all_page(ur)

        verme.small_time()

        verme.ex_refresh()
        sp = "span"
        tx = "Добавить в корзину"
        txx = "1"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()
        ur = "https://www.ozon.ru/cart"
        verme.goto_employees_all_page(ur)
        verme.small_time()
        verme.small_time()
        time.sleep(22222)


        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.keyDown('M')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('M')
        verme.small_time()
        verme.small_time()
        verme.click_coordinate()
        time.sleep(3333)
        ur = "#https://www.ozon.ru/cart"
        verme.goto_employees_all_page(ur)
        verme.small_time()
        verme.ex_refresh()
        verme.small_time()

        #el = "(//*[contains(@data-widget,'blockVertical')])[2]"
        # ur ="#https://www.ozon.ru/cart/#cartItem=823085083"
        # verme.goto_employees_all_page(ur)

        # sp = "span"
        # tx = "OK"
        # verme.move_to_txt(sp, tx)
        #
        # sp = "span"
        # tx = "OK"
        # txx = "1"
        # verme.click_only_txt_next(sp, tx, txx)
        # verme.small_time()
        # verme.ex_refresh()
        # sp = "span"
        # tx = "OK"
        # txx = "1"
        # verme.click_only_txt_next(sp, tx, txx)
        # verme.small_time()
        #
        # sp = "a"
        # tx = "href"
        # txx = "/cart"
        # txxx = "1"
        # verme.click_only_class_next(sp, tx, txx, txxx)
        # verme.small_time()
        # verme.small_time()
        #verme.page_down_once()

        time.sleep(22222)

        verme.ex_refresh()
        verme.page_down_once()
        sp = "span"
        tx = "OK"
        txx = "1"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()
        sp = "span"
        tx = "OK"
        txx = "1"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()
        sp = "span"
        tx = "OK"
        txx = "1"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()

        sp = "a"
        tx = "href"
        txx = "/cart"
        txxx = "1"
        verme.click_only_class_next(sp, tx, txx, txxx)
        verme.small_time()

        time.sleep(2222)

        sp = "div"
        tx = "class"
        txx = "tc4 a2-a"
        txxx = "1"
        verme.click_only_class_next(sp, tx, txx, txxx)
        verme.small_time()



        sp = "P"
        tx = "Пользуясь сайтом Ozon, вы соглашаетесь на использование "
        txx = "1"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()

        sp = "span"
        tx = "Перейти в корзину"
        txx = "3"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()



        sp = "span"
        tx = "Укажите адрес доставки"
        txx = "1"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()

        sp = "span"
        tx = "OK"
        txx = "1"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()

        sp = "span"
        tx = "class"
        txx = "qd7"
        verme.move_to_class(sp, tx, txx)
        verme.small_time()

        sp = "span"
        tx = "Изменить"
        txx = "1"
        verme.click_only_txt_next(sp, tx, txx)
        verme.small_time()

        # sp = "button"
        # tx = "type"
        # txx = "button"
        # txxx = "18"
        # verme.click_only_class_next(sp, tx, txx, txxx)
        # verme.small_time()

        # sp = "span"
        # tx = "OK"
        # txx = "1"
        # verme.click_only_txt_next(sp, tx, txx)
        # verme.small_time()

        time.sleep(22222)

        sp = "span"
        tx = "class"
        txx = "basket"
        txxx = "1"
        verme.click_only_class_next(sp, tx, txx, txxx)
        verme.small_time()


        verme.click_shifts_next()
        verme.click_shifts_done()


        z = self.APP.web_any_page.string_d
        o = z[5:10]
        print(z)
        z_2 = ("9" + str(z))
        verme.click_shifts_phone()
        verme.send_shifts_phone(z_2)
        verme.click_shifts_call()
        verme.goto_celery_page()
        v = "asdsadsfdvg@asdsffrgt.com"
        verme.send_login(v)
        v = "freftTRHTRH!@#13564"
        verme.send_password(v)
        verme.click_signin_celery()
        verme.send_login(z)
        verme.click_signin_celery()
        #time.sleep(22222)
        verme.click_phone_celery(z_2)
        x = verme.get_text_sms()
        verme.return_shifts_page()
        verme.send_sms_code_phone_4(x)
        verme.small_time()

        f = "Фамилия"
        f_1 = self.APP.web_any_page.string_letters
        f_2 = "84"
        verme.send_shifts_registration_txt(f, f_1, f_2)

        f = "Имя"
        f_2 = "88"
        verme.send_shifts_registration_txt(f, f_1, f_2)

        f = "Отчество"
        f_2 = "92"
        verme.send_shifts_registration_txt(f, f_1, f_2)

        g = "мужской"
        verme.click_shifts_registration_btn(g)

        data = "1990"
        month = "янв."
        day = "31"
        fm = "1"
        verme.click_shifts_registration_data(data, month, day, fm)

        s = "Гражданство"
        country = "Россия"
        verme.click_shifts_registration_country(s, country)

        next = "Продолжить"
        verme.click_shifts_registration_btn(next)

        s = "Фактическое место проживания"
        p = "г Москва, пр-кт Мира, д 111, кв 3"
        r = "115"
        verme.click_shifts_registration_slot(s, r, p )

        s = "Регионы подработки"
        p = "Москва"
        verme.click_shifts_registration_region(s, p)

        verme.click_shifts_registration_btn(next)
        verme.send_photo_shifts()
        verme.click_shifts_approve()
        vote = " Я принимаю "
        verme.click_shifts_registration_btn(vote)
        verme.click_shifts_registration_btn(next)




