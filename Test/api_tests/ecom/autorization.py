import allure
import pytest

import FW.WEB.AnyPage
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Authentication')
class TestApiCreateRequest(ApiBase):



    @allure.title('Authentication by code')
    @allure.severity(allure.severity_level.CRITICAL)
    def create_request_for_token(self, txt):
        body_data = {"username": f"{txt}", "verify_code": 0000, "grant_type": "call"}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        # response = requests.post("https://outsourcing-dev.verme.ru/api/v1/signin", data=body_data, headers=headers)
        # token = response.json()['access_token']

        return self



