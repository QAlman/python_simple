import allure
import pytest

import FW.WEB.AnyPage
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Authentication')
class TestApiCreateRequest(ApiBase):

    @allure.title('Authentication by code')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_request_code_a(self):
        # # Подготовка тела запроса
        # service_search = {
        #     "search": "Тестовая услуга создана не человеком =)",
        #     "filter":
        #         {
        #             "type" :"Service",
        #             "serviceTypes": ["Normal"]
        #         },
        #     "resultView": "List"
        #
        # }
        # #
        # services = self.APP.api_services_for_tickets.post_services_for_tickets_filter(service_search)

        # #
        # description = "API Test Description " + self.APP.time.get_time_now()

        #
        request_body = {
                          "card": "string",
                          "code": f"{FW.WEB.AnyPage.Locator.phone_code_api}",
                          "password": "string",
                          "firstName": "string_111",
                          "lastName": "string_asdeq",
                          "dateOfBirth": "2022-08-17T08:31:02.986Z",
                          "phone": f"{FW.WEB.AnyPage.AnyPage.string_d}",
                          "personalDataProcessingAgreed": True,
                          "isMobileApp": True,
                          "hash": "string",
                          "campaignId": "string"
                        }

        request = self.APP.api_requests.post_requests_code(request_body)
        print(request)

