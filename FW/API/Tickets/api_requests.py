import allure

from FW.API.APIBase import APIBase


class ApiRequests(APIBase):

    @allure.step('Get code.  POST /api/v1/signin')
    def post_requests_get_code(self, body, params=None):
        return self.requests_POST_code(self.get_base_url() + '/api/v1/signin', body, params)




    @allure.step('Authentication.  POST /api/v1/authentication/verifycallcode')
    def post_requests_code(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/v1/authentication/VerifyCode', body, params)


