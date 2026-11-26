from abc import ABC, abstractmethod
from typing import Any


class BasePlanes(ABC):
    """Класс-шаблон для работы с информацией о самолетах."""

    @abstractmethod
    def equal_speed(self, other) -> bool:
        pass

    @abstractmethod
    def best_speed(self, other) -> bool:
        pass

    @abstractmethod
    def equal_high_m(self, other) -> bool:
        pass

    @abstractmethod
    def best_high_m(self, other) -> bool:
        pass


class Airplane(BasePlanes):
    """Класс для работы с информацией о самолетах."""

    __callsign: str
    __country: str
    __high_m: float
    __speed: float

    @staticmethod
    def valid_data(callsign: str, country: str, high_m: float, speed: float) -> tuple:
        if not isinstance(callsign, str):
            raise TypeError

        if not callsign.strip():
            raise ValueError

        if not isinstance(country, str):
            raise TypeError

        if high_m is None or high_m < 0:
            high_m = 0.0
        if not isinstance(high_m, float):
            raise TypeError

        if speed is None:
            speed = 0.0

        if not isinstance(speed, float):
            raise TypeError
        return callsign, country, high_m, speed

    def __init__(
        self, callsign: str, country: str, high_m: float, speed: float
    ) -> None:
        callsign, country, high_m, speed = self.valid_data(
            callsign, country, high_m, speed
        )
        self.__callsign = callsign
        self.__country = country
        self.__high_m = high_m
        self.__speed = speed

    @property
    def callsign(self):
        return self.__callsign

    @property
    def country(self):
        return self.__country

    @property
    def high_m(self):
        return self.__high_m

    @property
    def speed(self):
        return self.__speed

    def equal_speed(self, other) -> bool:
        if not isinstance(other, Airplane):
            raise TypeError
        return self.speed == other.speed

    def best_speed(self, other) -> bool:
        if not isinstance(other, Airplane):
            raise TypeError

        return self.speed > other.speed

    def equal_high_m(self, other) -> bool:
        if not isinstance(other, Airplane):
            raise TypeError

        return self.high_m == other.high_m

    def best_high_m(self, other) -> bool:
        if not isinstance(other, Airplane):
            raise TypeError

        return self.high_m > other.high_m

    @classmethod
    def cast_to_object_list(cls, planes_data: dict[str, Any]) -> list:
        list_planes = planes_data["states"]

        planes = []

        for data in list_planes:
            cls.valid_data(data[1], data[2], data[7], data[9])
            plane = cls(data[1], data[2], data[7], data[9])
            planes.append(plane)
        return planes

    def become_to_dict(self) -> dict[str, Any]:
        plane_dict = {
            "callsign": self.__callsign,
            "country": self.__country,
            "high_m": self.__high_m,
            "speed": self.__speed,
        }
        return plane_dict
