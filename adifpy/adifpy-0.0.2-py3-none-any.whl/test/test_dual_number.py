import numpy as np
import pytest
import unittest

from Adifpy.differentiate.dual_number import DualNumber
from Adifpy.differentiate.helpers import isscalar


class TestDualNumber(unittest.TestCase):
    """Test class for DualNumber"""

    def test_creation(self):
        d = DualNumber(1, 2)
        assert isinstance(d, DualNumber) and \
            isscalar(d.real) and \
            isscalar(d.real)

        # Test str and repr
        assert type(str(d)) == str
        assert type(repr(d)) == str

    def test_catching(self):
        d = DualNumber(0, 0)

        type_error_expressions = [
            "d + 'S'",
            "d - 'S'",
            "'S' - d",
            "d * 'S'",
            "d / 'S'",
            "'S' / d",
            "d ** 'S'",
            "'S' ** d",
        ]

        for expression in type_error_expressions:
            with pytest.raises(TypeError):
                eval(expression)

    def test_add(self):
        d_r, d_d = 1, 2
        d = DualNumber(d_r, d_d)

        # Ensure integer addition works
        d1 = d + 1
        assert d1.real == d_r + 1 and d1.dual == d_d

        # Ensure floating addition works
        d2 = d + 2.5
        assert d2.real == d_r + 2.5 and d2.dual == d_d

        # Ensure dual number addition works
        d3_r, d3_d = 2, 4
        d3 = DualNumber(d3_r, d3_d)
        d4 = d + d3
        assert d4.real == d_r + d3_r and d4.dual == d_d + d3_d

    def test_mul(self):
        d_r, d_d = 1, 2
        d = DualNumber(d_r, d_d)

        # Integer multiplication
        d1 = d * 2
        assert d1.real == d_r * 2 and d1.dual == d_d * 2

        # Floating multiplication
        d2 = d * 2.5
        assert d2.real == d_r * 2.5 and d2.dual == d_d * 2.5

        d3_r, d3_d = 2, 4
        d3 = DualNumber(d3_r, d3_d)

        # Dual number multiplication
        d4 = d * d3
        assert d4.real == d_r * d3_r and \
            d4.dual == d_r * d3_d + d3_r * d_d

    def test_sub(self):
        d_r, d_d = 1, 2
        d = DualNumber(d_r, d_d)
        # Integer subtraction
        d1 = d - 1
        assert d1.real == d_r - 1 and d1.dual == d_d

        # Floating subtraction
        d2 = d - 2.5
        assert d2.real == d_r - 2.5 and d2.dual == d_d

        # Dual number subtraction
        d3_r, d3_d = 2, 4
        d3 = DualNumber(d3_r, d3_d)
        d4 = d - d3
        assert d4.real == d_r - d3_r and d4.dual == d_d - d3_d

    def test_truediv(self):
        d_r, d_d = 2, 4
        d = DualNumber(d_r, d_d)
        # Ensure integer division works
        d1 = d / 2
        assert d1.real == d_r / 2 and d1.dual == d_d / 2

        # Ensure floating division works
        d2 = d / 2.5
        assert d2.real == d_r / 2.5 and d2.dual == d_d / 2.5

        # Ensure dual number division works
        d3_r, d3_d = 4, 8
        d3 = DualNumber(d3_r, d3_d)
        d4 = d / d3
        assert d4.real == d_r / d3_r and \
            d4.dual == (d_d * d3_r - d3_d * d_r) / (d3_r ** 2)

    def test_pow(self):
        d_r, d_d = 3, 4
        d = DualNumber(d_r, d_d)

        d1 = d ** 2
        d2 = d ** -1.5
        d3 = d ** d
        d4 = pow(d, d)

        assert d1.real == pow(d_r, 2) and \
            d1.dual == d_d * 2 * d_r
        assert d2.real == pow(d_r, -1.5) and \
            d2.dual == d_d * -1.5 * pow(d_r, -2.5)
        assert d4.real == pow(d_r, d_r) and \
            d4.dual == d_r * pow(d_r, d_r - 1) * d_d + np.log(d_r) * pow(d_r, d_r) * d_d
        assert d4.real == d3.real and d4.dual == d3.dual

    def test_neg(self):
        d = DualNumber(1, 2)
        negd = -d
        assert negd.real == -1 and negd.dual == -2

    def test_radd(self):
        d = DualNumber(1, 2)

        d1 = 1 + d
        d2 = 2.5 + d

        assert d1.real == 2 and d1.dual == 2 and d2.real == 3.5 and d2.dual == 2

    def test_rmul(self):
        d = DualNumber(1, 2)

        d1 = 2 * d
        d2 = 2.5 * d

        assert d1.real == 2 and d1.dual == 4 and d2.real == 2.5 and d2.dual == 5.0

    def test_rsub(self):
        d = DualNumber(1, 2)

        d1 = 1 - d
        d2 = 0.5 - d

        assert d1.real == 0 and d1.dual == -2 and d2.real == -0.5 and d2.dual == -2

    def test_rtruediv(self):
        d = DualNumber(2, 3)

        d1 = 6 / d
        d2 = 4.8 / d

        assert d1.real == 3 and d1.dual == -d.dual * 6 / \
            pow(d.real, 2) and d2.real == 2.4 and d2.dual == - \
            d.dual * 4.8 / pow(d.real, 2)

    def test_rpow(self):
        d = DualNumber(2, 3)

        d1 = 5 ** d
        d2 = 1.5 ** d

        assert d1.real == pow(5, 2) and d1.dual == 3 * np.log(5) * pow(5, 2)
        assert d2.real == pow(1.5, 2) and d2.dual == 3 * \
            np.log(1.5) * pow(1.5, 2)
