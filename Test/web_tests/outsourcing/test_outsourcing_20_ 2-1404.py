import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('20: 2-1404 :  Тестирование Карточки Сотрудника - Версия1')
class TestOutsourcing_20(WebBase):

    @allure.title('20: 2-1404 :  Тестирование Карточки Сотрудника - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1404 :  Тестирование Карточки Сотрудника - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1404")
    @allure.description("Позитивный тест 2-1404 :  Тестирование Карточки Сотрудника - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_20(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()
        # ur = "https://outsourcing-auto.verme.ru/agency-employees-list/"
        # outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        nb = "2"
        outsourcing.outsourcing_click_cell(nb)
        outsourcing.click_only_menu()

        sp = "span"
        tx = "Создать сотрудника"
        outsourcing.click_only_txt(sp, tx)

        outsourcing.agency_create_employee()

        sp = "button"
        tx = "Добавить"
        outsourcing.click_only_txt(sp, tx)

        sp = "button"
        tx = "Редактировать сотрудника "
        outsourcing.click_only_txt(sp, tx)

        outsourcing.agency_edit_employee()

        sp = "button"
        tx = " Сохранить изменения "
        outsourcing.click_only_txt(sp, tx)

        sp = "span"
        tx = "Документы"
        outsourcing.click_only_txt(sp, tx)

        sp = "span"
        tx = "Компетенции"
        outsourcing.click_only_txt(sp, tx)

        sp = "span"
        tx = "Кадровые документы"
        outsourcing.click_only_txt(sp, tx)

        outsourcing.click_only_tabels()

        sp = "span"
        tx = "История переводов"
        outsourcing.click_only_txt(sp, tx)

        sp = "span"
        tx = "Лицевая биометрия"
        outsourcing.click_only_txt(sp, tx)

        #outsourcing.send_photo_agency()
        file = "02.jpg"
        outsourcing.send_photo_agency_all(file)

        sp = "button"
        tx = " Кадрировать и отправить "
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()

        sp = "span"
        tx = "Клиенты"
        outsourcing.click_only_txt(sp, tx)

        sp = "span"
        tx = "Мероприятия"
        outsourcing.click_only_txt(sp, tx)


        """
        Необходимо детализировать шаги теста

        """




