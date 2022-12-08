import pytest
from numpy import Inf, allclose, array
from numpy.ma import masked_where

from adcorr.corrections import correct_flatfield


def test_correct_flatfield_typical_2x2():
    assert allclose(
        array([[1.0, 4.0], [9.0, 16.0]]),
        correct_flatfield(
            array([[1.0, 2.0], [3.0, 4.0]]),
            array([[1.0, 2.0], [3.0, 4.0]]),
        ),
    )


def test_correct_flatfield_typical_3x3():
    assert allclose(
        array(
            [
                [1.0, 4.0, 9.0],
                [16.0, 25.0, 36.0],
                [49.0, 64.0, 81.0],
            ]
        ),
        correct_flatfield(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
        ),
    )


def test_correct_flatfield_typical_2x2x2():
    assert allclose(
        array(
            [
                [[1.0, 4.0], [9.0, 16.0]],
                [[25.0, 36.0], [49.0, 64.0]],
            ]
        ),
        correct_flatfield(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
        ),
    )


def test_correct_flatfield_masked_2x2():
    assert allclose(
        array([[Inf, 4.0], [9.0, Inf]]),
        correct_flatfield(
            masked_where(
                array([[True, False], [False, True]]),
                array([[1.0, 2.0], [3.0, 4.0]]),
            ),
            array([[1.0, 2.0], [3.0, 4.0]]),
        ).filled(Inf),
    )


@pytest.mark.numcertain
def test_correct_flatfield_numcertain():
    from numcertain import nominal, uncertain, uncertainty

    expected = array(
        [
            [uncertain(1.0, 0.14142136), uncertain(4.0, 0.56568542494)],
            [uncertain(9.0, 1.27279220614), uncertain(16.0, 2.2627416998)],
        ]
    )
    computed = (
        correct_flatfield(
            array(
                [
                    [uncertain(1.0, 0.1), uncertain(2.0, 0.2)],
                    [uncertain(3.0, 0.3), uncertain(4.0, 0.4)],
                ]
            ),
            array(
                [
                    [uncertain(1.0, 0.1), uncertain(2.0, 0.2)],
                    [uncertain(3.0, 0.3), uncertain(4.0, 0.4)],
                ]
            ),
        ),
    )
    assert allclose(nominal(expected), nominal(computed))
    assert allclose(uncertainty(expected), uncertainty(computed))


@pytest.mark.pint
def test_correct_flatfield_pint():
    from pint import UnitRegistry

    ureg = UnitRegistry(cache_folder=":auto:")

    assert allclose(
        array([[1.0, 4.0], [9.0, 16.0]]) * ureg.count,
        correct_flatfield(
            array([[1.0, 2.0], [3.0, 4.0]]) * ureg.count,
            array([[1.0, 2.0], [3.0, 4.0]]) * ureg.count,
        ),
    )
