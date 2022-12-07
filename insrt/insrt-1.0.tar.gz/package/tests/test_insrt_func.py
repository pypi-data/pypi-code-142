from ..insrt import insertion_sort  # импорт модуля используемого для сортировки методом вставки
import pytest


@pytest.mark.parametrize("arr, sorted_arr", [([3, 1, 2, 5, 4], [1, 2, 3, 4, 5]),
                                             ([421, 1232, 1213, 11, 1, 7], [1, 7, 11, 421, 1213, 1232]),
                                             ([3123124124, 11, 3124576, 99, 100], [11, 99, 100, 3124576, 3123124124]),
                                             ([3, 2, 1, 0], [0, 1, 2, 3]),
                                             ([1, -1, 0, -3, 45, 67, 890, -946, 33],
                                              [-946, -3, -1, 0, 1, 33, 45, 67, 890])])
def test_insrt_good(arr, sorted_arr):
    assert insertion_sort(arr) == sorted_arr
