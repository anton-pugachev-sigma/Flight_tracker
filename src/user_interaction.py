from src.airplanes import Airplane
from src.api_clients import APIPlanes
from src.json_saver import JsonFileSaver


def user_interaction():
    country = input("Введите название страны: ")
    while True:
        try:
            top_n = int(input("Введите количество самолетов для вывода в топ N: "))
            if isinstance(top_n, int) and top_n > 0:
                break
            elif top_n == 0:
                print("Введите положительное число")
            raise ValueError
        except ValueError:
            print("Введите число")

    filter_words = input(
        "Введите названия стран для фильтрации по стране регистрации: "
    ).split()
    api = APIPlanes()
    aeroplanes = api.get_info_planes(country)
    aeroplanes = Airplane.cast_to_object_list(aeroplanes)

    json_saver = JsonFileSaver()
    for plane in aeroplanes:
        json_saver.insert_info_plane(plane)

    top_planes = sorted(aeroplanes, reverse=True)[:top_n]
    filtered_planes = []
    for reg_country in filter_words:
        filtered_plane = json_saver.get_filtered_data(country=reg_country)
        filtered_planes.extend(filtered_plane)

    print(f"{top_n} самолетов:")
    for top_plane in top_planes:
        print(top_plane)
    print("Отфильтрованные самолеты по странам:")
    for country_plane in filtered_planes:
        print(country_plane)


user_interaction()


# filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)
#
# ranged_aeroplanes = get_aeroplanes_by_altitude(aeroplanes, altitude_range)
#
# sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
# top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
# print_aeroplanes(top_aeroplanes)
