#!/usr/bin/env python3
import requests

class Requests():

    def __init__(self, url, login, password):
        self.URL = url
        self.LOGIN = login
        self.PASSWORD = password
        self._authentication = {'login': self.LOGIN, 'password': self.PASSWORD}
        self.token = {}

    def token_authentication_api(self):
        result = requests.post(f'{self.URL}api/v2/auth/login/', json=self._authentication)
        self.token = {'Authorization': f'Bearer {result.json()["token"]}'}

    def post(self, data, path='', file=False):
        if file:
            return requests.post(f'{self.URL}{path}', files={'file': open(data, 'rb')}, headers=self.token).json()['data']
        else:
            res = requests.post(f'{self.URL}{path}', json=data, headers=self.token)
            return res.json()

    def get(self, path='', get_object=False):
        if get_object:
            return requests.get(f'{self.URL}{path}', headers=self.token)
        else:
            return requests.get(f'{self.URL}{path}', headers=self.token).json()

    def delete(self, data, path=''):
        return requests.delete(f'{self.URL}{path}', json=data, headers=self.token).json()
