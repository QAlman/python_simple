import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('Test 2  Тестирование сохранения фильтров и сортировки ')
class TestOutsourcing_2(WebBase):

    @allure.title('1: 2-1016 : Тестирование сохранения фильтров и сортировки - Версия 1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-1016 : Тестирование сохранения фильтров и сортировки - Версия 1", url="https://testlink.verme.ru/index.php?caller=login&viewer=")

    @allure.description("Позитивный тест 2-1016 : Тестирование сохранения фильтров и сортировки - Версия 1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def test_outsourcing_2(self):

        outsourcing = self.APP.web_activity.button_to_outsourcing()
        # self.APP.web_steps.step_test_1()
        # verme.click_shifts_next()
        # verme.click_shifts_done()
        # z = self.APP.web_any_page.string_d
        # o = z[5:10]
        # print(z)
        # verme.click_shifts_phone()
        # verme.send_shifts_phone(str(z))
        # verme.click_shifts_call()
        # verme.goto_celery_page()
        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        ur = "https://outsourcing-dev.verme.ru/agency-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()

        outsourcing.outsourcing_click_pagination()
        z = "20"
        e = "сотрудники"
        outsourcing.outsourcing_click_pagination_value(z)
        outsourcing.outsourcing_check_pagination_value(e, z)
        c = "9"
        outsourcing.outsourcing_click_cell(c)
        outsourcing.small_time()
        ur = "https://outsourcing-dev.verme.ru/agency-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.outsourcing_check_pagination_value(e, z)

        ur = "https://outsourcing-dev.verme.ru/employees/supervisors/agency/"
        outsourcing.goto_employees_all_page(ur)
        z = "20"
        e = "супервайзеры"
        outsourcing.outsourcing_click_pagination_value(z)
        z = "2"
        outsourcing.outsourcing_check_pagination_value(e, z)
        ur = "https://outsourcing-dev.verme.ru/agency-requests-list/"
        outsourcing.goto_employees_all_page(ur)
        ur = "https://outsourcing-dev.verme.ru/shifts-list/"
        outsourcing.goto_employees_all_page(ur)
        ur = "https://outsourcing-dev.verme.ru/agency-claims-list/"
        outsourcing.goto_employees_all_page(ur)
        ur = "https://outsourcing-dev.verme.ru/outsource-reports/"
        outsourcing.goto_employees_all_page(ur)



        ur = "https://outsourcing-dev.verme.ru/outsource/orglinks/client/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.outsourcing_click_pagination()
        z = "20"
        e = "связи"
        outsourcing.outsourcing_click_pagination_value(z)
        outsourcing.outsourcing_check_pagination_value(e, z)
        c = "9"
        outsourcing.outsourcing_click_cell(c)
        outsourcing.small_time()
        ur = "https://outsourcing-dev.verme.ru/outsource/orglinks/client/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.outsourcing_check_pagination_value(e, z)

        ur = "https://outsourcing-dev.verme.ru/client-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.outsourcing_click_pagination()
        z = "20"
        e = "сотрудники"
        outsourcing.outsourcing_click_pagination_value(z)
        z = "16"
        outsourcing.outsourcing_check_pagination_value(e, z)
        c = "9"
        outsourcing.outsourcing_click_cell(c)
        outsourcing.small_time()
        ur = "https://outsourcing-dev.verme.ru/client-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.outsourcing_check_pagination_value(e, z)

        ur = "https://outsourcing-dev.verme.ru/employees/supervisors/hq/"
        outsourcing.goto_employees_all_page(ur)

        ur = "https://outsourcing-dev.verme.ru/client-reports/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.outsourcing_click_pagination()
        z = "20"
        e = "отчёты"
        outsourcing.outsourcing_click_pagination_value(z)
        z= "3"
        outsourcing.outsourcing_check_pagination_value(e, z)
        c = "9"
        outsourcing.outsourcing_click_cell(c)
        outsourcing.small_time()
        ur = "https://outsourcing-dev.verme.ru/client-reports/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.outsourcing_check_pagination_value(e, z)

        ur = "https://outsourcing-dev.verme.ru/promo-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.outsourcing_click_pagination()
        z = "20"
        e = "сотрудники"
        outsourcing.outsourcing_click_pagination_value(z)
        z = "9"
        outsourcing.outsourcing_check_pagination_value(e, z)
        c = "9"
        outsourcing.outsourcing_click_cell(c)
        outsourcing.small_time()
        ur = "https://outsourcing-dev.verme.ru/promo-employees-list/"
        outsourcing.goto_employees_all_page(ur)
        outsourcing.small_time()
        outsourcing.outsourcing_check_pagination_value(e, z)

        ur = "https://outsourcing-dev.verme.ru/promo-reports/"
        outsourcing.goto_employees_all_page(ur)


        #time.sleep(22222)


        # verme.send_login(z)
        # verme.click_signin_celery()
        # verme.click_phone_celery(z)
        # x = verme.get_text_sms()
        # verme.return_shifts_page()
        # verme.send_sms_code_phone_4(x)
        # verme.small_time()
        #
        # f = "Фамилия"
        # f_1 = self.APP.web_any_page.string_letters
        # f_2 = "84"
        # verme.send_shifts_registration_txt(f, f_1, f_2)
        #
        # f = "Имя"
        # f_2 = "88"
        # verme.send_shifts_registration_txt(f, f_1, f_2)
        #
        # f = "Отчество"
        # f_2 = "92"
        # verme.send_shifts_registration_txt(f, f_1, f_2)
        #
        # g = "мужской"
        # verme.click_shifts_registration_btn(g)
        #
        # data = "1990"
        # month = "янв."
        # day = "31"
        # fm = "1"
        # verme.click_shifts_registration_data(data, month, day, fm)
        #
        # s = "Гражданство"
        # country = "Россия"
        # verme.click_shifts_registration_country(s, country)
        #
        # next = "Продолжить"
        # verme.click_shifts_registration_btn(next)
        #
        # s = "Фактическое место проживания"
        # p = "г Москва, пр-кт Мира, д 111, кв 3"
        # r = "115"
        # verme.click_shifts_registration_slot(s, r, p )
        #
        # s = "Регионы подработки"
        # p = "Москва"
        # verme.click_shifts_registration_region(s, p)
        #
        # verme.click_shifts_registration_btn(next)
        # verme.send_photo_shifts()
        # verme.click_shifts_approve()
        # vote = " Я принимаю "
        # verme.click_shifts_registration_btn(vote)
        # verme.click_shifts_registration_btn(next)




