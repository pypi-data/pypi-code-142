import os
import unittest
import pytest

from Adifpy.differentiate.evaluator import Evaluator
from Adifpy.visualize.graph_function import draw, plot_evaluator

SAVE_FILEPATH = "temporary.png"


class TestGraphFunction(unittest.TestCase):
    """Test class for Graph function"""

    def test_draw(self):
        """Test that draw function actually generates a graph"""
        # Ensure the draw function handles normal cases correctly
        draw(func=lambda x: x * x ** 2, x_range=[-3, 3], y_range=[-2, 2], save_path=SAVE_FILEPATH)
        assert os.path.exists(SAVE_FILEPATH)
        os.remove(SAVE_FILEPATH)

        draw(func=lambda x: 4, x_range=[-3, -2], save_path=SAVE_FILEPATH)
        assert os.path.exists(SAVE_FILEPATH)
        os.remove(SAVE_FILEPATH)

        # Ensure the test_draw function handles incorrect input
        with pytest.raises(AssertionError):
            draw(func=lambda x: x, x_range=2, y_range=[-2, 2], save_path=SAVE_FILEPATH)

        with pytest.raises(TypeError):
            draw(x_range=[-2, 2], save_path=SAVE_FILEPATH)

        with pytest.raises(AssertionError):
            draw(func=lambda x: x, x_range=[-2, 2], y_range='', save_path=SAVE_FILEPATH)

        with pytest.raises(Exception):
            def f(_): raise ValueError
            draw(func=f, x_range=[-2, 2], save_path=SAVE_FILEPATH)

        # Ensure the failed calls did not create a file
        assert not os.path.exists(SAVE_FILEPATH)

    def test_evaluator_draw(self):
        """Test that plot_evaluator function actually generates a graph"""
        # Ensure the test_evaluator function handles normal cases correctly
        plot_evaluator(Evaluator(lambda x: x), x_range=[-1, 1], save_path=SAVE_FILEPATH)
        assert os.path.exists(SAVE_FILEPATH)
        os.remove(SAVE_FILEPATH)

        # Ensure the test_evaluator function handles incorrect input
        with pytest.raises(AssertionError):
            plot_evaluator(Evaluator(lambda x: x), x_range=2, y_range=[-2, 2], save_path=SAVE_FILEPATH)

        with pytest.raises(TypeError):
            plot_evaluator(x_range=[-2, 2], save_path=SAVE_FILEPATH)

        with pytest.raises(AssertionError):
            plot_evaluator(Evaluator(lambda x: x), x_range=[-2, 2], y_range='', save_path=SAVE_FILEPATH)

        with pytest.raises(Exception):
            def f(_): raise ValueError
            plot_evaluator(Evaluator(f), x_range=[-2, 2], save_path=SAVE_FILEPATH)

        # Ensure the failed calls did not create a file
        assert not os.path.exists(SAVE_FILEPATH)