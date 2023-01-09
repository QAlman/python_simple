import math
import time
import requests
import allure
from selenium.webdriver.common.by import By
from FW.WEB.AnyPage import AnyPage


class Locator:
    ecom_url_34 = "https://stage.lentatest.com/product/hleb-rizhskijj-rossiya-500g-101869/"
    ecom_url_34_1 = "https://stage.lentatest.com/product/gc-buritto-vesovojj-rossiya-084250/"

    ecom_url_31 = "https://stage.lentatest.com/catalog/chajj-kofe-kakao/"
    ecom_url_31_t = "https://stage.lentatest.com/product/chajj-chernyjj-richard-royal-ceylon-mu-rossiya-100pak-381905/"
    ecom_url_31_b = "https://stage.lentatest.com/brand/richard/"
    ecom_url_26 = "https://stage.lentatest.com/catalog/alkogolnye-napitki/"
    ecom_url_26_1 = "https://stage.lentatest.com/product/viski-grants-triple-wood-alk40-velikobritaniya-07l-492102/"
    ecom_url_26_2 = "https://stage.lentatest.com/catalog/alkogolnye-napitki/vino/belye-vina/"
    ecom_url_26_3 = "https://stage.lentatest.com/product/klejjkarandash-365-dnejj-l10289-kitajj-354660/"
    ecom_url_24 = "https://stage.lentatest.com/catalog/moloko-syr-yajjco/"
    ecom_url_21 = "https://stage.lentatest.com/recepty/"
    ecom_url_21_1 = "https://stage.lentatest.com/recepty/catalog-recepty/f/vremena-goda=ves-god/"
    ecom_url_19 = "https://stage.lentatest.com/catalog/chajj-kofe-kakao/chajj/chernyjj-chajj/"
    ecom_url_15 = "https://stage.lentatest.com/catalog/bezalkogolnye-napitki/"
    ecom_url_15_1 = "https://stage.lentatest.com/product/voda-pitevaya-svyatojj-istochnik-negaz-pet-rossiya-5l-309510/"
    ecom_url_15_2 = "https://stage.lentatest.com/shoppinglist/"
    ecom_url_14 = "https://stage.lentatest.com/shoppinglist/"
    ecom_url_14_1 = "https://stage.lentatest.com/product/tomaty-na-vetke-ves-1kg-015182/"
    ecom_url_13 = "https://stage.lentatest.com/product/syr-365-dnejj-rossijjskijj-50-kusok-rossiya-200g-354392/"
    ecom_url_13_1 = "https://stage.lentatest.com/product/slivki-lenta-20-rossiya-200g-354363/"
    ecom_url_13_2 = "https://stage.lentatest.com/product/syr-365-dnejj-slivochnyjj-50-kusok-rossiya-300g-354391/"
    ecom_url_13_3 = "https://stage.lentatest.com/product/slivki-lenta-33-rossiya-200g-354364/"
    ecom_url_13_4 = "https://stage.lentatest.com/product/slivki-lenta-10-rossiya-200g-354361/"
    ecom_url_13_5 = "https://stage.lentatest.com/product/syr-365-dnejj-gollandskijj-45-kusok-rossiya-300g-354393/"
    ecom_url_13_6 = "https://stage.lentatest.com/product/syr-hochland-tvorozhnyjj-slivochnyjj-60-rossiya-140g-218460/"
    ecom_url_12 = "https://stage.lentatest.com/product/tomaty-slivovidnye-ves-1kg-024654/"
    ecom_url_9 = "https://stage.lentatest.com/catalog/myaso-ptica-kolbasa/"
    ecom_url_9_1 = "https://stage.lentatest.com/catalog/myaso-ptica-kolbasa/myaso-ohlazhdennoe/govyadina/"
    ecom_url_8 = "https://stage.lentatest.com/crazynew/"


    ecom_user = "9407718110"

    blank = "\b\b\b\b"
    txt_promo = "Вы получили скидку"
    txt_final = "Спасибо за заказ!"
    # address_market = "ул.  Савушкина, д. 112, лит. А"
    citypicker_close = (By.XPATH, "//div[@class='close-control']")
    cookie_close = (By.XPATH, "//*[@class='button__inner cookie-usage-notice__button-inner--desktop']")
    # iframe = (By.XPATH, "//iframe")
    registration_button = (By.XPATH, "//span[contains(.,'Войти')]")
    approve_terms = (By.XPATH, "//*[text()='Принимаю']")
    phone_field = (By.NAME, "phone")
    search_field = (By.XPATH, "//input[@class='catalog-search__field'][@placeholder='Поиск в каталоге и на сайте']")
    contains_txt = (By.XPATH, "//*[@class='text-highlight text-highlight--single-style'][contains(.,'Молоко')]")
    contains_txt_left = (By.XPATH, "(//*[@class='text-highlight__fragment'][contains(.,'Молоко')])[1]")

    page_title = (By.XPATH, "//*[@class='catalog-view__title']")
    next_button = (By.XPATH, "//button[contains(.,'Далее')]")
    approve_button = (By.XPATH, "//button[contains(.,'Подтвердить')]")
    continue_button = (By.XPATH, "//button[contains(.,'Продолжить')]")
    select_cat_button = (By.XPATH, "//button[contains(.,'Выбрать категории')]")
    apply_button = (By.XPATH, "//span[@class='button__inner'][text()='Применить']")
    range_left = (By.XPATH, "//*[@class='catalog-price-filter__prices-form']//preceding-sibling::input")
    range_right = (By.XPATH, "//*[@class='catalog-price-filter__prices-form']//following-sibling::input")
    send_keys_enter = (By.XPATH, "//*[@class='catalog-price-filter__prices-form']//following-sibling::input")
    compare_left = (
        "//div[@class='price-label sku-card-small-prices__price price-label--small price-label--primary']//span[(text()>='100')]")
    compare_left_min = (
        "//div[@class='price-label sku-card-small-prices__price price-label--small price-label--primary']//span[(text()<='99')]")
    compare_left_max = (
        "//div[@class='price-label sku-card-small-prices__price price-label--small price-label--primary']//span[(text()>='201')]")
    enterprise_field = (By.XPATH, "(//*[text()='Производитель'])[1]")
    show_next = (By.XPATH, "//*[text()='Показать ещё']")
    show_next_2 = (By.XPATH, "(//*[text()='Показать ещё'])[2]")
    select_brand = (By.XPATH, "(//*[@class='checkbox-field__label'])[3]")
    select_brand_2 = (By.XPATH, "//span[@class='checkbox-field__label'][contains(.,'4 ВОДЫ ДЮР-СО')]")
    get_brand = (By.XPATH, "//div[@class='sku-card-small-header__title']")
    select_fabric = (By.XPATH, "//span[@class='checkbox-field__label'][contains(.,'Абрау-Дюрсо')]")
    actions = (By.XPATH, "//*[@ga-event-label='Акции']")
    actions_for = (By.XPATH, "//*[@ga-event-label='Акции для спб']")

    # -------------citypiker
    select_delivery = (By.XPATH, "//*[contains(@class,'address-container__adress-location')]")
    #select_delivery = (By.XPATH, "//*[@class='address-container__adress-location']")
    select_delivery_only = (By.XPATH, "//span[@class='button__inner'][text()='Доставка']")
    select_delivery_or = (By.XPATH, "//span[@class='button__inner'][text()='Магазины']")


    select_city = (By.XPATH, "//span[@class='store-picker-city__label']")
    select_city_1 = (By.XPATH, "//span[@class='cities-list-item__name'][contains(.,'Санкт-Петербург и ЛО')]")
    select_city_2 = (By.XPATH, "//span[@class='cities-list-item__name'][contains(.,'Новосибирск')]")
    select_market = (By.XPATH,
                     "//*[@class='input-field__label'][text()='Введите адрес магазина']/following-sibling::input")
    select_market_2 = (By.XPATH, "(//*[@class='input-field__control input-field__control--native'])[2]")
    select_address = (By.XPATH, "//div[@class='stores-list-item__name'][text()='ул.  Савушкина, д. 112, лит. А']")
    # select_address_sample = (By.XPATH, f"//div[@class='stores-list-item__name'][text()='{address_market}']")
    select_market_final = (By.XPATH, "//span[@class='button__inner'][text()='Выбрать магазин']")
    select_market_final_2 = (By.XPATH, "//span[@class='button__inner'][text()='Выбрать']")

    # -------------citypiker

    check_item = ("//*[@class='discount-label-small discount-label-small--sku-card sku-card-small__discount-label']")

    sort_pop = (By.XPATH, "//div[@class='dropdown__label'][contains(.,'По популярности')]")
    sort_pop_1 = (By.XPATH, "//*[@class='dropdown__option-link dropdown__option-link--active'][contains(.,'По популярности')]")
    sort_chip = (By.XPATH, "//*[@class='dropdown__option-link'][contains(.,'Сначала дешевые')]")
    sort_chip_1 = (By.XPATH, "//div[@class='dropdown__label'][contains(.,'Сначала дешевые')]")
    sort_rich = (By.XPATH, "//*[@class='dropdown__option-link'][contains(.,'Сначала дорогие')]")
    sort_rich_1 = (By.XPATH, "//div[@class='dropdown__label'][contains(.,'Сначала дорогие')]")
    sort_discount = (By.XPATH, "//*[@class='dropdown__option-link'][contains(.,'По размеру скидки')]")
    sort_discount_1 = (By.XPATH, "//div[@class='dropdown__label'][contains(.,'По размеру скидки')]")
    sort_rating = (By.XPATH, "//*[@class='dropdown__option-link'][contains(.,'По рейтингу')]")
    sort_noda = (By.XPATH,
                 "//*[@class='link link--black catalog-category__link catalog-link catalog-link--category'][contains(.,'Кондитерские изделия')]")

    get_items_cart_one = (By.XPATH, "(//*[contains(@class,'sku-card-small-header__title')])[1]")

    family_field = (By.XPATH,
                    "(//*[normalize-space(text()) and normalize-space(.)='Заполните недостающие данные'])[1]/following::div[7]")
    family_field_last_name = (By.NAME, "lastName")
    family_field_first_name = (By.NAME, "firstName")
    family_field_patronymic_name = (By.NAME, "patronymic")
    family_field_mail = (By.NAME, "emailAddress")
    family_field_gender = (By.XPATH,
                           "(.//*[normalize-space(text()) and normalize-space(.)='Пол *'])[1]/following::*[name()='svg'][1]")
    family_field_gender_f = (By.XPATH,
                             "(.//*[normalize-space(text()) and normalize-space(.)='Женский'])[1]/following::span[1]")
    family_field_data = (By.NAME, "dateOfBirth")

    select_cat_1 = (By.XPATH,
                    "(//div[@class='category-loyalty__container'])[1]")
    select_cat_2 = (By.XPATH,
                    "(//div[@class='category-loyalty__container'])[3]")
    select_cat_3 = (By.XPATH,
                    "(//div[@class='category-loyalty__container'])[5]")
    select_cat_4 = (By.XPATH,
                    "(//div[@class='category-loyalty__container'])[7]")
    select_cat_5 = (By.XPATH,
                    "(//div[@class='category-loyalty__container'])[9]")

    popup_close = (By.XPATH, "//*[@class='popup__header']//div[@class='popup__close']")
    popup_close_reg = (By.XPATH, "//*[@class='popup__close']")
    add_basket_big = (By.XPATH, "//span[@class='basket-sku-control__text']")
    add_basket_small = (By.XPATH, "//*[@class='sku-card-small-basket-control__default-control']")
    rise_item = (By.XPATH, "//*[@class='basket-sku-control__input']")
    move_to_basket = (By.XPATH, "//*[@href='/-ecom/basket/']")
    move_to_favorites = (By.XPATH, "//*[@href='/shoppinglist/']")
    field_promo = (By.XPATH, "//input[@class='input-field__control input-field__control--native']")
    notif_promo = (By.XPATH, "//*[@class='input-field__successed-text'][contains(.,'Вы получили скидку')]")
    # notif_promo = "//*[@class='input-field__successed-text'][text()='Вы получили скидку 40%']"
    continue_button_next = (By.XPATH, "//span[@class='button__inner'][text()='Продолжить оформление']")

    promo_get_price_tips = (By.XPATH, "//*[@class='price-label total-price-check__price total-price-check__price--promocode price-label--simple']")
    promo_get_price = (
        By.XPATH, "//*[@class='price-label total-price-check__price price-label--simple']")
    promo_get_price_final = (
        By.XPATH, "//*[@class='price-label total-price-check__price price-label--middle price-label--primary']")

    select_flat = (By.XPATH, "//*[@class='input-field__label'][contains(.,'Квартира/Офис *')]/following-sibling::input")
    click_delivery_button = (By.XPATH, "//span[@class='button__inner'][text()='Оформить доставку']")

    select_other_card = (By.XPATH, "//*[@data-test-id='pay-other-card']")
    select_card = (By.XPATH, "//*[@id='pan']") #//*[@data-test-id='pay-other-card']
    select_card_2 = (By.XPATH, "//*[@id='expiry']")
    select_card_3 = (By.XPATH, "//*[@id='cvc']")
    send_pay = (By.XPATH, "//span[text()='Оплатить']")
    click_success = (By.XPATH, "//*[@class='btn-half btn-success']")
    final_table = (By.XPATH, "//*[@class='thanks-for-order__title']")
    header_catalog = (By.XPATH, "(//*[@class='header__catalog'])[1]")
    header_title = (By.XPATH, "//*[@class='header-with-link__title']")
    select_cheese = (By.XPATH, "//*[@href='/catalog/moloko-syr-yajjco/syr/tofu/']")
    select_cheese_1 = (By.XPATH, "(//*[@href='/catalog/moloko-syr-yajjco/syr/'][contains(.,'Сыр')])[1]")
    select_cheese_tips = "//*[@itemprop][contains(.,'сыр')]"
    catalog_tag = "//*[@class='catalog-tag catalog-tag--node']"
    select_milk = (By.XPATH, "(//*[@href='/catalog/moloko-syr-yajjco/'][contains(.,'Молоко, сыр, яйцо')])[1]")

    # 381905
    tee_select = (By.XPATH, "//*[@class='sku-card-small sku-card-small--ecom'][contains(.,'Чай черный RICHARD Royal Ceylon Цейлонский байховый, 100пак')]")
    move_to_brand = (By.XPATH, "//*[@class='sku-card-tab-params__label'][contains(.,'Бренд')]")
    move_to_item = "//*[@class='tabs__tab sku-card-tab__nav-item tabs__tab--active'][contains(.,'Характеристики')]"
    brand_select = (By.XPATH, "//*[@class='link sku-card-tab-params__link'][contains(.,'RICHARD')]")
    brand_page = (By.XPATH, "//*[@class='catalog-view__title']")

    check_basket_delivery = (By.XPATH, "//*[@class='sku-notice-in-basket__text']")
    other_item = (By.XPATH, "//*[@class='button button--link button--middle button--secondary sku-card-in-basket__control-button'][contains(.,'Выбрать другой')]")

    basket_reserv = (By.XPATH, "//span[@class='basket-sku-control__text'][contains(.,'Зарезервировать')]")
    basket_clear = (By.XPATH, "//span[@class='button__inner'][text()='Да, очистить']")
    basket_clear_el = "//span[@class='sku-list-in-basket-control__text'][text()='Очистить корзину']"
    basket_clear_else = (By.XPATH, "//span[@class='sku-list-in-basket-control__text'][text()='Очистить корзину']")

    receipts_block_check = (By.XPATH, "//*[@ga-event-label][contains(.,'Рецепты')]")
    receipts_selections_check = "//*[@class='recipe-page__title recipe-similar-recipes__title']"
    receipts_all_categories = (By.XPATH, "//*[@ga-event-label='Рецепты|Все категории']")
    receipts_add_to_favorites = (By.XPATH, "//*[contains(@href,'https://stage.lentatest.com/recepty/list/v/--/')]//*[@class='icon favourite-action__icon']")
    receipts_add_to_favorites_one = (By.XPATH, "(//span[@class='recipe-ingredients-list__button'])[1]")
    receipts_add_to_favorites_two = (By.XPATH, "//*[@href='https://stage.lentatest.com/shoppinglist/?tab=customskus']")
    receipts_in_favorites = (By.XPATH, "//*[@class='tabs__tab'][contains(.,'Рецепты')]")
    receipts_cart = (By.XPATH, "//*[contains(@href,'https://stage.lentatest.com/recepty/list/v/--/')]")
    receipts_cart_txt = (By.XPATH, "//*[@class='favourite-action__text']")
    receipts_cart_offer = (By.XPATH, "(//span[@class='page-sharing-control__share-toggler-text'])[1]")
    receipts_cart_vk = (By.XPATH, "(//*[@class='page-sharing-control__social-icon page-sharing-control__social-icon--vk'])[1]")
    receipts_cart_f = (By.XPATH, "(//*[@class='page-sharing-control__social-icon page-sharing-control__social-icon--facebook'])[1]")
    receipts_cart_pre_sharing = (By.XPATH, "//*[@class='page-sharing-control__menu page-sharing-control__menu--opened']")
    receipts_cart_ingredients = (By.XPATH, "//*[@class='recipe-checkbox__icon recipe-checkbox__icon--checked']//following-sibling::div")
    receipts_cart_ingredients_one = "//*[@class='recipe-checkbox__icon recipe-checkbox__icon--checked']"
    receipts_cart_item = "//*[@class='recipe-grid__item']"
    receipts_cart_clear_filter = (By.XPATH, "//*[contains(@class,'clear-button--catalog')]")
    receipts_cart_send_txt = (By.XPATH, "//*[contains(@placeholder,'Введите название')]")

    move_to_carousel = (By.XPATH, "//*[@class='other-skus-slider__slides glide__slides']")
    carousel_left = (By.XPATH, "(//*[contains(@class,'glide__arrow glide__arrow')])[3]")
    carousel_right = (By.XPATH, "(//*[contains(@class,'glide__arrow glide__arrow')])[4]")

    container_address = (By.XPATH, "//*[contains(@class,'sku-store-container__store-search-toggler')]")
    container_search = (By.XPATH, "//*[@class='store-search-field__field']")
    container_stock = (By.XPATH, "//*[@class='stock stock--many']")
    container_address_location = (By.XPATH, "//*[@class='address-container__adress-location']")

    favorites_add = (By.XPATH, "//*[@class='favourite-sku-control sku-page-control__favourite-control']")
    favorites_add_small = (By.XPATH, "//*[@class='icon sku-card-small-favorite-control__icon']")
    favorites_remove = (By.XPATH, "//*[@class='favourite-sku-control favourite-sku-control--active sku-page-control__favourite-control']")
    rating_get = "//*[@class='sku-page__commenter-rating-overview-stars js-sku-page-commenter-rating-overview-stars']"
    feedback_rating = "//*[@class='rating comment__rating']"
    feedback_comment = "//*[@class='comment__content']"
    feedback_click = (By.XPATH, "//*[@class='sku-page__commenter-rating-overview-label js-comments-scroll-link']")
    feedback_click_down = (By.XPATH, "//*[@ga-event-action='goToFeedback']")
    share_item = (By.XPATH, "//*[@class='page-sharing-control__share-toggler-text']")
    share_item_favorites = (By.XPATH, "//*[@class='sharing-control']")
    share_send = (By.XPATH, "//*[@class='sharing-control__menu-title']")
    click_manual_item = (By.XPATH, "//*[@class='custom-skus-adding-form__control custom-skus-adding-form__control--default']")
    send_manual_item = (By.XPATH, "//*[@class='custom-skus-adding-form__control']")

    teg_get = (By.XPATH, "//*[@class='catalog-tag catalog-tag--node']")
    scu_len = "//*[@class='sku-card-small-container']"
    button_repair = (By.XPATH, "(//*[contains(@class ,'custom-sku-in-favourites__removed-button')])")




