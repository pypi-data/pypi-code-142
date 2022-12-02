"""Int type generator."""

import random


def random_fixed_int(length, negative=False):
    """Generate fix length random int.

    Args:
        fix_length (int): fix length
        negetive (bool): if True, can generate negative int
    Return:
        (int): random int
    """
    # generate positive fixed length int
    positive = random.randint(10 ** (length - 1), 10**length - 1)

    # if negative is True, return positive or negative int
    if negative:
        if random.choice([True, False]):
            return positive

        return -positive

    # not negative return positive
    return positive
