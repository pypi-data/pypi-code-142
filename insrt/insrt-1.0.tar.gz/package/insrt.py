"""Каштанов Д.В.
КИ22-17/2Б
вариант 12
сортировка вставкой"""

import random


def insertion_sort(arr):
    """Функция принимающая список
    запускаем цикл по индексам списка arr
    :param key - элемент arr под индексом i,
    :param j - индекс предыдущего элемента arr,
    если текущий эллемент меньше предыдущего мы меняем их местами
    пока не встретится предыдущий элемент,который меньше текущего
    :return: None
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def menu():
    """
    Меню программы
    :param n - строка, вводимая пользователем, содержащая натуральное число.
    :return:
    """
    while True:
        n = input('Введите длину списка: ')
        print()
        if n == 'exit':
            break
        if not n.isdigit():
            print('Ошибка,введите корректное число', end='\n\n')
            continue
        elif n <= '1':
            print('Введите натуральное число большее 1', end='\n\n')
            continue
        a = [random.randint(1, 100) for i in range(int(n))]
        print(a, end='\n\n')
        print(insertion_sort(a))


if __name__ == '__main__':
    menu()
