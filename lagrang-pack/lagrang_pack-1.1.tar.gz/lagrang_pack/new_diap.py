def new_diap(diap):
    """
    Функция принимает один аргумент: diap

    >>> new_diap("30")
    (0, 30)
    >>> new_diap("5 7")
    (5, 7)
    >>> new_diap("7 100")
    (7, 100)

    :param diap: введёный пользователем отрезок
    :return: Если в диапазоне не числа, возвращается StrError. Если  числа в на отрезке кончились,
    возвращается ArgCountError. Если отрезок сущесивует, возвращается отрезок
    """
    if all(i.isdigit() for i in diap.split(' ')):
        if len(diap.split(' ')) == 1:
            diap = (0, int(diap))
        elif len(diap.split(' ')) == 2:
            diap = tuple(map(int, diap.split(' ')))
        else:
            return "ArgCountError"
        return diap
    else:
        return "StrError"
