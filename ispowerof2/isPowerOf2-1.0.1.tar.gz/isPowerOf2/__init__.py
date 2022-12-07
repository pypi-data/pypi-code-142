def isPowerOf2(number):
    """
    Check if a number is power of 2

    :param number: The number to check if it is power of 2.
    :type number: int

    """
    if number != 0 and (number & (number-1)) == 0:
        return True
    else:
        return False