from numpy import allclose, array

from adcorr.utils.geometry import azimuthal_angles, scattering_angles


def test_scattering_angles_typical_2x2():
    assert allclose(
        array([[0.0705931793, 0.0705931793], [0.0705931793, 0.0705931793]]),
        scattering_angles((2, 2), (1.0, 1.0), (0.1, 0.1), 1.0),
    )


def test_scattering_angles_typical_3x3():
    assert allclose(
        array(
            [
                [0.140489702, 0.0996686525, 0.140489702],
                [0.0996686525, 0.0, 0.0996686525],
                [0.140489702, 0.0996686525, 0.140489702],
            ]
        ),
        scattering_angles((3, 3), (1.5, 1.5), (0.1, 0.1), 1.0),
    )


def test_scattering_angles_typical_3x2():
    assert allclose(
        array(
            [
                [0.111341014, 0.111341014],
                [0.0499583957, 0.0499583957],
                [0.111341014, 0.111341014],
            ]
        ),
        scattering_angles((3, 2), (1.5, 1.0), (0.1, 0.1), 1.0),
    )


def test_scattering_angles_zero_pixels():
    assert 0 == scattering_angles((0, 0), (1.0, 1.0), (0.1, 0.1), 1.0).size


def test_scattering_angles_center_corner():
    assert allclose(
        array([[0.209033299, 0.156815685], [0.156815685, 0.0705931793]]),
        scattering_angles((2, 2), (2.0, 2.0), (0.1, 0.1), 1.0),
    )


def test_scattering_angles_center_outside():
    assert allclose(
        array([[0.140489702, 0.219987977], [0.219987977, 0.275642799]]),
        scattering_angles((2, 2), (-0.5, -0.5), (0.1, 0.1), 1.0),
    )


def test_scattering_angles_pixels_small():
    assert allclose(
        array([[7.07106781e-10, 7.07106781e-10], [7.07106781e-10, 7.07106781e-10]]),
        scattering_angles((2, 2), (1.0, 1.0), (1e-9, 1e-9), 1.0),
    )


def test_scattering_angles_pixels_large():
    assert allclose(
        array([[1.57079633, 1.57079633], [1.57079633, 1.57079633]]),
        scattering_angles((2, 2), (1.0, 1.0), (1e9, 1e9), 1.0),
    )


def test_scattering_angles_pixels_rectangular():
    assert allclose(
        array([[0.111341014, 0.111341014], [0.111341014, 0.111341014]]),
        scattering_angles((2, 2), (1.0, 1.0), (0.1, 0.2), 1.0),
    )


def test_scattering_angles_distance_small():
    assert allclose(
        array([[1.57079631, 1.57079631], [1.57079631, 1.57079631]]),
        scattering_angles((2, 2), (1.0, 1.0), (0.1, 0.1), 1e-9),
    )


def test_scattering_angles_distance_large():
    assert allclose(
        array([[7.07106781e-11, 7.07106781e-11], [7.07106781e-11, 7.07106781e-11]]),
        scattering_angles((2, 2), (1.0, 1.0), (0.1, 0.1), 1e9),
    )


def test_scattering_angles_distance_negative():
    assert allclose(
        array([[-0.0705931793, -0.0705931793], [-0.0705931793, -0.0705931793]]),
        scattering_angles((2, 2), (1.0, 1.0), (0.1, 0.1), -1.0),
    )


def test_azimuthal_angles_typical_2x2():
    assert allclose(
        array([[-2.35619449, -0.785398163], [2.35619449, 0.785398163]]),
        azimuthal_angles((2, 2), (1.0, 1.0), (0.1, 0.1)),
    )


def test_azimuthal_angles_typical_3x3():
    assert allclose(
        array(
            [
                [-2.35619449, -1.57079633, -0.78539816],
                [3.14159265, 0, 0],
                [2.35619449, 1.57079633, 0.78539816],
            ]
        ),
        azimuthal_angles((3, 3), (1.5, 1.5), (0.1, 0.1)),
    )


def test_azimuthal_angles_typical_3x2():
    assert allclose(
        array([[-2.03444394, -1.10714872], [3.14159265, 0], [2.03444394, 1.10714872]]),
        azimuthal_angles((3, 2), (1.5, 1.0), (0.1, 0.1)),
    )


def test_azimuthal_angles_zero_pixels():
    assert 0 == azimuthal_angles((0, 0), (1.0, 1.0), (0.1, 0.1)).size


def test_azimuthal_angles_center_corner():
    assert allclose(
        array([[-2.35619449, -1.89254688], [-2.8198421, -2.35619449]]),
        azimuthal_angles((2, 2), (2.0, 2.0), (0.1, 0.1)),
    )


def test_azimuthal_angles_center_outside():
    assert allclose(
        array([[0.785398163, 0.463647609], [1.10714872, 0.785398163]]),
        azimuthal_angles((2, 2), (-0.5, -0.5), (0.1, 0.1)),
    )


def test_azimuthal_angles_pixels_small():
    assert allclose(
        array([[-2.35619449, -0.785398163], [2.35619449, 0.785398163]]),
        azimuthal_angles((2, 2), (1.0, 1.0), (1e-9, 1e-9)),
    )


def test_azimuthal_angles_pixels_large():
    assert allclose(
        array([[-2.35619449, -0.785398163], [2.35619449, 0.785398163]]),
        azimuthal_angles((2, 2), (1.0, 1.0), (1e9, 1e9)),
    )


def test_azimuthal_angles_pixels_rectangular():
    assert allclose(
        array([[-2.67794504, -0.46364761], [2.67794504, 0.46364761]]),
        azimuthal_angles((2, 2), (1.0, 1.0), (0.1, 0.2)),
    )
