import unittest

import pynibs


class TestRegIonOfInterestSurface(unittest.TestCase):

    def test_regionofinterestsurface(self):
        roi = pynibs.RegionOfInterestSurface()
        for field in ["X_ROI", "Y_ROI", "Z_ROI"]:
            assert hasattr(roi, field)
        for field in ["x_roi", "x_roi", "x_roi"]:
            assert not hasattr(roi, field)


class TestRegionOfInterestVolume(unittest.TestCase):
    def test_regionofinterestvolume(self):
        roi = pynibs.RegionOfInterestVolume()
