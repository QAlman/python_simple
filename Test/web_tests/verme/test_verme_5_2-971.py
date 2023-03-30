# import time
# from random import random
# import allure
# import pytest
# from Test.web_tests.WebBase import WebBase
#
#
# @allure.feature('Web - Verme')
# @allure.story('Test 5  Регистрации')
# class TestVerme_5(WebBase):
#
#     @allure.title('5:  2-971 : Страница Смены модуль "График смен" в режиме день')
#     @allure.severity(allure.severity_level.CRITICAL)
#     @allure.link(name="2-971 : Регистрации на Shifts-dev - Version 1", url="https://testlink.verme.ru/index.php?caller=login&viewer=")
#
#     @allure.description("Позитивный тест 2-971 : Регистрации на Shifts-dev - Version 1")
#     @pytest.mark.CRITICAL
#     @pytest.mark.WebTest
#     @pytest.mark.skip
#     def test_verme_5(self):
#         verme = self.APP.web_activity.button_to_shifts()
#         self.APP.web_steps.step_test_1()
#         verme.click_shifts_next()
#         verme.click_shifts_done()
#         verme.click_shifts_phone()
#         z = "456473784"
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
#         verme.click_shifts_after_approve()
#         verme.click_shifts_after_reg()
#         d = "11"
#         verme.click_shifts_registration_btn(d)
#         verme.small_time()
#         t = " Инфо "
#         verme.click_shifts_title(t)
#         t = " Смены "
#         verme.click_shifts_title(t)
#         verme. click_shifts_day_present()
#         verme.small_time()
#         verme.small_time()
#         verme.small_time()
#
#         t = " Инфо "
#         verme.click_shifts_title(t)
#         t = " Смены "
#         verme.click_shifts_title(t)
#         s = verme.click_shifts_day_work()
#         verme.click_shifts_btn_content(s)
#
