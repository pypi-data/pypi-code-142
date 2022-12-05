# SPDX-FileCopyrightText: 2022 Dominik Vilsmeier
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import numpy as np


__all__ = ['AddDeltaWeights']


array = np.ndarray


class AddDeltaWeights:
    """This class adds `weights` to the Jacobian during the fitting process.

    The weights are appended along the row, as a diagonal matrix starting from
    the leftmost column. Remaining columns are padded with zeros.

    In the following illustration, the top block is the original Jacobian and
    the bottom block is the one containing the weights (``len(weights) == 3``
    and ``J.shape[1] == 6`` in this case). Any empty space in the bottom block
    indicates a zero element. It can be seen that at the left there is the
    diagonal matrix ``(w1, w2, w3)`` which is padded at the right with zeros
    to match the number of columns of the original Jacobian.

    .. code-block::

       +------------+
       |            |
       |            |
       |            |
       |  Jacobian  |
       |            |
       |            |
       |            |
       +------------+
       |w1          |
       |  w2        |
       |    w3      |
       +------------+

    """

    def __init__(self, weights: array):
        self.weights = weights
        self._old_x = np.zeros(0)

    def to_residuals(self, x: array, residuals: array) -> array:
        """Transform the given `residuals` taking into account the parameter estimate `x`."""
        return np.concatenate([
            residuals,
            (x - (self._old_x if self._old_x.size else x))[:len(self.weights)],
        ])

    def to_jacobian(self, x: array, jacobian: array) -> array:
        """Transform the given `jacobian` taking into account the parameter estimate `x`."""
        self._old_x = x
        jacobian = np.concatenate([
            jacobian,
            np.concatenate([
                np.diag(self.weights),
                np.zeros((len(self.weights), jacobian.shape[1] - len(self.weights))),
            ], axis=1),
        ], axis=0)
        return jacobian
