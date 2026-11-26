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


def test_insert_info_plane_raises_type_error(tmp_path, get_plane) -> None:
    plane = get_plane
    path = tmp_path / "test.json"
    file_1 = JsonFileSaver(path)
    file_1.insert_info_plane(plane)
    with pytest.raises(TypeError):
        file_1.insert_info_plane(0)  # type: ignore


def test_get_filtered_data_success(tmp_path, get_planes_json) -> None:
    planes = get_planes_json
    path = tmp_path / "test.json"
    with open(path, "w", encoding="Utf-8") as file:
        file.write(json.dumps(planes, ensure_ascii=False, indent=4))

    file_1 = JsonFileSaver(path)
    res = file_1.get_filtered_data(country="USA")

    for pl in res:
        assert pl.country == "USA"
    res_2 = file_1.get_filtered_data(speed=200.0)

    for plane in res_2:
        assert plane.speed == 200.0


def test_delete_info_plane_success(tmp_path, get_plane, get_planes_json) -> None:
    planes = get_planes_json
    path = tmp_path / "test.json"
    with open(path, "w", encoding="Utf-8") as file:
        file.write(json.dumps(planes, ensure_ascii=False, indent=4))

    with open(path, "r", encoding="Utf-8") as file:
        res = json.load(file)

    file_1 = JsonFileSaver(path)
    file_1.delete_info_plane(get_plane)

    with open(path, "r", encoding="Utf-8") as file:
        res_2 = json.load(file)

    assert res != res_2


def test_delete_info_plane_raises_type_error(tmp_path, get_planes_json) -> None:
    path = tmp_path / "test.json"
    file_1 = JsonFileSaver(path)
    with pytest.raises(TypeError):
        file_1.delete_info_plane(0)  # type: ignore


# return Airplane("SWR438A", "USA", 4000.0, 200.0)
