import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - Outsourcing')
@allure.story('40: 2-881 :   Проверка api со страниц Планирование смен аутсорсинга, Табели аутсорсинга, Планирование смен агенств ')
class TestOutsourcing_40(WebBase):

    @allure.title('40: 2-881 :  Проверка api со страниц Планирование смен аутсорсинга, Табели аутсорсинга, Планирование смен агенств - Версия1')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link(name="2-881 :  Проверка api со страниц Планирование смен аутсорсинга, Табели аутсорсинга, Планирование смен агенств - Версия1",
                 url="https://testlink.verme.ru/linkto.php?tprojectPrefix=2&item=testcase&id=2-880")
    @allure.description("Позитивный тест 2-881 :  Проверка api со страниц Планирование смен аутсорсинга, Табели аутсорсинга, Планирование смен агенств - Версия1")
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.test2_881
    #@pytest.mark.skip
    def test_outsourcing_40(self):
        outsourcing = self.APP.web_activity.button_to_outsourcing()

        v = "test_outsourcing_2023"
        outsourcing.send_login(v)
        v = "freftTRHTRH!@#13564"
        outsourcing.send_password(v)
        outsourcing.click_signin()
        outsourcing.small_time()


        """
        Необходимо уточнить по поводу возможности проверки api 
        и механизму


        """




