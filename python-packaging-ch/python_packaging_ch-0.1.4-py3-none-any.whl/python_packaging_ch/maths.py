import fire

from typing import Union


def add_numbers(
    a: Union[int, float], b: Union[int, float]
) -> Union[int, float]:

    return a + b


def subtract_numbers(
    a: Union[int, float], b: Union[int, float]
) -> Union[int, float]:

    return a - b


def multiply_numbers(
    a: Union[int, float], b: Union[int, float]
) -> Union[int, float]:

    return a * b


def divide_numbers(
    a: Union[int, float], b: Union[int, float]
) -> Union[int, float]:

    return a / b


def power_numbers(
    a: Union[int, float], b: Union[int, float]
) -> Union[int, float]:

    return a**b


def main():
    fire.Fire(add_numbers)


if __name__ == "__main__":
    main()
