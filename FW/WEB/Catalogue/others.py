import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FW.WEB.AnyPage import AnyPage


class Locator:
    cke_contents = (By.XPATH, '//div[@class="sidebar-catalogue-list__content"]')



class CustomFieldDictionaryWeb(AnyPage):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.cke_contents)

    @allure.step('Нажать кнопку "Создать справочник"')
    def button_create_catalogue(self):
        self.click_element(Locator.button_create_catalogue)
        return self

    @allure.step('Нажать кнопку "создайте новый"')
    def button_create_new(self):
        self.click_element(Locator.button_create_new)
        return self

    @allure.step('Нажать кнопку "Добавить" в дереве')
    def button_add_in_tree(self):
        self.click_element(Locator.button_add_in_tree)
        return self

    @allure.step('Нажать на первый справочник в дереве правой кнопкой мыши')
    def button_right_click_on_the_first_catalogue_in_tree(self):
        self.right_click_dy_xpath(Locator.right_click_in_tree)
        return self

    @allure.step('Нажать кнопку Добавить справочник во всплывающем меню в дереве')
    def button_add_catalogue_in_pop_up_block_in_tree(self):
        self.page_loaded()
        # Нажимаем на правую кнопку мыши в дереве
        self.button_right_click_on_the_first_catalogue_in_tree()
        # Нажимаем на кнопку "Добавить справочник" во всплывающем меню
        self.click_element(Locator.button_add_catalogue_in_pop_up_block)
        return self

