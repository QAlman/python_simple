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









