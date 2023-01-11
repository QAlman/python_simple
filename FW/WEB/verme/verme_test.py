import math
import time
import requests
import allure
from selenium.webdriver.common.by import By
from FW.WEB.AnyPage import AnyPage


class Locator:
    file = "01.jpg"
    sms_url = "https://outsourcing-dev.verme.ru/admin/notifications/notifyitem/"
    verme_url = "https://outsourcing-dev.verme.ru/auth/login/"
    shifts_dev_url = "https://shifts-dev.verme.ru/auth"

    login_verme = (By.XPATH, "//input[@type='text']")
    password_verme = (By.XPATH, "//input[@type='password']")
    login_signin = (By.XPATH, "//*[contains(@class ,'btn-primary')]")
    login_button_verme  = (By.XPATH, "//*[contains(@href ,'/saml/begin?idp=vermelogin&next=')]")
    login_field_verme = (By.XPATH, "//input[@id='userNameInput']")
    password_field_verme = (By.XPATH, "//input[@id='passwordInput']")
    login_button_signin = (By.XPATH, "//span[@id='submitButton']")

    shifts_next = (By.XPATH, "//*[contains(@data-test ,'next-button')]")
    shifts_done = (By.XPATH, "//*[contains(@data-test ,'done-button')]")
    shifts_phone = (By.XPATH, "//*[contains(@class ,'v-text-field__slot')][contains(.,'Номер телефона')]")
    shifts_phone_send = (By.XPATH, "(//*[contains(@id ,'input-')])[1]")
    shifts_call_phone = (By.XPATH, "//*[contains(@class ,'v-input__append-outer')]")
    celery_button_signin = (By.XPATH, "//input[@type='submit']")

    shifts_registration_calendar = (By.XPATH, "//*[contains(@class ,'vi-calendar')]")
    shifts_registration_next = (By.XPATH, "//*[contains(@class ,'vi-calendar')]")
    shifts_registration_approve = (By.XPATH, "//*[contains(@data-test ,'license-agreement-button')]")


