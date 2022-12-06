import pathlib
import unittest
from math import pi

import qiskit
from projectq.backends import Simulator

from qhal.hal import (angle_binary_representation,
                      qhal_from_qasm_str, qhal_from_qasm_file, 
                      QHALCommand, QHALCircuit)
from qhal.hal import Opcode as Op
from qhal.hal._qasm import insert_barriers_to_qasm, qhal_circuit_from_qiskit
from qhal.quantum_simulators import ProjectqQuantumSimulator


class QuantumCircuitToQhalTest(unittest.TestCase):
    """
    Test conversion from qiskit.QuantumCirctui to QHALCircuit
    """
    def test_one_qubit_fixed_rotations(self):
        """Test one-qubit rotations"""
        qc = qiskit.QuantumCircuit(1)

        # Pauli + H
        qc.x(0)
        qc.y(0)
        qc.z(0)
        qc.h(0)

        # Phase gates
        qc.t(0)
        qc.sdg(0)
        qc.tdg(0)
        qc.s(0)

        circ_qhal = qhal_circuit_from_qiskit(qc)
        
        qhal_cmds_ref = [
            QHALCommand(Op.START_SESSION),
            QHALCommand(Op.STATE_PREPARATION_ALL),
            QHALCommand(Op.X, qubits=[0]),
            QHALCommand(Op.Y, qubits=[0]),
            QHALCommand(Op.Z, qubits=[0]),
            QHALCommand(Op.H, qubits=[0]),
            QHALCommand(Op.T, qubits=[0]),
            QHALCommand(Op.INVS, qubits=[0]),
            QHALCommand(Op.INVT, qubits=[0]),
            QHALCommand(Op.S, qubits=[0]),
            QHALCommand(Op.END_SESSION),
        ]
        circ_qhal_ref = QHALCircuit(qhal_cmds_ref)
        self.assertEqual(circ_qhal, circ_qhal_ref)

    def test_one_qubit_parametrised_gates(self):
        """Test one-qubit parametrised gates"""
        qc = qiskit.QuantumCircuit(1)

        # Phase gates
        qc.p(pi/2, 0)

        # Rotations
        qc.rx(1, 0)
        qc.ry(2, 0)
        qc.rz(pi, 0)

        circ_qhal = qhal_circuit_from_qiskit(qc)

        qhal_cmds_ref = [
            QHALCommand(Op.START_SESSION),
            QHALCommand(Op.STATE_PREPARATION_ALL),
            QHALCommand(Op.PHASE,
                        args=[angle_binary_representation(pi/2)], qubits=[0]),
            QHALCommand(Op.RX,
                        args=[angle_binary_representation(1)], qubits=[0]),
            QHALCommand(Op.RY,
                        args=[angle_binary_representation(2)], qubits=[0]),
            QHALCommand(Op.RZ,
                        args=[angle_binary_representation(pi)], qubits=[0]),
            QHALCommand(Op.END_SESSION),
        ]
        circ_qhal_ref = QHALCircuit(qhal_cmds_ref)
        self.assertEqual(circ_qhal, circ_qhal_ref)

    def test_two_qubit_gates(self):
        """Test two-qubit gates"""
        qc = qiskit.QuantumCircuit(2)
        qc.cnot(1, 0)
        qc.swap(0, 1)
        qc.rzz(0.5, 1, 0)
        qc.rxx(0.5*pi, 0, 1)

        circ_qhal = qhal_circuit_from_qiskit(qc)

        qhal_cmds_ref = [
            QHALCommand(Op.START_SESSION),
            QHALCommand(Op.STATE_PREPARATION_ALL),
            QHALCommand(Op.CNOT, qubits=[1, 0]),
            QHALCommand(Op.SWAP, qubits=[0, 1]),
            QHALCommand(Op.RZZ,
                        args=[angle_binary_representation(0.5)], qubits=[1, 0]),
            QHALCommand(Op.RXX,
                        args=[angle_binary_representation(0.5*pi)], qubits=[0, 1]),
            QHALCommand(Op.END_SESSION),
        ]
        circ_qhal_ref = QHALCircuit(qhal_cmds_ref)
        self.assertEqual(circ_qhal, circ_qhal_ref)

    def test_measurement(self):
        """Test measurement"""
        qc = qiskit.QuantumCircuit(2, 2)
        qc.h(0)
        qc.cnot(0, 1)
        qc.measure([0, 1], [0, 1])

        circ_qhal = qhal_circuit_from_qiskit(qc)

        qhal_cmds_ref = [
            QHALCommand(Op.START_SESSION),
            QHALCommand(Op.STATE_PREPARATION_ALL),
            QHALCommand(Op.H, qubits=[0]),
            QHALCommand(Op.CNOT, qubits=[0, 1]),
            QHALCommand(Op.QUBIT_MEASURE, qubits=[0]),
            QHALCommand(Op.QUBIT_MEASURE, qubits=[1]),
            QHALCommand(Op.END_SESSION),
        ]
        circ_qhal_ref = QHALCircuit(qhal_cmds_ref)        
        self.assertEqual(circ_qhal, circ_qhal_ref)

    def test_unsupported_command(self):
        """Throw an exception if the command is not supported"""
        qc = qiskit.QuantumCircuit(2)
        qc.ms(0, [1])
        with self.assertRaises(NotImplementedError):
            qhal_from_qasm_str(qc.qasm())

    def test_multiqubit_commands(self):
        """Throw an exception if a 3-qubit/global operation is requested"""
        qc = qiskit.QuantumCircuit(3)
        qc.ccx(0, 1, 2)
        with self.assertRaises(NotImplementedError):
            qhal_from_qasm_str(qc.qasm())


