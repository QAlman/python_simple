import time
from random import random
import allure
import pytest
import FW.WEB.ecom.ecom_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Ecom')
@allure.story('Смок № 14')
class TestEcom_14(WebBase):

    @allure.title('Смок 14 Отзывы,комментарии,шаринг')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_ecom_14(self):

        ecom = self.APP.web_activity.button_to_ecom()
        self.APP.web_steps.step_test_14()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        ecom.select_address_self_any(address_market, city, sw)
        #time.sleep(4)
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_14_1)
        ecom.get_rating()
        ecom.click_feedback()
        ecom.get_feed_rating()
        ecom.get_feed_comment()
        ecom.page_up_local()
        ecom.click_share()
        ecom.click_favorites_item()
        ecom.open_page_all(FW.WEB.ecom.ecom_test.Locator.ecom_url_14)
        ecom.click_share_favorites()
        z = "Отправить список"
        ecom.check_share_send(z)
        o = "Ссылка"
        ecom.click_share_link(o)
        v = "Список"
        ecom.click_tab_tab(v)
        ecom.click_manual_send()
        vv = "картофель"
        ecom.send_manual_send(vv)
        ecom.send_enter_now()
        vvv = "макароны"
        ecom.send_manual_send(vvv)
        ecom.send_enter_now()
        ecom.click_share_favorites()
        z = "Отправить список"
        ecom.check_share_send(z)
        o = "Ссылка"
        ecom.click_share_link(o)







