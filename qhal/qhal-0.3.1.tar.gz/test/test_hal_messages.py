import itertools
import unittest

from qhal.hal._commands import (Opcode, QHALCommand,
                                command_creator, command_unpacker)

class QHALCommandTest(unittest.TestCase):
    """
    Basic tests for HAL command creation and result validation.
    """
    def test_roundtrip_qhal_commands(self):
        """Test roundtripping of the command packer/unpackers."""

        single_params = list(itertools.product(range(32), range(32), range(8)))
        dual_params = list(itertools.product(range(32), range(32), range(8), range(8)))

        for opcode in Opcode:
            if opcode == Opcode.Masks:
                continue
            if opcode.is_dual():
                for param_set in dual_params:
                    args = [param_set[0], param_set[1]]
                    qubits = [param_set[2], param_set[3]]
                    cmd = QHALCommand(opcode, args, qubits)

                    self.assertEqual(cmd.opcode, opcode)
                    self.assertEqual(cmd.args, args)
                    self.assertEqual(cmd.qubits, qubits)

                    self.assertEqual(
                        cmd, QHALCommand.from_binary(cmd.to_binary()))
            else:
                for param_set in single_params:
                    args = [param_set[0], param_set[1]]
                    qubit = param_set[2]
                    cmd = QHALCommand(opcode, args, [qubit])

                    self.assertEqual(cmd.opcode, opcode)
                    self.assertEqual(cmd.args, args)
                    self.assertEqual(cmd.qubits, [qubit, 0])
                    self.assertEqual(
                        cmd, QHALCommand.from_binary(cmd.to_binary()))

    def test_roundtrip_qhal_commands_old(self):
        """Test roundtripping of the command packer/unpackers."""

        single_params = list(itertools.product(range(32), range(32), range(8)))
        dual_params = list(itertools.product(
            range(32), range(32), range(8), range(8)))

        for opcode in Opcode:
            if opcode == Opcode.Masks:
                continue
            if opcode.is_dual():
                for param_set in dual_params:
                    args = [param_set[0], param_set[1]]
                    qubits = [param_set[2], param_set[3]]

                    self.assertEqual(command_unpacker(command_creator(
                        opcode.name, args, qubits)),
                        (opcode.name, "DUAL", args, qubits))
            else:
                for param_set in single_params:
                    args = [param_set[0], param_set[1]]
                    qubits = [param_set[2], 0]
                    self.assertEqual(command_unpacker(command_creator(
                        opcode.name, args, qubits)),
                        (opcode.name, "SINGLE", args, qubits))


if __name__ == "__main__":
    unittest.main()
