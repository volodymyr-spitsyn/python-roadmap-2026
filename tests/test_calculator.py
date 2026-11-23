import pytest

from my_first_project.calculator import add, divide, multiply, subtract


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(3, 2) == 1


def test_multiply() -> None:
    assert multiply(2, 3) == 6


def test_divide() -> None:
    assert divide(2, 2) == 1.0


def test_divide_not_int() -> None:
    assert divide(1, 2) == pytest.approx(0.5)
