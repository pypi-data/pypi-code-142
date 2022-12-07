"""Implements visualization of the function and its derivative"""

import matplotlib.pyplot as plt
import numpy as np

from Adifpy.differentiate.evaluator import Evaluator


def draw(func, x_range, y_range = None, save_path = None):
    """Graph a function

    Args:
        func (Callable): a function on which to evaluate
        pt (float): the point at which to evaluate
        x_range (list, optional): x range on which to plot the values
        save_path (str): path on which to save the image, or None to display
        y_range (list, optional): y range on which to plot the values
    """
    assert type(x_range) in [list, tuple] and len(x_range) == 2, \
        'Argument x_range must be a two-length list of tuple like [min, max]'

    x_values = np.arange(x_range[0], x_range[1], step=0.01)
    y_values = []
    dx_values = []

    evaluator = Evaluator(fn=func)

    for x in x_values:
        y, dx = evaluator(x)

        y_values.append(y)
        dx_values.append(dx)

    plt.plot(x_values, y_values, label="f(x)")
    plt.plot(x_values, dx_values, label="f'(x)")
    plt.title('f(x) and f\'(x)')

    plt.xlim(x_range)

    if y_range is not None:
        assert type(y_range) in [list, tuple] and len(y_range) == 2, \
            'Argument y_range must be a two-length list of tuple like [min, max]'
        plt.ylim(y_range)

    plt.legend()
    plt.grid()

    if save_path is not None:
        plt.savefig(save_path)
    else:
        plt.show()


def plot_evaluator(eval: Evaluator, x_range, y_range = None, save_path = None):
    """Plot an evaluator's function over a range"""
    draw(eval.fn, x_range, y_range, save_path)
