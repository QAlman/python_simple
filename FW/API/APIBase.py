import json
import allure
import requests
import base64

from json.decoder import JSONDecodeError
from FW.FWBase import FWBase


class APIBase(FWBase):

    def get_base_url(self):
        if self.manager.settings.use_internal_link_in_api:
            return self.manager.settings.GLOBAL[self.manager.settings.branch]['API']['Internal_Link']
        else:
            return self.manager.settings.GLOBAL[self.manager.settings.branch]['API']['External_Link']

    def get_header(self, content_type=True, headers=None):
        if headers is None:
            headers = {}
        else:
            return headers

        # if self.manager.group_data.access_token == '':
        #     self.manager.api_assets.get_token()
        #
        # if self.manager.settings.Authorization:
        #     if self.manager.group_data.token_type == 'Bearer':
        #         headers['Authorization'] = str(self.manager.group_data.token_type + ' ' + self.manager.group_data.access_token)

        if content_type:
            headers['Content-Type'] = 'application/json'
            headers['Accept'] = 'application/json'

        return headers

    def encode_in_base64(self, string):
        str_bytes = base64.b64encode(string.encode("UTF-8"))
        return str_bytes.decode("UTF-8")

    @allure.step('requests_GET')
    def requests_GET(self, get_URL, params=None):
        headers = self.get_header()

        response = requests.get(get_URL, headers=headers, params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'
        self.allure_request('GET', get_URL, str(headers), "", str(response.status_code), response.text)

        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('requests_POST')
    def requests_POST(self, get_URL, body, params=None):
        headers = self.get_header()

        response = requests.post(get_URL, headers=headers, data=json.dumps(body), params=params)
        self.manager.group_data.response = response
        response.encoding = 'utf-8'

        self.allure_request('POST', get_URL, str(headers), str(body), str(response.status_code), response.text)

        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('requests_POST_code')
    def requests_POST_code(self, get_URL, body, params=None):
        headers = self.get_header_token()

        response = requests.post(get_URL, headers=headers, data=json.dumps(body), params=params)
        self.manager.group_data.response = response
        response.encoding = 'utf-8'

        self.allure_request('POST', get_URL, str(headers), str(body), str(response.status_code), response.text)

        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('requests_PUT')
    def requests_PUT(self, get_URL, body, params=None):
        headers = self.get_header()

        response = requests.put(get_URL, headers=headers, data=json.dumps(body), params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'
        self.allure_request('PUT', get_URL, str(headers), str(body), str(response.status_code), response.text)

        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('requests_DELETE')
    def requests_DELETE(self, get_URL, params=None, body=None):
        headers = self.get_header()

        response = requests.delete(get_URL, headers=headers, data=json.dumps(body), params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'
        self.allure_request('DELETE', get_URL, str(headers), "", str(response.status_code), response.text)

        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('requests_PATCH')
    def requests_PATCH(self, get_URL, body, params=None):
        headers = self.get_header()

        response = requests.patch(get_URL, headers=headers, data=json.dumps(body), params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'
        self.allure_request('PATCH', get_URL, str(headers), str(body), str(response.status_code), response.text)

        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('upload_file')
    def requests_upload_file(self, file_path, file_name, file_type, api_URL, body=None, params=None):
        headers = self.get_header(content_type=True)

        if body is None:
            files = {'file': (str(file_name), open(file_path, 'rb'), str(file_type))}
        else:
            files = {'file': (str(file_name), open(file_path, 'rb'), str(file_type), body)}

        response = requests.post(api_URL, headers=headers, files=files, params=params)
        response.encoding = 'utf-8'

        self.allure_request('POST', api_URL, str(headers), "files", str(response.status_code), response.text)
        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('добавление файла')
    def upload_file(self, file_path, api_URL, body=None):
        # формируем данные для загрузки файла на сервер
        # Получаем формат файла
        file_type = self.manager.work_with_file.get_MIME_file_format(file_path)
        # получаем имя файла из пути до файла
        file_name = self.manager.work_with_file.get_file_name_by_path(file_path)
        # загрузка файла на сервер
        response = self.requests_upload_file(file_path, file_name, file_type, api_URL, body)
        return response

    @allure.step('request')
    def allure_request(self, request_type, url, headers, body, status_code, response):
        pass

    def get_api_external_link(self, internal_link=False):
        if internal_link is True:
            return self.manager.settings.GLOBAL[self.manager.settings.branch]['API']['Internal_Link']
        else:
            return self.manager.GroupData.GLOBAL[self.manager.settings.branch]['API']['External_Link']


