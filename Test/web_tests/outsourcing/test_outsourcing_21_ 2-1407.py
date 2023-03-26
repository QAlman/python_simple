import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 21  Тестирование редактора столбцов ')
class TestOutsourcing_21(WebBase):

    @allure.title('21: 2-1407 :  Тестирование редактора столбцов - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1407 :  Тестирование редактора столбцов - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-1407")
    @allure.description("Позитивный тест 2-1407 :  Тестирование редактора столбцов - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_outsourcing_21(self):
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

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        sp = "button"
        tx = "Столбцы"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()
        outsourcing.small_time()

        checkbox = 'ФИО'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Статусы'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Номер телефона'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Гражданство'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Компетенции'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Документы'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Регионы подработки'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Города'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Комментарий'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Менеджер'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Торговые сети'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Информация'
        outsourcing.click_checkbox_claim(checkbox)

        tx = "Восстановить"
        outsourcing.click_text_center_claim(tx)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/agency-requests-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        sp = "button"
        tx = "Столбцы"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()
        outsourcing.small_time()

        checkbox = 'Магазин'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Функции'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Период'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Получено'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Смены'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Часы'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Стоимость заявки'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Статус'
        outsourcing.click_checkbox_claim(checkbox)

        tx = "Восстановить"
        outsourcing.click_text_center_claim(tx)
        outsourcing.small_time()

        ur = "https://outsourcing-auto.verme.ru/shifts-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        ch = "Моя Смена"
        nb = "1"
        outsourcing.click_field_agency(ch, nb)
        outsourcing.small_time()

        sp = "button"
        tx = "Столбцы"
        outsourcing.click_only_txt(sp, tx)
        outsourcing.small_time()
        outsourcing.small_time()

        checkbox = 'Город'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Магазин'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Дата'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Функция'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Смена'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Стоимость'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Сотрудник'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Телефон'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'отметок'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Комментарий'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'SMS отправлено'
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
        checkbox = 'Статус'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Обновлено'
        outsourcing.click_checkbox_claim(checkbox)
        checkbox = 'Текст обращения'
        outsourcing.click_checkbox_claim(checkbox)

        tx = "Восстановить"
        outsourcing.click_text_center_claim(tx)
        outsourcing.small_time()


        #
        # sp = "span"
        # tx = "Создать сотрудника"
        # outsourcing.click_only_txt(sp, tx)
        #
        # nb = "2"
        # outsourcing.outsourcing_click_cell(nb)
        # outsourcing.click_only_menu()
        #
        # sp = "span"
        # tx = "Создать сотрудника"
        # outsourcing.click_only_txt(sp, tx)
        #
        # outsourcing.agency_create_employee()
        #
        # sp = "button"
        # tx = "Добавить"
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "button"
        # tx = "Редактировать сотрудника "
        # outsourcing.click_only_txt(sp, tx)
        #
        # outsourcing.agency_edit_employee()
        #
        # sp = "button"
        # tx = " Сохранить изменения "
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "span"
        # tx = "Документы"
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "span"
        # tx = "Компетенции"
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "span"
        # tx = "Кадровые документы"
        # outsourcing.click_only_txt(sp, tx)
        #
        # outsourcing.click_only_tabels()
        #
        # sp = "span"
        # tx = "История переводов"
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "span"
        # tx = "Лицевая биометрия"
        # outsourcing.click_only_txt(sp, tx)
        #
        # #outsourcing.send_photo_agency()
        # file = "02.jpg"
        # outsourcing.send_photo_agency_all(file)
        #
        # sp = "button"
        # tx = " Кадрировать и отправить "
        # outsourcing.click_only_txt(sp, tx)
        # outsourcing.small_time()
        #
        # sp = "span"
        # tx = "Клиенты"
        # outsourcing.click_only_txt(sp, tx)
        #
        # sp = "span"
        # tx = "Мероприятия"
        # outsourcing.click_only_txt(sp, tx)
        #
        #
        # """
        # Необходимо детализировать шаги теста
        #
        # """




