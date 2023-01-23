import math
import time
from typing import Type

import requests
import allure
from selenium.webdriver.common.by import By
from FW.WEB.AnyPage import AnyPage


class Locator:
    file = "01.jpg"
    sms_url = "https://outsourcing-dev.verme.ru/admin/notifications/notifyitem/"
    verme_url = "https://outsourcing-dev.verme.ru/auth/login/"
    # shifts_dev_url = "https://shifts-dev.verme.ru/auth"

    outsourcing_employees = "https://outsourcing-dev.verme.ru/agency-employees-list/"
    outsourcing_supervisors = "https://outsourcing-dev.verme.ru/employees/supervisors/agency/"

    login_verme = (By.XPATH, "//input[@type='text']")
    password_verme = (By.XPATH, "//input[@type='password']")
    login_signin = (By.XPATH, "//*[contains(@class ,'btn-primary')]")

    # shifts_filter_day_work = (By.XPATH, "(//*[contains(@class ,'v-calendar-weekly__day-label')]//following-sibling::div)[1]")


    outsourcing_pagination = (By.XPATH, "//*[@class='pagination__select custom-select']")
    outsourcing_pagination_value = (By.XPATH, "//option[contains(@value,'20')]")
    outsourcing_sort_fio = (By.XPATH, "//*[contains(@aria-colindex,'2')][contains(@class,'b-table-sort-icon-lef')]")






class outsourcing_create(AnyPage):

    def small_time(self):
        time.sleep(2)
        return self
    def big_time(self):
        time.sleep(4)
        return self
    def more_time(self):
        time.sleep(30)
        return self

    @allure.step('Передаем   Login')
    def send_login(self, txt):
        self.send_keys(Locator.login_verme, txt)
        self.allure_screenshot()

        return self

    @allure.step('Передаем   Password')
    def send_password(self, txt):
        self.send_keys(Locator.password_verme, txt)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем Войти')
    def click_signin(self):
        self.click_element_my(Locator.login_signin)
        self.allure_screenshot()

        return self

    #
    # @allure.step('Загрузить фото при регистрации')
    # def send_photo_shifts(self):
    #     el = (By.XPATH, "//*[contains(@type ,'file')][contains(@accept,'image/*')]")
    #     self.send_keys(el, "E:\\pvp-at\\02.jpg")
    #     time.sleep(3)
    #     self.allure_screenshot()
    #
    #     return self
    #


    @allure.step('Переходим на - Сотрудники')
    def goto_employees_page(self):
        self.goto_page(Locator.outsourcing_employees)
        time.sleep(2)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем на - к-во отображенных сотрудников на странице')
    def outsourcing_click_pagination(self):
        self.click_element_my(Locator.outsourcing_pagination)

        self.allure_screenshot()

        return self
    @allure.step('Выбираем к-во отображенных сотрудников на странице -  {txt}')
    def outsourcing_click_pagination_value(self, txt) -> Type[str]:
        el = (By.XPATH, f"//option[contains(@value,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return str

    @allure.step('Проверяем к-во отображенных {txt} на странице - {txt_1}')
    def outsourcing_check_pagination_value(self, txt, txt_1) -> Type[str]:
        m = f"Показаны {txt} с 1 по {txt_1} из"
        el = (By.XPATH, "//*[@class='pagination__per-page']")
        fin = self.get_text_my(el)
        print(fin)
        assert m in fin, "К-во элементов не корректно"
        self.allure_screenshot()

        return str


    @allure.step('Кликаем  ячейку с данными сотрудника')
    def outsourcing_click_cell(self, txt):
        el = (By.XPATH, f"(//td[contains(@role,'cell')])[{txt}]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Переходим на - {txt}')
    def goto_employees_all_page(self, txt):
        self.goto_page(txt)
        time.sleep(2)
        self.allure_screenshot()

        return self


    @allure.step('Кликаем  ячейку с данными сотрудника')
    def outsourcing_click_cell(self, txt):
        el = (By.XPATH, f"(//td[contains(@role,'cell')])[{txt}]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем сортировка по ФИО')
    def click_sort_fio(self):
        self.click_element_my(Locator.outsourcing_sort_fio)
        self.allure_screenshot()

        return self





    #//*[@role='tab'][contains(.,'График')]
    # @allure.step(' Проверяем диапазон цен >=100')
    # def compare_all(self):
    #     el_l = self.get_count_elements_my(Locator.compare_left)
    #     assert el_l >= 1, "Диапазон не соответсвует >=100"
    #
    #     el_l_min = self.get_count_elements_my(Locator.compare_left_min)
    #     assert el_l_min == 0, "Диапазон не соответсвует <= 99"
    #
    #     el_l_max = self.get_count_elements_my(Locator.compare_left_max)
    #     assert el_l_max == 0, "Диапазон не соответсвует >=201"
    #
    #     return self
    #

    #
    # @allure.step('В блоке итогов на чекауте цена соответствует цене на корзине')
    # def check_price_40(self, txt):
    #     el = self.get_text_my(Locator.promo_get_price)
    #     a = el.split('\n')[:-1]
    #     b = txt.split('\n')[:-1]
    #
    #     aa = ".".join(map(str, a))
    #     bb = ".".join(map(str, b))
    #
    #     aaa = float(aa)
    #     bbb = float(bb)
    #
    #     discount_price_10 = ('{:.1f}'.format(bbb / 100 * 40))
    #
    #     x = float('{:.1f}'.format(bbb / 100 * .5))  # погрешность цены
    #     percent_price_10 = float(discount_price_10)  # %
    #     range_simple_price_10_1 = math.floor(percent_price_10)  # округляем
    #     range_simple_price_10_2 = math.ceil(percent_price_10)
    #     total_1 = ((lambda ex, et: ex - et)(range_simple_price_10_1, 1))
    #     total_2 = ((lambda ex, et: ex + et)(range_simple_price_10_2, 1))
    #
    #     final_1 = float(total_1) + aaa
    #     final_2 = float(total_2) + aaa
    #
    #     assert final_1 <= bbb, "Проценты не верны - "
    #     assert final_2 >= bbb, "Проценты не верны + "
    #
    #     # assert range_simple_price_10_2 <= (discount_price + (x * 4)), "We have a problem"
    #     # total = ((lambda a, b: a + b)(p_1, discount_price_real))
    #     self.allure_screenshot()
    #
    #     return self

    #
    # @allure.step('Кликаем - ингредиенты')
    # def click_receipt_cart_ingredients(self, txt1, txt2):
    #     el = self.get_count_elements(Locator.receipts_cart_ingredients_one)
    #     el1 = (By.XPATH,
    #            f"//*[@class='recipe-checkbox__icon recipe-checkbox__icon--checked']//following-sibling::div[text()='{txt1}']")
    #     el2 = (By.XPATH,
    #            f"//*[@class='recipe-checkbox__icon recipe-checkbox__icon--checked']//following-sibling::div[text()='{txt2}']")
    #     self.click_element_my(el1)
    #     self.click_element_my(el2)
    #     em = 2
    #     el3 = ((lambda a, b: a - b)(el, em))
    #     assert el3 + em == el, "Ингредиенты не выбрались"
    #     self.allure_screenshot()
    #
    #     return self
    #




