import unittest

import numpy as np
import pytest

from Adifpy.differentiate.dual_number import logb, sigmoid
from Adifpy.differentiate.evaluator import Evaluator
from Adifpy.differentiate.forward_mode import forward_mode
from Adifpy.differentiate.helpers import isscalar


class TestForwardMode(unittest.TestCase):
    """Test class for forward mode"""

    def test_catching(self):
        """Ensure the forward_mode function handles common argument errors

        Test the arguments to the forward_mode function and ensure that incorrect
        argument types or incorrect number of arguments throw correctly.
        """
        def f(x): return x + 1

        # Invalid number of arguments
        with pytest.raises(TypeError):
            forward_mode(f, 0.5, 2, 3)

        # Invalid argument types
        with pytest.raises(TypeError):
            forward_mode(4, f, 0.5)

        with pytest.raises(TypeError):
            forward_mode(f, f, 1)

        with pytest.raises(TypeError):
            forward_mode(f, '3', 1)

        with pytest.raises(TypeError):
            forward_mode(None, 2, 1)

        fm = forward_mode(f, 0.45, 1)

        # Return value
        assert isinstance(fm, tuple)
        float(fm[0])
        float(fm[1])

        def f(_): raise RuntimeError
        with pytest.raises(RuntimeError):
            forward_mode(f, 0, 0)

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
                out_y, out_dx = e(x, force_mode='forward')
                self.assertAlmostEqual(out_y, y)
                self.assertAlmostEqual(out_dx, dx)

    def run_multi_fns(self, fns):
        """Run multi-dimensional functions through the evaluator and ensure the output is as expected

        Args:
            fns (list): a list of functions and evaluation points, in the following format:
                [(function, [test_cases]], where TEST_CASES is a list of test cases for the function.
                Each test case is in the following format:
                    (x_value, y_value, seed_vector derivative_at_x)
        """
        for fn, eval_pts in fns:
            e = Evaluator(fn)

            for x, y, seed, dx in eval_pts:
                out_y, out_dx = e(x, seed_vector=seed, force_mode='forward')

                # Account for output spaces of more than 1 dimension
                assert len(y) == len(out_y)
                for y_item, out_y_item in zip(y, out_y):
                    self.assertAlmostEqual(y_item, out_y_item)
                assert len(y) == len(dx) == len(out_dx)
                for dx_item, out_dx_item in zip(dx, out_dx):
                    self.assertAlmostEqual(dx_item, out_dx_item)

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
                [(64, 6, 0.02254211001389)]),
            (lambda x: sigmoid(x),
                [(0, 0.5, 0.25), (2, 0.88079707798, 0.104993585401893)]),
            (lambda x: logb(x, 5),
                [(125, 3, 0.004970679476)])
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

        multi_fns = [
            (lambda x: x * 0,
                [([3, 5], [0, 0], [1, 0], [0, 0])]),
            (lambda x: x + 1,
                [([3, 5], [4, 6], [1, 0], [1, 0])])
        ]

        self.run_fns(fns)
        self.run_multi_fns(multi_fns)

    def test_multi_dimension_catching(self):
        """Ensure dimension-related error are successfully handled"""
        pass

    def test_multi_trig(self):
        """Ensure mult-dimensional trigonometric functions are handled"""
        fns = [
            (lambda x: np.sin(x),
                [([0, np.pi / 2], [0, 1], [1, 0], [1, 0]),  # R^2 -> R^2
                ([0, np.pi / 2], [0, 1], [0, 1], [0, 0])]),  # R^2 -> R^2
            (lambda x: np.cos(x),
                [([0, np.pi / 2], [1, 0], [1, 0], [0, 0]),  # R^2 -> R^2
                ([0, np.pi / 2], [1, 0], [0, 1], [0, -1])]),  # R^2 -> R^2
            (lambda x: np.tan(x),
                [([0, np.pi / 4], [0, 1], [1, 0], [1, 0]),  # R^2 -> R^2
                ([0, np.pi / 4], [0, 1], [0, 1], [0, 2])]),  # R^2 -> R^2
            (lambda x: [np.sin(x[0]), np.cos(x[1])],
                [([0, np.pi / 2], [0, 0], [1, 0], [1, 0]),  # R^2 -> R^2
                 ([0, np.pi / 2], [0, 0], [0, 1], [0, -1])])  # R^2 -> R^2
        ]

        self.run_multi_fns(fns)

    def test_multi_inverse_trig(self):
        """Ensure mult-dimensional inverse trigonometric functions are handled"""
        fns = [
            (lambda x: np.arcsin(x),
                [([0, 0.5], [0, 0.5235987756], [1, 0], [1, 0]),
                 ([0, 0.5], [0, 0.5235987756], [0, 1], [0, 1.1547005383793])]),
            (lambda x: np.arccos(x),
                [([0, 0.5], [np.pi / 2, 1.04719755119], [1, 0], [-1, 0]),
                 ([0, 0.5], [np.pi / 2, 1.04719755119], [0, 1], [0, -1.1547005383793])]),
            (lambda x: np.arctan(x),
                [([0, 0.5], [0, 0.463647609], [1, 0], [1, 0]),
                 ([0, 0.5], [0, 0.463647609], [0, 1], [0, 0.8])])
        ]

        self.run_multi_fns(fns)

    def test_multi_hyperbolic_trig(self):
        """Ensure mult-dimensional hyperbolic trigonometric functions are handled"""
        fns = [
            (lambda x: np.sinh(x),
                [([0, 1], [0, 1.17520119364], [1, 0], [1, 0]),  # R^2 -> R^2
                ([0, 1], [0, 1.17520119364], [0, 1], [0, 1.54308063482])]),  # R^2 -> R^2
            (lambda x: np.cosh(x),
                [([0, 1], [1, 1.54308063482], [1, 0], [0, 0]),  # R^2 -> R^2
                ([0, 1], [1, 1.54308063482], [0, 1], [0, 1.17520119364])]),  # R^2 -> R^2
            (lambda x: np.tanh(x),
                [([0, 1], [0, 0.76159415595], [1, 0], [1, 0]),  # R^2 -> R^2
                ([0, 1], [0, 0.76159415595], [0, 1], [0, 0.41997434161])]),  # R^2 -> R^2

            (lambda x: [np.sinh(x[0]), np.cosh(x[1])],
                [([0, np.pi / 2], [0, 2.50917847865], [1, 0], [1, 0]),  # R^2 -> R^2
                 ([0, np.pi / 2], [0, 2.50917847865], [0, 1], [0, 2.30129890231])])  # R^2 -> R^2
        ]

        self.run_multi_fns(fns)

    def test_multi_inverse_hyperbolic_trig(self):
        """Ensure mult-dimensional inverse hyperbolic trigonometric functions are handled"""
        fns = [
            (lambda x: np.arcsinh(x),
                [([0, 1], [0, 0.88137358702], [1, 0], [1, 0]),  # R^2 -> R^2
                ([0, 1], [0, 0.88137358702], [0, 1], [0, 0.70710678118])]),  # R^2 -> R^2
            (lambda x: np.arccosh(x),
                [([1.5, 2], [0.962423650119, 1.31695789692], [1, 0], [0.894427191, 0]),  # R^2 -> R^2
                ([1.5, 2], [0.962423650119, 1.31695789692], [0, 1], [0, 0.57735026919])]),  # R^2 -> R^2
            (lambda x: np.arctanh(x),
                [([0, 0.5], [0, 0.54930614433], [1, 0], [1, 0]),  # R^2 -> R^2
                ([0, 0.5], [0, 0.54930614433], [0, 1], [0, 1.33333333333])]),  # R^2 -> R^2
        ]

        self.run_multi_fns(fns)

    def test_multi_combinations(self):
        """Ensure complex combinations of trigonometric functions are handled"""
        fns = [
            # Trig
            (lambda x: np.sin(x)*np.cos(x),
                [([0, np.pi / 2], [0, 0], [1, 0], [1, 0]),
                ([0, np.pi / 2], [0, 0], [0, 1], [0, -1])]),
            (lambda x: np.cos(x) - 1 / np.tan(x),
                [([np.pi / 3, np.pi / 2], [-0.0773502691, 0], [1, 0], [0.46730792955, 0]),
                ([np.pi / 3, np.pi / 2], [-0.0773502691, 0], [0, 1], [0, 0])]),
            (lambda x: np.sin(np.tan(x)),
                [([0, np.pi / 4], [0, 0.841470984807], [1, 0], [1, 0]),
                ([0, np.pi / 4], [0, 0.841470984807], [0, 1], [0, 1.080604611736])]),

            # Inverse Trig
            (lambda x: np.arcsin(x) * np.arccos(x),
                [([0, 0.5], [0, 0.54831135561], [1, 0], [1.57079632679, 0]),
                ([0, 0.5], [0, 0.54831135561], [0, 1], [0, 0.604599788078])]),
            (lambda x: 1 / np.arcsin(x) + np.arctan(x) * np.sin(x),
                [([0.25, 0.5], [4.018179493221, 2.13214382177], [1, 0], [-15.70580906762, 0]),
                ([0.25, 0.5], [4.018179493221, 2.13214382177], [0, 1], [0, -3.421413023432])]),
            (lambda x: np.arcsin(np.arctan(x)),
                [([0, np.pi / 4], [0, 0.7285303236876], [1, 0], [1, 0]),
                ([0, np.pi / 4], [0, 0.7285303236876], [0, 1], [0, 0.8288995617946])]),

            # Hyperbolic Trig
            (lambda x: np.sinh(x) * np.cosh(x),
                [([0, 0.5], [0, 0.5876005968219], [1, 0], [1, 0]),
                ([0, 0.5], [0, 0.5876005968219], [0, 1], [0, 1.543080634815])]),
            (lambda x: np.cosh(x) - 1 / np.tanh(x),
                [([0.25, 0.5], [-3.051575065194, -1.0363274485322722], [1, 0], [15.923404672939, 0]),
                ([0.25, 0.5], [-3.051575065194, -1.0363274485322722], [0, 1], [0, 4.2037896823249])]),
            (lambda x: np.sinh(np.tanh(x)),
                [([0, 1], [0, 0.8373830985134536], [1, 0], [1, 0]),
                ([0, 1], [0, 0.8373830985134536], [0, 1], [0, 0.547774459868575])]),

            # Inverse Hyperbolic Trig
            (lambda x: np.arcsinh(x) * np.arccosh(x),
                [([2, 3], [1.9012071393175443, 3.205461357152708], [1, 0], [1.4224448064119, 0]),
                ([2, 3], [1.9012071393175443, 3.205461357152708], [0, 1], [0, 1.2003475121727])]),
            (lambda x: np.sin(x)/np.arctanh(x),
                [([0.25, 0.5], [0.9686434968965406, 0.8727838629684895], [1, 0], [-0.251777927028, 0]),
                ([0.25, 0.5], [0.9686434968965406, 0.8727838629684895], [0, 1], [0, -0.5208921443029])]),
            (lambda x: np.arccosh(np.arctanh(x)),
                [([0.8, 0.9], [0.4405289378985, 0.937150188986], [1, 0], [6.10612758217, 0]),
                ([0.8, 0.9], [0.4405289378985, 0.937150188986], [0, 1], [0, 4.87114359734])])
        ]

        self.run_multi_fns(fns)

    def test_non_dual(self):
        """Test the sigmoid and logb functions on scalars for coherence"""
        def f(x): return sigmoid(x)

        inputs = [0, 0.5, 5, -5]
        correct = [0.5, 0.6224593312, 0.993307149, 0.00669285092]
        return_vals = [f(x) for x in inputs]

        for correct, output in zip(correct, return_vals):
            assert isscalar(output)
            self.assertAlmostEqual(correct, output)

        def g(v, b): return logb(v, b)

        inputs = [(9, 3), (16, 2), (5.1, 7.2)]
        correct = [2, 4, 0.82531594106]
        return_vals = [g(v, b) for v, b in inputs]

        for correct, output in zip(correct, return_vals):
            assert isscalar(output)
            self.assertAlmostEqual(correct, output)