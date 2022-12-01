from python_packaging_ch.maths import add_numbers


def test_add_numbers():

    assert add_numbers(1, 2) == 3, "adding 1 and 2 failed"
    assert add_numbers(10.1, 100) == 110.1, "adding 10.1 and 100 failed"
