import string
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from FW.FWBase import FWBase
from time import sleep


import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class WebBase(FWBase):

    def GetDriver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.get_driver()
        return self.manager.driver_instance.driver

    def allure_screenshot(self):
        try:
            allure.attach(self.GetDriver().get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(str(e))

    @allure.step('Open main page')
    def open_main_page_(self):

        main_page = self.manager.settings.GLOBAL[self.manager.settings.branch]['main_page']
        title = self.GetDriver().title
        if main_page not in title:
            self.GetDriver().get(main_page)

    @allure.step('GoTo URL - {page}')
    def goto_page(self, page):
        title = self.GetDriver().title
        if page not in title:
            self.GetDriver().get(page)

    @allure.step('click')
    def click_element(self, locator):
        try:
            web_element = self.find_element(locator)
            web_element.click()

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    @allure.step('Send keys')
    def send_keys(self, locator, text):
        try:
            web_element = self.find_element(locator)
            web_element.send_keys(text)

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)




    @allure.step('Send keys')
    def clear_and_send_keys(self, locator, text):
        try:
            web_element = self.find_element(locator)
            web_element.clear()
            web_element.send_keys(text)

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    @allure.step('Send keys ENTER')
    def send_keys_enter(self, locator):
        try:
            web_element = self.find_element(locator)
            web_element.send_keys(Keys.ENTER)

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    @allure.step('Send keys TAB')
    def send_keys_tab(self, locator):
        try:
            web_element = self.find_element(locator)
            web_element.send_keys(Keys.TAB)

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    def send_enter(self):
            time.sleep(1)
            actions_3 = ActionChains(self.GetDriver())
            actions_3.send_keys(Keys.ENTER)
            actions_3.perform()
            return self

    def send_keys_up_double(self):
            time.sleep(2)
            actions_3 = ActionChains(self.GetDriver())
            actions_3.send_keys(Keys.PAGE_UP)
            actions_3.send_keys(Keys.PAGE_UP)
            actions_3.perform()
            time.sleep(2)
            return self

    def send_keys_down_double(self):
            time.sleep(2)
            actions_3 = ActionChains(self.GetDriver())
            actions_3.send_keys(Keys.PAGE_DOWN)
            actions_3.send_keys(Keys.PAGE_DOWN)
            actions_3.perform()
            time.sleep(2)
            return self

    def send_keys_backspase(self, locator):
        try:
            web_element = self.find_element(locator)
            web_element.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
            web_element.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
            web_element.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
            web_element.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
            web_element.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
            web_element.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

        return self


    def send_keys_delete(self, locator):
        try:
            web_element = self.find_element(locator)
            web_element.send_keys(Keys.DELETE, Keys.DELETE, Keys.DELETE, Keys.DELETE)
            web_element.send_keys(Keys.DELETE, Keys.DELETE, Keys.DELETE, Keys.DELETE)
            web_element.send_keys(Keys.DELETE, Keys.DELETE, Keys.DELETE, Keys.DELETE)

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

        return self

    @allure.step('Send keysUP')
    def send_keys_up(self, locator):
        try:
            web_element = self.find_element(locator)
            web_element.send_keys(Keys.UP)

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    @allure.step('Send keysCTRL')
    def send_keys_ctrl(self, locator):
        try:
            web_element = self.find_element(locator)
            web_element.send_keys(Keys.CONTROL, 'a')

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    @allure.step('Send keys {txt}')
    def send_keys_my(self, txt, txt_1):
            actions_3 = ActionChains(self.GetDriver())
            actions_3.key_down(txt)
            actions_3.send_keys(txt_1)
            actions_3.perform()
            return self

    @allure.step('Send keys {txt}')
    def send_keys_once(self, txt):
            actions_3 = ActionChains(self.GetDriver())
            actions_3.send_keys(txt)
            actions_3.perform()
            return self

    def get_tag_text(self, locator):
        try:
            text = self.find_element(locator).text
            return text
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    def get_tag_attribute(self, locator, attribute_name):
        try:
            return self.find_element(locator).get_attribute(attribute_name)
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    def scroll_to_element(self, locator):
        try:
            element = self.find_element(locator).location_once_scrolled_into_view
            script = "window.scrollBy(" + str(element['x'] + 80) + ", " + str(element['y'] + 80) + ")"
            self.GetDriver().execute_script(script)
        except StaleElementReferenceException as e:
            self.allure_ElementNotVisibleException(e)

    @allure.step('Clear')
    def clear_keys(self, locator):
        try:
            self.find_element(locator).clear()
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    def get_current_url(self):
        return self.GetDriver().current_url

    @allure.step('Right click')
    def right_click_dy_xpath(self, locator):
        try:
            action_chains = ActionChains(self.GetDriver())
            action_chains.context_click(self.GetDriver().find_element(locator)).perform()
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    @allure.step('Double click')
    def double_click(self, locator):
        try:
            action_chains = ActionChains(self.GetDriver())
            action_chains.double_click(self.GetDriver().find_element(locator)).perform()
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)




    @allure.step('Refresh page')
    def refresh_the_page(self):
        try:
            self.GetDriver().refresh()
        except StaleElementReferenceException:
            pass

    @allure.step('Ввод текста в iframe:')
    def send_keys_in_frame(self, locator_frame, locator_in_frame, text):
        frame = self.find_element(locator_frame)
        self.GetDriver().switch_to.frame(frame)
        self.send_keys(locator_in_frame, text)
        self.GetDriver().switch_to.default_content()

    @allure.step('Переход на новую вкладку')
    def switch_to_tab(self):

         self.GetDriver().switch_to.window(self.GetDriver().window_handles[1])

    @allure.step('Возврат  на предыдущую вкладку')
    def return_to_tab(self):

         self.GetDriver().switch_to.window(self.GetDriver().window_handles[0])

    @allure.step('Открытие новой вкладки')
    def open_new_tab(self,txt):

         self.GetDriver().execute_script(f"window.open('{txt}')")

    @allure.step("Переход через страницу")
    def go_to_next_tab(self):
        actions = ActionChains(self.GetDriver())
        element = self.send_keys(Keys.CONTROL + Keys.TAB)
        actions.move_to_element(element)
        actions.perform()

    @allure.step("Закрыть вкладку")
    def close_tab(self):
        actions = ActionChains(self.GetDriver())
        #actions.key_down(Keys.CONTROL + 'w').send_keys('w').key_up(Keys.CONTROL).perform()
        actions.send_keys(Keys.LEFT_CONTROL + "w")
        actions.perform()



    @allure.step('Send keys')
    def send_keys_slow(self, locator, text, delay):
        """
        Замедленный вод текста в текстовое поле
        :param locator: адрес поля
        :param text: вводимый текст
        :param delay: задержка в милл. сек. между вводимыми буквами
        :return:
        """
        waiting_time = (1 / 1000) * delay
        try:
            self.scroll_to_element(locator)
            for char in text:
                sleep(waiting_time)
                self.find_element(locator).send_keys(char)
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    @allure.step('screenshot')
    def allure_screenshot(self):
        try:
            allure.attach(self.GetDriver().get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(str(e))

    @allure.step("select_element_by_visible_text:")
    def select_element_by_visible_text(self, locator, text):
        select = Select(self.GetDriver().find_element(locator))
        select.select_by_visible_text(text)

    @allure.step("move_to_element")
    def move_to_element(self, locator):
        actions = ActionChains(self.GetDriver())
        element = self.find_element_my_dp(locator)
        actions.move_to_element(element)
        actions.perform()

    @allure.step("send_page_up")
    def send_page_up(self):

        actions = ActionChains(self.GetDriver())
        actions.send_keys(Keys.PAGE_UP)
        actions.perform()

    @allure.step("send_page_down")
    def send_page_down(self):

        actions = ActionChains(self.GetDriver())
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

    @allure.step("send_Esc")
    def send_esc(self):

        actions = ActionChains(self.GetDriver())
        actions.send_keys(Keys.ESCAPE)
        actions.perform()

    @allure.step('Выбираем чекбокс terms ')
    def clic_approve_terms(self, locator, ):

        el = locator
        elem = self.find_element_my(el)
        size = elem.size
        w, h = size['width'], size['height']
        loc = elem.location
        print(w, h)
        print(loc)

        action_chains = ActionChains(self.GetDriver())
        action_chains.click(self.GetDriver().find_element(locator)).perform()
        self.allure_screenshot()

        return self



    # остановщик теста при ошибке
    @allure.step('ElementNotVisibleException')
    def allure_ElementNotVisibleException(self, exeption_text):
        self.allure_screenshot()
        assert True == False

    # остановщик теста при ошибке
    @allure.step('NoSuchElementException')
    def allure_NoSuchElementException(self, exeption_text):
        self.allure_screenshot()
        assert True == False

    # остановщик теста при ошибке
    @allure.step('StaleElementReferenceException')
    def allure_StaleElementReferenceException(self, exeption_text):
        assert True == False

    @allure.step('Получение количества элементов')
    def get_count_elements(self, locator):
        result = len(self.GetDriver().find_elements_by_xpath(locator))
        return result

    @allure.step('Получение количества элементов')
    def get_count_elements_my(self, locator):
        result = len(self.GetDriver().find_elements(By.XPATH, locator))
        return result

    @allure.step('get_console_log')
    def get_console_log(self):
        print(self.GetDriver().get_log('browser'))

    # ----------------------------------------------------------------------------------------

    def find_element(self, locator, wait=None):
        if wait is None:
            wait = self.manager.settings.time_element_Wait

        web_element = WebDriverWait(self.GetDriver(), wait).until(EC.presence_of_element_located(locator))
        return web_element

    # ------------------------------------------------------------------------------------------


    def find_elements(self, locator):
        return WebDriverWait(self.GetDriver(), self.manager.settings.time_element_Wait).until(EC.presence_of_all_elements_located(locator))

    # def find_elements_my(self, locator):
    #     return self.GetDriver().find_elements()
    #


    @allure.step("send_keys")
    def send_keys_pd(self, locator):
        actions = ActionChains(self.GetDriver())
        actions.send_keys(locator)
        actions.perform()

    @allure.step("is_displayed")
    def is_displayed(self, locator):
        is_displayed = self.find_element(locator).is_displayed()
        return is_displayed

    @allure.step("get_property")
    def get_prop(self, locator, txt):
        get_prop = self.find_element(locator).get_property(txt)

        return get_prop


    def find_element_my(self, locator):
        return WebDriverWait(self.GetDriver(), self.manager.settings.time_element_Wait).until(EC.element_to_be_clickable(locator))

    # dp - для простых устаревших методов
    def find_element_my_dp(self, locator):
        return self.GetDriver().find_element(By.XPATH, locator)

    @allure.step('click my')
    def click_element_my(self, locator):
        try:
            web_element = self.find_element_my(locator)
            web_element.click()

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    @allure.step('click my dp')
    def click_element_my_dp(self, locator):
        try:
            web_element = self.GetDriver().find_element(By.XPATH, locator)
            web_element.click()

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    def get_text_my(self, locator):
        try:
            text = self.find_element(locator).text
            return text
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)






