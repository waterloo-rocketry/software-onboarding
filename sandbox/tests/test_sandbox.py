import sandbox as sb
import math


def test_add_one():
    val = 10
    assert sb.add_one(val) == 11


def test_add_two():
    val = 1
    assert sb.add_two(val) == 3


def test_fibonnaci_by_index():
    indices = (0, 1, 2, 3, 19, 35, 74, 100)
    values = (0, 1, 1, 2, 4181, 9227465, 1304969544928657, 354224848179261915075)
    for index, val in zip(indices, values):
        assert sb.fibonacci_by_index(index) == val


def test_factorial():
    integer = 5
    assert sb.factorial(integer) == 120


def test_multiply_by_two():
    val = 1
    assert sb.multiply_by_two(val) == 2


def test_subtract_one():
    val = 1
    assert sb.subtract_one(val) == 0


def test_area_of_rect():
    length = 3
    width = 2
    assert sb.area_of_rect(length, width) == 6


def test_single_number():
    integers = [4, 1, 2, 1, 2]
    assert sb.single_number(integers) == 4


def test_ceil_sqrt():
    integer = 69420
    # assert math.ceil(math.sqrt(integer)) == sb.ceil_sqrt(integer)
