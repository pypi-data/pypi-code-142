import pytest
from numpy import Inf, allclose, array
from numpy.ma import masked_where

from adcorr.corrections import subtract_background


def test_background_subtraction_typical_2x2():
    assert allclose(
        array([[0.9, 1.8], [2.7, 3.6]]),
        subtract_background(
            array([[1.0, 2.0], [3.0, 4.0]]), array([[0.1, 0.2], [0.3, 0.4]])
        ),
    )


def test_background_subtraction_typical_3x3():
    assert allclose(
        array([[0.9, 1.8, 2.7], [3.6, 4.5, 5.4], [6.3, 7.2, 8.1]]),
        subtract_background(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
            array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]),
        ),
    )


def test_background_subtraction_typical_2x2x2():
    assert allclose(
        array([[[0.9, 1.8], [2.7, 3.6]], [[4.9, 5.8], [6.7, 7.6]]]),
        subtract_background(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([[0.1, 0.2], [0.3, 0.4]]),
        ),
    )


def test_correct_deadtime_masked_2x2():
    assert allclose(
        array(
            [
                [Inf, 1.8],
                [2.7, Inf],
            ]
        ),
        subtract_background(
            masked_where(
                array([[True, False], [False, True]]), array([[1.0, 2.0], [3.0, 4.0]])
            ),
            array([[0.1, 0.2], [0.3, 0.4]]),
        ).filled(Inf),
    )


@pytest.mark.numcertain
def test_background_subtraction_numcertain():
    from numcertain import nominal, uncertain, uncertainty

    expected = array(
        [
            [uncertain(0.9, 0.10049875621), uncertain(1.8, 0.20099751242)],
            [uncertain(2.7, 0.30149626863), uncertain(3.6, 0.40199502484)],
        ]
    )
    computed = subtract_background(
        array(
            [
                [uncertain(1.0, 0.1), uncertain(2.0, 0.2)],
                [uncertain(3.0, 0.3), uncertain(4.0, 0.4)],
            ]
        ),
        array(
            [
                [uncertain(0.1, 0.01), uncertain(0.2, 0.02)],
                [uncertain(0.3, 0.03), uncertain(0.4, 0.04)],
            ]
        ),
    )
    assert allclose(nominal(expected), nominal(computed))
    assert allclose(uncertainty(expected), uncertainty(computed))


@pytest.mark.pint
def test_background_subtraction_pint():
    from pint import UnitRegistry

    ureg = UnitRegistry(cache_folder=":auto:")

    assert allclose(
        array([[0.9, 1.8], [2.7, 3.6]]) * ureg.count,
        subtract_background(
            array([[1.0, 2.0], [3.0, 4.0]]) * ureg.count,
            array([[0.1, 0.2], [0.3, 0.4]]) * ureg.count,
        ),
    )
