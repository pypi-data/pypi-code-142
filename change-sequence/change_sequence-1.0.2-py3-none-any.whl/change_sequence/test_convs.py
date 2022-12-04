"""
test code for change_sequence module
"""
import pytest

from change_seq import conv, conv_


def test_conv_usual():
    """
    test is this func compress a string correctly

    """
    test_string = "weekend"
    expected = "we2kend"

    result = conv(test_string)
    assert result == expected


def test_conv_empty():
    """
    test is this func compress a string correctly

    """
    test_string = ""
    expected = ""

    result = conv(test_string)
    assert result == expected


def test_conv_no_one_double_letter():
    """
    test is this func compress a string correctly

    """
    test_string = "ab222cd"
    expected = "ab23cd"

    result = conv(test_string)
    assert result == expected


def test_conv_string_with_spaces():
    """
    test is this func compress a string correctly

    """
    test_string = "aabb   c3"
    expected = "a2b2 3c3"

    result = conv(test_string)
    assert result == expected


def test_conv__usual():
    """
    test is this func stretch a string correctly
    """
    test_string = "we2kend"
    expected = "weekend"

    result = conv_(test_string)
    assert result == expected


def test_conv__number_for_every_letter():
    """
    test is this func stretch a string correctly

    """
    test_string = "q6w5e4r3t2y1"
    expected = "qqqqqqwwwwweeeerrrtty"

    result = conv_(test_string)
    assert result == expected


def test_conv__empty():
    """
    test is this func stretch a string correctly

    """
    test_string = ""
    expected = ""

    result = conv_(test_string)
    assert result == expected


def test_conv__no_one_double_letter():
    """
    test is this func stretch a string correctly

    """
    test_string = "a1bcd1"
    expected = "abcd"

    result = conv_(test_string)
    assert result == expected


def test_conv__string_with_spaces():
    """
    test is this func stretch a string correctly

    """
    test_string = "aabb 3c3"
    expected = "aabb   ccc"

    result = conv_(test_string)
    assert result == expected


def test_conv__string_like_wwd():
    """
    test is this func compress a string correctly

    """
    test_string = "www12"
    expected = "wwwwwwwwwwwwww"

    result = conv_(test_string)
    assert result == expected


if __name__ == "__main__":
    pytest.main(["-v"])
