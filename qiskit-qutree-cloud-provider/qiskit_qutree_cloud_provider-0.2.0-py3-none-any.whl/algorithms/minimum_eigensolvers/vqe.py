from qiskit.primitives import BaseEstimator
from qiskit.circuit import QuantumCircuit
from qiskit.opflow import PauliSumOp
from qiskit.quantum_info.operators.base_operator import BaseOperator

from qiskit.algorithms.minimum_eigensolvers.sampling_vqe import (
    SamplingVQE,
    _compare_measurements,
)
from qiskit.algorithms.minimum_eigensolvers.diagonal_estimator import _DiagonalEstimator
from qiskit.algorithms.exceptions import AlgorithmError
from qiskit.algorithms.list_or_dict import ListOrDict
from qiskit.algorithms.minimum_eigensolvers.sampling_mes import (
    SamplingMinimumEigensolverResult,
)
from qiskit.algorithms.observables_evaluator import estimate_observables
from qiskit.algorithms.utils import validate_initial_point, validate_bounds

import numpy as np

from typing import Callable
from time import time
import logging

logger = logging.getLogger(__name__)


class EstimateOptSamplingVQE(SamplingVQE):
    """Modified version of :class:`.SamplingVQE` by taking an optional ``Estimator`` for the
    energy evaluation during optimization.
    """

    def __init__(self, *args, estimator: BaseEstimator | None = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.estimator = estimator

    def compute_minimum_eigenvalue(
        self,
        operator: BaseOperator | PauliSumOp,
        aux_operators: ListOrDict[BaseOperator | PauliSumOp] | None = None,
    ) -> SamplingMinimumEigensolverResult:
        # check that the number of qubits of operator and ansatz match, and resize if possible
        self._check_operator_ansatz(operator)

        if len(self.ansatz.clbits) > 0:
            self.ansatz.remove_final_measurements()
        if self.estimator is None:
            self.ansatz.measure_all()

        initial_point = validate_initial_point(self.initial_point, self.ansatz)

        bounds = validate_bounds(self.ansatz)

        evaluate_energy, best_measurement = self._get_evaluate_energy(
            operator, self.ansatz, return_best_measurement=True
        )

        start_time = time()

        if callable(self.optimizer):
            # pylint: disable=not-callable
            optimizer_result = self.optimizer(
                fun=evaluate_energy, x0=initial_point, bounds=bounds
            )
        else:
            # we always want to submit as many estimations per job as possible for minimal
            # overhead on the hardware
            was_updated = _set_default_batchsize(self.optimizer)

            optimizer_result = self.optimizer.minimize(
                fun=evaluate_energy, x0=initial_point, bounds=bounds
            )

            # reset to original value
            if was_updated:
                self.optimizer.set_max_evals_grouped(None)

        optimizer_time = time() - start_time

        logger.info(
            "Optimization complete in %s seconds.\nFound opt_params %s.",
            optimizer_time,
            optimizer_result.x,
        )

        if self.estimator is not None:
            self.ansatz.measure_all()
        final_state = (
            self.sampler.run([self.ansatz], [optimizer_result.x])
            .result()
            .quasi_dists[0]
        )

        if aux_operators is not None:
            aux_operators_evaluated = estimate_observables(
                _DiagonalEstimator(sampler=self.sampler),
                self.ansatz,
                aux_operators,
                optimizer_result.x,
            )
        else:
            aux_operators_evaluated = None

        return self._build_sampling_vqe_result(
            self.ansatz.copy(),
            optimizer_result,
            aux_operators_evaluated,
            best_measurement,
            final_state,
            optimizer_time,
        )

    def _get_evaluate_energy(
        self,
        operator: BaseOperator | PauliSumOp,
        ansatz: QuantumCircuit,
        return_best_measurement: bool = False,
    ) -> tuple[Callable[[np.ndarray], np.ndarray | float], dict]:
        num_parameters = ansatz.num_parameters
        if num_parameters == 0:
            raise AlgorithmError(
                "The ansatz must be parameterized, but has 0 free parameters."
            )

        # avoid creating an instance variable to remain stateless regarding results
        eval_count = 0

        best_measurement = {"best": None}

        def store_best_measurement(best):
            for best_i in best:
                if best_measurement["best"] is None or _compare_measurements(
                    best_i, best_measurement["best"]
                ):
                    best_measurement["best"] = best_i

        # XXX
        assert self.estimator is not None
        # TODO: callback=store_best_measurement
        estimator = self.estimator or _DiagonalEstimator(
            sampler=self.sampler,
            callback=store_best_measurement,
            aggregation=self.aggregation,
        )

        def evaluate_energy(parameters):
            nonlocal eval_count
            # handle broadcasting: ensure parameters is of shape [array, array, ...]
            parameters = np.reshape(parameters, (-1, num_parameters)).tolist()
            batch_size = len(parameters)

            estimator_result = estimator.run(
                batch_size * [ansatz], batch_size * [operator], parameters
            ).result()
            values = estimator_result.values

            if self.callback is not None:
                metadata = estimator_result.metadata
                for params, value, meta in zip(parameters, values, metadata):
                    eval_count += 1
                    self.callback(eval_count, params, value, meta)

            result = values if len(values) > 1 else values[0]
            return np.real(result)

        if return_best_measurement:
            return evaluate_energy, best_measurement

        return evaluate_energy


from qiskit.algorithms.optimizers import Optimizer, SPSA


def _set_default_batchsize(optimizer: Optimizer) -> bool:
    """Set the default batchsize, if None is set and return whether it was updated or not."""
    if isinstance(optimizer, SPSA):
        updated = optimizer._max_evals_grouped is None
        if updated:
            optimizer.set_max_evals_grouped(50)
    else:  # we only set a batchsize for SPSA
        updated = False

    return updated
