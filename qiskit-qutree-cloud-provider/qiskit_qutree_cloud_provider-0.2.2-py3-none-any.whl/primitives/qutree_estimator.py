"""
Estimator class
"""

from __future__ import annotations
from collections.abc import Iterable, Sequence
from typing import Any

import numpy as np

from qiskit.circuit import Parameter, QuantumCircuit
from qiskit.exceptions import QiskitError
from qiskit.opflow import PauliSumOp
from qiskit.quantum_info.operators.base_operator import BaseOperator

from qiskit.primitives.base import BaseEstimator, EstimatorResult
from qiskit.primitives.primitive_job import PrimitiveJob
from qiskit.primitives.utils import (
    _circuit_key,
    _observable_key,
    bound_circuit_to_instruction,
    init_circuit,
    init_observable,
)


class QuTreeEstimator(BaseEstimator):
    """
    Compute expectation value QuTree's tree tensornetwork operations

    :Run Options:
        - **quantum_instance** (QuantumInstance[QuTreeBackend]) --
    """

    def __init__(
        self,
        circuits: QuantumCircuit | Iterable[QuantumCircuit] | None = None,
        observables: BaseOperator
        | PauliSumOp
        | Iterable[BaseOperator | PauliSumOp]
        | None = None,
        parameters: Iterable[Iterable[Parameter]] | None = None,
        options: dict | None = None,
    ):
        """
        Args:
            circuits: circuits that represent quantum states.
            observables: observables to be estimated.
            parameters: Parameters of each of the quantum circuits.
                Defaults to ``[circ.parameters for circ in circuits]``.
            options: Default options.

        Raises:
            QiskitError: if some classical bits are not used for measurements.
        """
        if isinstance(circuits, QuantumCircuit):
            circuits = (circuits,)
        if circuits is not None:
            circuits = tuple(init_circuit(circuit) for circuit in circuits)

        if isinstance(observables, (PauliSumOp, BaseOperator)):
            observables = (observables,)
        if observables is not None:
            observables = tuple(
                init_observable(observable) for observable in observables
            )

        super().__init__(
            circuits=circuits,
            observables=observables,
            parameters=parameters,
            options=options,
        )
        self._is_closed = False
        self.quantum_instance = options.pop("quantum_instance")
        self.time_qutree = 0.0
        self._transpiled = set()

    def _call(
        self,
        circuits: Sequence[int],
        observables: Sequence[int],
        parameter_values: Sequence[Sequence[float]],
        **run_options,
    ) -> EstimatorResult:
        if self._is_closed:
            raise QiskitError("The primitive has been closed.")

        shots = run_options.pop("shots", None)
        if shots is not None and shots > 1:
            raise NotImplementedError(
                "Please use Qiskit's default Estimator for sampling-based expectation estimation"
            )

        metadata: list[dict[str, Any]] = [{}] * len(circuits)

        # print(circuits, observables) # XXX
        # print(self._parameters, self._observables) # XXX
        bound_circuits = []
        for i, value in zip(circuits, parameter_values):
            if len(value) != len(self._parameters[i]):
                raise QiskitError(
                    f"The number of values ({len(value)}) does not match "
                    f"the number of parameters ({len(self._parameters[i])})."
                )
            # print(i, self._circuits[i]) # XXX
            if (
                i not in self._transpiled
            ):  # We have received a new circuit with unexpanded block operator
                self._circuits[i] = self.quantum_instance.transpile(self._circuits[i])[
                    0
                ]
                self._transpiled.add(i)
                # print("after-trans", self._circuits[i])  # XXX
            bound_circuits.append(
                self._circuits[i]
                if len(value) == 0
                else self._circuits[i].bind_parameters(
                    dict(zip(self._parameters[i], value))
                )
            )
        sorted_observables = [self._observables[i] for i in observables]
        expectation_values = []
        for circ, obs in zip(bound_circuits, sorted_observables):
            if circ.num_qubits != obs.num_qubits:
                raise QiskitError(
                    f"The number of qubits of a circuit ({circ.num_qubits}) does not match "
                    f"the number of qubits of a observable ({obs.num_qubits})."
                )
            # from qiskit.quantum_info import Statevector
            # final_state = Statevector(bound_circuit_to_instruction(circ))
            # expectation_value = final_state.expectation_value(obs)
            # print(expectation_value)
            result = self.quantum_instance.backend.compute_expectation(obs, circ)
            self.time_qutree += result.time_taken / 1000
            expectation_value = result.expval
            # print(expectation_value)
            expectation_values.append(expectation_value)

        return EstimatorResult(np.real_if_close(expectation_values), metadata)

    def close(self):
        self._is_closed = True

    def _run(
        self,
        circuits: Sequence[QuantumCircuit],
        observables: Sequence[BaseOperator | PauliSumOp],
        parameter_values: Sequence[Sequence[float]],
        **run_options,
    ) -> PrimitiveJob:
        circuit_indices = []
        for circuit in circuits:
            key = _circuit_key(circuit)
            index = self._circuit_ids.get(key)
            if index is not None:
                circuit_indices.append(index)
            else:
                circuit_indices.append(len(self._circuits))
                self._circuit_ids[key] = len(self._circuits)
                self._circuits.append(circuit)
                self._parameters.append(circuit.parameters)
        observable_indices = []
        for observable in observables:
            observable = init_observable(observable)
            index = self._observable_ids.get(_observable_key(observable))
            if index is not None:
                observable_indices.append(index)
            else:
                observable_indices.append(len(self._observables))
                self._observable_ids[_observable_key(observable)] = len(
                    self._observables
                )
                self._observables.append(observable)
        job = PrimitiveJob(
            self._call,
            circuit_indices,
            observable_indices,
            parameter_values,
            **run_options,
        )
        job.submit()
        return job
