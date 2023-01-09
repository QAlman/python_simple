import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 5')
class TestEcom_5(WebBase):

    @allure.title('Смок 5 Фильтрация по Ноде,Тегу, бренду, производителю')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_5(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_5()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        ecom.select_address_self_any(address_market, city, sw)
        #ecom.page_up_local()
        ecom.open_noda_milk()
        z = "alti"
        ecom.get_tag_all(z)
        o = ecom.get_scu_all()
        assert o >= 2, "Карточек больше"
        ecom.get_tag_all(z)
        v = ecom.get_scu_all()
        assert v >= 2, "Карточек меньше"
        zz = "Сыр"
        ecom.select_items_all(zz)
        oo = "Плавленный сыр"
        ecom.select_items_all(oo)
        vv = "HOCHLAND"
        ecom.select_brand_all(vv)
        zzz = ecom.get_scu_all()
        assert zzz >= 8, "Карточек больше"
        ooo = "Хохланд Руссланд"
        ecom.select_fabric(ooo)
        vvv = ecom.get_scu_all()
        assert vvv == 2, "Карточек больше"








