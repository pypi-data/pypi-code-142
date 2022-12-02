def choice_sort(sort_list):
    """
    Сортировка выбором.
    Производит сортировку выбором и возвращает отсортированный список.
    >>> choice_sort([1.0, 2.3, 0.4, -5.0, -11.4])
    [-11.4, -5.0, 0.4, 1.0, 2.3]
    >>> choice_sort([-3.5, -5.9, 10.1, 2.2, 6.4, 8.8])
    [-5.9, -3.5, 2.2, 6.4, 8.8, 10.1]

    :param list sort_list: неотсортированный список
    :return: отсортированный список.
    """
    for i in range(len(sort_list)-1):
        min_value = min(sort_list[i::])
        index_min_value = sort_list.index(min_value, i)
        sort_list[i], sort_list[index_min_value] = min_value, sort_list[i]
    return sort_list


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
