# SPDX-FileCopyrightText: 2022 Dominik Vilsmeier
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from dataclasses import dataclass
import itertools as it
from typing import Callable, Collection
import warnings

import numpy as np
from scipy.optimize import least_squares  # type: ignore


__all__ = ['LeastSquares', 'GaussNewton', 'Feedback', 'Result']


array = np.ndarray
norm = np.linalg.norm


@dataclass
class Result:
    """This class mimics ``scipy.optimize.OptimizeResult`` and contains various information
       about the results of a fitting/optimization process.
    """

    x: array
    fun: array
    jac: array
    nfev: int
    njev: int
    status: int
    message: str

    @property
    def cost(self):
        return 0.5 * np.sum(self.fun**2)

    @property
    def grad(self):
        return self.jac.T @ self.fun

    @property
    def success(self):
        return self.status > 0


class Optimizer:
    def run(
        self,
        *,
        f: Callable[[array], array],
        j: Callable[[array], array],
        x0: array,
    ) -> Result:
        raise NotImplementedError


class LeastSquares(Optimizer):
    """A thin wrapper around :func:`scipy.optimize.least_squares`.

    Args:
        configuration: Any keyword-arguments for :func:`scipy.optimize.least_squares`.
    """

    def __init__(self, **configuration):
        self.configuration = configuration

    def run(
        self,
        *,
        f: Callable[[array], array],
        j: Callable[[array], array],
        x0: array,
    ) -> Result:
        result = least_squares(fun=f, x0=x0, jac=j, **self.configuration)
        return Result(
            x=result.x,
            fun=result.fun,
            jac=result.jac,
            nfev=result.nfev,
            njev=result.njev,
            status=result.status,
            message=result.message,
        )


class GaussNewton(Optimizer):
    """Implementation of the Gauss-Newton optimizer.

    Args:
        maxiter: Maximum number of iterations that will be performed.
        step_size: The step size used for updating the current guess during each iteration.
            This is a scaling factor in the sense that it is multiplied with the update obtained
            from solving the Gauss-Newton step. Hence, the `step_size` does not determine the actual
            magnitude of the update but rather it is a scaling factor for each update.
        drop_singular_values: Collection of indices of singular values that will be set to zero.
        ftol, xtol, gtol: See :func:`scipy.optimize.least_squares`.
    """

    def __init__(
        self,
        *,
        maxiter: int = None,
        step_size: float = 0.1,
        drop_singular_values: Collection[int] = (-2, -1),
        ftol: float = 1e-8,
        xtol: float = 1e-8,
        gtol: float = 1e-8,
    ):
        super().__init__()
        self.maxiter = maxiter
        self.step_size = step_size
        self.drop_singular_values = drop_singular_values
        self.ftol = ftol
        self.xtol = xtol
        self.gtol = gtol

    def run(
        self,
        *,
        f: Callable[[array], array],
        j: Callable[[array], array],
        x0: array,
    ) -> Result:

        compute_fun = f
        compute_jac = j

        def cost(r):
            return 0.5 * np.sum(r**2)

        pc = x0.copy()
        pc_residuals = compute_fun(pc)

        for iter_count in it.count():

            old_pc = pc.copy()
            old_residuals = pc_residuals
            c0 = cost(old_residuals)
            J = compute_jac(old_pc)

            if self.maxiter and iter_count >= self.maxiter:
                message, status = 'maxiter exceeded', 0
                break
            if check_gtol_satisfied(self.gtol, jacobian=J, residuals=old_residuals):
                message, status = 'gtol satisfied', 1
                break

            update = -solve_lstsq_via_svd_trunc(J, old_residuals, drop=self.drop_singular_values)

            # This could use `scipy.optimize.line_search` instead of a fixed step size.
            # However, line search requires more function evaluations.
            pc = old_pc + self.step_size*update
            pc_residuals = compute_fun(pc)
            c1 = cost(pc_residuals)

            if c1 > c0:
                warnings.warn(f'Gauss-Newton step diverged: {c1:.3e} > {c0:.3e}')
            else:
                is_ftol_satisfied = check_ftol_satisfied(self.ftol, old_cost=c0, new_cost=c1)
                is_xtol_satisfied = check_xtol_satisfied(self.xtol, old_x=old_pc, new_x=pc)
                if is_ftol_satisfied or is_xtol_satisfied:
                    if is_ftol_satisfied and is_xtol_satisfied:
                        message, status = 'ftol and xtol satisfied', 4
                    elif is_ftol_satisfied:
                        message, status = 'ftol satisfied', 2
                    elif is_xtol_satisfied:
                        message, status = 'xtol satisfied', 3
                    else:
                        assert False
                    break

        return Result(
            x=pc,
            fun=pc_residuals,
            jac=J,
            nfev=iter_count+1,
            njev=iter_count+1,
            status=status,
            message=message,
        )


