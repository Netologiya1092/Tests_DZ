import pytest
from main import check_triangle, calculate_square_area, get_longest_word

# Тест 1: Проверка треугольника
@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, True),
    (1, 1, 10, False),
    (10, 10, 10, True),
    (0, 0, 0, False)
])
def test_check_triangle(a, b, c, expected):
    assert check_triangle(a, b, c) == expected

# Тест 2: Площадь квадрата
@pytest.mark.parametrize("side, expected", [
    (5, 25),
    (10, 100),
    (0, None),
    (-5, None)
])
def test_calculate_square_area(side, expected):
    assert calculate_square_area(side) == expected

# Тест 3: Самое длинное слово
@pytest.mark.parametrize("words, expected", [
    (["apple", "banana", "cherry"], "banana"),
    (["python", "ai", "code"], "python"),
    ([], None)
])
def test_get_longest_word(words, expected):
    assert get_longest_word(words) == expected

