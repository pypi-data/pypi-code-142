def arabic_number_to_roman_numerals(arabic_number: int) -> str:
    if not isinstance(arabic_number, int):
        raise ValueError("The input should be an integer")
    elif arabic_number < 1:
        raise ValueError("The input should be at least 1")
    elif arabic_number > 3999:
        raise ValueError("The converter only supports arabic numbers up to 3999")

    roman = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }

    result = ""
    for i in sorted(roman.keys(), reverse=True):
        while arabic_number >= i:
            result += roman[i]
            arabic_number -= i
    return result
