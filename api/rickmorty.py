import requests

BASE_URL = 'https://rickandmortyapi.com/api/'

class RickMortyAPI:
    def __init__(self, base_url=BASE_URL, timeout=10):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout

    def get(self, resource, item_id):
        url = f'{self.base_url}/{resource}/{item_id}'
        response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()