import re

import pytest

from precisenumbers import coordinates as precisecoordinates


def test_Longitude_init():
    # Success case
    pc1 = precisecoordinates.Longitude('110.210')
    assert pc1.integer == 110
    assert pc1.fractional == 210
    assert pc1.precision == 3

    # Failure cases
    with pytest.raises(ValueError):
        precisecoordinates.Longitude(180.3)

    with pytest.raises(ValueError):
        precisecoordinates.Longitude(-180.3)


def test_Longitude_warning(caplog):
    precisecoordinates.Longitude(-10.3, precision=8)
    assert 'WARNING' in caplog.text
    assert 'precision exceeds maximum allowable value' in caplog.text

    # Make sure it only warns once
    precisecoordinates.Longitude(-10.3, precision=8)
    assert len(re.findall('precision exceeds maximum allowable value', caplog.text)) == 1


def test_Latitude_init():
    # Success case
    pc1 = precisecoordinates.Latitude('10.210')
    assert pc1.integer == 10
    assert pc1.fractional == 210
    assert pc1.precision == 3

    # Failure cases
    with pytest.raises(ValueError):
        precisecoordinates.Latitude(90.3)

    with pytest.raises(ValueError):
        precisecoordinates.Latitude(-90.3)


def test_Latitude_warning(caplog):
    precisecoordinates.Latitude(-10.3, precision=8)
    assert 'precision exceeds maximum allowable value' in caplog.text

    # Make sure it only warns once
    precisecoordinates.Longitude(-10.3, precision=8)
    assert len(re.findall('precision exceeds maximum allowable value', caplog.text)) == 1


def test_Coordinate_init():
    # Specified Precision
    cp1 = precisecoordinates.Coordinate('10.12345', '-0.1', precision=5)

    assert cp1.longitude.multiplier == 1
    assert cp1.longitude.integer == 10
    assert cp1.longitude.fractional == 12345
    assert cp1.longitude.precision == 5

    assert cp1.latitude.multiplier == -1
    assert cp1.latitude.integer == 0
    assert cp1.latitude.fractional == 10000
    assert cp1.latitude.precision == 5

    # Inferred, Same Precision
    cp2 = precisecoordinates.Coordinate('10.12345', '-0.1')

    assert cp2.longitude.multiplier == 1
    assert cp2.longitude.integer == 10
    assert cp2.longitude.fractional == 12345
    assert cp2.longitude.precision == 5

    assert cp2.latitude.multiplier == -1
    assert cp2.latitude.integer == 0
    assert cp2.latitude.fractional == 10000
    assert cp2.latitude.precision == 5

    # Inferred, Different Precisions
    cp3 = precisecoordinates.Coordinate('10.12345', '-0.1', same_precision=False)

    assert cp3.longitude.multiplier == 1
    assert cp3.longitude.integer == 10
    assert cp3.longitude.fractional == 12345
    assert cp3.longitude.precision == 5

    assert cp3.latitude.multiplier == -1
    assert cp3.latitude.integer == 0
    assert cp3.latitude.fractional == 1
    assert cp3.latitude.precision == 1

    with pytest.raises(ValueError):
        precisecoordinates.Coordinate(-10.3, 10.3, same_precision=False, precision=8)
