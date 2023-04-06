#  28 регистрация нового пользователя через корзину по коду
import allure
import pytest
from selenium import webdriver
import pytest_rerunfailures
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

import time, re
import random
import string
import datetime

class Test_28():
    @pytest.fixture()
    def test_setup(self):
        global driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1200")
        #chrome_options.add_argument("--headless")

        driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        driver.implicitly_wait(30)
        driver.set_page_load_timeout(30)
        driver.set_script_timeout(30)
        self.base_url = "http://158.160.30.28/"
        yield
        driver.close()
        driver.quit()

    @allure.feature('Test 28 регистрация нового пользователя через корзину по коду')
    #@allure.story('Story 28 ')
    @allure.step("регистрация нового пользователя через корзину по коду")
    def test_untitled_test_case_test_Registration_new_basket_code(self, test_setup):

        driver.get(self.base_url)


        # # ----------citypicker
        #
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "Username"))).click()  #
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "Username"))).send_keys("servadmin")
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "Password"))).click()  #
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "Password"))).send_keys("17442511")
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "button"))).click()


        time.sleep(4)
        driver.get("http://158.160.30.28/studio/")

        # WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, "//*[@class='input-field__label'][text()='Введите адрес магазина']/following-sibling::input"))).send_keys(
        #     "ул. Савушкина, д. 112, лит. А")
        #
        # WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, "//div[@class='stores-list-item__name'][text()='ул.  Савушкина, д. 112, лит. А']"))).click()
        #
        # WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, "//span[@class='button__inner'][text()='Выбрать магазин']"))).click()
        #
        # # ----------citypicker
        # #
        # time.sleep(7)

        time.sleep(22222)



        # ------------random-------
        def generate_random_string(length_1=9):
            letters = string.digits
            rand_string = ''.join(random.choice(letters) for i in range(length_1))
            return rand_string

        generate_random_string()

        string_d = generate_random_string()


        # -------------random-------

        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='close-control']"))).click()  # ----------citypicker close
        print(" 1 - ситипикер закрыли ")
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "//*[@class='button__inner cookie-usage-notice__button-inner--desktop']"))).click()  # close cookie

        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//span[contains(.,'Войти')]"))).click()

        driver.get("https://stage.lentatest.com/catalog/hlebobulochnye-izdeliya/")


        print(" 2 - В корзину ")
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'В корзину')]"))).click()

        time.sleep(2)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@href='/-ecom/basket/']"))).click()
        time.sleep(2)


        print(" 3 - Вход / Регистрация ")
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//span[contains(.,'Продолжить оформление')]"))).click()

        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.LINK_TEXT, "Регистрация"))).click()  # кнопка-ссылка Регистрация

        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "phone"))).click()

        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "phone"))).send_keys("9" + str(string_d))


        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Далее')]"))).click()
        print(" 3 - Вводим код")
        # -------------code-------
        time.sleep(2)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "(//*[@type='number'])[1]"))).send_keys("0")
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "(//*[@type='number'])[2]"))).send_keys("0")
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "(//*[@type='number'])[3]"))).send_keys("0")
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "(//*[@type='number'])[4]"))).send_keys("0")

        time.sleep(2)

        # -------------code-------

        # -----------random2--------
        def generate_random_string_2(length_2=9):
            letters2 = 'йцукенгшщзхфывапролджэячсмитьбюЫВАПРОЛЙЦУКЕНГШЩЗСМИТЬБЮ'
            rand_string2 = ''.join(random.choice(letters2) for i in range(length_2))
            return rand_string2

        generate_random_string_2()

        string_s = generate_random_string_2()


        # -----------random2-------

        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Подтвердить')]"))).click()
        #
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.CLASS_NAME, "registration__card-link-create"))).click()

        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "(.//*[normalize-space(text()) and normalize-space(.)='Заполните недостающие данные'])[1]/following::div[7]"))).click()
        print(" 4 - Заполните недостающие данные")
        # -----------RANDOM for name
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "lastName"))).send_keys(string_s)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "firstName"))).send_keys(string_s)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "patronymic"))).send_keys(string_s)
        # ----------RANDOM for name

        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "emailAddress"))).click()  # mail
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "emailAddress"))).send_keys(string_d + "@asd.tr")  # mail send

        # ---------- gender
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "(.//*[normalize-space(text()) and normalize-space(.)='Пол *'])[1]/following::*[name()='svg'][1]"))).click()  # gender
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "(.//*[normalize-space(text()) and normalize-space(.)='Женский'])[1]/following::span[1]"))).click()  # gender

        # --------------datapicker
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "dateOfBirth"))).click()  # date of birth
        time.sleep(1)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "dateOfBirth"))).send_keys("\b\b\b\b\b\b\b\b\b\b")  # date of birth space

        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "dateOfBirth"))).send_keys("17 11 2000")  # date of birth
        time.sleep(1)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.NAME, "dateOfBirth"))).send_keys(Keys.ENTER)  # date of birth
        time.sleep(1)
        # --------------datapicker


        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Продолжить')]"))).click()

        # print(" 5 - Придумайте новый пароль согласно требованиям")
        # # -----------pass
        #
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH,
        #      "(.//*[normalize-space(text()) and normalize-space(.)='Придумайте новый пароль согласно требованиям'])[1]/following::div[7]"))).click()
        # string_p = "!Qwe" + string_d  # value pass
        #
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.NAME, "password"))).send_keys(string_p)
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.NAME, "confirmedPassword"))).send_keys(string_p)
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, "//button[contains(.,'Подтвердить')]"))).click()
        #
        # # -----------pass

        # -----------select

        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "(//div[@class='category-loyalty__container'])[1]"))).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "(//div[@class='category-loyalty__container'])[3]"))).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "(//div[@class='category-loyalty__container'])[5]"))).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "(//div[@class='category-loyalty__container'])[7]"))).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "(//div[@class='category-loyalty__container'])[9]"))).click()
        time.sleep(2)
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(.,'Выбрать категории')]"))).click()

        print(" 6 - Выбрать категории")
        time.sleep(5)
        # -----------select

        # # -----------club
        #
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH,
        #      "/html/body/div[1]/div[1]/div/main/div/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div"))).click()  # first club
        # time.sleep(2)
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH,
        #      "/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[2]/button/span"))).click()  # approve first club
        # time.sleep(2)
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH,
        #      "/html/body/div[1]/div[1]/div/main/div/div[1]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[2]/div"))).click()  # second club
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH,
        #      "/html/body/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[4]/div/form/div[2]/div[1]/div/div[1]/div/div/input"))).send_keys(
        #     "ИмяРебенка")
        #
        # # --------------datapicker
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.NAME, "children[0].dateOfBirth"))).click()  # date of birth
        # time.sleep(1)
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.NAME, "children[0].dateOfBirth"))).send_keys("17 11 2015")  # date of birth
        # time.sleep(1)
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.NAME, "children[0].dateOfBirth"))).send_keys(Keys.ENTER)  # date of birth
        # time.sleep(1)
        # # --------------datapicker
        #
        #
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH,
        #      "/html/body/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[4]/div/form/div[2]/div[3]/div/div/label[1]/span"))).click()  # gender
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH,
        #      "/html/body/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[4]/div/form/div[3]/div/button/span"))).click()  # check box approve
        # WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, "//button[contains(.,'Вступить')]"))).click()  # approve second club

        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Продолжить')]"))).click()

        # -----------club
        print(" 7 - второй ситипикер")
        # ----------citypicker

        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='close-control']"))).click()  # ----------citypicker close

        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.CLASS_NAME, "popup__close"))).click()  # confirmation mail
        time.sleep(2)
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.CLASS_NAME, "popup__close"))).click()  # bonus
        time.sleep(2)
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//span[@class='header__profile-name-text']"))).click()  # profile

        print(" 8 - выходим из профиля")


        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
            (By.LINK_TEXT, "Выйти"))).click()

        print("--------------------------------------------------------------------------------------test 28 successful")
        #


        def log(message):
            print(message)