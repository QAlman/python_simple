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