class ecom_create(AnyPage):

    @allure.step('Закрываем ситипикер')
    def close_citypicker(self):
        self.click_element_my(Locator.citypicker_close)
        self.allure_screenshot()

        return self

    @allure.step('Закрываем куки')
    def close_cookie(self):
        self.click_element_my(Locator.cookie_close)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем Вход/Регистрация')
    def click_btn_registration(self):
        self.click_element_my(Locator.registration_button)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем поле телефона')
    def click_phone(self):
        self.click_element_my(Locator.phone_field)
        self.allure_screenshot()
        return self

    @allure.step('Вводим номер телефона ')
    def send_phone(self, txt_phone):
        self.send_keys_slow(Locator.phone_field, txt_phone, 100)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем Поиск в каталоге и на сайте')
    def click_search_field(self):
        self.click_element_my(Locator.search_field)
        self.allure_screenshot()

        return self

    @allure.step('Вводим название ')
    def send_name(self, txt):
        self.send_keys_slow(Locator.search_field, txt, 100)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем найденное название')
    def click_search_result(self, txt):
        el = (By.XPATH,f"(//*[@class='text-highlight__fragment'][contains(.,'{txt}')])[1]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Забираем кв-о заголовков  для подсчета')
    def counter_num(self):
        txt = self.get_tag_text(Locator.counter)

        return txt

    @allure.step('Забираем текст')
    def get_text(self):
        txt = self.get_tag_text(Locator.page_title)

        return txt

    def rand_text(self):
        txt_rand = self.string_d

        return txt_rand

    def rand_letters(self):
        txt_rand = self.string_letters

        return txt_rand

    @allure.step('Кликаем кнопку Далее')
    def click_next_button(self):
        self.click_element_my(Locator.next_button)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем кнопку Подтвердить')
    def click_approve_button(self):
        self.click_element_my(Locator.approve_button)
        self.allure_screenshot()

        return self

    @allure.step('Устанавливаем значение для начального диапазона цены')
    def send_range_left(self):
        self.send_keys(Locator.range_left, Locator.blank)
        self.send_keys(Locator.range_left, "100")
        self.allure_screenshot()

        return self

    @allure.step('Устанавливаем значение для конечного диапазона цены')
    def send_range_right(self):
        self.click_element_my(Locator.range_right)
        time.sleep(2)
        self.send_keys(Locator.range_right, Locator.blank)
        self.send_keys(Locator.range_right, "200")
        self.send_keys_tab(Locator.range_right)
        time.sleep(3)
        self.allure_screenshot()

        return self

    @allure.step(' Проверяем диапазон цен >=100')
    def compare_all(self):
        el_l = self.get_count_elements_my(Locator.compare_left)
        assert el_l >= 1, "Диапазон не соответсвует >=100"

        el_l_min = self.get_count_elements_my(Locator.compare_left_min)
        assert el_l_min == 0, "Диапазон не соответсвует <= 99"

        el_l_max = self.get_count_elements_my(Locator.compare_left_max)
        assert el_l_max == 0, "Диапазон не соответсвует >=201"

        return self

    @allure.step('Перемещаемся к выбору производителя')
    def move_to_enterprise(self):
        self.move_to_element(Locator.enterprise_field)
        self.allure_screenshot()

        return self

    @allure.step('Перемещаемся к акциям')
    def move_to_actions(self):
        self.move_to_element(Locator.actions)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем показать ещё')
    def show_next(self):
        self.click_element_my(Locator.show_next)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем показать ещё')
    def show_next_2(self):
        self.click_element_my(Locator.show_next_2)
        self.allure_screenshot()

        return self

    # @allure.step('Выбираем бренд и проверяем текст бренда на странице товара  ')
    # def select_brand(self):
    #     txt_brand = self.get_tag_text(Locator.select_brand)
    #     k = txt_brand.casefold()[:-1]
    #     self.click_element_my(Locator.select_brand)
    #     time.sleep(3)
    #     txt_cart = self.get_tag_text(Locator.get_brand)
    #     r = txt_cart.casefold()
    #     assert k in r, "Текст бренда на странице товара не найден"
    #     self.allure_screenshot()
    #
    #     return self
    #
    # @allure.step('Выбираем бренд 4 ВОДЫ ДЮР-СО и проверяем текст бренда на странице товара')
    # def select_brand_2(self):
    #     txt_brand = self.get_tag_text(Locator.select_brand_2)
    #     k = txt_brand.casefold()[:-1]
    #     self.click_element_my(Locator.select_brand_2)
    #     time.sleep(3)
    #     txt_cart = self.get_tag_text(Locator.get_brand)
    #     r = txt_cart.casefold()
    #     assert k in r, "Текст бренда на странице товара не найден"
    #     self.allure_screenshot()
    #
    #     return self

    @allure.step('Выбираем бренд {txt}')
    def select_brand_all(self, txt):
        el = (By.XPATH, f"//span[@class='checkbox-field__label'][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Проверяем текст бренда {txt} на странице товара')
    def check_select_brand_all(self, txt):
        el = (By.XPATH, f"//h1[@class='catalog-view__title'][contains(.,'{txt}')]")
        # k = txt_brand.casefold()[:-1]
        txt_cart = self.get_text_my(el)
        # r = txt_cart.casefold()
        assert txt in txt_cart, "Текст бренда на странице товара не найден"
        self.allure_screenshot()

        return self


    @allure.step('Выбираем фабрику производитель бренда {}')
    def select_fabric(self, txt):
        el = (By.XPATH, f"//span[@class='checkbox-field__label'][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self


    @allure.step('Выбираем {txt}')
    def select_actions(self, txt):
        ur = (By.XPATH, f"//*[@ga-event-label='{txt}']")
        self.click_element_my(ur)
        self.allure_screenshot()

        return self

    # @allure.step('Выбираем ТК самовывоз ')
    # def select_address(self, address_market):
    #     time.sleep(1)
    #     self.click_element_my(Locator.select_delivery)
    #     time.sleep(1)
    #     self.click_element_my(Locator.select_delivery_or)
    #     time.sleep(1)
    #     self.click_element_my(Locator.select_city)
    #     self.click_element_my(Locator.select_city_1)
    #     self.click_element_my(Locator.select_market)
    #     self.send_keys_slow(Locator.select_market, address_market, 100)
    #     select_address_sample = (By.XPATH, f"//div[@class='stores-list-item__name'][contains(.,'{address_market}')]")
    #
    #     self.click_element_my(select_address_sample)
    #     self.click_element_my(Locator.select_market_final)
    #     time.sleep(7)
    #     self.allure_screenshot()
    #
    #     return self

    # @allure.step('Выбрать ТК самовывоз {city} из {address_market} ')
    # def select_address_self(self, address_market, city):
    #     time.sleep(1)
    #     self.click_element_my(Locator.select_delivery)
    #     time.sleep(1)
    #     self.click_element_my(Locator.select_delivery_or)
    #     time.sleep(1)
    #     self.click_element_my(Locator.select_city)
    #     select_city_sample = (By.XPATH, f"//span[@class='cities-list-item__name'][contains(.,'{city}')]")
    #     self.click_element_my(select_city_sample)
    #     # self.click_element_my(Locator.select_city_1)
    #     self.click_element_my(Locator.select_market)
    #     self.send_keys_slow(Locator.select_market, address_market, 100)
    #     select_address_sample = (By.XPATH, f"//div[@class='stores-list-item__name'][contains(.,'{address_market}')]")
    #
    #     self.click_element_my(select_address_sample)
    #     self.click_element_my(Locator.select_market_final)
    #     time.sleep(7)
    #     self.allure_screenshot()
    #
    #     return self

    # @allure.step('Выбрать доставку {address_market}')
    # def select_address_2(self, address_market, txt):
    #     self.click_element_my(Locator.select_delivery)
    #     #time.sleep(2)
    #     self.click_element_my(Locator.select_city)
    #     self.click_element_my(Locator.select_city_2)
    #     self.click_element_my(Locator.select_delivery_only)
    #     #time.sleep(1)
    #     switch_select_market_2 = (By.XPATH, f"(//*[@class='input-field__control input-field__control--native'])[{txt}]")
    #     self.click_element_my(switch_select_market_2)
    #     #time.sleep(1)
    #     self.send_keys_slow(switch_select_market_2, "zov", 100)
    #     #time.sleep(1)
    #     self.send_keys_backspase(switch_select_market_2)
    #     #time.sleep(1)
    #     self.send_keys_backspase(switch_select_market_2)
    #     #time.sleep(1)
    #     self.send_keys_delete(switch_select_market_2)
    #     #time.sleep(1)
    #     self.click_element_my(switch_select_market_2)
    #     self.send_keys_slow(switch_select_market_2, address_market, 100)
    #     self.allure_screenshot()
    #     select_address_sample = (By.XPATH, f"//li[@class='auto-suggest-field__suggestion'][text()='{address_market}']")
    #
    #     self.click_element_my(select_address_sample)
    #     #time.sleep(2)
    #     self.click_element_my(Locator.select_market_final_2)
    #     #time.sleep(7)
    #     self.allure_screenshot()
    #
    #     return self


    # @allure.step('Выбрать доставку {address_market} в {city}')
    # def select_address_any(self, address_market, city, txt):
    #     self.click_element_my(Locator.select_delivery)
    #     time.sleep(2)
    #     self.click_element_my(Locator.select_city)
    #     select_city_sample = (By.XPATH, f"//span[@class='cities-list-item__name'][contains(.,'{city}')]")
    #     self.click_element_my(select_city_sample)
    #
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
    #
    #
    #     self.send_keys_slow(switch_select_market_2, address_market, 100)
    #     select_address_sample = (By.XPATH, f"//li[@class='auto-suggest-field__suggestion'][text()='{address_market}']")
    #     # time.sleep(2)
    #     self.click_element_my(select_address_sample)
    #     # time.sleep(2)
    #     self.click_element_my(Locator.select_market_final_2)
    #     # time.sleep(7)
    #     self.allure_screenshot()
    #
    #     return self

    @allure.step('Выбрать доставку {address_market} в {city}')
    def select_address_delivery_any(self, address_market, city, txt):
        self.click_element_my(Locator.select_delivery)
        time.sleep(2)
        self.click_element_my(Locator.select_city)
        select_city_sample = (By.XPATH, f"//span[@class='cities-list-item__name'][contains(.,'{city}')]")
        self.click_element_my(select_city_sample)
        time.sleep(2)
        self.click_element_my(Locator.select_delivery_only)
        # time.sleep(1)
        switch_select_market_2 = (By.XPATH, f"(//*[@class='input-field__control input-field__control--native'])[{txt}]")
        self.click_element_my(switch_select_market_2)
        # time.sleep(1)
        self.send_keys_slow(switch_select_market_2, "zov", 100)
        # time.sleep(1)
        self.send_keys_backspase(switch_select_market_2)
        # time.sleep(1)
        self.send_keys_backspase(switch_select_market_2)
        # time.sleep(1)
        self.send_keys_delete(switch_select_market_2)
        # time.sleep(1)
        self.click_element_my(switch_select_market_2)
        self.send_keys_slow(switch_select_market_2, address_market, 100)
        self.allure_screenshot()
        select_address_sample = (By.XPATH, f"//li[@class='auto-suggest-field__suggestion'][text()='{address_market}']")
        # time.sleep(2)
        self.click_element_my(select_address_sample)
        time.sleep(2)
        self.click_element_my(Locator.select_market_final_2)
        # time.sleep(7)
        self.allure_screenshot()

        return self

    @allure.step('Выбрать самовывоз {address_market} из {city} ')
    def select_address_self_any(self, address_market, city, txt):
        time.sleep(1)
        self.click_element_my(Locator.select_delivery)
        time.sleep(1)
        self.click_element_my(Locator.select_city)
        select_city_sample = (By.XPATH, f"//span[@class='cities-list-item__name'][contains(.,'{city}')]")
        self.click_element_my(select_city_sample)
        time.sleep(1)
        self.click_element_my(Locator.select_delivery_or)
        time.sleep(1)
        # time.sleep(1)
        switch_select_market_2 = (By.XPATH, f"(//*[@class='input-field__control input-field__control--native'])[{txt}]")
        self.click_element_my(switch_select_market_2)
        # time.sleep(1)
        self.send_keys_slow(switch_select_market_2, "zov", 100)
        # time.sleep(1)
        self.send_keys_backspase(switch_select_market_2)
        # time.sleep(1)
        self.send_keys_backspase(switch_select_market_2)
        # time.sleep(1)
        self.send_keys_delete(switch_select_market_2)
        # time.sleep(1)
        self.click_element_my(switch_select_market_2)
        self.send_keys_slow(switch_select_market_2, address_market, 100)
        self.allure_screenshot()
        time.sleep(2)
        select_address_sample = (By.XPATH, f"//div[@class='stores-list-item__name'][contains(.,'{address_market}')]")
        self.click_element_my(select_address_sample)
        # time.sleep(2)
        self.click_element_my(Locator.select_market_final)
        # time.sleep(7)
        self.allure_screenshot()

        return self


    @allure.step(
        'Посмотреть, что на страничке отображаются товары со скидками(товары бейджем скидки в углу карточки)')
    def check_items(self):
        el_discount = self.get_count_elements(Locator.check_item)
        assert el_discount > 1, "Нет товаров со скидками"

        self.allure_screenshot()

        return self

    @allure.step(
        'Применить сортировки( По популярности,  По размеру скидки, Сначала дешевые, сначала дорогие, по рейнтигу)')
    def sort_items(self):
        self.click_element_my(Locator.sort_pop)
        self.click_element_my(Locator.sort_chip)
        self.allure_screenshot()
        time.sleep(5)
        self.click_element_my(Locator.sort_chip_1)
        self.click_element_my(Locator.sort_rich)
        self.allure_screenshot()
        time.sleep(5)
        self.click_element_my(Locator.sort_rich_1)
        self.click_element_my(Locator.sort_discount)
        self.allure_screenshot()
        time.sleep(5)
        self.click_element_my(Locator.sort_discount_1)
        self.click_element_my(Locator.sort_rating)
        self.allure_screenshot()

        return self

    @allure.step('Применить сортировки( По популярности,)')
    def sort_items_pop(self):
        self.click_element_my(Locator.sort_pop)
        self.click_element_my(Locator.sort_pop_1)
        self.allure_screenshot()

        return self

    @allure.step('Забираем данные из карточки')
    def get_items_one(self, txt):
        el =self.get_text_my(Locator.get_items_cart_one)
        print(el)
        assert txt == el, "Сортировка не верная"
        self.allure_screenshot()

        return self




    @allure.step('Применить фильтры по цене, по бренду')
    def sort_brand(self):
        self.click_element_my(Locator.select_brand)
        self.send_page_up(Locator.select_brand)
        self.allure_screenshot()

        return self

    @allure.step(
        'Нажать на ноду на страничке( отображаются товары согласно выбранной ноде) Например в дереве нод выбрать "Кондитерские изделия" ')
    def sort_noda(self):
        self.click_element_my(Locator.sort_noda)
        self.allure_screenshot()

        return self

    @allure.step('Заполнить блок личных даных')
    def send_family(self, txt, txt_n):
        # self.click_element_my(Locator.family_field)
        #self.send_keys_slow(Locator.family_field_last_name, txt, 100)
        self.send_keys_slow(Locator.family_field_first_name, txt, 100)
        #self.send_keys_slow(Locator.family_field_patronymic_name, txt, 100)
        # self.click_element_my(Locator.family_field_mail)
        # self.send_keys_slow(Locator.family_field_mail, txt_n + "@asd.tr", 100)
        #self.click_element_my(Locator.family_field_gender)
        #self.click_element_my(Locator.family_field_gender_f)
        self.click_element_my(Locator.family_field_data)
        self.send_keys(Locator.family_field_data, Locator.blank + Locator.blank)
        self.send_keys_slow(Locator.family_field_data, "17 11 2000", 100)
        self.send_keys_enter(Locator.family_field_data)
        self.click_element_my(Locator.family_field_mail)
        self.send_keys_slow(Locator.family_field_mail, txt_n + "@asd.tr", 100)
        self.allure_screenshot()

        return self

    @allure.step('Нажать кнопку Продолжить')
    def click_continue(self):
        self.click_element_my(Locator.continue_button)
        self.allure_screenshot()

        return self

    @allure.step('Выбрать категории')
    def select_cat(self):
        self.click_element_my(Locator.select_cat_1)
        self.click_element_my(Locator.select_cat_2)
        self.click_element_my(Locator.select_cat_3)
        self.click_element_my(Locator.select_cat_4)
        self.click_element_my(Locator.select_cat_5)
        self.allure_screenshot()

        return self

    @allure.step('Нажать кнопку Выбрать категории')
    def select_cat_button(self):
        self.click_element_my(Locator.select_cat_button)
        self.allure_screenshot()

        return self

    @allure.step('Закрыть popup- mail')
    def close_popup_m(self):
        time.sleep(1)
        self.click_element_my(Locator.popup_close)
        time.sleep(1)
        self.allure_screenshot()

        return self

    @allure.step('Закрыть popup- bonus')
    def close_popup_b(self):
        self.click_element_my(Locator.popup_close)
        self.allure_screenshot()

        return self

    @allure.step('Добавить товары в корзину 101869 1шт ,084250 1кг')
    def add_basket(self):
        self.goto_page(Locator.ecom_url_34)
        time.sleep(3)
        self.click_element_my(Locator.add_basket_big)
        time.sleep(5)
        self.allure_screenshot()
        self.goto_page(Locator.ecom_url_34_1)
        time.sleep(3)
        self.click_element_my(Locator.add_basket_big)
        time.sleep(5)
        self.allure_screenshot()
        self.click_element_my(Locator.rise_item)
        self.send_keys(Locator.rise_item, Locator.blank)
        time.sleep(1)
        self.send_keys(Locator.rise_item, "1")
        time.sleep(1)
        self.send_keys_enter(Locator.rise_item)
        time.sleep(2)
        self.click_element_my(Locator.move_to_basket)
        self.allure_screenshot()

        return self

    @allure.step('Ввести промокод vp97picq (вы получили скидку 40%)')
    def add_promocode(self, promo):
        self.click_element_my(Locator.field_promo)
        self.send_keys_slow(Locator.field_promo, promo, 100)
        self.allure_screenshot()

        return self

    # @allure.step('Нажать применить (скидка применилась)')
    # def click_apply(self):
    #     self.click_element_my(Locator.apply_button)
    #     time.sleep(3)
    #     self.allure_screenshot()
    #     el_p = self.get_text_my(Locator.notif_promo)
    #     assert el_p == Locator.txt_promo, "Уведомлений нет ,что скидка применилась "
    #
    #     return self

    @allure.step('Нажать применить (скидка применилась)')
    def click_apply(self, txt):
        self.click_element_my(Locator.apply_button)
        time.sleep(3)
        self.allure_screenshot()
        el_p = self.get_text_my(Locator.notif_promo)
        assert Locator.txt_promo + txt in el_p, "Уведомлений нет ,что скидка применилась "

        return self

    def get_price(self):
        time.sleep(2)
        promo = self.get_text_my(Locator.promo_get_price)

        return promo

    def get_price_final(self):
        time.sleep(2)
        promo = self.get_text_my(Locator.promo_get_price_final)

        return promo

    def get_price_tips(self):
        time.sleep(2)
        promo = self.get_text_my(Locator.promo_get_price_tips)

        return promo

    @allure.step('6.Нажать продолжить оформление')
    def continue_next(self):
        self.click_element_my(Locator.continue_button_next)
        self.allure_screenshot()

        return self

    @allure.step('В блоке итогов на чекауте цена соответствует цене на корзине')
    def check_price(self, txt, fin, delivery):

        el = self.get_text_my(Locator.promo_get_price)
        a = fin.split('\n')[:-1]
        b = txt.split('\n')[:-1]

        aa = ".".join(map(str, a))
        bb = ".".join(map(str, b))

        aaa = float(aa)
        bbb = float(bb)

        discount_price_10 = ('{:.1f}'.format(bbb / 100 * 10))

        x = float('{:.1f}'.format(bbb / 100 * .5))  # погрешность цены
        percent_price_10 = float(discount_price_10)  # %
        range_simple_price_10_1 = math.floor(percent_price_10)  # округляем
        range_simple_price_10_2 = math.ceil(percent_price_10)
        total_1 = ((lambda ex, et: ex - et)(range_simple_price_10_1, 1))
        total_2 = ((lambda ex, et: ex + et)(range_simple_price_10_2, 1))

        dl = float(delivery)
        final_1 = bbb - float(total_1) + dl
        final_2 = bbb - float(total_2) + dl

        assert final_1 >= aaa, "Проценты не верны - "
        assert final_2 <= aaa, "Проценты не верны + "

        # assert range_simple_price_10_2 <= (discount_price + (x * 4)), "We have a problem"
        # total = ((lambda a, b: a + b)(p_1, discount_price_real))
        self.allure_screenshot()

        return self

    @allure.step('В блоке итогов на чекауте цена соответствует цене на корзине')
    def check_price_40(self, txt):

        el = self.get_text_my(Locator.promo_get_price)
        a = el.split('\n')[:-1]
        b = txt.split('\n')[:-1]

        aa = ".".join(map(str, a))
        bb = ".".join(map(str, b))

        aaa = float(aa)
        bbb = float(bb)

        discount_price_10 = ('{:.1f}'.format(bbb / 100 * 40))

        x = float('{:.1f}'.format(bbb/ 100 * .5))  # погрешность цены
        percent_price_10 = float(discount_price_10)  # %
        range_simple_price_10_1 = math.floor(percent_price_10)  # округляем
        range_simple_price_10_2 = math.ceil(percent_price_10)
        total_1 = ((lambda ex, et: ex - et)(range_simple_price_10_1, 1))
        total_2 = ((lambda ex, et: ex + et)(range_simple_price_10_2, 1))

        final_1 = float(total_1) + aaa
        final_2 = float(total_2) + aaa

        assert final_1 <= bbb, "Проценты не верны - "
        assert final_2 >= bbb, "Проценты не верны + "

        # assert range_simple_price_10_2 <= (discount_price + (x * 4)), "We have a problem"
        # total = ((lambda a, b: a + b)(p_1, discount_price_real))
        self.allure_screenshot()

        return self

    def check_price_basket(self, txt):
        el = self.get_text_my(Locator.promo_get_price_final)
        assert el == txt, "Цена не соответствует цене на корзине"
        self.allure_screenshot()

        return self


    @allure.step('8.Выбрать номер квартиры')
    def select_flat(self):
        self.click_element_my(Locator.select_flat)
        self.send_keys_slow(Locator.select_flat, "11", 100)
        self.allure_screenshot()

        return self

    @allure.step('9.Нажать " Оформить доставку"')
    def click_delivery(self):
        self.click_element_my(Locator.click_delivery_button)
        self.allure_screenshot()

        return self

    @allure.step('Выбрать другую карту')
    def click_other_card(self):
        self.click_element_my(Locator.select_other_card)
        self.allure_screenshot()

        return self

    @allure.step('10.на странице оплаты выбрать карту 4111 1111 1111 1111 2024/12 123')
    def select_card(self):
        self.click_element_my(Locator.select_card)
        self.send_keys_slow(Locator.select_card, "4111 1111 1111 1111", 100)
        self.send_keys_slow(Locator.select_card_2, "1224", 100)
        self.send_keys_slow(Locator.select_card_3, "123", 100)
        self.allure_screenshot()

        return self

    @allure.step('11. Нажать оплатить')
    def send_pay(self):
        self.click_element_my(Locator.send_pay)
        self.allure_screenshot()

        return self

    @allure.step('12. Нажать "Success"')
    def click_success(self):
        self.click_element_my(Locator.click_success)
        self.allure_screenshot()

        return self

    @allure.step('13.Заказ оформлен, отображается страничка "Спасибо за заказ"')
    def final_table(self):
        el_f = self.get_text_my(Locator.final_table)
        assert el_f == Locator.txt_final, "Не отображается страничка Спасибо за заказ"
        self.allure_screenshot()

        return self

    @allure.step('14. Сумма = сумме на корзине/чекауте')
    def check_final(self, txt):
        el_pf = self.get_text_my(Locator.promo_get_price_final)
        assert el_pf == txt, "Сумма != сумме на корзине/чекауте"
        self.allure_screenshot()

        return self

    def small_wait(self):
        time.sleep(10)

        return self

    @allure.step('переходим на страницу {txt} ')
    def open_page_all(self, txt):
        self.goto_page(txt)
        time.sleep(2)
        self.allure_screenshot()

        return self


    @allure.step('Открыть каталог ')
    def open_catalog(self):
        self.move_to_element(Locator.header_catalog)
        time.sleep(2)
        self.allure_screenshot()

        return self

    @allure.step('Проверяем header {txt}')
    def get_header_title(self, txt):
        el = self.get_text_my(Locator.header_title)
        assert txt == el, "Нет названия"
        self.allure_screenshot()

        return self

    @allure.step('Открыть ноду Молко/сыр/яйцо ')
    def open_noda_milk(self):
        self.goto_page(Locator.ecom_url_24)
        time.sleep(2)
        self.allure_screenshot()

        return self

    @allure.step('2.  Открыть ноду  "Чай, кофе, какао"')
    def open_noda_coffee(self):
        self.goto_page(Locator.ecom_url_31)
        time.sleep(2)
        self.allure_screenshot()

        return self

    @allure.step('Открыть ноду  "Все для дома"')
    def open_noda_forhome(self):
        self.goto_page(Locator.ecom_url_26_3)
        time.sleep(2)
        self.allure_screenshot()

        return self

    @allure.step('3. Перейти в ноду "Алкогольные напитки" https://stage.lentatest.com/catalog/alkogolnye-napitki/')
    def open_noda_alco(self):
        self.goto_page(Locator.ecom_url_26)
        time.sleep(2)
        self.allure_screenshot()

        return self

    def select_alco_item(self):
        self.goto_page(Locator.ecom_url_26_1)
        time.sleep(2)
        self.allure_screenshot()

        return self

    @allure.step('4. Выбрать подкатегорию Сыр->Тофу')
    def select_cheese(self):
        self.click_element_my(Locator.select_cheese)
        self.allure_screenshot()

        return self

    @allure.step('Над товарами в переходить в ноды сыр->Молоко,сыр,яйцо->Каталог Убедиться что при переходе по нодам через хлебный крошки товары отображаются')
    def select_cheese_milk(self):
        self.send_keys_up_double()
        self.click_element_my(Locator.select_cheese_1)


        el_c = self.get_count_elements(Locator.select_cheese_tips)
        assert el_c >= 0, "Нет хлебных крошек на станице Сыр"

        self.click_element_my(Locator.select_milk)
        time.sleep(2)
        el_c = self.get_count_elements(Locator.select_cheese_tips)
        assert el_c >= 1, "Нет хлебных крошек на станице Сыр"

        self.allure_screenshot()

        return self



    @allure.step('3. Открыть товар 381905 Чай черный RICHARD Royal Ceylon Цейлонский байховый')
    def select_tee(self):
        self.click_element_my(Locator.tee_select)
        self.allure_screenshot()

        return self

    @allure.step('Пролистать вниз до Характеристик')
    def move_to_item(self):
        self.move_to_element(Locator.move_to_item)
        self.allure_screenshot()

        return self

    @allure.step('Переместиться на карусель')
    def move_to_carousel(self):
        self.move_to_element(Locator.move_to_carousel)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем карусель влево')
    def click_carousel_left(self):
        self.click_element_my(Locator.carousel_left)
        self.allure_screenshot()

        return self
    @allure.step('Кликаем карусель вправо')
    def click_carousel_right(self):
        self.click_element_my(Locator.carousel_right)
        self.allure_screenshot()

        return self

    @allure.step('Пролистать вниз до Бренд')
    def move_to_brand(self):
        self.move_to_element(Locator.move_to_brand)
        self.allure_screenshot()

        return self

    def move_to_tee(self):
        self.move_to_element(Locator.tee_select)
        self.allure_screenshot()

        return self

    @allure.step('В характеристиках нажать на бренд "Richard"')
    def select_brand(self):
        self.click_element_my(Locator.brand_select)
        self.allure_screenshot()

        return self

    @allure.step('6. Открывается страница бренда "Richard"')
    def page_brand(self, txt):
        el_t = self.get_text_my(Locator.brand_page)
        assert txt in el_t," Страница бренда не найденна"
        self.allure_screenshot()

        return self

    @allure.step('7. Перейти на бренд по прямой ссылке  https://stage.lentatest.com/brand/richard/')
    def go_to_brand(self):
        self.goto_page(Locator.ecom_url_31_b)
        self.allure_screenshot()

        return self

    @allure.step('Добавить в корзину')
    def basket_add(self):
        self.click_element_my(Locator.add_basket_big)
        self.allure_screenshot()
        time.sleep(4)
        return self

    @allure.step('Добавить в корзину')
    def basket_add_small(self):
        self.click_element_my(Locator.add_basket_small)
        self.allure_screenshot()
        time.sleep(4)
        return self



    @allure.step('Перейти в корзину')
    def basket_move(self):
        self.click_element_my(Locator.move_to_basket)
        self.allure_screenshot()

        return self

    @allure.step('Проверяем отображение условия')
    def basket_check_delivery(self, txt):
        time.sleep(2)
        self.allure_screenshot()
        el_t = self.get_text_my(Locator.check_basket_delivery)
        self.allure_screenshot()
        assert txt == el_t, " Неправильно отображается условие Товар недоступен для доставки"

        return self

    @allure.step('Перейти в избранное')
    def favorites_move(self):
        self.click_element_my(Locator.move_to_favorites)
        self.allure_screenshot()

        return self

    @allure.step('Перейти в избранном в рецепты')
    def favorites_receipts(self):
        self.click_element_my(Locator.receipts_in_favorites)
        self.allure_screenshot()

        return self




    @allure.step('Нажать Выбрать другой')
    def click_next_item(self):
        self.click_element_my(Locator.other_item)
        self.allure_screenshot()

        return self

    def switch_to_new_tab(self):
        time.sleep(1)
        self.switch_to_tab()
        self.allure_screenshot()

        return self

    @allure.step('8. Открывается нода "Каталог->Чай,кофе,какао-> Чай-> Черный чай" отображаются товары')
    def check_noda_black_tee(self):
        u = self.get_current_url()
        assert u == Locator.ecom_url_19, "URL не соответствует ожидаемому"
        self.allure_screenshot()

        return self

    @allure.step('10. Отображается страничка ноды https://stage.lentatest.com/catalog/alkogolnye-napitki/vino/belye-vina/')
    def check_noda_alco(self):
        u = self.get_current_url()
        assert u == Locator.ecom_url_26_2, "URL не соответствует ожидаемому"
        self.allure_screenshot()

        return self

    def clear_basket(self):
        el_b = self.get_count_elements(Locator.basket_clear_el)
        if el_b == 0:
            print("корзина пуста")
        else:
            self.click_element_my(Locator.basket_clear_else)
            self.click_element_my(Locator.basket_clear)

        return self


    def clear_favorites_receipt(self):
        i = self.get_count_elements("//*[@class='icon favourite-action__icon']")
        if i == 0:
            print("в избранном ничего нет")
        else:
            for i in range(1, i + 1):
                  x = i
                  r = (By.XPATH, f"(//*[@class='icon favourite-action__icon'])[{x}]")
                  elem = self.click_element_my(r)
                  time.sleep(0.1)
        self.allure_screenshot()
        return self

    @allure.step('Нажать сбросить все фильтры')
    def click_clear_item(self):
        self.click_element_my(Locator.receipts_cart_clear_filter)
        self.allure_screenshot()

        return self

    @allure.step('Вводим название {txt}')
    def send_receipt_item(self, txt):
        self.click_element_my(Locator.receipts_cart_send_txt)
        self.send_keys_slow(Locator.receipts_cart_send_txt, txt, 100)
        self.allure_screenshot()

        return self




    def page_up_local(self):
        self.send_keys_up_double()

        return self

    def page_down_local(self):
        self.send_keys_down_double()

        return self


    @allure.step('Проверяем отображение блока {txt}')
    def check_view_block(self, txt):
        el_u = (By.XPATH, f"//*[contains(@class,'recipe-start-page-list__title')][contains(.,'{txt}')] ")
        el = self.get_text_my(el_u)
        assert txt in el, f"Блок {txt} не найден"
        self.allure_screenshot()

        return self

    @allure.step('Проверяем отображение блока {txt}')
    def check_view_block_f(self, txt):
        el_u = (By.XPATH, "//*[contains(@class,'button button--link button--square recipe-favourites__button')]")
        el = self.get_text_my(el_u)
        #print(el)
        #assert el in txt, f"Блок {txt} не найден"
        self.allure_screenshot()

        return self

    @allure.step('Проверяем отображение подборок рецептов')
    def check_view_selections(self):
        el = self.get_count_elements(Locator.receipts_selections_check)
        assert el > 1, "Отображение подборок рецептов не корректно"
        self.allure_screenshot()

        return self


    @allure.step('Проверяем отображение заголовков - Рецепты с видео')
    def check_view_all_title(self, txt):
        el = (By.XPATH, f"//*[contains(@class,'recipe-page__title recipe-catalog__title')][contains(.,'{txt}')]")
        self.is_displayed(el)
        self.allure_screenshot()

        return self

    @allure.step('Нажать "{}"')
    def clic_all_categories(self, txt):
        el = (By.XPATH, f"//*[@ga-event-label='{txt}']")
        self.click_element_my(el)
        self.allure_screenshot()

        return self



    @allure.step('Добавить в избранное')
    def clic_add_favotites(self):
        self.click_element_my(Locator.receipts_add_to_favorites)
        self.allure_screenshot()

        return self

    @allure.step('Открываем карточку рецепта')
    def clic_receipt_cart(self):
        self.click_element_my(Locator.receipts_cart)
        self.allure_screenshot()

        return self

    @allure.step('Проверяем карточку рецепта')
    def check_receipt_cart(self, txt):
        el = self.get_text_my(Locator.receipts_cart_txt)
        assert el == txt, "В избранном - не корректно отображается"
        self.allure_screenshot()

        return self

    @allure.step('Кликаем - В избранном ')
    def click_receipt_cart_favorites(self):
        self.click_element_my(Locator.receipts_cart_txt)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем - поделиться')
    def click_receipt_cart_offer(self):
        self.click_element_my(Locator.receipts_cart_offer)
        self.allure_screenshot()

        return self

    @allure.step('Проверяем карточку рецепта VK and F')
    def check_receipt_cart_vk_f(self):
        self.is_displayed(Locator.receipts_cart_pre_sharing)
        self.is_displayed(Locator.receipts_cart_vk)
        self.is_displayed(Locator.receipts_cart_f)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем - ингредиенты')
    def click_receipt_cart_ingredients(self, txt1, txt2):
        el = self.get_count_elements(Locator.receipts_cart_ingredients_one)
        el1 = (By.XPATH, f"//*[@class='recipe-checkbox__icon recipe-checkbox__icon--checked']//following-sibling::div[text()='{txt1}']")
        el2 = (By.XPATH, f"//*[@class='recipe-checkbox__icon recipe-checkbox__icon--checked']//following-sibling::div[text()='{txt2}']")
        self.click_element_my(el1)
        self.click_element_my(el2)
        em = 2
        el3 = ((lambda a, b: a - b)(el, em))
        assert el3 + em == el, "Ингредиенты не выбрались"
        self.allure_screenshot()

        return self


    @allure.step('Кликаем - ингредиент')
    def click_receipt_cart_ingredient_one(self, txt):
        el = (By.XPATH, f"(//*[@class='recipe-checkbox__label'][text()='{txt}'])[1]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем - Блюда по ингредиентам')
    def click_receipt_ingredient_one(self, txt):
        el = (By.XPATH, f"//*[contains(@class,'recipe-ingredients-slider__card-title')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self


    def get_receipt_tag_tree(self, txt):
        elu = (By.XPATH, f"//*[text()='{txt}']/following::span[1]")
        el = self.get_text_my(elu)
        self.allure_screenshot()

        return el


    @allure.step('Проверяем чекбокс {}')
    def check_receipt_cart_checkbox(self, txt):
        el_u = (f"//*[@class='recipe-checkbox__icon recipe-checkbox__icon--checked']//following-sibling::div[text()='{txt}']")
        el = self.get_count_elements(Locator.receipts_cart_ingredients_one)
        assert el >= 1, f"Чекбокс {txt} не выбран"
        self.allure_screenshot()

        return self

    @allure.step('Проверяем кв-во рецептов на странице')
    def check_receipt_cart_item(self, txt):

        el = self.get_count_elements(Locator.receipts_cart_item)
        assert str(el) == txt, "Колличество рецептов на странице не корректно"
        self.allure_screenshot()

        return self


    @allure.step('Кликаем В избранное')
    def clic_add_cart_one(self):
        self.click_element_my(Locator.receipts_add_to_favorites_one)
        self.allure_screenshot()

        return self

    def check_add_cart_one(self, txt):
        el = self.get_text_my(Locator.receipts_add_to_favorites_two)
        self.allure_screenshot()
        #assert el == txt, "Кнопка не поменяла название на - Перейти в избранное"
        print(el)
        return self

    @allure.step('Кликаем tags {txt}')
    def clic_tag_item(self, txt):
        el = (By.XPATH, f"//*[@class='recipe-tags__item'][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Проверяем URL')
    def check_url_receipt(self, txt):
        el = self.get_current_url()
        assert el == txt, "URL не корректен"
        self.allure_screenshot()

        return self

#//*[@class='recipe-checkbox__icon recipe-checkbox__icon--checked']//following-sibling::div[contains(.,'весь год')]



    @allure.step('Принимаем  соглашение')
    def clic_approve_terms_ecom(self):
        self.click_element_my(Locator.approve_terms)
        self.allure_screenshot()

        return self

    @allure.step('Закрываем попап')
    def popup_close_reg(self):
        self.click_element_my(Locator.popup_close_reg)
        self.allure_screenshot()

        return self

    @allure.step('refresh')
    def refresh(self):
        self.refresh_the_page()
        self.allure_screenshot()

        return self

    @allure.step('Проверка контейнера на наличие {txt}')
    def check_container(self, txt):
        el_1 = "//*[@class='sku-page-control__store-container sku-store-container']"
        el_2 = "(//*[@class='sku-store-container__delivery-info-name'])[1]"
        el_3 = "(//*[@class='sku-store-container__delivery-info-name'])[2]"
        el_4 = "//*[@class='stock stock--many sku-store-container__stock']"
        g_el_1 = self.get_count_elements(el_1)
        assert g_el_1 == 1, "Контейнера нет"
        g_el_2 = self.get_count_elements(el_2)
        assert g_el_2 == 1, "Самовывоза нет"
        g_el_3 = self.get_count_elements(el_3)
        assert g_el_3 == 1, "Доставки нет"
        g_el_4 = self.get_count_elements(el_4)
        assert g_el_4 == 1, "Колличества нет"
        g_el = self.get_text_my(Locator.container_address)
        assert g_el in txt, "Адрес не верный"
        self.allure_screenshot()

        return self


    @allure.step('Переходим по адресу')
    def click_container_address(self):
        self.click_element_my(Locator.container_address)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем поиск по адресу')
    def click_container_search(self):
        self.click_element_my(Locator.container_search)
        self.allure_screenshot()

        return self

    @allure.step('Передаем адрес {txt}')
    def send_container_search(self, txt):
        self.send_keys_slow(Locator.container_search, txt, 100)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем результат поиска {txt}')
    def click_container_search_address(self, txt):
        ur = (By.XPATH, f"//*[@class='store-with-stock__name'][contains(.,'{txt}')]")
        self.click_element_my(ur)
        self.allure_screenshot()

        return self

    @allure.step('Отображается к-во товара {txt}')
    def check_container_search_address(self, txt):
        el = self.get_text_my(Locator.container_stock)
        assert el == txt, "К-во товара не отображается"
        self.allure_screenshot()

        return self

    @allure.step('Проверяем отображаемый адрес ')
    def check_address_location(self):
        el = self.get_text_my(Locator.container_address_location)
        print(el)
        self.allure_screenshot()

        return el

    @allure.step('Кликаем отзывы ')
    def click_feedback(self):
        self.click_element_my(Locator.feedback_click)
        self.allure_screenshot()

        return self

    @allure.step('Проверяем наличие рейтинга ')
    def get_rating(self):
        el = self.get_count_elements(Locator.rating_get)
        assert el == 1, "Рейтинг не отображается"
        self.allure_screenshot()

        return self

    @allure.step('Проверяем наличие рейтинга в отзывах ')
    def get_feed_rating(self):
        el = self.get_count_elements(Locator.feedback_rating)
        assert el >= 1, "Рейтинг не отображается"
        self.allure_screenshot()

        return self

    @allure.step('Проверяем наличие  отзывов ')
    def get_feed_comment(self):
        el = self.get_count_elements(Locator.feedback_comment)
        assert el >= 1, "Отзывы не отображается"
        self.allure_screenshot()

        return self

    @allure.step('Нажимаем - поделиться')
    def click_share(self):
        self.click_element_my(Locator.share_item)
        el_1 = "//*[@class='page-sharing-control__social-icon page-sharing-control__social-icon--vk']"
        el_2 = "//*[@class='page-sharing-control__social-icon page-sharing-control__social-icon--facebook']"
        g_el_1 = self.get_count_elements(el_1)
        g_el_2 = self.get_count_elements(el_2)
        assert g_el_1 == 1
        assert g_el_2 == 1
        self.allure_screenshot()

        return self

    @allure.step('Добавляем в избранное ')
    def click_favorites_item(self):
        self.click_element_my(Locator.favorites_add)
        self.allure_screenshot()

        return self

    @allure.step('Нажимаем - поделиться - в избранном')
    def click_share_favorites(self):
        self.click_element_my(Locator.share_item_favorites)
        self.allure_screenshot()

        return self

    @allure.step('Отображается окно {txt}')
    def check_share_send(self, txt):
        el = self.get_text_my(Locator.share_send)
        assert el == txt, "Отправить список не отобраилось"
        self.allure_screenshot()

        return self

    @allure.step('Кликаем  {txt}')
    def click_share_link(self, txt):
        ur = (By.XPATH, f"//*[@class='sharing-option__label'][contains(.,'{txt}')]")
        self.click_element_my(ur)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем  {txt}')
    def click_tab_tab(self, txt):
        ur = (By.XPATH, f"//*[@class='tabs__tab'][contains(.,'{txt}')]")
        self.click_element_my(ur)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем  - Введите товар вручную')
    def click_manual_send(self):
        self.click_element_my(Locator.click_manual_item)
        self.allure_screenshot()

        return self

    @allure.step('Вводим  {}')
    def send_manual_send(self, txt):
        self.send_keys_slow(Locator.send_manual_item, txt, 100)
        self.allure_screenshot()

        return self

    @allure.step('Нажимаем Enter')
    def send_enter_now(self):
        self.send_enter()
        self.allure_screenshot()

        return self

    @allure.step('Выбираем тэг {txt}')
    def get_tag_all(self, txt):
        el = (By.XPATH, f"//*[contains(@class,'catalog-tag catalog-tag--node')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем в избранное ')
    def click_favorites_small(self):
        time.sleep(1)
        self.click_element_my(Locator.favorites_add_small)
        time.sleep(1)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем из избранного ')
    def click_favorites_remove(self):
        time.sleep(1)
        self.click_element_my(Locator.favorites_remove)
        time.sleep(1)
        self.allure_screenshot()

        return self


    @allure.step('К-во карточек')
    def get_scu_all(self):
        el = self.get_count_elements(Locator.scu_len)
        self.allure_screenshot()

        return el

    @allure.step('Выбираем {txt}')
    def select_items_all(self, txt):
        el = (By.XPATH, f"//*[contains(@class,'catalog-category__link')][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Кликаем {txt}')
    def click_button_all(self, txt):
        el = (By.XPATH, f"//span[@class='button__inner'][contains(.,'{txt}')]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Удаляем {txt}')
    def click_button_delete(self, txt):
        el = (By.XPATH, f"(//*[contains(@class ,'custom-sku-in-favourites__button-text')])[{txt}]")
        self.click_element_my(el)
        self.allure_screenshot()

        return self

    @allure.step('Восстанавливаем  ')
    def click_button_repair(self):
        self.click_element_my(Locator.button_repair)
        self.allure_screenshot()

        return self






