"""Int type generator."""

import random


def random_fixed_int(length):
    """Generate fix length random int.

    Args:
        fix_length (int): fix length
    Return:
        (int): random int
    """
    return random.randint(10 ** (length - 1), 10**length - 1)
