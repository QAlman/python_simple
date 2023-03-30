# import time
# from random import random
# import allure
# import pytest
# from Test.web_tests.WebBase import WebBase
#
#
# @allure.feature('Web - Verme')
# @allure.story('Test 6  Регистрации')
# class TestVerme_6(WebBase):
#
#     @allure.title('6: 2-972 : Проверка резервации смен')
#     @allure.severity(allure.severity_level.CRITICAL)
#     @allure.link(name="2-972 : 2-972 : Проверка резервации смен", url="https://testlink.verme.ru/index.php?caller=login&viewer=")
#
#     @allure.description("Позитивный тест 2-972 : 2-972 : Проверка резервации смен")
#     @pytest.mark.CRITICAL
#     @pytest.mark.WebTest
#     @pytest.mark.skip
#     def test_verme_6(self):
#
#         verme = self.APP.web_activity.button_to_shifts()
#         self.APP.web_steps.step_test_1()
#         verme.click_shifts_next()
#         verme.click_shifts_done()
#         verme.click_shifts_phone()
#         z = "920918147"
#         verme.send_shifts_phone(str(z))
#         verme.click_shifts_call()
#         verme.goto_celery_page()
#         v = "asdsadsfdvg@asdsffrgt.com"
#         verme.send_login(v)
#         v = "freftTRHTRH!@#13564"
#         verme.send_password(v)
#         verme.click_signin_celery()
#         verme.send_login(z)
#         verme.click_signin_celery()
#         verme.click_phone_celery(z)
#         x = verme.get_text_sms()
#         verme.return_shifts_page()
#         verme.send_sms_code_phone_4(x)
#         verme.small_time()
#
#         verme.click_shifts_after_approve()
#         fl = " График "
#         verme.get_shifts_click_field(fl)
#         verme.click_shifts_after_reg()
#
#         d = "11"
#         verme.click_shifts_btn_content(d)
#         verme.small_time()
#         t = " Инфо "
#         verme.click_shifts_title(t)
#         t = " Смены "
#         verme.click_shifts_title(t)
#         verme.get_shifts_click_field(fl)
#
#         s = verme.click_shifts_day_work()
#         verme.click_shifts_btn_content(s)
#         verme.big_time()
#         verme.get_shifts_first()
#         #verme.get_shifts_first_close()
#         verme.get_shifts_first_open()
#
#         d = " Да "
#         verme.click_shifts_btn_content(d)
#         #time.sleep(22222)
#         ch = "Моя смена"
#         ch_1 = "Назначена"
#         verme.get_shifts_first_open_chip(ch, ch_1)
#         d = " Отказаться "
#         verme.click_shifts_btn_content(d)
#         verme.small_time()
#         d = " Да "
#         verme.click_shifts_btn_content(d)
#         verme.big_time()
#
#
#
#
#
#
