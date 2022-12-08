from unittest.mock import MagicMock, patch

import pytest
from numpy import Inf, allclose, array
from numpy.ma import masked_where
from pytest import raises

from adcorr.corrections import correct_angular_efficiency

from ..inaccessable_mock import AccessedError, inaccessable_mock


def test_correct_angular_efficiency_typical_2x2():
    assert allclose(
        array([[100.2517, 200.5035], [300.7553, 401.0071]]),
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]), (1.0, 1.0), (0.1, 0.1), 1.0, 0.1, 0.1
        ),
    )


def test_correct_angular_efficiency_typical_3x3():
    assert allclose(
        array(
            [
                [99.5156, 200.0091, 298.5468],
                [400.0182, 502.5042, 600.02734],
                [696.6092, 800.0365, 895.6404],
            ]
        ),
        correct_angular_efficiency(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
            (1.5, 1.5),
            (0.1, 0.1),
            1.0,
            0.1,
            0.1,
        ),
    )


def test_correct_angular_efficiency_typical_2x2x2():
    assert allclose(
        array(
            [
                [[100.2517, 200.5035], [300.7553, 401.0071]],
                [[501.2588, 601.5106], [701.7624, 802.0142]],
            ]
        ),
        correct_angular_efficiency(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            (1.0, 1.0),
            (0.1, 0.1),
            1.0,
            0.1,
            0.1,
        ),
    )


def test_correct_angular_efficiency_masked_2x2():
    assert allclose(
        array([[Inf, 200.5035], [300.7553, Inf]]),
        correct_angular_efficiency(
            masked_where(
                array([[True, False], [False, True]]),
                array([[1.0, 2.0], [3.0, 4.0]]),
            ),
            (1.0, 1.0),
            (0.1, 0.1),
            1.0,
            0.1,
            0.1,
        ).filled(Inf),
    )


def test_correct_angular_efficiency_passes_beam_center_to_scattering_angles_only():
    with raises(AccessedError):
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]),
            inaccessable_mock(tuple[float, float]),
            (0.1, 0.1),
            1.0,
            0.1,
            0.1,
        )
    with patch(
        "adcorr.corrections.angular_efficiency.scattering_angles",
        MagicMock(return_value=array([[0.5, 0.5], [0.5, 0.5]])),
    ):
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]),
            inaccessable_mock(tuple[float, float]),
            (0.1, 0.1),
            1.0,
            0.1,
            0.1,
        )


def test_correct_angular_efficiency_passes_pixel_sizes_to_scattering_angles_only():
    with raises(AccessedError):
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]),
            (1.0, 1.0),
            inaccessable_mock(tuple[float, float]),
            1.0,
            0.1,
            0.1,
        )
    with patch(
        "adcorr.corrections.angular_efficiency.scattering_angles",
        MagicMock(return_value=array([[0.5, 0.5], [0.5, 0.5]])),
    ):
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]),
            (1.0, 1.0),
            inaccessable_mock(tuple[float, float]),
            1.0,
            0.1,
            0.1,
        )


def test_correct_angular_efficiency_passes_distance_to_scattering_angles_only():
    with raises(AccessedError):
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]),
            (1.0, 1.0),
            (0.1, 0.1),
            inaccessable_mock(float),
            0.1,
            0.1,
        )
    with patch(
        "adcorr.corrections.angular_efficiency.scattering_angles",
        MagicMock(return_value=array([[0.5, 0.5], [0.5, 0.5]])),
    ):
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]),
            (1.0, 1.0),
            (0.1, 0.1),
            inaccessable_mock(float),
            0.1,
            0.1,
        )


def test_correct_angular_efficiency_absorption_coefficient_zero():
    with raises(ValueError):
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]), (1.0, 1.0), (0.1, 0.1), 1.0, 0.0, 0.1
        )


def test_correct_angular_efficiency_absorption_coefficient_negative():
    with raises(ValueError):
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]), (1.0, 1.0), (0.1, 0.1), 1.0, -0.5, 0.1
        )


def test_correct_angular_efficiency_thickness_zero():
    with raises(ValueError):
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]), (1.0, 1.0), (0.1, 0.1), 1.0, 0.1, 0.0
        )


def test_correct_angular_efficiency_thickness_negative():
    with raises(ValueError):
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]), (1.0, 1.0), (0.1, 0.1), 1.0, 0.1, -0.5
        )


@pytest.mark.numcertain
def test_correct_angular_efficiency_numcertain():
    from numcertain import nominal, uncertain, uncertainty

    expected = array(
        [
            [uncertain(100.2517, 10.0251769), uncertain(200.5035, 20.0503538)],
            [uncertain(300.7553, 30.07553071), uncertain(401.0071, 40.10070761)],
        ]
    )
    computed = correct_angular_efficiency(
        array(
            [
                [uncertain(1.0, 0.1), uncertain(2.0, 0.2)],
                [uncertain(3.0, 0.3), uncertain(4.0, 0.4)],
            ]
        ),
        (1.0, 1.0),
        (0.1, 0.1),
        1.0,
        0.1,
        0.1,
    )
    assert allclose(nominal(expected), nominal(computed))
    assert allclose(uncertainty(expected), uncertainty(computed))


@pytest.mark.pint
def test_correct_angular_efficiency_pint():
    from pint import UnitRegistry

    ureg = UnitRegistry(cache_folder=":auto:")

    assert allclose(
        (array([[100.2517, 200.5035], [300.7553, 401.0071]]) * ureg.count),
        correct_angular_efficiency(
            array([[1.0, 2.0], [3.0, 4.0]]) * ureg.count,
            (1.0, 1.0),
            (0.1 * ureg.meter, 0.1 * ureg.meter),
            1.0 * ureg.meter,
            0.1 * ureg.count / ureg.meter,
            0.1 * ureg.meter,
        ),
    )
