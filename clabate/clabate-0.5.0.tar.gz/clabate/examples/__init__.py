'''
Clabate examples.
This is also a test suite.

Copyright 2022 AXY axy@declassed.art
License: BSD, see LICENSE for details.
'''

def assert_equal(a, b, msg=None):
    '''
    This function can be replaced with one from a unit testing framework.
    See test/test_examples.py
    '''
    if a == b:
        return
    else:
        print('--- Assertion Error: not equal ---')
        if msg:
            print(msg)
            print('----------------------------------')
        print(a)
        print('----------------------------------')
        print(b)
        print('----------------------------------')
        raise AssertionError()
