import json

import pytest

from src.json_saver import JsonFileSaver


def test_insert_info_plane_success(tmp_path, get_plane) -> None:
    plane = get_plane
    path = tmp_path / "test.json"
    file_1 = JsonFileSaver(path)
    file_1.insert_info_plane(plane)
    with open(path, "r", encoding="Utf-8") as file:
        res = json.load(file)
    assert res[-1] == {
        "callsign": "SWR438A",
        "country": "USA",
        "high_m": 4000.0,
        "speed": 200.0,
    }


# return Airplane("SWR438A", "USA", 4000.0, 200.0)
