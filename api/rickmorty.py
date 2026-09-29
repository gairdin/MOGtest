import requests

# базовый адрес апи рика и морти
API_URL = "https://rickandmortyapi.com/api/"


class RickMortyAPI:
    def __init__(self, base_url=API_URL, timeout=10):
        # убираю слэш в конце, иначе будет двойной слэш в урле
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, resource, item_id):
        # собираю урл вручную, потому что жду готовую строку
        url = self.base_url + "/" + resource + "/" + str(item_id)
        resp = requests.get(url, timeout=self.timeout)
        # если придет 404 или 500 - тут вылетит ошибка, это норм
        resp.raise_for_status()
        data = resp.json()
        return data