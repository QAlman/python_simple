import time
import random
import string
import allure
from selenium.webdriver.common.by import By

from FW.WEB.web_base import WebBase


class Locator:
    user_avatar = (By.CSS_SELECTOR, '[test_id="menu-current-user"]')
    profile_exit_btn = (By.CSS_SELECTOR, '[test_id="profile-exit"]')
    profile_exit_submit_btn = (By.CSS_SELECTOR, '[test_id="profile-exit-submit"]')
    citypicker_close = (By.XPATH, "//div[@class='close-control']")
    cookie_close = (By.XPATH, "//*[@class='button__inner cookie-usage-notice__button-inner--desktop']")
    phone_code_api = "000000"
    phone_code_all = "//*[@type='number']"

    phone_code_1 = (By.XPATH, "(//*[@type='number'])[1]")
    phone_code_2 = (By.XPATH, "(//*[@type='number'])[2]")
    phone_code_3 = (By.XPATH, "(//*[@type='number'])[3]")
    phone_code_4 = (By.XPATH, "(//*[@type='number'])[4]")
    phone_code_5 = (By.XPATH, "(//*[@type='number'])[5]")
    phone_code_6 = (By.XPATH, "(//*[@type='number'])[6]")

class AnyPage(WebBase):

    @allure.step('Смена авторизованного пользователя')
    def change_user(self, user_login, user_password):
        """
        Данный метод не может вернуть экземплар класса
        :param user_login:
        :param user_password:
        :return:
        """
        current_url = self.get_current_url()
        self.exit_the_profile()
        self.click_exit_submit_btn()
        self.manager.web_login.login_log_pas(user_login, user_password)
        self.goto_page(current_url)
        time.sleep(5)

    @allure.step('Выход из профиля')
    def exit_the_profile(self):
        # Наводим курсор аватар пользователя
        self.move_to_element(Locator.user_avatar)
        # Кнопка выхода из профиля
        self.click_element(Locator.profile_exit_btn)
        return self

    @allure.step('Нажать кнопку подтверждения выхода из профиля')
    def click_exit_submit_btn(self):
        # Кнопка подтверждения выхода из профиля
        self.click_element(Locator.profile_exit_submit_btn)
        return self

    @allure.step('Закрываем ситипикер')
    def close_citypiker(self):
        self.click_element_my(Locator.citypicker_close)
        self.allure_screenshot()
        return self

    @allure.step('Закрываем куки')
    def close_cookie(self):
        self.click_element_my(Locator.cookie_close)
        self.allure_screenshot()
        return self


    def generate_random_string(length_1=9):
        letters = string.digits
        rand_string = ''.join(random.choice(letters) for i in range(length_1))
        return rand_string
    string_d = generate_random_string()

    def generate_random_string_letters(length_2=9):
        letters2 = 'йцукенгшщзхфывапролджэячсмитьбюЫВАПРОЛЙЦУКЕНГШЩЗСМИТЬБЮ'
        rand_string2 = ''.join(random.choice(letters2) for i in range(length_2))
        return rand_string2
    string_letters = generate_random_string_letters()





    @allure.step('Отправляем 4 значения кода смс')
    def send_sms_code_phone_4(self, *args):
        self.send_keys(Locator.phone_code_1, *args)
        self.send_keys(Locator.phone_code_2, *args)
        self.send_keys(Locator.phone_code_3, *args)
        self.send_keys(Locator.phone_code_4, *args)
        self.allure_screenshot()
        return self

    @allure.step('Отправляем 6 значений кода смс')
    def send_sms_code_phone_6(self, *args):
        time.sleep(1)
        self.send_keys(Locator.phone_code_1, *args)
        self.send_keys(Locator.phone_code_2, *args)
        self.send_keys(Locator.phone_code_3, *args)
        self.send_keys(Locator.phone_code_4, *args)
        self.send_keys(Locator.phone_code_5, *args)
        self.send_keys(Locator.phone_code_6, *args)
        self.allure_screenshot()
        return self



    @allure.step('Отправляем код смс')
    def send_sms_code_phone(self, *args):
        time.sleep(1)
        i = self.get_count_elements("//*[@data-id]")
        if i == 4:
            self.send_sms_code_phone_4(*args)
        else:
            self.send_sms_code_phone_6(*args)
        self.allure_screenshot()

        return self
