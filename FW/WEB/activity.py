import time
import allure

from selenium.webdriver.common.by import By
from FW.WEB.AnyPage import AnyPage


class Locator:

    activity_subheader = (By.XPATH, '//div[@class="activity-subheader"]')
    button_folder_create = (By.XPATH, "//*[text()='Создать папку']")  # -- my
    sandwich = (By.XPATH, "//*[@class='sandwich']") # --- my

    verme_url = "https://outsourcing-dev.verme.ru/"
    shifts_dev_url = "https://shifts-dev.verme.ru/auth"
    ousourcing_auto = "https://outsourcing-auto.verme.ru/"

    integral_wb = "https://www.wildberries.ru/"
    integral_oz_4 = "https://www.ozon.ru/"
    integral_oz_order = "https://www.ozon.ru/my/orderlist"
    integral_oz_3 = "https://www.ozon.ru/product/sviter-1037132494/?_fr=1687178147&advert=GnbNSkk1jw36ydN_Pgz7UAi6DmNUPcQWyfvKXYVGvi59TL7JdrMDjhbMRDRcwbOdkHckXGm56SfZcFZIFGElSTjhqWIEmdGg6Cx6uNs7gnTMVdAPUKDrnIvwqfcZV58jPT6o-G2taqQY4A8Sg2Ybj2AjMxyTdoWk8FGBX0F7lBlv55Q06U9j1uFwvPvprXiVzlcXcBr2x0vVh4lyQ4yejK08ZXOgeGni8g6Wl6x7lfZ2OI64Y9Y-krEcPX1Tb0lrKqHoszDhGw&avtc=1&avte=2&avts=1687177916&sh=E03SvnJg7A"
    integral_oz_2 = "https://www.ozon.ru/search/?deny_category_prediction=true&from_global=true&product_id=1037132494&text=%D0%A1%D0%B2%D0%B8%D1%82%D0%B5%D1%80"
    integral_oz_1 = "https://www.ozon.ru/product/sviter-1037132494/?_fr=1687178454&oos_search=false&sh=E03SvjpfPQ"
    integral_oz_5 = "https://www.ozon.ru/product/sviter-tvoe-863192976/?_fr=1687178743&asb=PzP6U4ByYLgzPyRxh%252BFwtwdplgGGfsGdFafpxKDsNuM%253D&asb2=u5Uk72yyOI99d8KK6rufBqLi99kOBhem-Fwb8Emk5H4dXacdr85Yk1o1s0wz7R42&avtc=1&avte=2&avts=1687178711&keywords=%D0%A1%D0%B2%D0%B8%D1%82%D0%B5%D1%80&sh=E03SvitN3g"



    #integral_oz_6 = "https://www.ozon.ru/modal/city_selector?neaf=f&pv=0&searchCity=&select_location=7dfa745e-aa19-4688-b121-b655c11e482f&sl_hash=02b286c370ebb324d922785b741e75b6204be1740b7d8f17f6381fbde81835ed&src_main=%2Finfo%2Fmap%2F%3F_fr%3D1687197558&src_modal=%2Fmodal%2Faddressbook%3Fsrc_main%3D%252Finfo%252Fmap%252F%253F_fr%253D1687197558"


    #integral_oz_6 = "https://www.ozon.ru/modal/city_selector?neaf=f&pv=0&searchCity=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80&select_location=&src_main=%2Finfo%2Fmap%2F%3F_fr%3D1687197558&src_modal=%2Fmodal%2Faddressbook%3Fsrc_main%3D%252Finfo%252Fmap%252F%253F_fr%253D1687197558"


    #integral_oz_6 = "https://www.ozon.ru/modal/commonDelivery?msid=b5f8803e-8b00-4a43-ad82-177f2dff1f55&neaf=f&nfr=t&pid=7&pp=427967&pv=2&src_main=%2Fproduct%2Fohotnichiy-binokl-eschenbach-arena-d-10h50-b-dlya-ohoty-turisticheskiy-dlya-rybalki-universalnyy-214937059%2F%3Fsh%3DE03SvomQqA&src_modal=%2Fmodal%2Faddressbook%3Fsrc_main%3D%252Fproduct%252Fohotnichiy-binokl-eschenbach-arena-d-10h50-b-dlya-ohoty-turisticheskiy-dlya-rybalki-universalnyy-214937059%252F%253Fsh%253DE03SvomQqA&tab=pp"

    #integral_oz_6 = "https://www.ozon.ru/product/ohotnichiy-binokl-eschenbach-arena-d-10h50-b-dlya-ohoty-turisticheskiy-dlya-rybalki-universalnyy-214937059/?_fr=1687198487&sh=E03SvomQqA"

    #integral_oz_6 = "https://www.ozon.ru/product/ohotnichiy-binokl-eschenbach-arena-d-10h50-b-dlya-ohoty-turisticheskiy-dlya-rybalki-universalnyy-214937059/?_fr=1687198487&sh=E03SvomQqA&accessibilityMode=1"


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
        self.goto_page(Locator.integral_oz_4)
        time.sleep(1)
        return self.manager.web_outsourcing

    @allure.step('Работа c URL ozon')
    def button_to_integral_oz_order(self):
        # Переходим на целевую страницу теста
        #self.goto_page(Locator.verme_url)
        self.goto_page(Locator.integral_oz_order)
        time.sleep(1)
        return self.manager.web_outsourcing









