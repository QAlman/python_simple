# import time
# from random import random
# import allure
# import pytest
# from Test.web_tests.WebBase import WebBase
#
#
# @allure.feature('Web - Outsourcing')
# @allure.story('Test 29   Тестирование страницы - Версия1')
# class _TestOutsourcing_29(WebBase):
#
#     @allure.title('29: 2-986 :  Тестирование страницы - Версия1')
#     @allure.severity(allure.severity_level.CRITICAL)
#     @allure.link(name="2-986 :  Тестирование страницы - Версия1",
#                  url="https://testlink.verme.ru/index.php?caller=login&viewer=")
#     @allure.description("Позитивный тест 2-986 :  Тестирование страницы - Версия1")
#     @pytest.mark.CRITICAL
#     @pytest.mark.WebTest
#     @pytest.mark.skip
#     def _test_outsourcing_29(self):
#         outsourcing = self.APP.web_activity.button_to_outsourcing()
#
#         v = "test_outsourcing_2023"
#         outsourcing.send_login(v)
#         v = "freftTRHTRH!@#13564"
#         outsourcing.send_password(v)
#         outsourcing.click_signin()
#         outsourcing.small_time()
#         ur = "https://outsourcing-auto.verme.ru/client-quotas-list/"
#         outsourcing.goto_employees_all_page(ur)
#         outsourcing.small_time()
#
#         ch = "SPAR"
#         nb = "1"
#         outsourcing.click_field_agency(ch, nb)
#         outsourcing.small_time()
#
#         sp = "button"
#         tx = "Действия"
#         outsourcing.click_only_txt(sp, tx)
#         outsourcing.small_time()
#
#         """
#         Необходимо детализировать шаги теста
#
#         """
#
#
#
#
#
