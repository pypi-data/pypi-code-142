from python_packaging_ch.maths import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
    power_numbers,
)


def test_add_numbers():

    assert add_numbers(1, 2) == 3, "adding 1 and 2 failed"
    assert add_numbers(10.1, 100) == 110.1, "adding 10.1 and 100 failed"


def test_subtract_numbers():

    assert subtract_numbers(1, 2) == -1, "subtracting 1 and 2 failed"
    assert (
        subtract_numbers(10.1, 100) == -89.9
    ), "subtracting 10.1 and 100 failed"


def test_multiply_numbers():

    assert multiply_numbers(1, 2) == 2, "multiplying 1 and 2 failed"
    assert (
        multiply_numbers(10.1, 100) == 1010
    ), "multiplying 10.1 and 100 failed"


def test_divide_numbers():

    assert divide_numbers(1, 2) == 0.5, "dividing 1 and 2 failed"
    assert divide_numbers(10, 100) == 0.10, "dividing 10 and 100 failed"


def test_power_numbers():

    assert power_numbers(2, 2) == 4, "powering 2 and 2 failed"
    assert power_numbers(2, 4) == 16, "powering 2 and 4 failed"
