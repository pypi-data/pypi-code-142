NUMBER_FOR_REST = 11

CPF = {
    "first_digit": [10, 9, 8, 7, 6, 5, 4, 3, 2],
    "second_digit": [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
}

CNPJ = {
    "first_digit": [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
    "second_digit": [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
}


def extract_digits(value):
    return "".join(list(filter(lambda x: x.isdigit(), value)))


def first_digit_cpf_checker_is_valid(value: str):
    combinations = list(zip(CPF.get("first_digit"), [int(x) for x in value[:10]]))
    sum_ = 0
    for item in combinations:
        x, y = item
        sum_ += x * y
    rest_of_division = sum_ % NUMBER_FOR_REST
    result = 0 if rest_of_division < 2 else NUMBER_FOR_REST - rest_of_division
    return result == int(value[9])


def second_digit_cpf_checker_is_valid(value: str):
    combinations = list(zip(CPF.get("second_digit"), [int(x) for x in value[:11]]))
    sum_ = 0
    for item in combinations:
        x, y = item
        sum_ += x * y
    rest_of_division = sum_ % NUMBER_FOR_REST
    result = 0 if rest_of_division < 2 else NUMBER_FOR_REST - rest_of_division
    return result == int(value[10])


def first_digit_cnpj_checker_is_valid(value: str):
    combinations = list(zip(CNPJ.get("first_digit"), [int(x) for x in value[:12]]))
    sum_ = 0
    for item in combinations:
        x, y = item
        sum_ += x * y
    rest_of_division = sum_ % NUMBER_FOR_REST
    result = 0 if rest_of_division < 2 else NUMBER_FOR_REST - rest_of_division
    return result == int(value[12])


def second_digit_cnpj_checker_is_valid(value: str):
    combinations = list(zip(CNPJ.get("second_digit"), [int(x) for x in value[:13]]))
    sum_ = 0
    for item in combinations:
        x, y = item
        sum_ += x * y
    rest_of_division = sum_ % NUMBER_FOR_REST
    result = 0 if rest_of_division < 2 else NUMBER_FOR_REST - rest_of_division
    return result == int(value[13])


def cnpj_or_cpf_is_valid(value: str):
    value = extract_digits(value)
    result = False
    if len(value) == 11 and (
        first_digit_cpf_checker_is_valid(value) and second_digit_cpf_checker_is_valid(value)
    ):
        result = True
    if len(value) == 14 and (
        first_digit_cnpj_checker_is_valid(value) and second_digit_cnpj_checker_is_valid(value)
    ):
        result = True
    return result
