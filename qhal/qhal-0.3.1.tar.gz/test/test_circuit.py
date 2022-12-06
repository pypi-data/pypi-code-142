import unittest

from projectq.backends import Simulator

from qhal.hal import measurement_unpacker, Opcode, QHALCommand, QHALCircuit
from qhal.quantum_simulators import ProjectqQuantumSimulator

class TestQHALCircuit(unittest.TestCase):
    """Test QHALCircuit works properly"""

    def test_qhal_circuit_functionality(self):
        """
        Construct, run, and check results of a QHALCircuit.
        """

        # Test constructor
        cmds = [
            QHALCommand(Opcode.START_SESSION),
            QHALCommand(Opcode.STATE_PREPARATION_ALL),
            QHALCommand(Opcode.H, qubits=[0]),
            QHALCommand(Opcode.CNOT, qubits=[0, 1]),
            QHALCommand(Opcode.QUBIT_MEASURE, qubits=[0]),
            QHALCommand(Opcode.QUBIT_MEASURE, qubits=[1]),
        ]

        circ = QHALCircuit(cmds)
        self.assertEqual(circ.commands, cmds)
        self.assertEqual(len(circ), len(cmds))


        projQ_backend = ProjectqQuantumSimulator(
            register_size=2,
            seed=234,
            backend=Simulator
        )

        def accept_command(cmd):
            return projQ_backend.accept_command(cmd.to_binary())

        # Get responses, state should be (|00> + |11>)
        responses = list(map(accept_command, circ.commands))
        res1 = measurement_unpacker(responses[-2])[-1]
        res2 = measurement_unpacker(responses[-1])[-1]
        self.assertEqual(res1, res2)

    def test_qhal_circuit_add_and_append(self):
        """
        Test add_command / append of QHALCircuit
        """
        circ = QHALCircuit()
        circ.add_command(Opcode.STATE_PREPARATION, qubits=[0])
        circ.append(QHALCommand(Opcode.STATE_PREPARATION, qubits=[1]))
        self.assertEqual(
            circ.commands[0], QHALCommand(Opcode.STATE_PREPARATION, qubits=[0]))
        self.assertEqual(
            circ.commands[1], QHALCommand(Opcode.STATE_PREPARATION, qubits=[1]))

        with self.assertRaises(TypeError):
            circ.add_command("H", qubits=[0])

    def test_qhal_circuit_binary(self):
        """
        Tests the binary conversion of QHALCircuit
        """
        cmds = [
            QHALCommand(Opcode.START_SESSION),
            QHALCommand(Opcode.STATE_PREPARATION_ALL),
            QHALCommand(Opcode.H, qubits=[0]),
            QHALCommand(Opcode.CNOT, qubits=[0, 1]),
            QHALCommand(Opcode.QUBIT_MEASURE, qubits=[0]),
            QHALCommand(Opcode.QUBIT_MEASURE, qubits=[1]),
        ]
        circ = QHALCircuit(cmds)
        circ.to_file("test_circuit.qhal")

        circ1 = QHALCircuit.from_file("test_circuit.qhal")
        self.assertEqual(circ1.commands, circ.commands)

if __name__ == "__main__":
    unittest.main()
