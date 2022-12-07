import argparse
from .insrt import insertion_sort  # импорт модуля используемого для сортировки методом вставки
import pytest


def main():
    """
    Основная часть программы, реализующая интерфейс командной строки.
    :param --array,-a - принимает список, который нужно отсортировать.
    :param --test,-t - запуск тестов, реализованных с помощью модуля pytest.
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--array', '-a', type=str, help='Введите список,который необходимо отсортировать')
    parser.add_argument('--test', '-t', type=bool, dest='test', action=argparse.BooleanOptionalAction,
                        help='Запуск тестов')
    args = parser.parse_args()
    if not args.array and not args.test:
        print("Введите аргумент и его значение")
    if args.array:
        array = args.array
        array = array.split(',')
        for i in range(len(array)):
            array[i] = int(array[i])
        print(f'Отсортированный список:{insertion_sort(array)}')
    if args.test:
        pytest.main(["-v", "package/tests/test_insrt_func.py"])


if __name__ == '__main__':
    main()
