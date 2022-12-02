from validate import validate_input

def calculate_sundaram(n):
    '''
    расчёт решета Сундарама

    >>> calculate_sundaram(6)
    [2, 3, 5]

    >>> calculate_sundaram(15)
    [2, 3, 5, 7, 11, 13]

    :return list[int]: решето Сундарама
    '''

    sundaram = validate_input(n)
    if not sundaram:
        return

    f_formula = int((sundaram - 1) / 2)
    marked = [0] * (f_formula + 1)
    for i in range(1, f_formula + 1):
        j = i

        while (i + j + 2 * i * j) <= f_formula:
            marked[i + j + 2 * i * j] = 1
            j += 1

    res_arr = []
    if sundaram > 2:
        res_arr.append(2)

    for i in range(1, f_formula + 1):
        if marked[i] == 0:
            res_arr.append(2 * i + 1)
    
    return res_arr


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

