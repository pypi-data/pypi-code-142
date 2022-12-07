import pytest
import unittest

from Adifpy.differentiate.evaluator import Evaluator
from Adifpy.differentiate.forward_mode import forward_mode
from Adifpy.differentiate.reverse_mode import reverse_mode


class TestEvaluator(unittest.TestCase):
    """Test class for evaluator"""

    def test_coherence(self):
        """Ensure using an Evaluator gives the same results as explicitly calling differentiation functions"""
        fns = [
            lambda x: x*x,
            lambda x: 5*x + x*5 + x**2,
            lambda x: 0,
            lambda x: -x + 3
        ]

        eval_pts = [1, 5, 0, -3, -0.2]

        for fn in fns:
            e = Evaluator(fn)

            for pt in eval_pts:
                assert e(pt, force_mode='forward') == forward_mode(fn, pt, seed_vector=1)
                assert e(pt, force_mode='reverse') == reverse_mode(fn, pt, seed_vector=1)

    def test_invalid_input(self):
        """Tests functionality of Evaluator when incorrect args passed"""

        e = Evaluator(fn=lambda x: x*x)

        with pytest.raises(TypeError):
            e(1, 1, 'bingbong')

        with pytest.raises(TypeError):
            e(1, 'ff', 'bingbong')

        def fn_bad(_):
            raise Exception

        with pytest.raises(RuntimeError):
            Evaluator(fn_bad)(1)

        def fn_bad_2(x):
            return x + 'hi'

        with pytest.raises(RuntimeError):
            Evaluator(fn_bad_2)(1)

        with pytest.raises(TypeError):
            Evaluator(lambda x: x)(pt=0, seed_vector='Bad')

        # Ensure that seed vector is requried for functions whose input space is not R
        with pytest.raises(AttributeError):
            Evaluator(lambda x: x[0] + x[1])([0, 2])

        # Ensure that a function that returns None is caught
        with pytest.raises(RuntimeError):
            Evaluator(lambda x: None)(0)

        # Ensure a user can only force forward or reverse mode
        with pytest.raises(ValueError):
            Evaluator(lambda x: x)(0, force_mode='Other')

        with pytest.raises(TypeError):
            Evaluator(lambda x: x)('a')

        # Ensure reverse mode cannot be called on multi-dimensional functions
        with pytest.raises(NotImplementedError):
            Evaluator(lambda x: x[0] + x[1])([0, 1], seed_vector=[1, 0], force_mode='reverse')