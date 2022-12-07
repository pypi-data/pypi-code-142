import unittest

import numpy as np
from projectq import MainEngine
from projectq.ops import (All, C, CNOT, DaggeredGate, H, Measure, R,
                          Rx, Ry, Rz, S, SqrtX, Swap, T, X, Y, Z,
                          Rxx, Rzz)
from projectq.backends import Simulator

from qhal.quantum_simulators import ProjectqQuantumSimulator
from qhal.hal import (QHALCommand, Opcode, 
                      binary_angle_conversion, measurement_unpacker)

class TestQuantumSimulators(unittest.TestCase):
    """
    Test that checks the projQ output by running a simple test circuit and
    checking that the final wavefunction is as expected.
    """

    def test_circuit_equivalence(self):
        """Test circuit programmed in QHAL is equivalent to that
        programmed directly in ProjectQ"""
        # set the size of the register
        n_qubits = 3

        projQ_backend = ProjectqQuantumSimulator(
            register_size=n_qubits,
            seed=234,
            backend=Simulator
        )

        hal_circuit = [
            ["START_SESSION", [0], [0]],
            ["STATE_PREPARATION_ALL", [0], [0]],
            ['X', [0], [0]],
            ['H', [0], [1]],
            ["T", [0], [0]],
            ["SX", [0], [1]],
            ["T", [0], [2]],
            ["S", [0], [2]],
            ["SWAP", [0,0], [1,2]],
            ["T", [0], [2]],
            ["INVS", [0], [2]],
            ['RZ', [672], [1]],
            ['SQRT_X', [0], [0]],
            ['PSWAP', [200,0], [0,1]],
            ["CNOT", [0,0], [0,2]],
            ["H", [0], [2]],
            ["PIXY", [458], [2]],
        ]

        for cmd in hal_circuit:
            projQ_backend.accept_command(QHALCommand(
                Opcode[cmd[0]], *cmd[1:]).to_binary())

        # extract wavefunction at the end of the circuit (before measuring)
        psi_projq_hal = np.array(projQ_backend._engine.backend.cheat()[1])
        projQ_backend.accept_command(QHALCommand(Opcode.END_SESSION).to_binary())

        projQ_eng = MainEngine()
        projQ_register = projQ_eng.allocate_qureg(n_qubits)
        qubit0 = projQ_register[0]
        qubit1 = projQ_register[1]
        qubit2 = projQ_register[2]

        pq_circuit = [
            (X, qubit0),
            (H, qubit1),
            (T, qubit0),
            (X, qubit1),
            (S, qubit1),
            (T, qubit2),
            (S, qubit2),
            (Swap, (qubit1, qubit2)),
            (T, qubit2),
            (DaggeredGate(S), qubit2),
            (Rz(binary_angle_conversion(672)), qubit1),
            (SqrtX, qubit0),
            ### PSWAP:
            (CNOT, (qubit1, qubit0)),
            (R(binary_angle_conversion(200)), qubit0),
            (CNOT, (qubit0, qubit1)),
            (CNOT, (qubit1, qubit0)),
            ###
            (CNOT, (qubit0, qubit2)),
            (H, qubit2),
            (Rz(binary_angle_conversion(-2*458)), qubit2),
            (Rx(binary_angle_conversion(32768)), qubit2)
        ]

        for command in pq_circuit:
            #pylint: disable=expression-not-assigned
            command[0] | command[1]
            projQ_eng.flush()

        psi_projq_sim = np.array(projQ_eng.backend.cheat()[1])
        #pylint: disable=expression-not-assigned
        All(Measure) | projQ_register
        projQ_eng.flush()

        for n, i in enumerate(list(psi_projq_sim)):
            self.assertAlmostEqual(i, list(psi_projq_hal)[n], places=10)

    def test_individual_qubit_measurements(self):
        """Test qubits are measured correctly"""
        projQ_backend = ProjectqQuantumSimulator(
            register_size=2,
            seed=234,
            backend=Simulator
        )

        circuit = [
            ["START_SESSION", [0], [0]],
            ["STATE_PREPARATION_ALL", [0], [0]],
            ['X', [0], [0]],
            ["QUBIT_MEASURE", [0], [0]],
            ["QUBIT_MEASURE", [0], [1]],
        ]

        def accept_command(cmd): return projQ_backend.accept_command(
            QHALCommand(Opcode[cmd[0]], *cmd[1:]).to_binary())

        responses = map(accept_command, circuit)
        measurements = [res for res in responses if res is not None]

        decoded_hal_result_0 = measurement_unpacker(measurements[0])
        decoded_hal_result_1 = measurement_unpacker(measurements[1])

        self.assertEqual(decoded_hal_result_0[0], 0)
        self.assertEqual(decoded_hal_result_0[3], 1)
        self.assertEqual(decoded_hal_result_1[0], 1)
        self.assertEqual(decoded_hal_result_1[3], 0)

    def test_variable_basis_measurement(self):
        """Tests that measuring in a rotated basis is equivalent
        to a rotation then measurement in the computational basis.
        """

        n = 4

        projQ_backend = ProjectqQuantumSimulator(
            register_size=n,
            seed=234,
            backend=Simulator
        )

        circuit = [
            QHALCommand(Opcode.START_SESSION),
            QHALCommand(Opcode.STATE_PREPARATION_ALL),
        ]

        list_arg0 = [0, 458, 0, 672]
        list_arg1 = [0, 0, 234, 458]

        for i in range(n):
            circuit.append(QHALCommand(Opcode.RY, [list_arg0[i]], [i]))
            circuit.append(QHALCommand(Opcode.RZ, [list_arg1[i]], [i]))
            circuit.append(QHALCommand(Opcode.QUBIT_MEASURE,
                                [list_arg0[i], list_arg1[i]], [i]))

        accept_command = lambda cmd : projQ_backend.accept_command(cmd.to_binary())

        responses = map(accept_command, circuit)
        measurements = [measurement_unpacker(res)[3] for res in responses if res is not None]
        self.assertTrue(all(m == 0 for m in measurements))

    def test_measurement_failures(self):
        """Tests that you can't measure the same qubit twice, or can't
        manipulate the qubit after measurement, but you can if you re-prepare
        the qubit state.
        """

        # single qubit
        projQ_backend = ProjectqQuantumSimulator(
            register_size=1,
            seed=234,
            backend=Simulator
        )

        circuit = [
            ["START_SESSION", [0], [0]],
            ["STATE_PREPARATION_ALL", [0], [0]],
            ['X', [0], [0]],
            ['QUBIT_MEASURE', [0], [0]]
        ]

        for cmd in circuit:
            hal_cmd = QHALCommand(Opcode[cmd[0]], *cmd[1:])
            projQ_backend.accept_command(hal_cmd.to_binary())

        with self.assertRaises(ValueError):
            projQ_backend.accept_command(
                QHALCommand(Opcode.QUBIT_MEASURE, [0, 0], [0]).to_binary()
            )
        projQ_backend.accept_command(QHALCommand(Opcode.END_SESSION).to_binary())

        # multi qubit
        projQ_backend = ProjectqQuantumSimulator(
            register_size=2,
            seed=234,
            backend=Simulator
        )

        circuit = [
            ["START_SESSION", [0], [0]],
            ["STATE_PREPARATION_ALL", [0], [0]],
            ['X', [0], [0]],
            ['QUBIT_MEASURE', [0, 0], [0]]
        ]

        for cmd in circuit:
            hal_cmd = QHALCommand(Opcode[cmd[0]], *cmd[1:])
            projQ_backend.accept_command(hal_cmd.to_binary())

        # try double measurement
        with self.assertRaises(ValueError):
            projQ_backend.accept_command(
                QHALCommand(Opcode.QUBIT_MEASURE, [0, 0], [0]).to_binary()
            )

        # try manipulation after measurement
        with self.assertRaises(ValueError):
            projQ_backend.accept_command(
                QHALCommand(Opcode.X, [0], [0]).to_binary()
            )

        # re-prepare state of qubit, then try bit-flip and measure
        projQ_backend.accept_command(
            QHALCommand(Opcode.STATE_PREPARATION, [0], [0]).to_binary()
        )
        projQ_backend.accept_command(
            QHALCommand(Opcode.X, [0], [0]).to_binary()
        )
        res = projQ_backend.accept_command(
            QHALCommand(Opcode.QUBIT_MEASURE, [0, 0], [0]).to_binary()
        )

        self.assertEqual(res, 1)

        projQ_backend.accept_command(QHALCommand(Opcode.END_SESSION).to_binary())

    def test_qubit_index_offset(self):
        """Tests that we can address qubit indices that exist
        """

        projQ_backend = ProjectqQuantumSimulator(
            register_size=11,
            seed=234,
            backend=Simulator)

        circuit = [
            ["START_SESSION", [0], [0]],
            ["STATE_PREPARATION_ALL", [0], [0]],
            ["PAGE_SET_QUBIT_0", [0], [10]],  # set offset
            ['X', [0], [0]],  # qubit index = 0 now refers to index = 10
            ['QUBIT_MEASURE', [0, 0], [0]],
            ['END_SESSION', [0], [0]]
        ]

        def accept_command(cmd):
            return projQ_backend.accept_command(QHALCommand(
                Opcode[cmd[0]], *cmd[1:]).to_binary())

        results = list(map(accept_command, circuit))
        res = measurement_unpacker(results[-2])

        self.assertEqual(res[0], 0)
        self.assertEqual(res[1], 10)  # offset is still set
        self.assertEqual(res[3], 1)

    def test_error_op_after_end_session(self):
        """Test that an error is thrown if commands are sent after a sessino ends"""
        projQ_backend = ProjectqQuantumSimulator(
            register_size=2,
            seed=234,
            backend=Simulator
        )

        projQ_backend.accept_command(
            QHALCommand(Opcode.START_SESSION, [0], [0]).to_binary())
        projQ_backend.accept_command(
            QHALCommand(Opcode.END_SESSION, [0], [0]).to_binary())

        with self.assertRaises(AttributeError):
            projQ_backend.accept_command(
                QHALCommand(Opcode.STATE_PREPARATION_ALL, [0], [0]).to_binary())

    def test_start_session_after_end_session(self):
        """Test that a session can start after another ends"""
        projQ_backend = ProjectqQuantumSimulator(
            register_size=2,
            seed=234,
            backend=Simulator
        )

        accept_command = lambda cmd : projQ_backend.accept_command(
            QHALCommand(Opcode[cmd[0]], *cmd[1:]).to_binary())

        accept_command(["START_SESSION", [0], [0]])
        with self.assertRaises(ValueError):
            accept_command(["START_SESSION", [0], [0]])
        accept_command(["END_SESSION", [0], [0]])

        circuit = [
            ["START_SESSION", [0], [0]],
            ["STATE_PREPARATION_ALL", [0], [0]],
            ['H', [0], [0]],
            ['X', [0], [1]],
            ['CNOT', [0, 0], [0, 1]],
            ["QUBIT_MEASURE", [0, 0], [0]],
            ["QUBIT_MEASURE", [0, 0], [1]],
            ["END_SESSION", [0], [0]]
        ]

        responses = map(accept_command, circuit)
        responses = list(responses)

        decoded_hal_result_0 = measurement_unpacker(responses[-3])
        decoded_hal_result_1 = measurement_unpacker(responses[-2])

        self.assertEqual(decoded_hal_result_0[0], 0)
        self.assertEqual(decoded_hal_result_1[0], 1)
        self.assertEqual((decoded_hal_result_0[3] + decoded_hal_result_1[3]), 1)

if __name__ == "__main__":
    unittest.main()
