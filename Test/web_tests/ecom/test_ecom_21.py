import time
from random import random
import allure
import pytest

import FW.WEB.ecom.ecom_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 21')
class TestEcom_21(WebBase):

    @allure.title('Смок 21 Рецепты (авторизованный/неавторизованный) - неавторизованный ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_21(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_21()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        city = "Санкт-Петербург и ЛО"
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        ecom.select_address_self_any(address_market, city, sw)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_21)
        br = "Рецепты"
        ba = "Статьи"
        bv = "Видео"
        bf = "Избранное"
        ecom.check_view_block(br)
        ecom.check_view_block(ba)
        ecom.check_view_block(bv)
        ecom.check_view_block(bf)
        ecom.check_view_selections()
        cr = "Рецепты|Все категории"
        ecom.clic_all_categories(cr)
        #ecom.clic_add_favotites()
        ecom.clic_receipt_cart()
        #iz = "В избранном"
        #ecom.check_receipt_cart(iz)
        #ecom.click_receipt_cart_favorites()
        #iz = "В избранное"
        #ecom.check_receipt_cart(iz)
        ecom.click_receipt_cart_offer()
        ecom.check_receipt_cart_vk_f()
        igr1 = "Вода без газа"
        igr2 = "Сливки (40%)"
        ecom.click_receipt_cart_ingredients(igr1, igr2)
        ecom.clic_add_cart_one()
        iz3 = "Перейти в избранное"
        ecom.check_add_cart_one(iz3)
        tag = "Весь год"
        ecom.clic_tag_item(tag)
        ur = FW.WEB.ecom.ecom_test.Locator.ecom_url_21_1
        ecom.check_url_receipt(ur)
        tag_2 = "весь год"
        ecom.check_receipt_cart_checkbox(tag_2)
        tag_3 = "бобовые"
        itm = ecom.get_receipt_tag_tree(tag_3)
        ecom.click_receipt_cart_ingredient_one(tag_3)
        ecom.check_receipt_cart_item(itm)
        ecom.page_down_local()
        ecom.click_clear_item()
        ecom.page_up_local()
        av = "авокадо"
        ecom.send_receipt_item(av)
        ecom.page_up_local()
        ecom.click_receipt_cart_ingredient_one(av)
        # блок с ингридиентами
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_21)
        cv = "Видео|Показать все"
        ecom.clic_all_categories(cv)
        tl = "Рецепты с видео"
        ecom.check_view_all_title(tl)
        mc = "Новый год"
        ecom.click_receipt_cart_ingredient_one(mc)
        # блок работы с рецептами видео
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_21)
        cta = "Смотреть все|Блюда с ягодами и фруктами"
        ecom.clic_all_categories(cta)
        tls = "Блюда с ягодами и фруктами"
        ecom.check_view_all_title(tls)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_21)
        en = "Лосось (филе)"
        ecom.click_receipt_ingredient_one(en)
        tlsl = "Каталог рецептов: лосось (филе)"
        ecom.check_view_all_title(tlsl)
        itl = "2"
        ecom.check_receipt_cart_item(itl)



