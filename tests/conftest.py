from typing import Any

import pytest

from src.airplanes import Airplane


@pytest.fixture
def get_info_plane() -> dict[str, Any]:
    return {
        "states": [
            [
                "511187",
                "MBU9AG  ",
                "Estonia",
                1795594958,
                1795594959,
                6.6741,
                46.9037,
                11277.6,
                False,
                218.48,
                230.35,
                0.33,
                None,
                11193.78,
                "6665",
                False,
                0,
            ],
            [
                "471d64",
                "WZZ4Q   ",
                "Hungary",
                1795594959,
                1795594959,
                8.4878,
                47.1744,
                9174.48,
                False,
                201.67,
                158.61,
                6.18,
                None,
                9144,
                "6731",
                False,
                0,
            ],
            [
                "300a87",
                "ITY217  ",
                "Italy",
                1795594959,
                1795594959,
                8.5774,
                46.7238,
                10447.02,
                False,
                202.61,
                174.46,
                -8.78,
                None,
                10424.16,
                "7303",
                False,
                0,
            ],
        ],
        "time": 1795594960,
    }


@pytest.fixture
def get_cord() -> list[dict[str, Any]]:
    return [
        {
            "addresstype": "country",
            "boundingbox": ["41.1850968", "82.0586232", "-180.0000000", "180.0000000"],
            "class": "boundary",
            "display_name": "Россия",
            "importance": 0.9369385991476754,
            "lat": "64.6863136",
            "licence": "Data © OpenStreetMap contributors, ODbL 1.0. "
            "http://osm.org/copyright",
            "lon": "97.7453061",
            "name": "Россия",
            "osm_id": 60189,
            "osm_type": "relation",
            "place_id": 159039381,
            "place_rank": 4,
            "type": "administrative",
        }
    ]


@pytest.fixture
def get_plane() -> Airplane:
    return Airplane("SWR438A", "USA", 4000.0, 200.0)


@pytest.fixture
def get_planes_json() -> list[dict[str, Any]]:
    return [
        {"callsign": "SWR438A", "country": "USA", "high_m": 420.0, "speed": 200.0},
        {"callsign": "SWR438A", "country": "Russia", "high_m": 420.0, "speed": 210.0},
        {"callsign": "SWR438A", "country": "Russia", "high_m": 420.0, "speed": 200.0},
        {"callsign": "SWR438A", "country": "UK", "high_m": 420.0, "speed": 4000.0},
        {"callsign": "SWR438A", "country": "USA", "high_m": 4000.0, "speed": 200.0},
    ]
