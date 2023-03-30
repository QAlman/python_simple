import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 39   Тестирование push оповещений')
class _TestOutsourcing_39(WebBase):

    @allure.title('39: 2-1074 :  Тестирование push оповещений - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1074 :  Тестирование push оповещений - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-1074 :  Тестирование push оповещений - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def _test_outsourcing_39(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/admin/notifications/notifytemplates/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/admin/notifications/notifyitem/ "
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()



        sp = "a"
        tx = "Добавить Очередь оповещения"
        outsourcing.click_only_txt(sp, tx)
        #time.sleep(22222)
        # sp = "a"
        # tx = "Добавить Шаблон оповещений"
        # outsourcing.click_only_txt(sp, tx)

        # chb = "checked"
        # tx = "Табель - разрешить агентства создание корректировок"
        # id_12 = "id_config_set-12-value"
        # outsourcing.chekbox_all(chb, tx, id_12)
        # #
        # t_1 = "input"
        # t_2 = "name"
        # t_3 = "_save"
        # outsourcing.click_only_class(t_1, t_2, t_3)
        #
        # #time.sleep(22222)

        """
        Необходимо расписать шаги подробно и разбить тест на несколько
        с использованием  заранее подготовленных пользователнй

        """

        # c = "9"
        # outsourcing.outsourcing_click_cell(c)

        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # #outsourcing.click_sort_fio()
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/employees/supervisors/agency/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/client-employees-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/client-shifts-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/client-reports/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/promo-employees-list/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)
        # outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/promo-reports/"
        # outsourcing.goto_employees_all_page(ur)
        # outsourcing.small_time()
        # dt = "1"
        # outsourcing.click_sort_all(dt)




