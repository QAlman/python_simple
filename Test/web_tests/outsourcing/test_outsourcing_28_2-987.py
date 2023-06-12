import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('28: 2-987 :  Тестирование фильтров на страницах - Версия1')
class TestOutsourcing_28(WebBase):

    @allure.title('28: 2-987 :  Тестирование фильтров на страницах - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1014 :  Тестирование фильтров на страницах - Версия1",
                 url="https://testlink.verme.ru/index.php?caller=login&viewer=")
    @allure.description("Позитивный тест 2-987 :  Тестирование фильтров на страницах - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_987
    @pytest.mark.skip
    def test_outsourcing_28(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        ur = "https://outsourcing-auto.verme.ru/agency-claims-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Тестовое агентство М.Видео"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        sp = "button"
        tx = "Столбцы"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        checkbox = '#'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Магазин'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Тип обращения'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Обновлено'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Текст обращения'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Статус'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Смена статуса'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Файлы'
        outsourcing.click_checkbox_claim(checkbox)

        tx = "Восстановить"
        outsourcing.click_text_center_claim(tx)
        outsourcing.small_time()




        ur = "https://outsourcing-auto.verme.ru/client-claims-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = 'Группа "М.Видео-Эльдорадо"'
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        sp = "button"
        tx = "Столбцы"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        checkbox = '#'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Город'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Магазин'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Агентство'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Тип обращения'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Обновлено'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Текст обращения'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Статус'
        outsourcing.click_checkbox_claim(checkbox)


        tx = "Восстановить"
        outsourcing.click_text_center_claim(tx)
        outsourcing.small_time()

        """
        Необходимо детализировать шаги теста

        """





