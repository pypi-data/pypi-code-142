import unittest

import numpy as np
import pytest

from Adifpy.differentiate.evaluator import Evaluator
from Adifpy.differentiate.reverse_mode import reverse_mode
from Adifpy.differentiate.node import Node
from Adifpy.differentiate.helpers import isscalar


class TestReverseMode(unittest.TestCase):
    """Test class for reverse mode"""

    def test_catching(self):
        """Ensure the reverse_mode function handles common argument errors

        Test the arguments to the reverse_mode function and ensure that incorrect
        argument types or incorrect number of arguments throw correctly.
        """
        def f(x): return x + 1

        # Invalid number of arguments
        with pytest.raises(TypeError):
            reverse_mode(f, 0.5, 2, 3)

        # Invalid argument types
        with pytest.raises(TypeError):
            reverse_mode(4, f, 0.5)

        with pytest.raises(TypeError):
            reverse_mode(f, f, 1)

        with pytest.raises(TypeError):
            reverse_mode(f, '3', 1)

        with pytest.raises(TypeError):
            reverse_mode(None, 2, 1)

        fm = reverse_mode(f, 0.45, 1)

        # Return value
        assert isinstance(fm, tuple)
        float(fm[0])
        float(fm[1])

        def f(_): raise RuntimeError
        with pytest.raises(RuntimeError):
            reverse_mode(f, 0, 0)

    def test_node_creation(self):
        n = Node(0)
        assert isscalar(n.value)

        # Test str and repr
        assert type(str(n)) == str
        assert type(repr(n)) == str

    def test_node_catching(self):
        n = Node(0)

        type_error_expressions = [
            "n + 'S'",
            "n - 'S'",
            "'S' - n",
            "n * 'S'",
            "n / 'S'",
            "'S' / n",
            "n ** 'S'",
            "'S' ** n",
        ]

        for expression in type_error_expressions:
            with pytest.raises(TypeError):
                eval(expression)

    def run_fns(self, fns):
        """Run functions through the evaluator and ensure the output is as expected

        Args:
            fns (list): a list of functions and evaluation points, in the following format:
                [(function, [test_cases]], where TEST_CASES is a list of test cases for the function.
                Each test case is in the following format:
                    (x_value, y_value, derivative_at_x)
        """
        for fn, eval_pts in fns:
            e = Evaluator(fn)

            for x, y, dx in eval_pts:
                out_y, out_dx = e(x, force_mode='reverse')
                self.assertAlmostEqual(out_y, y)
                self.assertAlmostEqual(out_dx, dx)

    def test_trig(self):
        """Ensure basic trigonometric functions are handled"""
        fns = [
            (lambda x: np.sin(x),
                [(0, 0, 1), (np.pi, 0, -1)]),
            (lambda x: np.cos(x),
                [(0, 1, 0), (np.pi, -1, 0)]),
            (lambda x: np.tan(x),
                [(0, 0, 1), (np.pi / 4, 1, 2)])
        ]

        self.run_fns(fns)

    def test_inverse_trig(self):
        """Ensure inverse trigonometric functions are handled"""
        fns = [
            (lambda x: np.arcsin(x),
                [(0.5, np.arcsin(0.5), pow(1 - pow(0.5, 2), -1 / 2))]),
            (lambda x: np.arccos(x),
                [(0.5, np.arccos(0.5), -pow(1 - pow(0.5, 2), -1 / 2))]),
            (lambda x: np.arctan(x),
                [(0.5, np.arctan(0.5), 1 / (1 + pow(0.5, 2)))])
        ]

        self.run_fns(fns)

    def test_hyperbolic_trig(self):
        """Ensure hyperbolic trigonometric functions are handled"""
        fns = [
            (lambda x: np.sinh(x),
                [(0.5, np.sinh(0.5), np.cosh(0.5))]),
            (lambda x: np.cosh(x),
                [(0.5, np.cosh(0.5), np.sinh(0.5))]),
            (lambda x: np.tanh(x),
                [(0.5, np.tanh(0.5), 1 - pow(np.tanh(0.5), 2))])
        ]

        self.run_fns(fns)

    def test_inverse_hyperbolic_trig(self):
        """Ensure inverse hyperbolic trigonometric functions are handled"""
        fns = [
            (lambda x: np.arcsinh(x),
                [(0.5, np.arcsinh(0.5), pow(pow(0.5, 2) + 1, -1 / 2))]),
            (lambda x: np.arccosh(x),
                [(1.5, np.arccosh(1.5), pow(pow(1.5, 2) - 1, -1 / 2))]),
            (lambda x: np.arctanh(x),
                [(0.5, np.arctanh(0.5), pow(1 - pow(0.5, 2), -1))])
        ]

        self.run_fns(fns)

    def test_unaries(self):
        """Ensure unary operations are handled"""
        fns = [
            (lambda x: np.exp(x),
                [(1, np.e, np.e), (-2, np.exp(-2), np.exp(-2))]),
            (lambda x: np.exp(3 * x**2),
                [(2, np.exp(12), 12 * np.exp(12))]),
            (lambda x: np.sqrt(x),
                [(9, 3, 1/6)]),
            (lambda x: np.log(x),
                [(np.e, 1, 1 / np.e)]),
            (lambda x: np.log10(x),
                [(100, 2, 0.00434294481903)]),
            (lambda x: np.log2(x),
                [(64, 6, 0.02254211001389)])
        ]

        self.run_fns(fns)

    def test_combinations(self):
        """Ensure complex combinations of basic functions are handled"""
        fns = [
            (lambda x: x,
                [(), ()]),
            (lambda x: x,
                [(), ()]),
            (lambda x: x,
                [(), ()])
        ]

        # self.run_fns(fns)

    def test_trivial(self):
        """Ensure trivial functions are handled"""
        fns = [
            (lambda x: 0,
                [(0, 0, 0), (5, 0, 0)]),
            (lambda x: x * 0,
                [(0, 0, 0), (5, 0, 0)]),
            (lambda x: x + 3,
                [(0, 3, 1), (-5, -2, 1)]),
            (lambda x: (5*x - 3) / (2*x),
                [(1, 1, 3/2), (-2, 13/4, 3/8)]),
            (lambda x: -x**x,
                [(1, -1, -1), (3, -27, -56.662531794)]),
            (lambda x: (3**(1 / x)) / 4,
                [(1, 0.75, -0.823959216501), (-2, 0.1443375672974, -0.039642756287)]),
            (lambda x: 3*x - x + (-2 - x) + (3 + x),
                [(0, 1, 2), (-5, -9, 2)])
        ]

        self.run_fns(fns)
