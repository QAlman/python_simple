import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Verme')
@allure.story('Test 2  Регистрации')
class TestVerme_2(WebBase):

    @allure.title('2:  Регистрации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-967 : Регистрации на Shifts-dev - Version 1", url="https://testlink.verme.ru/index.php?caller=login&viewer=")

    @allure.description("Позитивный тест 2-967 : Регистрации на Shifts-dev - Version 1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_verme_2(self):
        verme = self.APP.web_activity.button_to_shifts()
        self.APP.web_steps.step_test_1()
        verme.click_shifts_next()
        verme.click_shifts_done()
        z = self.APP.web_any_page.string_d
        o = z[5:10]
        print(z)
        verme.click_shifts_phone()
        verme.send_shifts_phone(str(z))
        verme.click_shifts_call()
        verme.goto_celery_page()
        v = "asdsadsfdvg@asdsffrgt.com"
        verme.send_login(v)
        v = "freftTRHTRH!@#13564"
        verme.send_password(v)
        verme.click_signin_celery()
        verme.send_login(z)
        verme.click_signin_celery()
        verme.click_phone_celery(z)
        x = verme.get_text_sms()
        verme.return_shifts_page()
        verme.send_sms_code_phone_4(x)

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
        verme.click_shifts_registration_slot(s, r, p)

        s = "Регионы подработки"
        p = "Москва"
        verme.click_shifts_registration_region(s, p)

        verme.click_shifts_registration_btn(next)
        verme.send_photo_shifts()
        verme.click_shifts_approve()
        vote = " Я принимаю "
        verme.click_shifts_registration_btn(vote)
        verme.click_shifts_registration_btn(next)

        verme.click_shifts_after_approve()
        verme.click_shifts_move_to_documents()
        verme.click_shifts_andes()
        m = "1"
        verme.click_shifts_add_doc(m)

        bik = "044525202"
        account = "40817810630082478612"
        verme.click_shifts_add_bank(bik, account)
        verme. click_shifts_andes()
        verme.small_time()
        verme.click_shifts_andes()
        m = "2"
        verme.click_shifts_add_doc(m)
        inn = "526317984689"
        verme.click_shifts_add_inn(inn)
        verme.click_shifts_andes()
        verme.small_time()
        verme.click_shifts_andes()
        m = "3"
        verme.click_shifts_add_doc(m)
        med = "23452332"
        verme.click_shifts_add_med(med)

        data = None
        month = None
        day = "1"
        nm = "2"
        nm_2 = "3"
        verme.click_shifts_registration_med_data(day, nm, nm_2)
        verme.send_photo_shifts()
        verme.click_shifts_andes_all(nm)
        verme.small_time()
        verme.click_shifts_andes()
        m = "4"
        verme.click_shifts_add_doc(m)
        passp = "3314542316"
        verme.click_shifts_add_passport(passp)
        verme.send_photo_shifts()
        verme.click_shifts_andes_all(nm)
        verme.small_time()
        verme.click_shifts_andes()
        m = "5"
        verme.click_shifts_add_doc(m)

        verme.click_shifts_add_therapist()
        verme.send_photo_shifts()
        verme.click_shifts_andes_all(nm)
        verme.small_time()
        verme.click_shifts_andes()

