"""Defines a QHAL circuit
"""

from typing import List

import numpy as np
from numpy import uint64

from ._commands import Opcode, QHALCommand


class QHALCircuit():
    """Defines a QHAL circuit
    """
    def __init__(self, commands: List[QHALCommand] = None):
        self._commands = []
        if commands is None:
            pass
        elif isinstance(commands, list):
            for cmd in commands:
                self._commands.append(cmd)
        else:
            raise TypeError("List of commands must be of type List[QHALCommand]")

    def __len__(self):
        return len(self._commands)

    @property
    def commands(self):
        """Get the list of commands"""
        return self._commands

    def __eq__(self, other: "QHALCircuit"):
        return (len(self) == len(other) and
                all([self.commands[ii] == other.commands[ii] for ii in range(len(self))]))

    #pylint: disable=invalid-name
    def add_command(self, op: Opcode, args: List[int] = None, qubits: List[int] = None):
        """Create a new command at the end of the circuit"""
        self._commands.append(QHALCommand(op, args, qubits))

    def append(self, cmd: QHALCommand):
        """Append a QHALCommand at the end of the circuit"""
        if not isinstance(cmd, QHALCommand):
            raise TypeError("Command must of type QHALCommand")
        self._commands.append(cmd)

    def to_binary(self) -> List[uint64]:
        """Convert circuit to list of integer QHAL commands"""
        return [cmd.to_binary() for cmd in self.commands]

    def to_file(self, filename: str = None):
        """Serialise circuit to a file"""
        with open(filename, "wb") as out_file:
            for cmd_int in self.to_binary():
                out_file.write(cmd_int.tobytes())

    @classmethod
    def from_binary(cls, cmd_int_list: List[uint64]) -> "QHALCircuit":
        """Convert list of integer QHAL commands to a circuit"""
        commands = [QHALCommand.from_binary(cmd) for cmd in cmd_int_list]
        return QHALCircuit(commands=commands)

    @classmethod
    def from_file(cls, filename: str = None) -> "QHALCircuit":
        """Deserialise binary file to QHAL circuit"""
        cmd_int_list = np.fromfile(filename, dtype=uint64)
        return cls.from_binary(cmd_int_list)
