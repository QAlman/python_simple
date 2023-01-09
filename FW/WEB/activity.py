import time
import allure

from selenium.webdriver.common.by import By
from FW.WEB.AnyPage import AnyPage


class Locator:

    activity_subheader = (By.XPATH, '//div[@class="activity-subheader"]')
    button_folder_create = (By.XPATH, "//*[text()='Создать папку']")  # -- my
    sandwich = (By.XPATH, "//*[@class='sandwich']") # --- my

    verme_url = "https://outsourcing-dev.verme.ru/"





class Activity(AnyPage):

    def page_loaded(self):
        #self.find_element(Locator.activity_subheader)
        pass

    @allure.step('Работа c URL VERME')
    def button_to_verme(self):
        # Переходим на целевую страницу теста
        self.goto_page(Locator.verme_url)
        time.sleep(3)
        return self.manager.web_ecom