class Feedback(Optimizer):
    """Implementation of a feedback-like optimizer which uses a constant Jacobian.

    The Jacobian is computed once for the initial guess of parameters and then used throughout
    the optimization procedure.

    The sum of number of quadrupoles, horizontal BPMs and steerers, vertical BPMs and steerers
    must match the number of columns in the Jacobian. Similarly, the number of BPMs and steerers
    must match the size of the computed ORM or residuals.

    Args:
        maxiter: Maximum number of iterations that will be performed.
        drop_singular_values: Collection of indices of singular values that will be set to zero.
        ftol, xtol, gtol: See :func:`scipy.optimize.least_squares`.
    """

    def __init__(
        self,
        *,
        maxiter: int = None,
        drop_singular_values: Collection[int] = (-2, -1),
        ftol: float = 1e-8,
        xtol: float = 1e-8,
        gtol: float = 1e-8,
    ):
        super().__init__()
        self.maxiter = maxiter
        self.drop_singular_values = drop_singular_values
        self.ftol = ftol
        self.xtol = xtol
        self.gtol = gtol

    def run(
        self,
        *,
        f: Callable[[array], array],
        j: Callable[[array], array],
        x0: array,
    ) -> Result:

        def cost(r):
            return 0.5 * np.sum(r**2)

        J = j(x0)
        guess = x0.copy()
        residuals = f(guess)
        c0 = cost(residuals)

        for iter_count in it.count():

            if self.maxiter and iter_count >= self.maxiter:
                message, status = 'maxiter exceeded', 0
                break
            if check_gtol_satisfied(self.gtol, jacobian=J, residuals=residuals):
                message, status = 'gtol satisfied', 1
                break

            update = -solve_lstsq_via_svd_trunc(
                J,
                residuals,
                drop=self.drop_singular_values,
            )
            guess += update
            residuals = f(guess)

            c1 = cost(residuals)

            if c1 > c0:
                warnings.warn(f'Feedback step diverged: {c1:.3e} > {c0:.3e}')
            else:
                is_ftol_satisfied = check_ftol_satisfied(self.ftol, old_cost=c0, new_cost=c1)
                is_xtol_satisfied = check_xtol_satisfied(self.xtol, old_x=guess-update, new_x=guess)
                if is_ftol_satisfied or is_xtol_satisfied:
                    if is_ftol_satisfied and is_xtol_satisfied:
                        message, status = 'ftol and xtol satisfied', 4
                    elif is_ftol_satisfied:
                        message, status = 'ftol satisfied', 2
                    elif is_xtol_satisfied:
                        message, status = 'xtol satisfied', 3
                    else:
                        assert False
                    break

            c0 = c1

        return Result(
            x=guess,
            fun=residuals,
            jac=j(guess),
            nfev=iter_count+1,
            njev=iter_count+1,
            status=status,
            message=message,
        )


def solve_lstsq_via_svd_trunc(A: array, b: array, *, drop: Collection[int]) -> array:
    """Solve a linear least squares system via SVD and truncating a specified number of singular values.

    Args:
        A: The matrix containing the coefficients of the system of linear equations.
        b: The r.h.s. vector (can be given as a 1d-array).
        drop: Collection of indices of singuar values that will be dropped from the SVD (set to zero).

    Returns:
        The solution of the system.
    """
    drop = sorted(drop)
    u, s, vh = np.linalg.svd(A, full_matrices=False)
    s_new = s.copy()
    s_new[drop] = 0
    A_new = u @ (np.diag(s_new) @ vh)
    u, s, vh = np.linalg.svd(A_new.T @ A_new, full_matrices=False)
    s[drop] = 1  # prevent division by zero
    s_inv = 1 / s
    s_inv[drop] = 0
    AA_inv = vh.T @ (np.diag(s_inv) @ u.T)
    return AA_inv @ (A.T @ b)


def check_ftol_satisfied(ftol: float, *, old_cost: float, new_cost: float) -> bool:
    """Check if the `ftol` condition is satisified for the given values.

    For details see :func:`scipy.optimize.least_squares`.
    """
    return old_cost > new_cost and old_cost - new_cost < ftol*old_cost


def check_gtol_satisfied(gtol: float, *, jacobian: array, residuals: array) -> bool:
    """Check if the `gtol` condition is satisified for the given values.

    For details see :func:`scipy.optimize.least_squares`.
    """
    return np.abs(jacobian.T @ residuals / (norm(jacobian.T, axis=1) * norm(residuals))).max() < gtol


def check_xtol_satisfied(xtol: float, *, old_x: array, new_x: array) -> bool:
    """Check if the `xtol` condition is satisified for the given values.

    For details see :func:`scipy.optimize.least_squares`.
    """
    return norm(new_x - old_x) < xtol * (xtol + norm(old_x))
