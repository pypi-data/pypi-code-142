import sys


def say_hello(name='World'):
    """Say hello.
    >>> bob, *_ = getfixture('names')
    >>> bob
    'Bob'
    >>> say_hello(bob)
    'Hello Bob!'
    >>> say_hello(1, 2) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: ... takes from 0 to 1 ... but 2 were given
    """
    return f'Hello {name}!'


if __name__ == "__main__":

    try:
        your_name = sys.argv[1]
        print(say_hello(your_name))
    except IndexError:
        print('Please enter your name.')  