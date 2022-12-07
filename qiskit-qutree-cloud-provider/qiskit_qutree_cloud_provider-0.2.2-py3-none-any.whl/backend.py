from qiskit.providers import BackendV2 as Backend
from qiskit.transpiler import Target
from qiskit.providers import Options
from qiskit.circuit.parameter import Parameter
from qiskit.circuit.library import (
    HGate,
    XGate,
    YGate,
    ZGate,
    SGate,
    SdgGate,
    IGate,
    UGate,
    CXGate,
    CZGate,
)
from qiskit.circuit.measure import Measure
from qiskit.result import Result
import grpc
import numpy as np

from .job import SyncJob
from .rpc import qutree_pb2, qutree_pb2_grpc
from ._version import __version__

from contextlib import contextmanager
import warnings
from abc import ABCMeta, abstractmethod


class QuTreeBackend(Backend, metaclass=ABCMeta):

    MAX_NQUBITS = 128

    def __init__(self, name="QuTreeBackend"):
        super().__init__(name=name, backend_version=__version__)

        self._target = Target(num_qubits=self.MAX_NQUBITS)
        theta, phi, lam = Parameter("θ"), Parameter("ϕ"), Parameter("λ")
        for _g in (
            HGate(),
            XGate(),
            YGate(),
            ZGate(),
            SGate(),
            SdgGate(),
            IGate(),
            UGate(theta, phi, lam),
            CXGate(),
            CZGate(),
            Measure(),
        ):
            self._target.add_instruction(_g)

        self.options.set_validator("shots", (1, 4096))
        self.options.set_validator("tree_type", ["binary", "train", "compact"])
        self.options.set_validator("tree_structure", str)
        self.options.set_validator("vbond_dim", (1, 2048))

    @classmethod
    def _default_options(cls):
        return Options(shots=1024, tree_type="binary", tree_structure="", vbond_dim=32)

    @property
    def target(self):
        return self._target

    @property
    def max_circuits(self):
        return None

    def _update_options(self, kwargs):
        _kwargs = {}
        for k, v in kwargs.items():
            if k not in self.options.__dict__:
                warnings.warn(
                    f"Option {k} is not used by this backend", UserWarning, stacklevel=2
                )
                continue
            _kwargs[k] = v
        self.options.update_options(**_kwargs)

    @abstractmethod
    def _run(self, circuits, **kwargs):
        """Circuit execution without the Qiskit job boilerplates"""
        pass

    def run(self, circuits, **kwargs):
        if type(circuits) not in (list, tuple):
            circuits = [circuits]
        rs = self._run(circuits, **kwargs)
        results = []
        time_stat = 0
        for r in rs:
            data = dict(
                counts=r.counts,
            )
            results.append(
                dict(
                    success=True,
                    shots=self.options.shots,
                    data=data,
                )
            )
            time_stat += r.time_taken
        job_id = ""
        result = Result.from_dict(
            dict(
                results=results,
                success=True,
                backend_name=self.name,
                backend_version=self.backend_version,
                job_id=job_id,
                qobj_id=", ".join(x.name for x in circuits),
                time_taken=time_stat / 1000,
            )
        )
        return SyncJob(self, job_id, result)

    @abstractmethod
    def compute_expectation(self, obs, circuit, **kwargs):
        """Compute <circuit|obs|circuit>
        Internal interface for ``QuTreeEstimator``.
        """
        pass


class QuTreeCloudBackend(QuTreeBackend):
    def __init__(self, addr):
        super().__init__(name="QuTreeCloudBackend")
        self.addr = addr

    @contextmanager
    def _connect(self):
        grpc_chan = (
            grpc.secure_channel(self.addr, grpc.ssl_channel_credentials())
            if self.addr.endswith(":443")
            else grpc.insecure_channel(self.addr)
        )
        with grpc_chan as channel:
            yield qutree_pb2_grpc.QuTreeRunnerStub(channel)

    def _run(self, circuits, **kwargs):
        self._update_options(kwargs)
        with self._connect() as stub:
            response = stub.RunCircuit(
                qutree_pb2.CircuitsWithOptions(
                    circuits=[circuit_pack(c) for c in circuits],
                    options=qutree_pb2.Options(**self.options.__dict__),
                )
            )
        return response.results

    def compute_expectation(self, obs, circuit, **kwargs):
        self._update_options(kwargs)
        with self._connect() as stub:
            response = stub.ComputeExpectation(
                qutree_pb2.CircuitsObservablesWithOptions(
                    circuits=[circuit_pack(circuit)],
                    observables=[pauli_pack(obs)],
                    options=qutree_pb2.Options(**self.options.__dict__),
                )
            )
        return response.results[0]


def circuit_encode(circuit):
    for op in circuit:
        if op.operation.name == "barrier":  # FIXME
            continue
        yield (
            op.operation.name,
            [circuit.find_bit(q).index for q in op.qubits],
            op.operation.params,
        )


def circuit_pack(circuit):
    return qutree_pb2.Circuit(
        ops=[
            qutree_pb2.Operation(name=name, qubits=qubits, params=params)
            for name, qubits, params in circuit_encode(circuit)
        ],
        nqubit=circuit.num_qubits,
    )


def pauli_encode(obs):
    for pauli, coeff in zip(obs.paulis, np.real(obs.coeffs)):
        yield (
            coeff,
            np.nonzero(pauli.z)[0],
            np.nonzero(pauli.x)[0],
        )


def pauli_pack(obs):
    return qutree_pb2.Observable(
        paulis=[
            qutree_pb2.PauliOp(coeff=coeff, ind_z=ind_z, ind_x=ind_x)
            for coeff, ind_z, ind_x in pauli_encode(obs)
        ],
    )
