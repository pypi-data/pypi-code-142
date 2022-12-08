from unittest.mock import MagicMock, patch

import pytest
from numpy import Inf, allclose, array, pi
from numpy.ma import masked_where
from pytest import raises

from adcorr.corrections import correct_polarization

from ..inaccessable_mock import AccessedError, inaccessable_mock


def test_correct_polarization_typical_2x2():
    assert allclose(
        array([[0.997512, 1.99502], [2.99254, 3.99005]]),
        correct_polarization(
            array([[1.0, 2.0], [3.0, 4.0]]), (1.0, 1.0), (0.1, 0.1), 1.0, 0.25
        ),
    )


def test_correct_polarization_typical_3x3():
    assert allclose(
        array(
            [
                [0.990196, 1.99505, 2.97059],
                [3.9703, 5.0, 5.95545],
                [6.93137, 7.9802, 8.91176],
            ]
        ),
        correct_polarization(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
            (1.5, 1.5),
            (0.1, 0.1),
            1.0,
            0.25,
        ),
    )


def test_correct_polarization_typical_2x2x2():
    assert allclose(
        array(
            [
                [[0.997512, 1.99502], [2.99254, 3.99005]],
                [[4.98756, 5.98507], [6.98259, 7.98010]],
            ]
        ),
        correct_polarization(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            (1.0, 1.0),
            (0.1, 0.1),
            1.0,
            0.25,
        ),
    )


def test_correct_polarization_masked_2x2():
    assert allclose(
        array([[Inf, 1.99502], [2.99254, Inf]]),
        correct_polarization(
            masked_where(
                array([[True, False], [False, True]]),
                array([[1.0, 2.0], [3.0, 4.0]]),
            ),
            (1.0, 1.0),
            (0.1, 0.1),
            1.0,
            0.25,
        ).filled(Inf),
    )


def test_correct_polarization_passes_beam_center_to_scattering_angles_only():
    with raises(AccessedError):
        correct_polarization(
            array([[1.0, 2.0], [3.0, 4.0]]),
            inaccessable_mock(tuple[float, float]),
            (0.1, 0.1),
            1.0,
            0.25,
        )
    with patch(
        "adcorr.corrections.polarization.scattering_angles",
        MagicMock(return_value=array([[0.5, 0.5], [0.5, 0.5]])),
    ), patch(
        "adcorr.corrections.polarization.azimuthal_angles",
        MagicMock(return_value=array([[pi / 4, -pi / 4], [-pi / 4, pi / 4]])),
    ):
        correct_polarization(
            array([[1.0, 2.0], [3.0, 4.0]]),
            inaccessable_mock(tuple[float, float]),
            (0.1, 0.1),
            1.0,
            0.25,
        )


def test_correct_polarization_passes_pixel_sizes_to_scattering_angles_only():
    with raises(AccessedError):
        correct_polarization(
            array([[1.0, 2.0], [3.0, 4.0]]),
            (1.0, 1.0),
            inaccessable_mock(tuple[float, float]),
            1.0,
            0.25,
        )
    with patch(
        "adcorr.corrections.polarization.scattering_angles",
        MagicMock(return_value=array([[0.5, 0.5], [0.5, 0.5]])),
    ), patch(
        "adcorr.corrections.polarization.azimuthal_angles",
        MagicMock(return_value=array([[pi / 4, -pi / 4], [-pi / 4, pi / 4]])),
    ):
        correct_polarization(
            array([[1.0, 2.0], [3.0, 4.0]]),
            (1.0, 1.0),
            inaccessable_mock(tuple[float, float]),
            1.0,
            0.25,
        )


def test_correct_polarization_passes_distance_to_geometry_utils_only():
    with raises(AccessedError):
        correct_polarization(
            array([[1.0, 2.0], [3.0, 4.0]]),
            (1.0, 1.0),
            (0.1, 0.1),
            inaccessable_mock(float),
            0.25,
        )
    with patch(
        "adcorr.corrections.polarization.scattering_angles",
        MagicMock(return_value=array([[0.5, 0.5], [0.5, 0.5]])),
    ), patch(
        "adcorr.corrections.polarization.azimuthal_angles",
        MagicMock(return_value=array([[pi / 4, -pi / 4], [-pi / 4, pi / 4]])),
    ):
        correct_polarization(
            array([[1.0, 2.0], [3.0, 4.0]]),
            (1.0, 1.0),
            (0.1, 0.1),
            inaccessable_mock(float),
            0.25,
        )


def test_correct_polarization_horizontal_polarization_zero():
    assert allclose(
        array(
            [
                [0.990196, 2.0, 2.97059],
                [3.9604, 5.0, 5.94059],
                [6.93137, 8.0, 8.91176],
            ]
        ),
        correct_polarization(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
            (1.5, 1.5),
            (0.1, 0.1),
            1.0,
            0.0,
        ),
    )


def test_correct_polarization_horizontal_polarization_one():
    assert allclose(
        array(
            [
                [0.990196, 1.9802, 2.97059],
                [4.0, 5.0, 6.0],
                [6.93137, 7.92079, 8.91176],
            ]
        ),
        correct_polarization(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
            (1.5, 1.5),
            (0.1, 0.1),
            1.0,
            1.0,
        ),
    )


def test_correct_polarization_horizontal_polarization_negative():
    with raises(ValueError):
        correct_polarization(
            array([[1.0, 2.0], [3.0, 4.0]]), (1.5, 1.5), (0.1, 0.1), 1.0, -0.1
        )


def test_correct_polarization_horizontal_polarization_exceeds_one():
    with raises(ValueError):
        correct_polarization(
            array([[1.0, 2.0], [3.0, 4.0]]), (1.0, 1.0), (0.1, 0.1), 1.0, 1.1
        )


def test_correct_polarization_horizontal_polarization_half():
    assert allclose(
        array(
            [
                [0.990196, 1.9901, 2.97059],
                [3.9802, 5.0, 5.9703],
                [6.93137, 7.9604, 8.91176],
            ]
        ),
        correct_polarization(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
            (1.5, 1.5),
            (0.1, 0.1),
            1.0,
            0.5,
        ),
    )


@pytest.mark.numcertain
def test_correct_polarization_numcertain():
    from numcertain import nominal, uncertain, uncertainty

    expected = array(
        [
            [uncertain(0.997512, 0.0997512), uncertain(1.99502, 0.199502)],
            [uncertain(2.99254, 0.299254), uncertain(3.99005, 0.399005)],
        ]
    )
    computed = (
        correct_polarization(
            array(
                [
                    [uncertain(1.0, 0.1), uncertain(2.0, 0.2)],
                    [uncertain(3.0, 0.3), uncertain(4.0, 0.4)],
                ]
            ),
            (1.0, 1.0),
            (0.1, 0.1),
            1.0,
            0.25,
        ),
    )
    assert allclose(nominal(expected), nominal(computed))
    assert allclose(uncertainty(expected), uncertainty(computed))


@pytest.mark.pint
def test_correct_polarization_pint():
    from pint import UnitRegistry

    ureg = UnitRegistry(cache_folder=":auto:")

    assert allclose(
        array([[0.997512, 1.99502], [2.99254, 3.99005]]) * ureg.count,
        correct_polarization(
            array([[1.0, 2.0], [3.0, 4.0]]) * ureg.count,
            (1.0, 1.0),
            (0.1 * ureg.meter, 0.1 * ureg.meter),
            1.0 * ureg.meter,
            0.25,
        ),
    )
