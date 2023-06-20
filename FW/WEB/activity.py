import time
import allure

from selenium.webdriver.common.by import By
from FW.WEB.AnyPage import AnyPage


class Locator:

    activity_subheader = (By.XPATH, '//div[@class="activity-subheader"]')
    button_folder_create = (By.XPATH, "//*[text()='Создать папку']")  # -- my
    sandwich = (By.XPATH, "//*[@class='sandwich']") # --- my


    #integral_oz = "https://www.ozon.ru/modal/addressbook?src_main=%2Fproduct%2Fkraska-tikkurila-44939-bystrosohnushchaya-do-85-akrilatno-lateksnaya-matovoe-pokrytie-9-kg-belyy-823085083%2F%3Favtc%3D1%26avte%3D2%26avts%3D1687291648%26c%3Dtop_banner_pdp%26pid%3Dozon_ru%26sh%3DQAyjYhW3vA"
    integral_oz = "https://www.ozon.ru/"
    integral_oz_1 = "https://www.ozon.ru/product/kraska-tikkurila-44939-bystrosohnushchaya-do-85-akrilatno-lateksnaya-matovoe-pokrytie-9-kg-belyy-823085083/?avtc=1&avte=2&avts=1687291648&sh=QAyjYhW3vA"
    integral_oz_5 = "https://www.ozon.ru/product/sviter-tvoe-863192976/?_fr=1687178743&asb=PzP6U4ByYLgzPyRxh%252BFwtwdplgGGfsGdFafpxKDsNuM%253D&asb2=u5Uk72yyOI99d8KK6rufBqLi99kOBhem-Fwb8Emk5H4dXacdr85Yk1o1s0wz7R42&avtc=1&avte=2&avts=1687178711&keywords=%D0%A1%D0%B2%D0%B8%D1%82%D0%B5%D1%80&sh=E03SvitN3g"
    integral_wb = "https://www.wildberries.ru/catalog/86096509/detail.aspx"



class Activity(AnyPage):

    def page_loaded(self):
        #self.find_element(Locator.activity_subheader)
        pass

    @allure.step('Работа c URL VERME')
    def button_to_verme(self):
        # Переходим на целевую страницу теста
        #self.goto_page(Locator.verme_url)
        self.goto_page(Locator.shifts_dev_url)
        time.sleep(1)
        return self.manager.web_verme

    @allure.step('Работа c URL Shifts')
    def button_to_shifts(self):
        # Переходим на целевую страницу теста
        #self.goto_page(Locator.verme_url)
        self.goto_page(Locator.shifts_dev_url)
        time.sleep(1)
        return self.manager.web_verme

    @allure.step('Работа c URL outsourcing')
    def button_to_outsourcing(self):
        # Переходим на целевую страницу теста
        #self.goto_page(Locator.verme_url)
        self.goto_page(Locator.ousourcing_auto)
        time.sleep(1)
        return self.manager.web_outsourcing

    @allure.step('Работа c URL outsourcing_dev')
    def button_to_outsourcing_dev(self):
        # Переходим на целевую страницу теста
        #self.goto_page(Locator.verme_url)
        self.goto_page(Locator.verme_url)
        time.sleep(1)
        return self.manager.web_outsourcing

    @allure.step('Работа c URL wb')
    def button_to_integral_wb(self):
        # Переходим на целевую страницу теста
        #self.goto_page(Locator.verme_url)
        self.goto_page(Locator.integral_wb)
        time.sleep(1)
        return self.manager.web_outsourcing

    @allure.step('Работа c URL ozon')
    def button_to_integral_oz(self):
        # Переходим на целевую страницу теста
        #self.goto_page(Locator.verme_url)
        self.goto_page(Locator.integral_oz)
        time.sleep(1)
        return self.manager.web_verme

    @allure.step('Работа c URL ozon')
    def button_to_integral_oz_order(self):
        # Переходим на целевую страницу теста
        #self.goto_page(Locator.verme_url)
        self.goto_page(Locator.integral_oz_order)
        time.sleep(1)
        return self.manager.web_verme









