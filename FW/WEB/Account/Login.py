import allure
#from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from FW.WEB.AnyPage import AnyPage


class Locator:
    local_form = (By.CSS_SELECTOR, '[test_id="local-form"]')
    input_login = (By.ID, 'loginInput')
    input_password = (By.ID, 'passwordInput')
    select_local_form = (By.CSS_SELECTOR, '[test_id="adsf-sign-in"]')
    local_submit_button = (By.XPATH, '//*[@test_id="local-submit-button"]')


class Login(AnyPage):

    @allure.step('Вход по логину и паролю')
    def login_log_pas(self, login, password):
        self.click_element(Locator.local_form)
        self.send_keys(Locator.input_login, login)
        self.send_keys(Locator.input_password, password)
        self.click_element(Locator.local_submit_button)
        self.manager.web_activity.page_loaded()
        return self.manager.web_activity

    @allure.step('Вход через AD')
    def login_ad(self):
        self.click_element(Locator.select_local_form)
        self.manager.web_activity.page_loaded()
        return self.manager.web_activity
