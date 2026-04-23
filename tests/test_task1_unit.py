import pytest

from task1_functions import check_email, check_month, get_cost


@pytest.mark.parametrize(
    "email, expected",
    [
        ("helloworld@d.ru", True),
        ("мояпочта@нетология.ру", True),
        ("python@email.net", True),
        ("hello world@d.ru", False),
        ("hello@@d.ru", False),
        ("helloworldd.ru", False),
        ("@mail.ru", False),
        ("em@iIru", False),
        ("em@ii.ru", True),
    ],
)
def test_check_email(email, expected):
    assert check_email(email) is expected


@pytest.mark.parametrize(
    "month, expected",
    [
        (1, "Зима"),
        (4, "Весна"),
        (7, "Лето"),
        (10, "Осень"),
        (12, "Зима"),
        (0, "Некорректный номер месяца"),
        (13, "Некорректный номер месяца"),
        (18, "Некорректный номер месяца"),
    ],
)
def test_check_month(month, expected):
    assert check_month(month) == expected


@pytest.mark.parametrize(
    "weight, expected",
    [
        (1, "Стоимость доставки: 200 руб."),
        (9, "Стоимость доставки: 200 руб."),
        (10, "Стоимость доставки: 200 руб."),
        (11, "Стоимость доставки: 500 руб."),
        (12, "Стоимость доставки: 500 руб."),
        (100, "Стоимость доставки: 500 руб."),
    ],
)
def test_get_cost(weight, expected):
    assert get_cost(weight) == expected