class verme_create(AnyPage):

    @allure.step('Передаем   Login')
    def send_login(self, txt):
        self.send_keys_slow(Locator.login_verme, txt, 100)
        self.allure_screenshot()

        return self

    @allure.step('Передаем   Password')
    def send_password(self, txt):
        self.send_keys_slow(Locator.password_verme, txt, 100)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем Войти')
    def click_signin(self):
        self.click_element_my(Locator.login_signin)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем войти с помощью Verme Login')
    def click_vermelogin(self):
        self.click_element_my(Locator.login_button_verme)
        self.allure_screenshot()

        return self

    @allure.step('Передаем  Verme Login')
    def send_vermelogin(self, txt):
        self.send_keys_slow(Locator.login_field_verme, txt, 100)
        self.allure_screenshot()

        return self

    @allure.step('Передаем  Verme Password')
    def send_vermepassword(self, txt):
        self.send_keys_slow(Locator.password_field_verme, txt, 100)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем Sign in')
    def click_vermesignin(self):
        self.click_element_my(Locator.login_button_signin)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем Далее')
    def click_shifts_next(self):
        self.click_element_my(Locator.shifts_next)
        time.sleep(1)
        self.click_element_my(Locator.shifts_next)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем Приступим')
    def click_shifts_done(self):
        self.click_element_my(Locator.shifts_done)
        self.allure_screenshot()

        return self


    @allure.step('Кликаем поле-  телефон')
    def click_shifts_phone(self):
        self.click_element_my(Locator.shifts_phone)
        self.allure_screenshot()

        return self

    @allure.step('Передаем телефон  {txt}')
    def send_shifts_phone(self, txt):
        #self.send_keys_slow(Locator.shifts_phone_send, str(9) + txt, 100)
        self.send_keys(Locator.shifts_phone_send, str(9) + txt)
        self.allure_screenshot()

        return self


    @allure.step('Кликаем  - вызов')
    def click_shifts_call(self):
        self.click_element_my(Locator.shifts_call_phone)
        self.allure_screenshot()

        return self

    @allure.step('Отправляем 4 значения кода смс')
    def send_sms_code_phone_4(self, txt):
        phone_code_1 = (By.XPATH, "(//*[@type='tel'])[1]")
        phone_code_2 = (By.XPATH, "(//*[@type='tel'])[2]")
        phone_code_3 = (By.XPATH, "(//*[@type='tel'])[3]")
        phone_code_4 = (By.XPATH, "(//*[@type='tel'])[4]")

        self.send_keys(phone_code_1, txt[1:2])
        self.send_keys(phone_code_2, txt[2:3])
        self.send_keys(phone_code_3, txt[3:4])
        self.send_keys(phone_code_4, txt[4:5])
        self.allure_screenshot()
        return self

    @allure.step('Переходим в celery ')
    def goto_celery_page(self):
        time.sleep(1)
        self.open_new_tab(Locator.sms_url)
        self.switch_to_tab()
        self.allure_screenshot()

        return self

    @allure.step('Кликаем Войти')
    def click_signin_celery(self):
        self.click_element_my(Locator.celery_button_signin)
        self.allure_screenshot()

        return self
    @allure.step('Кликаем номер телефона {txt}')
    def click_phone_celery(self, txt):
        el = (By.XPATH, f"//*[contains(@href ,'change/?_changelist_filters=q%3D{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Забираем текст SMS')
    def get_text_sms(self):
        time.sleep(3)
        el = (By.XPATH, "(//span[contains(@class ,'ace_string')])[2]")
        txt = self.get_tag_text(el)

        return txt

    @allure.step('Возврат в shifts ')
    def return_shifts_page(self):
        time.sleep(1)
        self.return_to_tab()
        self.allure_screenshot()

        return self


    @allure.step('Отправляем {txt} - {txt_1}  на регистрацию')
    def send_shifts_registration_txt(self, txt, txt_1, txt_2):
        time.sleep(1)
        el = (By.XPATH, f"//*[contains(@class ,'v-input__slot')][contains(.,'{txt}')]")
        self.click_element_my(el)
        el_2 = (By.XPATH, f"//*[contains(@id,'input-{txt_2}')]")
        self.send_keys(el_2, txt_1)

        self.allure_screenshot()

        return self

    @allure.step('Выбираем  {txt} при регистрации')
    def click_shifts_registration_btn(self, txt):
        el = (By.XPATH, f"//*[contains(@class ,'v-btn__content')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Выбираем дату рождения -  {txt}, {txt_1}, {txt_2} при регистрации')
    def click_shifts_registration_data(self, txt, txt_1, txt_2):
        self.click_element_my(Locator.shifts_registration_calendar)
        el = (By.XPATH, f"//*[contains(@class ,'v-date-picker-years')]//*[contains(.,'{txt}')]")
        self.click_element_my(el)
        el_1 = (By.XPATH, f"//*[contains(@class ,'v-btn__content')][contains(.,'{txt_1}')]")
        self.click_element_my(el_1)
        el_2 = (By.XPATH, f"//*[contains(@class ,'v-btn__content')][contains(.,'{txt_2}')]")
        self.click_element_my(el_2)

        self.allure_screenshot()

        return self


    @allure.step('Выбираем гражданство -  {txt} при регистрации')
    def click_shifts_registration_country(self, txt, txt_1):

        el = (By.XPATH, f"//*[contains(@class ,'v-select__slot')][contains(.,'{txt}')]")
        self.click_element_my(el)
        el_1 = (By.XPATH, f"//*[contains(@class ,'text-body')][contains(.,'{txt_1}')]")
        self.click_element_my(el_1)

        self.allure_screenshot()

        return self

    @allure.step('Выбираем местонахождение -  {txt_2} при регистрации')
    def click_shifts_registration_slot(self, txt, txt_1, txt_2):

        el = (By.XPATH, f"//*[contains(@class ,'v-select__slot')][contains(.,'{txt}')]")
        self.click_element_my(el)
        el_1 = (By.XPATH, f"//*[contains(@id ,'input-{txt_1}')]")
        self.send_keys(el_1, txt_2)
        el_3 = (By.XPATH, f"//*[contains(@class ,'py-1 text-body')][contains(. ,'{txt_2}')]")
        self.click_element_my(el_3)
        self.allure_screenshot()

        return self

    @allure.step('Выбираем регион -  {txt_1} при регистрации')
    def click_shifts_registration_region(self, txt, txt_1):

        el = (By.XPATH, f"//*[contains(@class ,'v-select__slot')][contains(.,'{txt}')]")
        self.click_element_my(el)
        el_1 = (By.XPATH, f"//*[contains(@class ,'v-list-item__title')][contains(.,'{txt_1}')]")
        self.click_element_my(el_1)
        self.allure_screenshot()

        return self

    @allure.step('Загрузить фото при регистрации')
    def send_photo_shifts(self):
        el = (By.XPATH, "//*[contains(@type ,'file')][contains(@accept,'image/*')]")
        self.send_keys(el, "E:\\pvp-at\\01.jpg")
        time.sleep(3)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть согласие при регистрации')
    def click_shifts_approve(self):
        time.sleep(3)
        self.click_element_my(Locator.shifts_registration_approve)
        self.allure_screenshot()

        return self


    #
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
    # @allure.step('Перемещаемся к выбору производителя')
    # def move_to_enterprise(self):
    #     self.move_to_element(Locator.enterprise_field)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Выбираем бренд {txt}')
    # def select_brand_all(self, txt):
    #     el = (By.XPATH, f"//span[@class='checkbox-field__label'][contains(.,'{txt}')]")
    #     self.click_element_my(el)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Проверяем текст бренда {txt} на странице товара')
    # def check_select_brand_all(self, txt):
    #     el = (By.XPATH, f"//h1[@class='catalog-view__title'][contains(.,'{txt}')]")
    #     # k = txt_brand.casefold()[:-1]
    #     txt_cart = self.get_text_my(el)
    #     # r = txt_cart.casefold()
    #     assert txt in txt_cart, "Текст бренда на странице товара не найден"
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Выбираем {txt}')
    # def select_actions(self, txt):
    #     ur = (By.XPATH, f"//*[@ga-event-label='{txt}']")
    #     self.click_element_my(ur)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Выбрать доставку {address_market} в {city}')
    # def select_address_delivery_any(self, address_market, city, txt):
    #     self.click_element_my(Locator.select_delivery)
    #     time.sleep(2)
    #     self.click_element_my(Locator.select_city)
    #     select_city_sample = (By.XPATH, f"//span[@class='cities-list-item__name'][contains(.,'{city}')]")
    #     self.click_element_my(select_city_sample)
    #     time.sleep(2)
    #     self.click_element_my(Locator.select_delivery_only)
    #     # time.sleep(1)
    #     switch_select_market_2 = (By.XPATH, f"(//*[@class='input-field__control input-field__control--native'])[{txt}]")
    #     self.click_element_my(switch_select_market_2)
    #     # time.sleep(1)
    #     self.send_keys_slow(switch_select_market_2, "zov", 100)
    #     # time.sleep(1)
    #     self.send_keys_backspase(switch_select_market_2)
    #     # time.sleep(1)
    #     self.send_keys_backspase(switch_select_market_2)
    #     # time.sleep(1)
    #     self.send_keys_delete(switch_select_market_2)
    #     # time.sleep(1)
    #     self.click_element_my(switch_select_market_2)
    #     self.send_keys_slow(switch_select_market_2, address_market, 100)
    #     self.allure_screenshot()
    #     select_address_sample = (By.XPATH, f"//li[@class='auto-suggest-field__suggestion'][text()='{address_market}']")
    #     # time.sleep(2)
    #     self.click_element_my(select_address_sample)
    #     time.sleep(2)
    #     self.click_element_my(Locator.select_market_final_2)
    #     # time.sleep(7)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Забираем данные из карточки')
    # def get_items_one(self, txt):
    #     el = self.get_text_my(Locator.get_items_cart_one)
    #     print(el)
    #     assert txt == el, "Сортировка не верная"
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Заполнить блок личных даных')
    # def send_family(self, txt, txt_n):
    #     # self.click_element_my(Locator.family_field)
    #     # self.send_keys_slow(Locator.family_field_last_name, txt, 100)
    #     self.send_keys_slow(Locator.family_field_first_name, txt, 100)
    #     # self.send_keys_slow(Locator.family_field_patronymic_name, txt, 100)
    #     # self.click_element_my(Locator.family_field_mail)
    #     # self.send_keys_slow(Locator.family_field_mail, txt_n + "@asd.tr", 100)
    #     # self.click_element_my(Locator.family_field_gender)
    #     # self.click_element_my(Locator.family_field_gender_f)
    #     self.click_element_my(Locator.family_field_data)
    #     self.send_keys(Locator.family_field_data, Locator.blank + Locator.blank)
    #     self.send_keys_slow(Locator.family_field_data, "17 11 2000", 100)
    #     self.send_keys_enter(Locator.family_field_data)
    #     self.click_element_my(Locator.family_field_mail)
    #     self.send_keys_slow(Locator.family_field_mail, txt_n + "@asd.tr", 100)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Добавить товары в корзину 101869 1шт ,084250 1кг')
    # def add_basket(self):
    #     self.goto_page(Locator.ecom_url_34)
    #     time.sleep(3)
    #     self.click_element_my(Locator.add_basket_big)
    #     time.sleep(5)
    #     self.allure_screenshot()
    #     self.goto_page(Locator.ecom_url_34_1)
    #     time.sleep(3)
    #     self.click_element_my(Locator.add_basket_big)
    #     time.sleep(5)
    #     self.allure_screenshot()
    #     self.click_element_my(Locator.rise_item)
    #     self.send_keys(Locator.rise_item, Locator.blank)
    #     time.sleep(1)
    #     self.send_keys(Locator.rise_item, "1")
    #     time.sleep(1)
    #     self.send_keys_enter(Locator.rise_item)
    #     time.sleep(2)
    #     self.click_element_my(Locator.move_to_basket)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Ввести промокод vp97picq (вы получили скидку 40%)')
    # def add_promocode(self, promo):
    #     self.click_element_my(Locator.field_promo)
    #     self.send_keys_slow(Locator.field_promo, promo, 100)
    #     self.allure_screenshot()
    #
    #     return self
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
    # def check_price_basket(self, txt):
    #     el = self.get_text_my(Locator.promo_get_price_final)
    #     assert el == txt, "Цена не соответствует цене на корзине"
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
    # @allure.step('Удаляем {txt}')
    # def click_button_delete(self, txt):
    #     el = (By.XPATH, f"(//*[contains(@class ,'custom-sku-in-favourites__button-text')])[{txt}]")
    #     self.click_element_my(el)
    #     self.allure_screenshot()
    #
    #     return self




