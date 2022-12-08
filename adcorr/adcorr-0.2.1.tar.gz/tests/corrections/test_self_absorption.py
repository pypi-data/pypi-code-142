from unittest.mock import MagicMock, patch

import pytest
from numpy import Inf, allclose, array
from numpy.ma import masked_where
from pytest import raises

from adcorr.corrections import correct_self_absorption

from ..inaccessable_mock import AccessedError, inaccessable_mock


def test_correct_self_absorption_typical_2x2():
    assert allclose(
        array([[0.999135, 1.99827], [2.99741, 3.99654]]),
        correct_self_absorption(
            array([[1.0, 2.0], [3.0, 4.0]]),
            array([1.0]),
            array([0.5]),
            (1.0, 1.0),
            (0.1, 0.1),
            1.0,
        ),
    )


def test_correct_self_absorption_typical_3x3():
    assert allclose(
        array(
            [
                [0.996559, 1.99655, 2.98968],
                [3.99309, 5.0, 5.98964],
                [6.97592, 7.98619, 8.96903],
            ]
        ),
        correct_self_absorption(
            array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
            array([1.0]),
            array([0.5]),
            (1.5, 1.5),
            (0.1, 0.1),
            1.0,
        ),
    )


def test_correct_self_absorption_typical_2x2x2():
    assert allclose(
        array(
            [
                [[0.999135, 1.99827], [2.99741, 3.99654]],
                [[4.99820, 5.99785], [6.99749, 7.99713]],
            ]
        ),
        correct_self_absorption(
            array([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]),
            array([1.0, 2.0]),
            array([0.5, 1.5]),
            (1.0, 1.0),
            (0.1, 0.1),
            1.0,
        ),
    )


def test_correct_self_absorption_masked_2x2():
    assert allclose(
        array([[Inf, 1.99827], [2.99741, Inf]]),
        correct_self_absorption(
            masked_where(
                array([[True, False], [False, True]]),
                array([[1.0, 2.0], [3.0, 4.0]]),
            ),
            array([1.0]),
            array([0.5]),
            (1.0, 1.0),
            (0.1, 0.1),
            1.0,
        ).filled(Inf),
    )


def test_correct_self_absorption_passes_beam_center_to_scattering_angles_only():
    with raises(AccessedError):
        correct_self_absorption(
            array([[1.0, 2.0], [3.0, 4.0]]),
            array([1.0]),
            array([0.5]),
            inaccessable_mock(tuple[float, float]),
            (0.1, 0.1),
            1.0,
        )
    with patch(
        "adcorr.corrections.self_absorption.scattering_angles",
        MagicMock(return_value=array([[0.5, 0.5], [0.5, 0.5]])),
    ):
        correct_self_absorption(
            array([[1.0, 2.0], [3.0, 4.0]]),
            array([1.0]),
            array([0.5]),
            inaccessable_mock(tuple[float, float]),
            (0.1, 0.1),
            1.0,
        )


def test_correct_self_absorption_passes_pixel_sizes_to_scattering_angles_only():
    with raises(AccessedError):
        correct_self_absorption(
            array([[1.0, 2.0], [3.0, 4.0]]),
            array([1.0]),
            array([0.5]),
            (1.0, 1.0),
            inaccessable_mock(tuple[float, float]),
            1.0,
        )
    with patch(
        "adcorr.corrections.self_absorption.scattering_angles",
        MagicMock(return_value=array([[0.5, 0.5], [0.5, 0.5]])),
    ):
        correct_self_absorption(
            array([[1.0, 2.0], [3.0, 4.0]]),
            array([1.0]),
            array([0.5]),
            (1.0, 1.0),
            inaccessable_mock(tuple[float, float]),
            1.0,
        )


def test_correct_self_absorption_passes_distance_to_scattering_angles_only():
    with raises(AccessedError):
        correct_self_absorption(
            array([[1.0, 2.0], [3.0, 4.0]]),
            array([1.0]),
            array([0.5]),
            (1.0, 1.0),
            (0.1, 0.1),
            inaccessable_mock(float),
        )
    with patch(
        "adcorr.corrections.self_absorption.scattering_angles",
        MagicMock(return_value=array([[0.5, 0.5], [0.5, 0.5]])),
    ):
        correct_self_absorption(
            array([[1.0, 2.0], [3.0, 4.0]]),
            array([1.0]),
            array([0.5]),
            (1.0, 1.0),
            (0.1, 0.1),
            inaccessable_mock(float),
        )


@pytest.mark.numcertain
def test_correct_self_absorption_numcertain():
    from numcertain import nominal, uncertain, uncertainty

    expected = (
        array(
            [
                [uncertain(0.999135, 0.0999135), uncertain(1.99827, 0.199827)],
                [uncertain(2.99741, 0.299741), uncertain(3.99654, 0.399654)],
            ]
        ),
    )
    computed = (
        correct_self_absorption(
            array(
                [
                    [uncertain(1.0, 0.1), uncertain(2.0, 0.2)],
                    [uncertain(3.0, 0.3), uncertain(4.0, 0.4)],
                ]
            ),
            array([1.0]),
            array([0.5]),
            (1.0, 1.0),
            (0.1, 0.1),
            1.0,
        ),
    )
    assert allclose(nominal(expected), nominal(computed))
    assert allclose(uncertainty(expected), uncertainty(computed))


@pytest.mark.pint
def test_correct_self_absorption_pint():
    from pint import UnitRegistry

    ureg = UnitRegistry(cache_folder=":auto:")

    assert allclose(
        array([[0.999135, 1.99827], [2.99741, 3.99654]]) * ureg.count,
        correct_self_absorption(
            array([[1.0, 2.0], [3.0, 4.0]]) * ureg.count,
            array([1.0]) * ureg.count / ureg.second,
            array([0.5]) * ureg.count / ureg.second,
            (1.0, 1.0),
            (0.1 * ureg.meter, 0.1 * ureg.meter),
            1.0 * ureg.meter,
        ),
    )
