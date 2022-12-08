import pytest
from numpy import Inf, allclose, array
from numpy.ma import masked_where
from pytest import raises

from adcorr.corrections import normalize_frame_time


def test_normalize_frame_time_typical_2x2():
    assert allclose(
        array(
            [
                [10.0, 20.0],
                [30.0, 40.0],
            ]
        ),
        normalize_frame_time(array([[1.0, 2.0], [3.0, 4.0]]), array([0.1])),
    )


def test_normalize_frame_time_typical_3x3():
    assert allclose(
        array(
            [
                [10.0, 20.0, 30.0],
                [40.0, 50.0, 60.0],
                [70.0, 80.0, 90.0],
            ]
        ),
        normalize_frame_time(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]), array([0.1])
        ),
    )


def test_normalize_frame_time_typical_2x2x2():
    assert allclose(
        array(
            [
                [
                    [10.0, 20.0],
                    [30.0, 40.0],
                ],
                [
                    [50.0, 60.0],
                    [70.0, 80.0],
                ],
            ]
        ),
        normalize_frame_time(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([0.1, 0.1]),
        ),
    )


def test_normalize_frame_time_masked_2x2():
    assert allclose(
        array(
            [
                [Inf, 20.0],
                [30.0, Inf],
            ]
        ),
        normalize_frame_time(
            masked_where(
                array([[True, False], [False, True]]),
                array([[1.0, 2.0], [3.0, 4.0]]),
            ),
            array([0.1]),
        ).filled(Inf),
    )


def test_normalize_frame_time_count_times_singular():
    assert allclose(
        array(
            [
                [
                    [10.0, 20.0],
                    [30.0, 40.0],
                ],
                [
                    [50.0, 60.0],
                    [70.0, 80.0],
                ],
            ]
        ),
        normalize_frame_time(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]), array([0.1])
        ),
    )


def test_normalize_frame_time_count_times_vector():
    assert allclose(
        array(
            [
                [
                    [10.0, 20.0],
                    [30.0, 40.0],
                ],
                [
                    [25.0, 30.0],
                    [35.0, 40.0],
                ],
            ]
        ),
        normalize_frame_time(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([0.1, 0.2]),
        ),
    )


def test_normalize_frame_time_count_times_zero():
    with raises(ValueError):
        normalize_frame_time(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]), array([0.0])
        )


def test_normalize_frame_time_count_times_negative():
    with raises(ValueError):
        normalize_frame_time(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([0.1, -0.1]),
        )


@pytest.mark.numcertain
def test_normalize_frame_time_numcertain():
    from numcertain import nominal, uncertain, uncertainty

    expected = array(
        [
            [uncertain(10.0, 1.0), uncertain(20.0, 2.0)],
            [uncertain(30.0, 3.0), uncertain(40.0, 4.0)],
        ]
    )
    computed = normalize_frame_time(
        array(
            [
                [uncertain(1.0, 0.1), uncertain(2.0, 0.2)],
                [uncertain(3.0, 0.3), uncertain(4.0, 0.4)],
            ]
        ),
        array([0.1]),
    )
    assert allclose(nominal(expected), nominal(computed))
    assert allclose(uncertainty(expected), uncertainty(computed))


@pytest.mark.pint
def test_normalize_frame_time_pint():
    from pint import UnitRegistry

    ureg = UnitRegistry(cache_folder=":auto:")

    assert allclose(
        array(
            [
                [10.0, 20.0],
                [30.0, 40.0],
            ]
        )
        * ureg.count
        / ureg.second,
        normalize_frame_time(
            array([[1.0, 2.0], [3.0, 4.0]]) * ureg.count, array([0.1]) * ureg.second
        ),
    )
