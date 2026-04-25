# Домашнее задание к лекции 4. Tests

Решение обязательных задач и дополнительный Selenium-тест страницы авторизации из раздела `4.Tests`.

### Задача №1. Unit-тесты
Выбраны 3 задачи из модуля Основы работы с Python:
- проверка email (https://netology.ru/profile/program/py-144/lessons/532908/lesson_items/2884525);
- сезон года по номеру месяца(https://netology.ru/profile/program/py-144/lessons/532907/lesson_items/2884522);
- стоимость доставки(https://netology.ru/profile/program/py-144/lessons/532907/lesson_items/2884520).

Файл с функциями:
- `src/task1_functions.py`

Файл с тестами:
- `tests/test_task1_unit.py`

Во всех тестах используется параметризация через `pytest.mark.parametrize`.

### Задача №2. Автотест API Яндекс.Диска
Файл:
- `tests/test_yandex_disk_api.py`

Что проверяется:
- успешное создание папки;
- папка действительно существует после создания;
- создание папки без токена;
- создание папки с неверным токеном;
- повторное создание уже существующей папки.

### Задача №3. Selenium-тест авторизации Яндекса
Файл:
- `tests/test_yandex_auth_selenium.py`

> Это дополнительная задача из домашней работы. Из-за 2FA тест проверяет открытие страницы авторизации и наличие поля ввода, а не полный логин.(

## Установка

```bash
python -m venv venv
```

### Windows
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### macOS / Linux
```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Настройка переменных окружения

Создайте файл `.env` по примеру `.env.example`.
.env подгружается через python-dotenv из tests/conftest.py

Пример:

```env
YANDEX_DISK_TOKEN=ваш_oauth_токен
YANDEX_LOGIN=ваш_логин
YANDEX_PASSWORD=ваш_пароль
```

## Как получить OAuth-токен Яндекс.Диска

1. Создайте приложение в кабинете разработчика Яндекса.
2. Получите OAuth-токен для Яндекс.Диска.
3. Подставьте токен в `.env`.

## Как запускать тесты

Запустить все тесты:

```bash
pytest -v
```

Запустить только 1 задание:

```bash
pytest -v tests/test_task1_unit.py
```

Запустить только API-тесты:

```bash
pytest -v tests/test_yandex_disk_api.py
```

Запустить только Selenium-тест:

```bash
pytest -v tests/test_yandex_auth_selenium.py
```

## Структура проекта

```text
netology_4_tests_solution/
├── .env.example
├── pytest.ini
├── README.md
├── requirements.txt
├── src/
│   └── task1_functions.py
└── tests/
    ├── test_task1_unit.py
    ├── test_yandex_auth_selenium.py
    └── test_yandex_disk_api.py
```
