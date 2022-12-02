"""Int type generator."""

import random


def random_int(fix_length):
    """Generate fix length random int.

    Args:
        fix_length (int): fix length
    Return:
        (int): random int
    """
    return random.randint(10 ** (fix_length - 1), 10**fix_length - 1)
