"""
ll2wm function definition
"""

import numpy
from ocutils import earth_radius


def ll2wm(lat, lon, lon0=0):

    """
    Convert latitude and longitude to Web-Mercator coordinates.

    args...
        lat: Numpy array of latitudes (degrees)
        lon: Numpy array of longitudes (degrees)
    kwargs...
        lon0: longitude of reference meridian (degrees)
    returns...
        x: Numpy array of horizontal distances (m)
        y: Numpy array of vertical distances (m)
    """

    if numpy.any(lat <= -90) or numpy.any(lat >= 90):
        raise ValueError('Latitude must be > -90 and < 90 degrees')

    if numpy.any(lon < -180) or numpy.any(lon > 180):
        raise ValueError('Longitude must be >= -180 and <= 180 degrees')

    lonr = numpy.deg2rad(lon)
    lonr0 = numpy.deg2rad(lon0)
    latr = numpy.deg2rad(lat)

    x = earth_radius * (lonr - lonr0)

    y = earth_radius * numpy.log(numpy.tan(numpy.pi / 4 + latr / 2))

    return x, y
