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
    shifts_registration_after_approve = (By.XPATH, "//*[contains(@data-test ,'disallow-button')]")
    shifts_registration_move_to_doc = (By.XPATH, "//*[contains(@href ,'/documents')]")
    shifts_registration_andes = (By.XPATH, "//*[contains(@class ,'v-btn__content')]")
    shifts_registration_andes_next = (By.XPATH, "(//*[contains(@class ,'v-btn__content')])[2]")
    shifts_registration_btn_close = (By.XPATH, "//*[contains(@data-test,'message-close')]")
    shifts_registration_type_numder = (By.XPATH, "//*[contains(@type ,'number')]")
    shifts_registration_type_text = (By.XPATH, "//input[contains(@type ,'text')]")
    shifts_registration_type_button = (By.XPATH, "//input[contains(@type ,'text')]")
    shifts_registration_button_after_reg = (By.XPATH, "//button[contains(@class ,'v-step__button')]")
    shifts_filter = (By.XPATH, "//*[contains(@data-test ,'filter-button')]")
    shifts_filter_next = (By.XPATH, "//*[contains(@data-test ,'next-button')]")
    shifts_filter_prev = (By.XPATH, "//*[contains(@data-test ,'prev-button')]")
    shifts_filter_apply = (By.XPATH, "//*[contains(@data-test ,'apply')]")
    shifts_filter_day_present = (By.XPATH, "//*[contains(@class ,'v-calendar-weekly__day v-present')]")
    shifts_filter_day_work = (By.XPATH, "(//*[contains(@class ,'v-calendar-weekly__day-label')]//following-sibling::div)[1]")
    shifts_filter_get = (By.XPATH, "//*[contains(@class,'cursor-pointer px-3 pt-3')]")
    shifts_filter_close_first = (By.XPATH, "//*[contains(@data-test,'close-button')]")
    shifts_filter_open_first = (By.XPATH, "//*[contains(@data-test,'ok-button')]")
    shifts_filter_open_first_chip = (By.XPATH, "//*[@class='app-chip__text'][contains(.,'Моя смена')]")
    shifts_filter_avatar = (By.XPATH, "//*[@data-test='user']")
    shifts_admin_quee = (By.XPATH, "//*[@href='/admin/notifications/notifyitem/']")





