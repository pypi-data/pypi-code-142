import os
from unittest import TestCase

from matplotlib.testing.decorators import cleanup
from parameterized import parameterized

from linefolio.quantrocket_moonshot import from_moonshot_csv


class PositionsTestCase(TestCase):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    @parameterized.expand(
        [
            ({},),
            ({"slippage": 1},),
            ({"round_trips": True},),
            ({"hide_positions": True},),
            ({"cone_std": 1},),
            ({"bootstrap": True},),
        ]
    )
    @cleanup
    def test_create_full_tear_sheet_breakdown(self, kwargs):
        from_moonshot_csv(self.__location__ + "/test_data/moonline-tearsheet.csv", **kwargs)
