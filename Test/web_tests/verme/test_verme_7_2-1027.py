import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Verme')
@allure.story('Test 7  Регистрации')
class TestVerme_7(WebBase):

    @allure.title('7:  2-1027 : Авторизация в МС - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-974 : Регистрации на Shifts-dev - Version 1", url="https://testlink.verme.ru/index.php?caller=login&viewer=")

    @allure.description("Позитивный тест 2-1027 : Авторизация в МС - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def test_verme_7(self):

        verme = self.APP.web_activity.button_to_shifts()
        self.APP.web_steps.step_test_1()
        verme.click_shifts_next()
        verme.click_shifts_done()
        z = "491675366"
        verme.click_shifts_phone()
        verme.send_shifts_phone(str(z))
        verme.click_shifts_call()
        verme.small_time()
        ph = "+7 949 167-53-66"
        verme.get_shifts_phone_compare(ph)
        o = " Изменить номер "
        verme.click_shifts_btn_content(o)
        verme.click_shifts_call()
        verme.get_shifts_phone_compare(ph)

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
        verme.small_time()

        verme.click_shifts_after_approve()
        verme.click_shifts_after_reg()
        verme.shifts_click_avatar()
        verme.small_time()

        o = " Выйти из приложения "
        verme.click_shifts_btn_content(o)

        verme.click_shifts_call()
        verme.get_shifts_phone_compare(ph)
        verme.more_time()
        o = " Отправить код по смс "
        verme.click_shifts_btn_content(o)
        verme.small_time()
        verme.get_shifts_phone_compare(ph)

        verme.switch_to_tab()
        verme.shifts_click_quee()
        verme.small_time()
        verme.send_login(z)
        verme.click_signin_celery()
        verme.click_phone_celery(z)
        x = verme.get_text_sms()
        verme.return_shifts_page()
        verme.send_sms_code_phone_4(x)
        verme.small_time()
        verme.shifts_click_avatar()


