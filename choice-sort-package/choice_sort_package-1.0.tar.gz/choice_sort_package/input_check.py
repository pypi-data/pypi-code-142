def input_raw_list(raw_str):
    """
    Создание неотсортированного списка.
    Принимает строку, состоящую из элементов и преобразует в список
    элементов типа float, после чего возвращает его.
    значение.
    :return: неотсортированный список элементов.
    """
    try:
        raw_list = list(map(float, raw_str.split()))
    except ValueError:
        print('Только числа!')
    else:
        return raw_list
