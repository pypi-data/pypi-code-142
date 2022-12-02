def is_prime(number):
    i = 3
    composite = False
    if number % 2 == 0:
        return False
    while i**2 < number:
        if number % i == 0:
            composite = True
            break
        i += 2
    if composite:
        return False
    else:
        return True
