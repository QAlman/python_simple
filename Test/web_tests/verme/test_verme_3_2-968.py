import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Verme')
@allure.story('Test 3  Регистрации')
class TestVerme_3(WebBase):

    @allure.title('3: 2-968 : Фильтры смен')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-968 : Регистрации на Shifts-dev - Version 1", url="https://testlink.verme.ru/index.php?caller=login&viewer=")

    @allure.description("Позитивный тест 2-968 : Регистрации на Shifts-dev - Version 1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_verme_3(self):
        verme = self.APP.web_activity.button_to_shifts()
        self.APP.web_steps.step_test_1()
        verme.click_shifts_next()
        verme.click_shifts_done()
        verme.click_shifts_phone()
        z = "456473784"
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
        verme.small_time()

        verme.click_shifts_after_approve()
        verme.click_shifts_after_reg()

        verme.click_shifts_filter()
        fl = "1"
        verme.send_shifts_filter_data(fl)
        fl = "2"
        verme.send_shifts_filter_data(fl)
        fl = "3"
        verme.send_shifts_filter_data(fl)
        fl = "4"
        verme.send_shifts_filter_data(fl)
        # fl = "5"
        # verme.send_shifts_filter_data(fl) # метро
        fl = "6"
        verme.send_shifts_filter_data(fl)

        verme.click_shifts_filter_apply()


