# import time
# from random import random
# import allure
# import pytest
# from Test.web_tests.WebBase import WebBase
#
#
# @allure.feature('Web - Outsourcing')
# @allure.story('Test 2  Тестирование сохранения фильтров и сортировки ')
# class _TestOutsourcing_2(WebBase):
#
#     @allure.title('1: 2-1016 : Тестирование сохранения фильтров и сортировки - Версия 1')
#     @allure.severity(allure.severity_level.CRITICAL)
#     @allure.link(name="2-1016 : Тестирование сохранения фильтров и сортировки - Версия 1", url="https://testlink.verme.ru/index.php?caller=login&viewer=")
#
#     @allure.description("Позитивный тест 2-1016 : Тестирование сохранения фильтров и сортировки - Версия 1")
#     @pytest.mark.CRITICAL
#     @pytest.mark.WebTest
#     @pytest.mark.skip
#     def _test_outsourcing_2(self):
#         outsourcing = self.APP.web_activity.button_to_outsourcing()
#
#         v = "test_outsourcing_2023"
#         outsourcing.send_login(v)
#         v = "freftTRHTRH!@#13564"
#         outsourcing.send_password(v)
#         outsourcing.click_signin()
#         # ur = "https://outsourcing-auto.verme.ru/agency-employees-list/"
#         # outsourcing.goto_employees_all_page(ur)
#         outsourcing.small_time()
#         dx = "2"
#         dt = "1"
#         outsourcing.click_sort_all(dx, dt)
#         #outsourcing.click_sort_fio()
#         outsourcing.small_time()
#         ur = "https://outsourcing-auto.verme.ru/employees/supervisors/agency/"
#         outsourcing.goto_employees_all_page(ur)
#         outsourcing.small_time()
#         outsourcing.click_sort_all(dx, dt)
#
#         outsourcing.small_time()
#         ur = "https://outsourcing-auto.verme.ru/client-employees-list/"
#         outsourcing.goto_employees_all_page(ur)
#         outsourcing.small_time()
#         outsourcing.click_sort_all(dx, dt)
#
#         outsourcing.small_time()
#         ur = "https://outsourcing-auto.verme.ru/client-shifts-list/"
#         outsourcing.goto_employees_all_page(ur)
#         outsourcing.small_time()
#         dx = "5"
#         outsourcing.click_sort_all(dx, dt)
#
#         outsourcing.small_time()
#         ur = "https://outsourcing-auto.verme.ru/client-reports/"
#         outsourcing.goto_employees_all_page(ur)
#         outsourcing.small_time()
#         dx = "2"
#         outsourcing.click_sort_all(dx, dt)
#
#         outsourcing.small_time()
#         ur = "https://outsourcing-auto.verme.ru/promo-employees-list/"
#         outsourcing.goto_employees_all_page(ur)
#         outsourcing.small_time()
#         outsourcing.click_sort_all(dx, dt)
#
#         outsourcing.small_time()
#         ur = "https://outsourcing-auto.verme.ru/promo-reports/"
#         outsourcing.goto_employees_all_page(ur)
#         outsourcing.small_time()
#         outsourcing.click_sort_all(dx, dt)
#
#
#
#