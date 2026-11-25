from abc import ABC, abstractmethod

import requests


class APIClient(ABC):
    """Класс шаблон для работы с API сервисами"""

    @abstractmethod
    def get_cords(self, country: str):
        pass

    @abstractmethod
    def get_info_planes(self, country: str):
        pass


class APIPlanes(APIClient):
    """Класс для получения информации о самолетах, находящихся в пределах заданной страны"""

    # country: str
    def __init__(self) -> None:
        self.url_nominatim = "https://nominatim.openstreetmap.org/search"
        self.url_opensky = "https://opensky-network.org/api/states/all"

    def get_cords(self, country: str) -> list[float]:
        params = {"country": country, "format": "json"}
        headers = {"User-Agent": "super_user"}
        response = requests.get(url=self.url_nominatim, params=params, headers=headers)
        res = response.json()

        cords = list(map(float, res[0]["boundingbox"]))
        return cords

    def get_info_planes(self, country: str):
        url = self.url_opensky
        cords = self.get_cords(country)
        params = {
            "lamin": cords[0],
            "lomin": cords[1],
            "lamax": cords[2],
            "lomax": cords[3],
        }

        headers = {"User-Agent": "super_user"}
        response = requests.get(url=url, params=params, headers=headers)
        res = response.json()
        return res
