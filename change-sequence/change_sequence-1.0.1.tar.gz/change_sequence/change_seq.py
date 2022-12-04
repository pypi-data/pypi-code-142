"""Конвертация строк"""


def find_int(string, i):
    """Поиск числа, которое идет после символа с индексом i

    >>> find_int("qa12ss", 1)
    12

    >>> find_int("aa1b321f", 1)
    1

    Args:
        string (str): строка введенная пользователем
        i (int): индекс обрабатываемого символа

    Returns:
        int: число, которое идет после символа с индексом i
    """
    cnt = ""
    j = 0  # счетчик кол-ва цифр в числе
    while string[(i + 1) + j].isdigit():
        cnt += string[(i + 1) + j]
        j += 1
    return int(cnt)


def conv(string):
    """Конвертирует длинную строку в сокращенную,
     посредством замены одинаковых символов числом - их кол-вом

    >>> conv("qqqqqqwwwwweeeerrrtty")
    'q6w5e4r3t2y'

    >>> conv("aaaa3f12j")
    'a43f12j'

    Args:
        string (str): строка введенная пользователем

    Returns:
        str: измененная строка, приведенная к короткому виду
    """
    string += "🃏"
    mas = []
    cnt = 0
    i = 0
    while i < len(string) - 1:
        cnt += 1
        if string[i] != string[i + 1]:
            if cnt == 1:
                mas.append(string[i])
            else:
                mas.append([string[i], cnt])
            cnt = 0
        i += 1

    mas = ''.join([''.join([str(u) for u in i]) for i in mas])
    return mas


def conv_(string):
    """Конвертирует короткую строку в длинную,
     посредством умножения символов на соответствующие числа, идущие за ними

    >>> conv_("aaa3f12j")
    'aaaaaffffffffffffj'

    >>> conv_("we2kend")
    'weekend'

    Args:
        string (str): строка введенная пользователем

    Returns:
        str: измененная строка, приведенная к длнному виду
    """
    string += "🃏"
    mas = ""
    i = 0
    while i < len(string) - 1:
        if string[i + 1].isdigit():
            coefficient = find_int(string, i)
            mas += string[i] * coefficient
            i += len(str(coefficient))
        else:
            mas += string[i]
        i += 1
    return mas


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
