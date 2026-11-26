from unittest.mock import patch

import pytest

from src.api_clients import APIPlanes


@patch("requests.get")
def test_get_cords_success(mock_response, get_cord) -> None:
    mock_response.return_value.json.return_value = get_cord
    test_api_plane = APIPlanes()
    res = test_api_plane.get_cords("Russia")
    assert res[0] == 41.1850968
    assert res[2] == -180.0000000


@patch("requests.get")
def test_get_info_planes_success(mock_response, get_info_plane, get_cord) -> None:
    mock_response.return_value.json.side_effect = [get_cord, get_info_plane]
    test_api_plane = APIPlanes()
    info_planes = test_api_plane.get_info_planes("Russia")
    assert info_planes["states"][0][2] == "Estonia"
    assert info_planes["states"][0][1].strip() == "MBU9AG"
