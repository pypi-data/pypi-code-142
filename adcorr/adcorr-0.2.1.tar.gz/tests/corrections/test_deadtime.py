import pytest
from numpy import Inf, allclose, array
from numpy.ma import masked_where
from pytest import raises

from adcorr.corrections import correct_deadtime


def test_correct_deadtime_typical_2x2():
    assert allclose(
        array(
            [
                [1.00005, 2.00020],
                [3.00045, 4.00080],
            ]
        ),
        correct_deadtime(array([[1.0, 2.0], [3.0, 4.0]]), array([0.1]), 3e-6, 2e-6),
    )


def test_correct_deadtime_typical_3x3():
    assert allclose(
        array(
            [
                [1.00005, 2.00020, 3.00045],
                [4.00080, 5.00125, 6.00180],
                [7.00245, 8.00320, 9.00405],
            ]
        ),
        correct_deadtime(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
            array([0.1]),
            3e-6,
            2e-6,
        ),
    )


def test_correct_deadtime_typical_2x2x2():
    assert allclose(
        array(
            [
                [
                    [1.00005, 2.00020],
                    [3.00045, 4.00080],
                ],
                [
                    [5.00125, 6.00180],
                    [7.00245, 8.00320],
                ],
            ]
        ),
        correct_deadtime(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([0.1, 0.1]),
            3e-6,
            2e-6,
        ),
    )


def test_correct_deadtime_masked_2x2():
    assert allclose(
        array(
            [
                [Inf, 2.00020],
                [3.00045, Inf],
            ]
        ),
        correct_deadtime(
            masked_where(
                array([[True, False], [False, True]]),
                array([[1.0, 2.0], [3.0, 4.0]]),
            ),
            array([0.1]),
            3e-6,
            2e-6,
        ).filled(Inf),
    )


def test_correct_deadtime_count_times_singular():
    assert allclose(
        array(
            [
                [
                    [1.00005, 2.00020],
                    [3.00045, 4.00080],
                ],
                [
                    [5.00125, 6.00180],
                    [7.00245, 8.00320],
                ],
            ]
        ),
        correct_deadtime(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([0.1]),
            3e-6,
            2e-6,
        ),
    )


def test_correct_deadtime_count_times_vector():
    assert allclose(
        array(
            [
                [
                    [1.00005, 2.00020],
                    [3.00045, 4.00080],
                ],
                [
                    [5.00063, 6.00090],
                    [7.00123, 8.00160],
                ],
            ]
        ),
        correct_deadtime(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([0.1, 0.2]),
            3e-6,
            2e-6,
        ),
    )


def test_correct_deadtime_count_times_zero():
    with raises(ValueError):
        correct_deadtime(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([0.0]),
            3e-6,
            2e-6,
        )


def test_correct_deadtime_count_times_negative():
    with raises(ValueError):
        correct_deadtime(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([0.1, -0.1]),
            3e-6,
            2e-6,
        )


def test_correct_deadtime_minimum_pulse_separation_zero():
    assert allclose(
        array(
            [
                [1.00002, 2.00008],
                [3.00018, 4.00032],
            ]
        ),
        correct_deadtime(array([[1.0, 2.0], [3.0, 4.0]]), array([0.1]), 0.0, 2e-6),
    )


def test_correct_deadtime_minimum_pulse_separation_negative():
    with raises(ValueError):
        correct_deadtime(array([[1.0, 2.0], [3.0, 4.0]]), array([0.1]), -3e-6, 2e-6)


def test_correct_deadtime_minimum_arrival_separation_zero():
    assert allclose(
        array(
            [
                [1.00002, 2.00008],
                [3.00018, 4.00032],
            ]
        ),
        correct_deadtime(array([[1.0, 2.0], [3.0, 4.0]]), array([0.1]), 2e-6, 0.0),
    )


def test_correct_deadtime_minimum_arrival_separation_negative():
    with raises(ValueError):
        correct_deadtime(array([[1.0, 2.0], [3.0, 4.0]]), array([0.1]), 3e-6, -2e-6)


def test_correct_deadtime_minimum_separations_zero():
    assert allclose(
        array([[1.0, 2.0], [3.0, 4.0]]),
        correct_deadtime(array([[1.0, 2.0], [3.0, 4.0]]), array([0.1]), 0.0, 0.0),
    )


@pytest.mark.numcertain
def test_correct_deadtime_numcertain():
    from numcertain import nominal, uncertain, uncertainty

    expected = array(
        [
            [uncertain(1.00005, 0.100005), uncertain(2.00020, 0.200020)],
            [uncertain(3.00045, 0.300045), uncertain(4.00080, 0.400080)],
        ]
    )
    computed = (
        correct_deadtime(
            array(
                [
                    [uncertain(1.0, 0.1), uncertain(2.0, 0.2)],
                    [uncertain(3.0, 0.3), uncertain(4.0, 0.4)],
                ]
            ),
            array([0.1]),
            3e-6,
            2e-6,
        ),
    )
    assert allclose(nominal(expected), nominal(computed))
    assert allclose(uncertainty(expected), uncertainty(computed))


@pytest.mark.pint
def test_correct_deadtime_pint():
    from pint import UnitRegistry

    ureg = UnitRegistry(cache_folder=":auto:")

    assert allclose(
        array(
            [
                [1.00005, 2.00020],
                [3.00045, 4.00080],
            ]
        )
        * ureg.count,
        correct_deadtime(
            array([[1.0, 2.0], [3.0, 4.0]]) * ureg.count,
            array([0.1]) * ureg.second,
            3.0 * ureg.microsecond,
            2.0 * ureg.microsecond,
        ),
    )
