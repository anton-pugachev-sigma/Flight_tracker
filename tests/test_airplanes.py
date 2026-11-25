import pytest

from src.airplanes import Airplane


def test_init_airplane_object_success() -> None:
    airplane = Airplane("SWR438A", "USA", 4000.0, 200.0)
    assert airplane.callsign == "SWR438A"
    assert airplane.country == "USA"
    assert airplane.high_m == 4000.0
    assert airplane.speed == 200.0


def test_bad_speed_raise_error() -> None:
    with pytest.raises(TypeError):
        Airplane("SWR438A", "USA", 4000, "очень быстро")  # type: ignore


#
def test_none_args_airplane_returns_zero() -> None:
    airplane = Airplane("SWR438A", "USA", None, None)  # type: ignore
    assert airplane.high_m == 0.0
    assert airplane.speed == 0.0


def test_bad_high_m_raise_error() -> None:
    with pytest.raises(TypeError):
        Airplane("SWR438A", "USA", "200.0", 200.0)  # type: ignore


def test_bad_country_raise_error() -> None:
    with pytest.raises(TypeError):
        Airplane("SWR438A", 123, 20.0, 200.0)  # type: ignore


def test_bad_callsign_raise_error() -> None:
    with pytest.raises(ValueError):
        Airplane("", "russia", 20.0, 200.0)


def test_equal_speed_success() -> None:
    airplane_1 = Airplane("SWR438A", "USA", 4000.0, 200.0)
    airplane_2 = Airplane("SWR438A", "USA", 4000.0, 200.0)

    assert airplane_1.equal_speed(airplane_2) is True


def test_equal_speed_diff_class_raise_error() -> None:
    airplane_1 = Airplane("SWR438A", "USA", 4000.0, 200.0)
    num = 10

    with pytest.raises(TypeError):
        airplane_1.equal_speed(num)


def test_best_speed_success() -> None:
    airplane_1 = Airplane("SWR438A", "USA", 4000.0, 210.0)
    airplane_2 = Airplane("SWR438A", "USA", 4000.0, 200.0)

    assert airplane_1.best_speed(airplane_2) is True


def test_best_speed_diff_class_raise_typeerror() -> None:
    airplane_1 = Airplane("SWR438A", "USA", 4000.0, 210.0)
    string = "mumu"

    with pytest.raises(TypeError):
        airplane_1.best_speed(string)


def test_equal_high_m_success() -> None:
    airplane_1 = Airplane("SWR438A", "USA", 4000.0, 200.0)
    airplane_2 = Airplane("SWR438A", "USA", 4000.0, 200.0)

    assert airplane_1.equal_high_m(airplane_2) is True


def test_equal_high_m_diff_class_raise_error() -> None:
    airplane_1 = Airplane("SWR438A", "USA", 4000.0, 200.0)
    num = 10

    with pytest.raises(TypeError):
        airplane_1.equal_high_m(num)


def test_best_high_m_success() -> None:
    airplane_1 = Airplane("SWR438A", "USA", 4200.0, 200.0)
    airplane_2 = Airplane("SWR438A", "USA", 4000.0, 200.0)

    assert airplane_1.best_high_m(airplane_2) is True


def test_best_high_m_diff_class_raise_typeerror() -> None:
    airplane_1 = Airplane("SWR438A", "USA", 4000.0, 210.0)
    string = "mumu"

    with pytest.raises(TypeError):
        airplane_1.best_high_m(string)


def test_cast_to_object_list_success(get_info_plane) -> None:
    planes = Airplane.cast_to_object_list(get_info_plane)
    assert isinstance(planes[0], Airplane)

    assert planes[0].callsign == "MBU9AG  "
    assert planes[0].country == "Estonia"


def test_airplane_negative_height_returns_zero() -> None:
    airplane_1 = Airplane("SWR438A", "USA", -4200.0, 200.0)
    assert airplane_1.high_m == 0.0
