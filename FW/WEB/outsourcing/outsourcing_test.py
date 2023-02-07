import math
import time
from typing import Type
import datetime
import requests
import os.path
import allure
from selenium.webdriver.common.by import By
from FW.WEB.AnyPage import AnyPage
from selenium.webdriver.common.keys import Keys


class Locator:
    file = "01.jpg"
    sms_url = "https://outsourcing-dev.verme.ru/admin/notifications/notifyitem/"
    verme_url = "https://outsourcing-dev.verme.ru/auth/login/"
    # shifts_dev_url = "https://shifts-dev.verme.ru/auth"

    outsourcing_employees = "https://outsourcing-dev.verme.ru/agency-employees-list/"
    outsourcing_supervisors = "https://outsourcing-dev.verme.ru/employees/supervisors/agency/"
    outsourcing_outsource_schedule = "https://outsourcing-dev.verme.ru/outsource-schedule/"

    login_verme = (By.XPATH, "//input[@type='text']")
    password_verme = (By.XPATH, "//input[@type='password']")
    login_signin = (By.XPATH, "//*[contains(@class ,'btn-primary')]")

    # shifts_filter_day_work = (By.XPATH, "(//*[contains(@class ,'v-calendar-weekly__day-label')]//following-sibling::div)[1]")


    outsourcing_pagination = (By.XPATH, "//*[@class='pagination__select custom-select']")
    outsourcing_pagination_value = (By.XPATH, "//option[contains(@value,'20')]")
    outsourcing_sort_fio = (By.XPATH, "//*[contains(@aria-colindex,'2')][contains(@class,'b-table-sort-icon-lef')]")
    outsourcing_toolbar = (By.XPATH, "//*[contains(@class,'card-toolbar')]")
    outsourcing_btn_menu = (By.XPATH, "//*[contains(@class,'dropdown b-dropdown btn-group')]")
    outsourcing_btn_download = (By.XPATH, "//*[contains(@class,'la-file-download icon-2x')]")
    outsourcing_btn_tabels = (By.XPATH, "//span[contains(@class,'navi-text font-size-lg')][contains(.,'Табели')]")

    to_file = '01.jpg'






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

    @allure.step('Кликаем на - к-во отображенных элементов на странице')
    def outsourcing_click_pagination(self):
        self.click_element_my(Locator.outsourcing_pagination)

        self.allure_screenshot()

        return self
    @allure.step('Выбираем к-во отображенных эдементов на странице -  {txt}')
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

    @allure.step('Кликаем  поле - {txt}')
    def outsourcing_click_row(self, txt):
        el = (By.XPATH, f"(//td[contains(@role,'cell')])[{txt}]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Переходим на - {txt}')
    def goto_employees_all_page(self, txt):
        self.goto_page(txt)
        time.sleep(1)
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

    @allure.step('Кликаем сортировку')
    def click_sort_all(self, txt, txt_1):
        el = (By.XPATH, f"(//*[contains(@aria-colindex,'{txt}')])[{txt_1}]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Проверяем сортировку для {txt_1}')
    def check_sort_fio(self, txt, txt_1) -> Type[str]:
        el = (By.XPATH, f"(//*[contains(@class,'text-wrap')])[{txt}]")
        fin = self.get_text_my(el)
        assert fin[:1] == txt_1
        self.allure_screenshot()

        return fin

    @allure.step('Проверяем сортировку')
    def check_sort_all(self, txt) -> Type[str]:
        el = (By.XPATH, f"(//*[contains(@aria-sort,'none')])[{txt}]")
        fin = self.get_text_my(el)
        #assert fin[:1] == txt_1
        self.allure_screenshot()

        return fin

    @allure.step('Выбираем  {txt}')
    def click_field_agency(self, txt, txt_1) -> Type[str]:
        el = (By.XPATH, "//input[contains(@class,'vue-treeselect__input')]")
        self.click_element_my(el)
        self.send_keys(el, txt)
        time.sleep(1)
        el_1 = (By.XPATH, f"(//*[contains(@class,'vue-treeselect__label')][contains(.,'{txt}')])[{txt_1}]")
        self.click_element_my(el_1)
        self.allure_screenshot()

        return self

    @allure.step('Выбираем смену в {txt}')
    def get_shifts_agency(self, txt, txt_1) -> Type[str]:

        el = (By.XPATH, f"(//*[contains(@class,'schedule__event')])[{txt}]")
        self.click_element_my(el)
        el_1 = (By.XPATH, "//*[contains(@class,'input-icon input-icon-right')]")
        self.click_element_my(el_1)
        time.sleep(1)
        el_2 = (By.XPATH, f"//*[contains(@class,'d-flex flex-column mb-1')][contains(.,'{txt_1}')]")
        self.click_element_my(el_2)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем - {txt}')
    def click_mutation(self, txt):
        el = (By.XPATH, f"//*[contains(@class,'ml-auto btn btn-sm btn-primary')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Проверяем изменения ')
    def check_mutation_(self):
        el = (By.XPATH, "//*[contains(@class,'schedule__event-wrap')]")
        el_1 = f"//*[contains(@class,'btn btn-sm btn-danger')][contains(.,' Удалить смену ')]"
        el_2 = (By.XPATH, "(//*[contains(@class,'app-modal__close')])[2]")

        k = Keys.ESCAPE
        fields = self.find_elements(el)
        for element in fields:
            self.click_element_my(el)
            time.sleep(1)
            #self.GetDriver().refresh()
            self.send_esc()
            # self.click_element_my_dp(el_1)


        self.allure_screenshot()

        return self

    @allure.step(' Добавляем смену ')
    def add_shifts_in_agency(self, txt, txt_1) -> Type[object]:
        el = (By.XPATH, f"(//*[contains(@data-zone,'work-area')])[{txt}]")
        self.click_element_my(el)
        el_1 = (By.XPATH, "//*[contains(@class,'input-icon input-icon-right')]")
        self.click_element_my(el_1)
        time.sleep(4)
        el_2 = (By.XPATH, f"//*[contains(@class,'d-flex flex-column mb-1')][contains(.,'{txt_1}')]")
        self.click_element_my(el_2)

        self.allure_screenshot()

        return object

    @allure.step(' Добавляем смену ')
    def add_shifts_in_agency_by_num(self, txt, txt_1) -> Type[object]:
        el = (By.XPATH, f"(//*[contains(@data-zone,'work-area')])[{txt}]")
        self.click_element_my(el)
        el_1 = (By.XPATH, "//*[contains(@class,'input-icon input-icon-right')]")
        self.click_element_my(el_1)
        time.sleep(2)
        el_2 = (By.XPATH, f"(//*[contains(@class,'list-item')])[{txt_1}]")
        self.click_element_my(el_2)

        self.allure_screenshot()

        return object

    @allure.step(' Добавляем смену ')
    def add_shifts_row_agency(self, txt, txt_1) -> Type[str]:
        el = (By.XPATH, f"(//*[contains(@data-zone,'row')])[{txt}]")
        self.click_element_my(el)
        el_1 = (By.XPATH, "//*[contains(@class,'input-icon input-icon-right')]")
        self.click_element_my(el_1)
        time.sleep(4)
        el_2 = (By.XPATH, f"//*[contains(@class,'d-flex flex-column mb-1')][contains(.,'{txt_1}')]")
        self.click_element_my(el_2)

        self.allure_screenshot()

        return self

    @allure.step(' Выбираем дату ')
    def click_datapicker(self, txt, txt_1, txt_2, txt_3):
        dp = (By.XPATH, "//*[contains(@class,'dropdown b-dropdown btn-group')]")
        self.click_element_my(dp)
        dp_1 = (By.XPATH, "//*[contains(@class,'datepicker-btn-current-year')]")
        self.click_element_my(dp_1)
        dp_2 = (By.XPATH, f"//*[contains(@data-year,'{txt}')]")
        self.click_element_my(dp_2)
        dp_3 = (By.XPATH, f"(//*[contains(@data-month,'{txt_1}')])[{txt_2}]")
        self.click_element_my(dp_3)
        dp_4 = (By.XPATH, f"(//*[contains(@class,'datepicker-week-number')])[{txt_3}]")
        self.click_element_my(dp_4)
        self.allure_screenshot()

        return self


    @allure.step(' Выбираем месяц ')
    def click_datapicker_month(self,txt_1, txt_2):
        dp = (By.XPATH, "//*[contains(@class,'dropdown b-dropdown btn-group')]")
        self.click_element_my(dp)
        dp_3 = (By.XPATH, f"(//*[contains(@data-month,'{txt_1}')])[{txt_2}]")
        self.click_element_my(dp_3)
        self.allure_screenshot()

        return self


    @allure.step('Проверяем и выполняем - {txt_1}')
    def check_mutation(self, txt, txt_1):
        el = "//*[contains(@class,'schedule__event-wrap')]"
        el_1 = f"//*[contains(@class,'btn btn-sm btn-danger')][contains(.,'{txt_1}')]"

        fin = self.get_count_elements_my(el)
        dp = fin + 1

        time.sleep(1)
        for x in range(-dp, -1):
            fv = x + 1
            self.click_element_my_dp(f"(//*[contains(@class,'schedule__event-wrap')])[{fv * -1}]")
            time.sleep(1)
            self.click_element_my_dp(el_1)
            time.sleep(1)
            # self.GetDriver().refresh()
            # time.sleep(1)
            # if x == 0:
            #     break
        self.allure_screenshot()

        return self


    @allure.step(' Кликаем  смену ')
    def click_shifts_in_agency(self, txt) -> Type[object]:
        el = (By.XPATH, f"(//*[contains(@data-zone,'work-area')])[{txt}]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step(' Кликаем  смену где {txt}')
    def click_shifts_in_shedule(self, txt) -> Type[object]:
        el = (By.XPATH, f"(//*[contains(@title,'{txt}')])[1]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step(' Кликаем  фильтр')
    def click_shifts_filter(self) -> Type[object]:
        el = (By.XPATH, "//*[contains(@class,'btn-text-dark-50')]")
        self.click_element_my(el)

        self.allure_screenshot()

        return self

    @allure.step(' Кликаем  редактировать сотрудника')
    def click_shifts_toolbar(self) -> Type[object]:
        self.click_element_my(Locator.outsourcing_toolbar)
        self.allure_screenshot()

        return object

    @allure.step(' Кликаем  {txt}')
    def click_textarea(self, txt) -> Type[object]:
        el = (By.XPATH, f"//*[contains(@placeholder,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return object

    @allure.step(' Передаем  {txt}')
    def send_textarea(self, txt, txt_1) -> Type[object]:
        el = (By.XPATH, f"//*[contains(@placeholder,'{txt}')]")
        self.send_keys(el, txt_1)
        self.allure_screenshot()

        return object

    @allure.step(' Передаем  {txt}')
    def send_bcs_textarea(self, txt) -> Type[object]:
        el = (By.XPATH, f"//*[contains(@placeholder,'{txt}')]")
        self.send_keys_backspase(el)
        self.allure_screenshot()

        return object

    @allure.step(' Кликаем  {txt}')
    def click_button(self, txt) -> Type[object]:
        el = (By.XPATH, f"//button[contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return object

    @allure.step(' Проверяем -  {txt}')
    def check_alert(self, txt) -> Type[object]:
        el = (By.XPATH, "//*[contains(@class,'invalid-feedback')]")
        fin = self.get_text_my(el)
        assert txt == fin, "Сообщение не корректно"
        self.allure_screenshot()

        return object

    @allure.step(' Кликаем-  {txt}')
    def click_list_status(self, txt) -> Type[object]:
        el = (By.XPATH, f"//*[contains(@class,'d-block')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return object

    @allure.step(' Выбираем  -  {txt}')
    def select_list_status(self, txt) -> Type[object]:
        el = (By.XPATH, f"//*[contains(@class,'list-item')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return object

    @allure.step('Проверяем отсутствие смен')
    def check_mutation_out(self) -> Type[object]:
        el = "//*[contains(@class,'schedule__event-wrap')]"
        fin = self.get_count_elements_my(el)
        assert fin < 1, "Смены присутствуют"
        self.allure_screenshot()

        return object

    @allure.step('Проверяем наличие смен')
    def check_mutation_on(self) -> Type[object]:
        el = "//*[contains(@class,'schedule__event-wrap')]"
        self.click_element_my_dp(el)
        fin = self.get_count_elements_my(el)
        assert fin >= 1, "Смены отсутствуют"
        self.allure_screenshot()

        return object


    @allure.step('Перемещаемся к элементу')
    def move_to_shifts_any(self, txt) -> Type[object]:
        el = "//*[contains(@class,'readonly')]"
        self.click_element_my_dp(el)
        self.send_page_down()
        time.sleep(1)
        self.move_to_element(txt)
        self.allure_screenshot()

        return object


    @allure.step('Удаляем все смены')
    def del_shifts_all(self, txt, txt_1) -> Type[object]:
        self.send_keys_my(txt, txt_1)
        self.allure_screenshot()

        return object

    @allure.step(' Кликаем  {txt}')
    def click_only_txt(self, txt, txt_1) -> Type[object]:
        el = (By.XPATH, f"//{txt}[contains(.,'{txt_1}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return object


    def datetime_only_data(self) -> str:
        x = datetime.datetime.now()
        date_time = datetime.datetime.today()
        sd = (date_time.strftime('%H:%M'))
        date_day = datetime.date.today()
        dd = date_day.day
        date = x.strftime("%m.%Y")
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        month, year = date.split('.')

        fin = f'{months[int(month) - 1]} {year} г.'
        full = str(dd) + " " + str(fin) + " " + str(sd)

        return full

    def datetime_only_time(self, txt, txt_1) -> str:
        date = datetime.datetime.today()
        sd = (date.strftime('%H:%M'))

        return sd

    @allure.step(' Проверяем выгрузку excel - {txt}')
    def check_excel_ui(self, txt, txt_1, txt_2, txt_3) -> Type[object]:
        el = (By.XPATH, f"(//*[contains(@class,'field-headquarter nowrap')])[1]")
        el_1 = (By.XPATH, f"(//*[contains(@class,'field-user nowrap')])[1]")
        el_2 = (By.XPATH, f"(//*[contains(@class,'field-show_status')])[1]")
        el_3 = (By.XPATH, f"(//*[contains(@class,'field-dt_created nowrap')])[1]")

        fin = self.get_text_my(el)
        fin_1 = self.get_text_my(el_1)
        fin_2 = self.get_text_my(el_2)
        fin_3 = self.get_text_my(el_3)

        assert txt == fin , "Отчет не создан"
        # assert txt_1 == fin_1, "Отчет не создан"
        assert txt_2 == fin_2, "Отчет не создан"
        assert txt_3 == fin_3, "Отчет не создан"
        print(fin_3)
        print(txt_3)

        self.allure_screenshot()

        return object

    @allure.step('Кликаем кнопку меню')
    def click_only_menu(self) -> Type[object]:
        self.click_element_my(Locator.outsourcing_btn_menu)
        self.allure_screenshot()

        return object

    @allure.step('Заполняем данные пользователя')
    def agency_create_employee(self):

        fd = self.string_letters
        time.sleep(1)
        rs = str(fd)
        fn = self.string_d
        f_tel = str(fn)
        el_3 = (By.XPATH, f"(//*[contains(@type,'text')])[3]")
        el_4 = (By.XPATH, f"(//*[contains(@type,'text')])[4]")
        el_5 = (By.XPATH, f"(//*[contains(@type,'text')])[5]")
        el_6 = (By.XPATH, f"(//*[contains(@type,'text')])[6]")
        el_7 = (By.XPATH, f"(//*[contains(@type,'text')])[7]")
        el_8 = (By.XPATH, f"(//*[contains(@type,'text')])[8]")
        el_9 = (By.XPATH, f"(//*[contains(@type,'text')])[9]")
        el_tel = (By.XPATH, "//*[contains(@type,'tel')]")

        self.send_keys(el_3, rs)
        self.send_keys(el_4, rs)
        self.send_keys(el_5, rs)
        self.send_keys(el_6, rs)
        self.click_element_my(el_7)
        self.send_keys(el_7, "01.01.2000")
        self.send_keys(el_8, rs)
        self.send_keys(el_9, rs)
        self.send_keys(el_tel, "+7 9" + str(f_tel))

        self.allure_screenshot()

        return self


    @allure.step('Редактируем данные пользователя')
    def agency_edit_employee(self):

        fd = self.string_letters
        time.sleep(1)
        rs = str(fd)
        fn = self.string_d
        f_tel = str(fn)
        # el_3 = (By.XPATH, f"(//*[contains(@type,'text')])[3]")
        el_4 = (By.XPATH, f"(//*[contains(@type,'text')])[4]")
        el_5 = (By.XPATH, f"(//*[contains(@type,'text')])[5]")
        el_6 = (By.XPATH, f"(//*[contains(@type,'text')])[6]")
        # el_7 = (By.XPATH, f"(//*[contains(@type,'text')])[7]")
        # el_8 = (By.XPATH, f"(//*[contains(@type,'text')])[8]")
        # el_9 = (By.XPATH, f"(//*[contains(@type,'text')])[9]")
        # el_tel = (By.XPATH, "//*[contains(@type,'tel')]")

        # self.send_keys(el_3, rs)
        self.send_keys(el_4, rs)
        self.send_keys(el_5, rs)
        self.send_keys(el_6, rs)
        # self.click_element_my(el_7)
        # self.send_keys(el_7, "01.01.2000")
        # self.send_keys(el_8, rs)
        # self.send_keys(el_9, rs)
        # self.send_keys(el_tel, "+7 9" + str(f_tel))

        self.allure_screenshot()

        return self

    @allure.step('Кликаем кнопку скачать файл')
    def click_omly_download(self) -> Type[object]:
        self.click_element_my(Locator.outsourcing_btn_download)
        self.allure_screenshot()

        return object

    @allure.step('Кликаем кнопку Табели')
    def click_only_tabels(self) -> Type[object]:
        self.click_element_my(Locator.outsourcing_btn_tabels)
        self.allure_screenshot()

        return object

    @allure.step('Загрузить фото при регистрации')
    def send_photo_agency(self) -> Type[object]:
        el = (By.XPATH, "//*[contains(@type ,'file')][contains(@accept,'image/*')]")
        self.send_keys(el, "E:\\pvp-at\\02.jpg")
        time.sleep(3)
        self.allure_screenshot()

        return object

    @allure.step('Загрузить фото при регистрации ')
    def send_photo_agency_all(self, txt) -> Type[object]:
        #el = (By.XPATH, "//*[contains(@type ,'file')][contains(@accept,'image/*')]")
        el = (By.XPATH, "//*[contains(@type ,'file')][contains(@accept,'')]")
        fll = os.path.dirname(os.path.abspath(__file__))

        self.send_keys(el, fll + f"\\{txt}")
        #print(os.getcwd())
        time.sleep(3)
        self.allure_screenshot()

        return object



    @allure.step('Меняем пагинацию')
    def send_pagination_agency(self):
        el = (By.XPATH, "//*[contains(@class,'pagination__select custom-select')]")
        self.click_element_my(el)

        self.send_keys(el, "E:\\pvp-at\\02.jpg")
        time.sleep(3)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем файл в clime')
    def click_file_claim(self):
        el = (By.XPATH, "//*[contains(@class,'pagination__select custom-select')]")
        self.click_element_my(el)

        self.send_keys(el, "E:\\pvp-at\\02.jpg")
        time.sleep(3)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем чекбокс - {txt}')
    def click_checkbox_claim(self, txt):
        el = (By.XPATH, f"//*[contains(@class,'form-control__checkbox-item')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем - {txt}')
    def click_text_center_claim(self, txt):
        el = (By.XPATH, f"//*[contains(@class,'text-center')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

        # dp = fin + 1
        #
        # time.sleep(1)
        # for x in range(-dp, -1):
        #     fv = x + 1
        #     self.click_element_my_dp(f"(//*[contains(@class,'schedule__event-wrap')])[{fv * -1}]")
        #     time.sleep(1)
        #     self.click_element_my_dp(el_1)
        #     time.sleep(1)
        #     # self.GetDriver().refresh()
        #     # time.sleep(1)
        #     # if x == 0:
        #     #     break
        # self.allure_screenshot()
        #
        # return self


        # while fin >= 1:
        #     self.click_element_my_dp(f"(//*[contains(@class,'schedule__event-wrap')])[{fin}]")
        #     self.click_element_my_dp(el_1)
        #
        #     if fin == 0:
        #         break
        #     fin -= 1
        # if fin >= 1:
        #     self.click_element_my_dp(el_1)
        #
        # else:
        #     # self.click_element_my(el_2)
        #     self.GetDriver().refresh()

        # self.allure_screenshot()
        #
        # return self

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




