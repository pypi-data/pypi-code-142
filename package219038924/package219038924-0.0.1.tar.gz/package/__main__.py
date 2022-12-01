import numpy as np


def binary_search(lst, search_item):
    lon = 0
    high = len(lst) - 1

    while lon <= high:
        middle = (lon + high) // 2
        guess = lst[middle]
        if guess == search_item:
            return True

        if guess > search_item:
            high = middle - 1
        else:
            lon = middle + 1
    return False


while True:
    lst = input('Введите значения: ')
    lst = lst.split()
    value = input('Выберите элемент: ')

    array = np.array(lst)

    result = binary_search(array, value)
    if result:
        print(*np.where(array == value)[0])
    else:
        print(None)

    while end := input('Для завершения программы введите 1. Для продолжения введите 2: '):
        if end == '1' or end == '2':
            break
    if end == '1':
        break

