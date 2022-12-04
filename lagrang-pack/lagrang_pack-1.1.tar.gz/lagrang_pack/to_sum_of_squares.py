from math import sqrt


def to_sum_of_squares(n: int, k: 'squares count:int') -> list:
    """
    Функция принимает два аргумента: n и k, переводит эти значения в список

    >>> to_sum_of_squares(0,0)
    []
    >>> to_sum_of_squares(0,5)
    [0]
    >>> to_sum_of_squares(20,4)
    [1, 1, 9, 9]

    :param n: Исходное число, если оно является квадратом
    :param k: Счётчик квадратов
    :return: Если n < 0 или k < 0, возвращается пустой массив. Если n = произведение двух наибольших квадратов,
    возвращается n. Если decomposition сущесивует, возвращается список квадратов в сумме числа.
    """
    if (n < 0) or (k <= 0):
        return []
    maximum = round(sqrt(n))
    if n == maximum * maximum:
        return [n]
    for c in range(1, maximum + 1):
        decomposition = to_sum_of_squares((n - c * c), k - 1)
        if decomposition:
            return [c * c] + decomposition


if __name__ == '__main__':
    import doctest
    doctest.testmod()
