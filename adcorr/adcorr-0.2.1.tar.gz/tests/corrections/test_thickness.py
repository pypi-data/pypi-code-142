import pytest
from numpy import Inf, allclose, array
from numpy.ma import masked_where
from pytest import raises

from adcorr.corrections import normalize_thickness


def test_normalize_thickness_typical_2x2():
    assert allclose(
        array([[0.5, 1.0], [1.5, 2.0]]),
        normalize_thickness(array([[1.0, 2.0], [3.0, 4.0]]), 2.0),
    )


def test_normalize_thickness_typical_3x3():
    assert allclose(
        array([[0.5, 1.0, 1.5], [2.0, 2.5, 3.0], [3.5, 4.0, 4.5]]),
        normalize_thickness(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]), 2.0
        ),
    )


def test_normalize_thickness_typical_2x2x2():
    assert allclose(
        array([[[0.5, 1.0], [1.5, 2.0]], [[2.5, 3.0], [3.5, 4.0]]]),
        normalize_thickness(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]), 2.0
        ),
    )


def test_normalize_thickness_masked_2x2():
    assert allclose(
        array([[Inf, 1.0], [1.5, Inf]]),
        normalize_thickness(
            masked_where(
                array([[True, False], [False, True]]),
                array([[1.0, 2.0], [3.0, 4.0]]),
            ),
            2.0,
        ).filled(Inf),
    )


def test_normalize_thickness_thickess_zero():
    with raises(ValueError):
        normalize_thickness(array([[1.0, 2.0], [3.0, 4.0]]), 0.0)


def test_normalize_thickness_thickess_negative():
    with raises(ValueError):
        normalize_thickness(array([[1.0, 2.0], [3.0, 4.0]]), -1.0)


def test_normalize_thickness_thickess_small():
    assert allclose(
        array([[1e6, 2e6], [3e6, 4e6]]),
        normalize_thickness(array([[1.0, 2.0], [3.0, 4.0]]), 1e-6),
    )


def test_normalize_thickness_thickess_large():
    assert allclose(
        array([[1e-6, 2e-6], [3e-6, 4e-6]]),
        normalize_thickness(array([[1.0, 2.0], [3.0, 4.0]]), 1e6),
    )


@pytest.mark.numcertain
def test_normalize_thickness_numcertain():
    from numcertain import nominal, uncertain, uncertainty

    expected = array(
        [
            [uncertain(0.5, 0.05), uncertain(1.0, 0.10)],
            [uncertain(1.5, 0.15), uncertain(2.0, 0.20)],
        ]
    )
    computed = (
        normalize_thickness(
            array(
                [
                    [uncertain(1.0, 0.1), uncertain(2.0, 0.2)],
                    [uncertain(3.0, 0.3), uncertain(4.0, 0.4)],
                ]
            ),
            2.0,
        ),
    )
    assert allclose(nominal(expected), nominal(computed))
    assert allclose(uncertainty(expected), uncertainty(computed))


@pytest.mark.pint
def test_normalize_thickness_pint():

    from pint import UnitRegistry

    ureg = UnitRegistry(cache_folder=":auto:")

    assert allclose(
        array([[0.5, 1.0], [1.5, 2.0]]) * ureg.count / ureg.meter,
        normalize_thickness(
            array([[1.0, 2.0], [3.0, 4.0]]) * ureg.count, 2.0 * ureg.meter
        ),
    )
