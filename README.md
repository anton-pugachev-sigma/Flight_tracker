# Flight_tracker

## Описание:


## Установка
#### Клонируйте репозиторий:
```bash
git clone https://github.com/anton-pugachev-sigma/Online_store_project
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



#### Примеры использования
```python
```