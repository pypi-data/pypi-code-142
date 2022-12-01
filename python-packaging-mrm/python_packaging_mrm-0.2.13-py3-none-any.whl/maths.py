from typing import Union


def add_numbers(a: int, b: int) -> int:
    return a + b


def add_numbers_diff_types(
    a: Union[int, float], b: Union[int, float]
) -> Union[int, float]:
    return int(a + b)


def subtract_numbers(a: int, b: int) -> int:
    return a - b
