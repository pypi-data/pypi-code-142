from pythonator_123.amazing_function import do_the_amazing


def test_add_numbers():
    assert do_the_amazing(10, 20) == 30
    assert do_the_amazing(20, 20) == 40
