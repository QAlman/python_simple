import allure

from FW.API.APIBase import APIBase


class ApiTasks(APIBase):

    @allure.step('Список задач. POST /api/Tasks/Filter')
    def post_tasks_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Tasks/Filter', body, params)

    @allure.step('Получение задачи по ключу. GET /api/Tasks/{id}')
    def get_tasks_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Tasks/{id}', params)

