import allure
import requests

from FW.API.APIBase import APIBase


class Token(APIBase):

    @allure.step('Получение токена для пользователя {user_name}. get_token')
    def get_token(self, user_name='SystemOperator'):
        """
        Метод получения АПИ токена
        :param user_name: Имя пользователя берётся из пользователей указанных в файле settings для запускаемого branch
        :return:
        """
        url = self.manager.settings.GLOBAL[self.manager.settings.branch]['API']['AUTH_URL']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.manager.settings.GLOBAL[self.manager.settings.branch]['USERS'][user_name]['User_id'],
            'client_secret': self.manager.settings.GLOBAL[self.manager.settings.branch]['USERS'][user_name]['client_secret'],
        }
        response = requests.post(url, headers=headers, data=body)

        self.manager.group_data.response = response
        response = response.json()
        self.manager.group_data.access_token = response['access_token']
        self.manager.group_data.expires_in = response['expires_in']
        self.manager.group_data.token_type = response['token_type']
