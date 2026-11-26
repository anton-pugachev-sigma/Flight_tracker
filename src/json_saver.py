import json
from abc import ABC, abstractmethod

from src.airplanes import Airplane
from src.get_root import get_root


class BaseFileSaver(ABC):
    """Класс-шаблон для работы с информацией о самолетах в файле"""

    @abstractmethod
    def insert_info_plane(self, plane: Airplane) -> None:
        pass

    @abstractmethod
    def get_filtered_data(
        self,
        *,
        callsign: str | None = None,
        country: str | None = None,
        high_m: float | None = None,
        speed: float | None = None,
    ) -> list[Airplane]:
        pass

    @abstractmethod
    def delete_info_plane(self, plane: Airplane) -> None:
        pass


class JsonFileSaver(BaseFileSaver):
    """Класс для работы с информацией о самолетах в json файле"""

    __way: str
    base_path = get_root() / "data" / "planes.json"

    def __init__(self, way: str = base_path) -> None:
        self.__way = way

    @property
    def way(self):
        return self.__way

    def read_data(self):
        try:
            with open(self.way, "r", encoding="UTF-8") as file:
                planes_list = json.load(file)
        except FileNotFoundError:
            planes_list = []

        except json.JSONDecodeError:
            planes_list = []
        return planes_list

    def insert_info_plane(self, plane: Airplane) -> None:
        if not isinstance(plane, Airplane):
            raise TypeError
        planes_list = self.read_data()
        planes_list.append(plane.become_to_dict())
        with open(self.way, "w", encoding="UTF-8") as file:
            file.write(json.dumps(planes_list, ensure_ascii=False, indent=4))

    def get_filtered_data(
        self,
        *,
        callsign: str | None = None,
        country: str | None = None,
        high_m: float | None = None,
        speed: float | None = None,
    ) -> list[Airplane]:

        planes = self.read_data()
        filtered_planes = planes
        if callsign is not None:
            filtered_planes = [
                plane
                for plane in filtered_planes
                if plane["callsign"].lower() == callsign.lower()
            ]

        if country is not None:
            filtered_planes = [
                plane
                for plane in filtered_planes
                if plane["country"].lower() == country.lower()
            ]

        if high_m is not None:
            filtered_planes = [
                plane for plane in filtered_planes if plane["high_m"] == high_m
            ]

        if speed is not None:
            filtered_planes = [
                plane for plane in filtered_planes if plane["speed"] == speed
            ]

        final_planes = [Airplane(**plane) for plane in filtered_planes]
        return final_planes

    def delete_info_plane(self, plane: Airplane):
        if not isinstance(plane, Airplane):
            raise TypeError
        planes_list = self.read_data()
        len_start = len(planes_list)
        plane_dict = plane.become_to_dict()

        planes_list = [plan for plan in planes_list if plan != plane_dict]
        len_end = len(planes_list)

        if len_start != len_end:
            with open(self.way, "w", encoding="UTF-8") as file:
                file.write(json.dumps(planes_list, ensure_ascii=False, indent=4))


# a  = JsonFileSaver()
# plane_a = Airplane("SWR438A", "UK", 420.0, 4000.0)
# a.insert_info_plane(plane_a)
# path = get_root() / 'data' / 'planes.json'
# with open(path, 'r', encoding='Utf-8') as file:
#     res = json.load(file)
#     print(type(res))
# print(res[0])
