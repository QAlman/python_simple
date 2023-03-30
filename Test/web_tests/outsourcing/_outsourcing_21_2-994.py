# import time
# from random import random
# import allure
# import pytest
# from Test.web_tests.WebBase import WebBase
#
#
# @allure.feature('Web - Outsourcing')
# @allure.story('Test 21   Тестирование страницы')
# class _TestOutsourcing_21(WebBase):
#
#     @allure.title('21: 2-994 :  Тестирование страницы - Версия1')
#     @allure.severity(allure.severity_level.CRITICAL)
#     @allure.link(name="2-994 :  Тестирование страницы - Версия1",
#                  url="https://testlink.verme.ru/index.php?caller=login&viewer=")
#     @allure.description("Позитивный тест 2-994 :  Тестирование страницы - Версия1")
#     @pytest.mark.CRITICAL
#     @pytest.mark.WebTest
#     @pytest.mark.skip
#     def _test_outsourcing_21(self):
#         outsourcing = self.APP.web_activity.button_to_outsourcing()
#
#         v = "test_outsourcing_2023"
#         outsourcing.send_login(v)
#         v = "freftTRHTRH!@#13564"
#         outsourcing.send_password(v)
#         outsourcing.click_signin()
#         outsourcing.small_time()
#
#         ur = "https://outsourcing-auto.verme.ru/client-schedule"
#         outsourcing.goto_employees_all_page(ur)
#
#         ch = "ТЦ АвиаПарк"
#         nb = "1"
#         outsourcing.click_field_agency(ch, nb)
#         outsourcing.small_time()
#         sp = "span"
#         tx = " Для выбранного магазина нет доступных смен "
#         outsourcing.click_only_txt(sp, tx)
#
#
#
#
#
