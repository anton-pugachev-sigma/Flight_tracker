# Flight_tracker

## Описание:
Flight_tracker - это программа, которая собирает данные о самолетах в воздушных пространствах стран.

## Установка
#### Клонируйте репозиторий:
```bash
git clone https://github.com/anton-pugachev-sigma/Flight_tracker
```

#### Установите poetry:
```bash
pip install poetry
```

#### Установите все зависимости:
```bash
poetry install
```

## Тестирование
#### Запуск всех тестов
```bash
poetry run pytest
```

#### Запуск тестов с отчетом о покрытии кода
```bash
poetry run pytest --cov=src --cov-report=html
```

#### Запуск форматеров
```bash
poetry run black .
poetry run isort .
```

#### Запуск линтеров
```bash
poetry run flake8 .
poetry run mypy .
```


## Документация
#### В пакете src содержатся модули:

```airplanes``` - содержит класс для работы с информацией о самолетах.

```api_clients``` - класс для получения информации о самолетах, находящихся в пределах заданной страны с помощью API

```get_root``` - содержит функцию для получения корня проекта

```json_saver``` - содержит класс для работы с информацией о самолетах в json файле

#### Примеры использования api_clients.py
```python
from src.api_clients import APIPlanes

#Получаем координаты России
test_api_plane = APIPlanes()
res = test_api_plane.get_cords("Russia")

#Получаем информацию о самолетах в воздушном пространстве России 
test_api_plane = APIPlanes()
info_planes = test_api_plane.get_info_planes("Russia")
```