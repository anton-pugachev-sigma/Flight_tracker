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
    def get_filtered_data(self, filtered_list: list):
        pass

    @abstractmethod
    def delete_info_plane(self, plane: Airplane) -> None:
        pass


class JsonFileSaver(BaseFileSaver):
    way: str
    base_path = get_root() / "data" / "planes.json"

    def __init__(self, way: str = base_path) -> None:
        self.way = way

    def insert_info_plane(self, plane: Airplane) -> None:
        try:
            with open(self.way, "r", encoding="UTF-8") as file:
                planes_list = json.load(file)
        except FileNotFoundError:
            planes_list = []

        except json.JSONDecodeError:
            planes_list = []

        planes_list.append(plane.become_to_dict())
        with open(self.way, "w", encoding="UTF-8") as file:
            file.write(json.dumps(planes_list, ensure_ascii=False, indent=4))

    def get_filtered_data(self, filtered_list: list):
        pass

    def delete_info_plane(self, plane: Airplane):
        pass


# a  = JsonFileSaver()
# plane_a = Airplane("SWR438A", "USA", 420.0, 200.0)
# a.insert_info_plane(plane_a)
# path = get_root() / 'data' / 'planes.json'
# with open(path, 'r', encoding='Utf-8') as file:
#     res = json.load(file)
#     print(type(res))
# print(res[0])
