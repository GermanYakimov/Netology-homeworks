import requests
from pprint import pprint
from urllib.parse import *


App_ID = '5936713ef28f4d289a233a9ca269e899'
access_token = 'AQAAAAAdztsdAASt1aMiDHn8mE2kilp1kssbM5E'


class YMBase:

    def __init__(self, access_token):
        self.access_token = access_token

    def get_headers(self):
        return {
            'Authorization': 'OAuth ' + self.access_token,
            'Content_type': 'application/x-yametrika+json'
        }



class User(YMBase):
    URL = 'https://api-metrika.yandex.ru/management/v1/'

    def get_counters(self):
        response = requests.get(
            urljoin(self.URL, 'counters'),
            headers=self.get_headers()
        )

        return response.json()['counters']

    def get_counter_info(self, counter_id):
        response = requests.get(
            urljoin(self.URL, 'counter/{}'.format(counter_id)),
            headers=self.get_headers()
        )

        return response.json()


class Counter(YMBase):
    STAT_URL = 'https://api-metrica.yandex.ru/stat/v1/data'

    def __init__(self, id, access_token):
        self.id = id
        super().__init__(access_token)

    def get_visits(self):
        headers = self.get_headers()

        params = {
            'id': self.id,
            'metrics': 'ym:s:visits'
        }

        return requests.get(self.STAT_URL, params=params, headers=headers).json()

    def get_views(self):
        headers = self.get_headers()

        params = {
            'id': self.id,
            'metrics': 'ym:s:pageviews'
        }

        return requests.get(self.STAT_URL, params=params, headers=headers).json()

    def get_users(self):
        headers = self.get_headers()

        params = {
            'id': self.id,
            'metrics': 'ym:s:users'
        }

        return requests.get(self.STAT_URL, params=params, headers=headers).json()


user = User(access_token)
counters = user.get_counters()

print('Visits: ')
for c in counters:
    counter = Counter(c['id'], access_token)
    pprint(counter.get_visits())

print('\nViews: ')
for c in counters:
    counter = Counter(c['id'], access_token)
    pprint(counter.get_views())

print('\nUsers: ')
for c in counters:
    counter = Counter(c['id'], access_token)
    pprint(counter.get_users())