class verme_create(AnyPage):

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

    @allure.step('Выбираем дату рождения -  {data}, {month}, {day} при регистрации')
    def click_shifts_registration_data(self, data, month, day, nm):
        first = (By.XPATH, f"(//*[contains(@class ,'vi-calendar')])[{nm}]")
        self.click_element_my(first)
        el = (By.XPATH, f"//*[contains(@class ,'v-date-picker-years')]//*[contains(.,'{data}')]")
        self.click_element_my(el)
        el_1 = (By.XPATH, f"//*[contains(@class ,'v-btn__content')][contains(.,'{month}')]")
        self.click_element_my(el_1)
        el_2 = (By.XPATH, f"//*[contains(@class ,'v-btn__content')][contains(.,'{day}')]")
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
        self.send_keys(el, "E:\\pvp-at\\02.jpg")
        time.sleep(3)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть согласие при регистрации')
    def click_shifts_approve(self):
        time.sleep(3)
        self.click_element_my(Locator.shifts_registration_approve)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть модальное окно')
    def click_shifts_after_approve(self):
        time.sleep(1)
        self.click_element_my(Locator.shifts_registration_after_approve)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть модальное окно - документы')
    def click_shifts_move_to_documents(self):
        self.click_element_my(Locator.shifts_registration_move_to_doc)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку на модальном окне')
    def click_shifts_andes(self):
        self.click_element_my(Locator.shifts_registration_andes)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку - {txt}')
    def click_shifts_btn_content(self, txt):
        el = (By.XPATH, f"//*[contains(@class ,'v-btn__content')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Закрыть сообщение')
    def click_shifts_btn_close(self):
        self.click_element_my(Locator.shifts_registration_btn_close)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку - добавить документ')
    def click_shifts_add_doc(self, txt):
        el = (By.XPATH, f"(//*[contains(@data-test ,'new-document-button')])[{txt}]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку - добавить банк')
    def click_shifts_add_bank(self, txt_1, txt_3):
        el = (By.XPATH, "//*[contains(@role ,'combobox')]")
        self.click_element_my(el)
        el_1 = (By.XPATH, "//*[contains(@type ,'number')]")
        self.send_keys(el_1, txt_1)
        time.sleep(3)
        el_2 = (By.XPATH, "//*[contains(@class ,'v-list--dense theme--light')]")
        self.click_element_my(el_2)
        el_3 = (By.XPATH, "(//*[contains(@type ,'number')])[2]")
        self.send_keys(el_3, txt_3)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку - добавить ИНН')
    def click_shifts_add_inn(self, txt):

        self.click_element_my(Locator.shifts_registration_type_numder)
        self.send_keys(Locator.shifts_registration_type_numder, txt)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку - добавить медицинскую книжку')
    def click_shifts_add_med(self, txt):

        self.click_element_my(Locator.shifts_registration_type_numder)
        self.send_keys(Locator.shifts_registration_type_numder, txt)
        self.allure_screenshot()

        return self

    @allure.step('Выбираем период действия  медкнижки при регистрации')
    def click_shifts_registration_med_data(self,  day, nm, nm_2):
        first = (By.XPATH, f"(//*[contains(@class ,'vi-calendar')])[{nm}]")
        self.click_element_my(first)
        el_2 = (By.XPATH, f"//*[contains(@class ,'v-btn__content')][contains(.,'{day}')]")
        self.click_element_my(el_2)
        second = (By.XPATH, f"(//*[contains(@class ,'vi-calendar')])[{nm_2}]")
        self.click_element_my(second)
        el_3 = (By.XPATH, "//*[contains(@class ,'v-btn__content')]//*[contains(@class ,'vi-angle-right')]")
        self.click_element_my(el_3)
        self.click_element_my(el_3)
        self.click_element_my(el_3)
        time.sleep(2)
        el_4 = (By.XPATH, f"//*[contains(@class ,'v-btn__content')][contains(.,'{day}')]")
        self.click_element_my(el_4)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку на модальном окне')
    def click_shifts_andes_all(self, txt):
        self.click_element_my(Locator.shifts_registration_andes_next)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку - добавить паспорт')
    def click_shifts_add_passport(self, txt):

        self.click_element_my(Locator.shifts_registration_type_text)
        self.send_keys(Locator.shifts_registration_type_text, txt)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку - добавить терапевта')
    def click_shifts_add_therapist(self):
        first = (By.XPATH, "//button[contains(@class ,'vi-calendar')]")
        self.click_element_my(first)
        el = (By.XPATH, "//*[contains(@class ,'theme--light primary--text')]")
        self.click_element_my(el)

        self.allure_screenshot()

        return self

    @allure.step('После регистрации кликнуть кнопку - понятно')
    def click_shifts_after_reg(self):
        self.click_element_my(Locator.shifts_registration_button_after_reg)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку смена - фильтр')
    def click_shifts_filter(self):
        self.click_element_my(Locator.shifts_filter)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку смена - фильтр следующий месяц')
    def click_shifts_filter_next(self):
        self.click_element_my(Locator.shifts_filter_next)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть кнопку смена - фильтр предыдущий месяц')
    def click_shifts_filter_prev(self):
        self.click_element_my(Locator.shifts_filter_prev)
        self.allure_screenshot()

        return self

    @allure.step('Работа с фильтром ')
    def send_shifts_filter_data(self, txt):
        el = (By.XPATH, f"(//*[contains(@role ,'combobox')])[{txt}]")
        self.click_element_my(el)
        el_1 = (By.XPATH, "(//*[contains(@class ,'d-flex flex-column py-1')])[1]")
        self.click_element_my(el_1)
        self.allure_screenshot()

        return self



    @allure.step('Кликнуть кнопку apply')
    def click_shifts_filter_apply(self):
        self.click_element_my(Locator.shifts_filter_apply)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть сегодняшний день')
    def click_shifts_day_present(self):
        self.click_element_my(Locator.shifts_filter_day_present)
        self.allure_screenshot()

        return self

    @allure.step('Кликнуть смену')
    def click_shifts_day_work(self) -> str:
        el = self.get_tag_attribute(Locator.shifts_filter_day_work , "data-date")
        d = el[8:10]
        self.allure_screenshot()

        return d

    @allure.step('Кликнуть - {txt}')
    def click_shifts_title(self, txt):
        el = (By.XPATH, f"//*[contains(@class,'text-description')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Выбрать смену')
    def get_shifts_first(self):
        self.click_element_my(Locator.shifts_filter_get)
        self.allure_screenshot()

        return self

    @allure.step('Выбрать -  закрыть смену')
    def get_shifts_first_close(self):
        self.click_element_my(Locator.shifts_filter_close_first)
        self.allure_screenshot()

        return self

    @allure.step('Выбрать - принять смену')
    def get_shifts_first_open(self):
        self.click_element_my(Locator.shifts_filter_open_first)
        self.allure_screenshot()

        return self

    @allure.step('Выбрать - {txt} ')
    def get_shifts_first_open_chip(self, txt, txt_1):
        el = (By.XPATH, f"//*[@class='app-chip__text'][contains(.,'{txt}')]")
        self.click_element_my(el)
        time.sleep(3)
        el_1 = (By.XPATH, f"//*[@class='app-chip__text'][contains(.,'{txt_1}')]")
        fin = self.get_text_my(el_1)
        print(fin)
        self.allure_screenshot()

        return self

    @allure.step('Выбрать - {txt} ')
    def get_shifts_click_field(self, txt):
        el = (By.XPATH, f"//*[@role='tab'][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Проверяем - {txt} ')
    def get_shifts_phone_compare(self, txt):
        el = (By.XPATH, "//*[@class='text--base']")
        fin = self.get_text_my(el)
        time.sleep(1)
        assert txt == fin, 'Телефон не корректен'
        self.allure_screenshot()

        return self

    @allure.step('Кликаем аватар')
    def shifts_click_avatar(self):
        self.click_element_my(Locator.shifts_filter_avatar)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем - очередь оповещений')
    def shifts_click_quee(self):
        self.click_element_my(Locator.shifts_admin_quee)
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




