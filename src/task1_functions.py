"""Функции для задания №1.

Здесь выбраны 3 задачи из модуля Основы языка программирования Python:
- проверка email (https://netology.ru/profile/program/py-144/lessons/532908/lesson_items/2884525);
- сезон года по номеру месяца(https://netology.ru/profile/program/py-144/lessons/532907/lesson_items/2884522);
- стоимость доставки(https://netology.ru/profile/program/py-144/lessons/532907/lesson_items/2884520).
"""


def check_email(email: str) -> bool:
    """Проверяет email по упрощённым правилам задания.

    Email считается корректным, если:
    - в нём нет пробелов,
    - есть ровно один символ @,
    - есть хотя бы одна точка,
    - @ не стоит первым символом,
    - после @ есть хотя бы один символ,
    - после @ есть точка.
    """
    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    if "." not in email:
        return False

    login_part, domain_part = email.split("@")

    if not login_part:
        return False

    if not domain_part:
        return False

    if "." not in domain_part:
        return False

    return True


def check_month(month: int) -> str:
    """Возвращает сезон по номеру месяца."""
    if month in (12, 1, 2):
        return "Зима"
    if month in (3, 4, 5):
        return "Весна"
    if month in (6, 7, 8):
        return "Лето"
    if month in (9, 10, 11):
        return "Осень"
    return "Некорректный номер месяца"


def get_cost(weight: int) -> str:
    """Возвращает стоимость доставки."""
    if weight > 10:
        return "Стоимость доставки: 500 руб."
    return "Стоимость доставки: 200 руб."