from __future__ import annotations

from .vqe import EstimateOptSamplingVQE

from qiskit.algorithms.optimizers import Minimizer, Optimizer
from qiskit.algorithms.exceptions import AlgorithmError
from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library.n_local.qaoa_ansatz import QAOAAnsatz
from qiskit.quantum_info.operators.base_operator import BaseOperator
from qiskit.opflow import PauliSumOp, PrimitiveOp
from qiskit.primitives import BaseSampler, BaseEstimator
from qiskit.utils.validation import validate_min

from typing import Callable, Any
import numpy as np


class EstimateOptSamplingQAOA(EstimateOptSamplingVQE):
    """Modified version of :class:`.QAOA` by taking an optional ``Estimator`` for the
    energy evaluation during optimization.
    """

    def __init__(
        self,
        sampler: BaseSampler,
        optimizer: Optimizer | Minimizer,
        *,
        reps: int = 1,
        initial_state: QuantumCircuit | None = None,
        mixer: QuantumCircuit | BaseOperator | PauliSumOp = None,
        initial_point: np.ndarray | None = None,
        aggregation: float | Callable[[list[float]], float] | None = None,
        callback: Callable[[int, np.ndarray, float, dict[str, Any]], None]
        | None = None,
        estimator: BaseEstimator | None = None,
    ) -> None:
        validate_min("reps", reps, 1)

        self.reps = reps
        self.mixer = mixer
        self.initial_state = initial_state
        self._cost_operator = None

        super().__init__(
            sampler=sampler,
            ansatz=None,
            optimizer=optimizer,
            initial_point=initial_point,
            aggregation=aggregation,
            callback=callback,
            estimator=estimator,
        )

    def _check_operator_ansatz(self, operator: BaseOperator | PauliSumOp):
        if isinstance(operator, BaseOperator):
            try:
                operator = PrimitiveOp(operator)
            except TypeError as error:
                raise AlgorithmError(
                    f"Unsupported operator type {type(operator)} passed to QAOA."
                ) from error
        # Recreates a circuit based on operator parameter.
        self.ansatz = QAOAAnsatz(
            operator,
            self.reps,
            initial_state=self.initial_state,
            mixer_operator=self.mixer,
        ).decompose()  # TODO remove decompose once #6674 is fixed
