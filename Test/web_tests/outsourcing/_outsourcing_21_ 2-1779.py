# import time
# from random import random
# import datetime
# import allure
# import pytest
# from Test.web_tests.WebBase import WebBase
# from selenium.webdriver.common.keys import Keys
#
#
# @allure.feature('Web - Outsourcing')
# @allure.story('Test 21    Тестирование страницы "Планировние доступностей" ')
# class _TestOutsourcing_21(WebBase):
#
#     @allure.title('21: 2-1779 :     Тестирование страницы "Планировние доступностей" - Версия1')
#     @allure.severity(allure.severity_level.CRITICAL)
#     @allure.link(name='2-1779 :      Тестирование страницы "Планировние доступностей" - Версия1',
#                  url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1779")
#     @allure.description('Позитивный тест 2-1779 :      Тестирование страницы "Планировние доступностей" - Версия1')
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
#         ur = "https://outsourcing-auto.verme.ru/outsource/orglinks/client/"
#         outsourcing.goto_employees_all_page(ur)
#         outsourcing.small_time()
#
#         ch = "SPAR"
#         nb = "1"
#         outsourcing.click_field_agency(ch, nb)
#         outsourcing.small_time()
#
#         # ur = "https://outsourcing-auto.verme.ru/client-reports/"
#         # outsourcing.goto_employees_all_page(ur)
#         # outsourcing.small_time()
#         #
#         # ch = "Эльдорадо а442"
#         # nb = "1"
#         # outsourcing.click_field_agency(ch, nb)
#         # outsourcing.small_time()
#         #
#         # ur = "https://outsourcing-auto.verme.ru/promo-reports/"
#         # outsourcing.goto_employees_all_page(ur)
#         # outsourcing.small_time()
#         #
#         # ch = "Директ Кредит"
#         # nb = "1"
#         # outsourcing.click_field_agency(ch, nb)
#         # outsourcing.small_time()