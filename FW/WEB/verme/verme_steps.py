import time

import allure
from selenium.webdriver.common.by import By
from FW.WEB.AnyPage import AnyPage




class verme_steps(AnyPage):

    @allure.step('ШАГИ')
    def step_test_1(self):
        print("1. Открыть портал Shifts-dev \n"
              "2. В поле авторизации ввести произвольный номер телефона(номер должен начинаться с 9)\n"
              "3. Заполняем данные пользователя Обязательные поля: Фамилия Имя  Отчество Дата рождение Пол Гражданство Фактическое место проживание Регионы подработки\n "
              "4.Загружаем аватар пользвателя\n")

        return self


