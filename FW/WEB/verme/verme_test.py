import math
import time
import requests
import allure
from selenium.webdriver.common.by import By
from FW.WEB.AnyPage import AnyPage


class Locator:
    verme_url = "https://outsourcing-dev.verme.ru/auth/login/"


class verme_create(AnyPage):

    @allure.step('Закрываем ситипикер')
    def close_citypicker(self):
        self.click_element_my(Locator.citypicker_close)
        self.allure_screenshot()

        return self
    #
    # @allure.step('Забираем текст')
    # def get_text(self):
    #     txt = self.get_tag_text(Locator.page_title)
    #
    #     return txt
    #
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
    # @allure.step('Перемещаемся к выбору производителя')
    # def move_to_enterprise(self):
    #     self.move_to_element(Locator.enterprise_field)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Выбираем бренд {txt}')
    # def select_brand_all(self, txt):
    #     el = (By.XPATH, f"//span[@class='checkbox-field__label'][contains(.,'{txt}')]")
    #     self.click_element_my(el)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Проверяем текст бренда {txt} на странице товара')
    # def check_select_brand_all(self, txt):
    #     el = (By.XPATH, f"//h1[@class='catalog-view__title'][contains(.,'{txt}')]")
    #     # k = txt_brand.casefold()[:-1]
    #     txt_cart = self.get_text_my(el)
    #     # r = txt_cart.casefold()
    #     assert txt in txt_cart, "Текст бренда на странице товара не найден"
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Выбираем {txt}')
    # def select_actions(self, txt):
    #     ur = (By.XPATH, f"//*[@ga-event-label='{txt}']")
    #     self.click_element_my(ur)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Выбрать доставку {address_market} в {city}')
    # def select_address_delivery_any(self, address_market, city, txt):
    #     self.click_element_my(Locator.select_delivery)
    #     time.sleep(2)
    #     self.click_element_my(Locator.select_city)
    #     select_city_sample = (By.XPATH, f"//span[@class='cities-list-item__name'][contains(.,'{city}')]")
    #     self.click_element_my(select_city_sample)
    #     time.sleep(2)
    #     self.click_element_my(Locator.select_delivery_only)
    #     # time.sleep(1)
    #     switch_select_market_2 = (By.XPATH, f"(//*[@class='input-field__control input-field__control--native'])[{txt}]")
    #     self.click_element_my(switch_select_market_2)
    #     # time.sleep(1)
    #     self.send_keys_slow(switch_select_market_2, "zov", 100)
    #     # time.sleep(1)
    #     self.send_keys_backspase(switch_select_market_2)
    #     # time.sleep(1)
    #     self.send_keys_backspase(switch_select_market_2)
    #     # time.sleep(1)
    #     self.send_keys_delete(switch_select_market_2)
    #     # time.sleep(1)
    #     self.click_element_my(switch_select_market_2)
    #     self.send_keys_slow(switch_select_market_2, address_market, 100)
    #     self.allure_screenshot()
    #     select_address_sample = (By.XPATH, f"//li[@class='auto-suggest-field__suggestion'][text()='{address_market}']")
    #     # time.sleep(2)
    #     self.click_element_my(select_address_sample)
    #     time.sleep(2)
    #     self.click_element_my(Locator.select_market_final_2)
    #     # time.sleep(7)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Забираем данные из карточки')
    # def get_items_one(self, txt):
    #     el = self.get_text_my(Locator.get_items_cart_one)
    #     print(el)
    #     assert txt == el, "Сортировка не верная"
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Заполнить блок личных даных')
    # def send_family(self, txt, txt_n):
    #     # self.click_element_my(Locator.family_field)
    #     # self.send_keys_slow(Locator.family_field_last_name, txt, 100)
    #     self.send_keys_slow(Locator.family_field_first_name, txt, 100)
    #     # self.send_keys_slow(Locator.family_field_patronymic_name, txt, 100)
    #     # self.click_element_my(Locator.family_field_mail)
    #     # self.send_keys_slow(Locator.family_field_mail, txt_n + "@asd.tr", 100)
    #     # self.click_element_my(Locator.family_field_gender)
    #     # self.click_element_my(Locator.family_field_gender_f)
    #     self.click_element_my(Locator.family_field_data)
    #     self.send_keys(Locator.family_field_data, Locator.blank + Locator.blank)
    #     self.send_keys_slow(Locator.family_field_data, "17 11 2000", 100)
    #     self.send_keys_enter(Locator.family_field_data)
    #     self.click_element_my(Locator.family_field_mail)
    #     self.send_keys_slow(Locator.family_field_mail, txt_n + "@asd.tr", 100)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Добавить товары в корзину 101869 1шт ,084250 1кг')
    # def add_basket(self):
    #     self.goto_page(Locator.ecom_url_34)
    #     time.sleep(3)
    #     self.click_element_my(Locator.add_basket_big)
    #     time.sleep(5)
    #     self.allure_screenshot()
    #     self.goto_page(Locator.ecom_url_34_1)
    #     time.sleep(3)
    #     self.click_element_my(Locator.add_basket_big)
    #     time.sleep(5)
    #     self.allure_screenshot()
    #     self.click_element_my(Locator.rise_item)
    #     self.send_keys(Locator.rise_item, Locator.blank)
    #     time.sleep(1)
    #     self.send_keys(Locator.rise_item, "1")
    #     time.sleep(1)
    #     self.send_keys_enter(Locator.rise_item)
    #     time.sleep(2)
    #     self.click_element_my(Locator.move_to_basket)
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Ввести промокод vp97picq (вы получили скидку 40%)')
    # def add_promocode(self, promo):
    #     self.click_element_my(Locator.field_promo)
    #     self.send_keys_slow(Locator.field_promo, promo, 100)
    #     self.allure_screenshot()
    #
    #     return self
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
    # def check_price_basket(self, txt):
    #     el = self.get_text_my(Locator.promo_get_price_final)
    #     assert el == txt, "Цена не соответствует цене на корзине"
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
    # @allure.step('Удаляем {txt}')
    # def click_button_delete(self, txt):
    #     el = (By.XPATH, f"(//*[contains(@class ,'custom-sku-in-favourites__button-text')])[{txt}]")
    #     self.click_element_my(el)
    #     self.allure_screenshot()
    #
    #     return self




