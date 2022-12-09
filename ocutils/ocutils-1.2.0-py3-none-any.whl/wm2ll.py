"""
wm2ll function definition
"""

import numpy
from ocutils import earth_radius


def wm2ll(x, y, lon0=0):

    """
    Convert Web-Mercator coordinates to latitude and longitude.

    args...
        x: Numpy array of horizontal distances (m)
        y: Numpy array of vertical distances (m)
    kwargs...
        lon0: longitude of reference meridian (degrees)
    returns...
        lat: Numpy array of latitudes (degrees)
        lon: Numpy array of longitudes (degrees)
    """

    lonr0 = numpy.deg2rad(lon0)

    lonr = lonr0 + x / earth_radius

    latr = 2 * numpy.arctan(numpy.exp(y / earth_radius)) - numpy.pi / 2

    lon = numpy.rad2deg(lonr)
    lat = numpy.rad2deg(latr)

    return lat, lon
