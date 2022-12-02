def validate_input(inp):
    '''
    Преобразование 
    вводимых пользователем значений
    и перехват возможных исключений

    :param inp: Входное значение
    :return: int | bool
    '''
    try:
        candidate = int(inp)
        if candidate < 3:
            print('Число < 3')
            return False
        return candidate
    except ValueError:
        print('\nВведено некорректное значение '
              '(n >= 3), попробуйте снова')
        return False