class QasmToQhalTest(unittest.TestCase):
    """Test successful conversions of OpenQASM to QHAL.
    """

    def test_invalid_openqasm(self):
        """Throw an exception if the input OpenQASM is invalid"""
        qasm_str = "Random string"
        with self.assertRaises(qiskit.qasm.QasmError):
            qhal_from_qasm_str(qasm_str)

        qasm_str = "x q[0]"
        with self.assertRaises(qiskit.qasm.QasmError):
            qhal_from_qasm_str(qasm_str)

        qasm_str = "x q0"
        with self.assertRaises(qiskit.qasm.QasmError):
            qhal_from_qasm_str(qasm_str)

    def test_circuit_from_file(self):
        """Test converting from an OpenQASM file"""

        file_openqasm = pathlib.Path(__file__).parent / "data" / "test_circuit.qasm"
        qhal_cmds_ref = [
            QHALCommand(Op.START_SESSION),
            QHALCommand(Op.STATE_PREPARATION_ALL),
            QHALCommand(Op.H, qubits=[0]),
            QHALCommand(Op.CNOT, qubits=[0, 1]),
            QHALCommand(Op.RX,
                args=[angle_binary_representation(2)], qubits=[0]),
            QHALCommand(Op.S, qubits=[0]),
            QHALCommand(Op.RZ,
                args=[angle_binary_representation(5)], qubits=[0]),
            QHALCommand(Op.RY,
                args=[angle_binary_representation(0.2)], qubits=[1]),
            QHALCommand(Op.PHASE,
                args=[angle_binary_representation(pi/2)], qubits=[1]),
            QHALCommand(Op.Y, qubits=[1]),
            QHALCommand(Op.CNOT, qubits=[0, 1]),
            QHALCommand(Op.INVT, qubits=[0]),
            QHALCommand(Op.INVS, qubits=[0]),
            QHALCommand(Op.RZZ, args=[angle_binary_representation(pi/2)],
                qubits=[0, 1]),
            QHALCommand(Op.RXX, args=[angle_binary_representation(pi/2)],
                            qubits=[0, 1]),
            QHALCommand(Op.SX, qubits=[1]),
            QHALCommand(Op.SWAP, qubits=[0, 1]),
            QHALCommand(Op.ID, qubits=[0, 0]),
            QHALCommand(Op.QUBIT_MEASURE, qubits=[0]),
            QHALCommand(Op.QUBIT_MEASURE, qubits=[1]),
            QHALCommand(Op.END_SESSION)
        ]
        circ_hal_ref = QHALCircuit(qhal_cmds_ref)
        circ_qhal = qhal_from_qasm_file(file_openqasm)

        self.assertEqual(circ_qhal, circ_hal_ref)

    def test_barriers(self):
        """Test that `insert_barriers_to_qasm` successfully preserves
        the order of operations in the case of identity commutators, e.g.

        x q[0];
        x q[1];

        compared to:

        x q[1];
        x q[0];

        """

        qasm_str = "\n".join([
            "OPENQASM 2.0;",
            """include "qelib1.inc";""",
            "qreg q[2];",
            "h q[1];",
            "y q[0];",
        ])

        circ_qhal_ref = QHALCircuit([
            QHALCommand(Op.START_SESSION),
            QHALCommand(Op.STATE_PREPARATION_ALL),
            QHALCommand(Op.H, qubits=[1]),
            QHALCommand(Op.Y, qubits=[0]),
            QHALCommand(Op.END_SESSION),
        ])

        # The H and Y gates will commute
        self.assertNotEqual(qhal_from_qasm_str(qasm_str), circ_qhal_ref)
        self.assertEqual(
            set(qhal_from_qasm_str(qasm_str).to_binary()),
            set(circ_qhal_ref.to_binary()))

        # The barriers preserve the order of operations
        self.assertEqual(circ_qhal_ref,
                         qhal_from_qasm_str(insert_barriers_to_qasm(qasm_str)))

    def test_qasm_circuit_executes_successfully(self):
        """Test a QHAL circuit from OpenQASM runs on the simulator
        """
        qasm_str = """OPENQASM 2.0;
                      include "qelib1.inc";
                      qreg q[2];
                      creg c[2];
                      h q[0];
                      cx q[0], q[1];
                      measure q[0]->c[0];
                      measure q[1]->c[1];
        """

        qhal_program = qhal_from_qasm_str(qasm_str)

        sim = ProjectqQuantumSimulator(
            register_size=2,
            seed=234,
            backend=Simulator
        )

        for cmd in qhal_program.to_binary():
            sim.accept_command(cmd)

if __name__ == "__main__":
    unittest.main()