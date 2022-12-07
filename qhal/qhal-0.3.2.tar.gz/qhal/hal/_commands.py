"""
All the commands respect the following structure:

+------------------+----------+-----------------+-----------------------------+
| Command type     | OPCODE   | ARGUMENT        | RELATIVE_QUBIT_IDX          |
|                  |          |                 |                             |
| Control, Single, | Command  | Argument for    | Relative index of the       |
| or Dual Qubit    | to       | the command     | QUBIT                       |
| command          | execute  |                 |                             |
+==================+==========+=================+=============================+
| CONTROL COMMANDS | [63-52]  | [51-36]         | [35-0] BASE_QUBIT0/1_IDX    |
+------------------+----------+-----------------+-----------------------------+
| SINGLE QUBIT     | [63-52]  | [51-36] padding | [19-10] padding             |
| COMMANDS         |          |                 |                             |
|                  |          | [35-20] arg     | [9-0] RELATIVE_QUBIT0_IDX   |
+------------------+----------+-----------------+-----------------------------+
| DUAL QUBIT       | [63-52]  | [51-36] arg1    | [19-10] RELATIVE_QUBIT1_IDX |
| COMMANDS         |          |                 |                             |
|                  |          | [35-20] arg0    | [9-0] RELATIVE_QUBIT0_IDX   |
+------------------+----------+-----------------+-----------------------------+

OPCODE is structured as:
SINGLE/DUAL | CONSTANT/PARAMETRIC   |   OPCODE
[63]        |   [62]                |   [61-52]

"""

from enum import Enum, IntFlag, IntEnum
from typing import List, Tuple
import warnings

from numpy import uint64


class Opcode(Enum):
    """
    Opcode enum

    Defines the list of allowable QHAL operations and 
    their integer representations.
    """
    NOP = 0

    class Masks(IntFlag):
        """
        Masks used to decompose/create the opcodes

        An operation is 
        - CONST if it takes no parameters
        - PARAM otherwise.

        An operation is 
        - SINGLE if it operates on one qubit or takes one qubit index,
        - DUAL if it operates on two.
        """
        # Relative to 12-bit OPCODE
        CONST = 0x0
        PARAM = 0x400

        SINGLE = 0x0
        DUAL = 0x800

    ## Configuration Session
    START_SESSION = 1 | Masks.SINGLE | Masks.CONST
    END_SESSION = 2 | Masks.SINGLE | Masks.CONST
    PAGE_SET_QUBIT_0 = 3 | Masks.SINGLE | Masks.CONST
    PAGE_SET_QUBIT_1 = 4 | Masks.SINGLE | Masks.CONST
    STATE_PREPARATION_ALL = 5 | Masks.SINGLE | Masks.CONST
    STATE_PREPARATION = 6 | Masks.SINGLE | Masks.CONST
    QUBIT_MEASURE = 7 | Masks.SINGLE | Masks.PARAM
    REQUEST_METADATA =8 | Masks.DUAL | Masks.PARAM

    # SINGLE WORD Commands
    ## Arbitrary Rotations
    RX = 10 | Masks.SINGLE | Masks.PARAM
    RY = 11 | Masks.SINGLE | Masks.PARAM
    RZ = 12 | Masks.SINGLE | Masks.PARAM
    R = 13 | Masks.SINGLE | Masks.PARAM

    ## Paulis
    PAULI_X = 20 | Masks.SINGLE | Masks.CONST
    PAULI_Y = 21 | Masks.SINGLE | Masks.CONST
    PAULI_Z = 22 | Masks.SINGLE | Masks.CONST

    ## Others
    H = 30 | Masks.SINGLE | Masks.CONST
    PHASE = 31 | Masks.SINGLE | Masks.PARAM
    T = 32 | Masks.SINGLE | Masks.CONST
    S = 33 | Masks.SINGLE | Masks.CONST
    X = 34 | Masks.SINGLE | Masks.CONST
    Y = 35 | Masks.SINGLE | Masks.CONST
    Z = 36 | Masks.SINGLE | Masks.CONST
    INVT = 37 | Masks.SINGLE | Masks.CONST
    INVS = 38 | Masks.SINGLE | Masks.CONST
    SX = 39 | Masks.SINGLE | Masks.CONST
    SY = 40 | Masks.SINGLE | Masks.CONST
    PIXY = 41 | Masks.SINGLE | Masks.PARAM
    PIYZ = 42 | Masks.SINGLE | Masks.PARAM
    PIZX = 43 | Masks.SINGLE | Masks.PARAM
    SQRT_X = 44 | Masks.SINGLE | Masks.CONST

    ## Flow commands (still to be considered/not accepted yet)
    FOR_START = 50 | Masks.SINGLE | Masks.PARAM
    FOR_END = 51 | Masks.SINGLE | Masks.PARAM
    IF = 52 | Masks.SINGLE | Masks.PARAM
    WHILE = 53 | Masks.SINGLE | Masks.PARAM

    # DUAL WORD Commands
    CNOT = 60 | Masks.DUAL | Masks.CONST
    SWAP = 61 | Masks.DUAL | Masks.CONST
    PSWAP = 62 | Masks.DUAL | Masks.PARAM
    RZZ = 63 | Masks.DUAL | Masks.PARAM
    RXX = 64 | Masks.DUAL | Masks.PARAM

    # VERSIONING
    ID = 1000 | Masks.SINGLE | Masks.CONST

    def is_dual(self) -> bool:
        "Returns true if command with this opcode operates on two qubits rather than one"
        return bool(int(self.value) & int(Opcode.Masks.value.DUAL.value))

    def has_param(self) -> bool:
        "Returns true if command with this opcode has parameters"
        return bool(int(self.value) & int(Opcode.Masks.value.PARAM.value))


class QHALCommand:
    """
    Class to describe a QHAL command.
    """
    # pylint: disable=dangerous-default-value,invalid-name
    def __init__(self, op: Opcode, args: List[int] = None, qubits: List[int] = None):
        """Constructor of a QHAL Command

        Parameters
        ----------
        op : Opcode
            The quantum operation
        args : List[int], optional
            Non-qubit arguments to the operation. Takes up to two.
        qubits : List[int], optional
            Qubit indicies. Takes up to two.
        """
        if not isinstance(op, Opcode):
            raise TypeError("Opcode must be of type Opcode!")
        self._opcode = op

        args = [0, 0] if args is None else args
        if not isinstance(args, list) or len(args) > 2:
            raise TypeError(
                "Arguments must be a None or a list of length two or less")
        self._arg0 = args[0]
        self._arg1 = args[1] if len(args) > 1 else 0

        qubits = [0, 0] if qubits is None else qubits
        if not isinstance(qubits, list) or len(qubits) > 2:
            raise TypeError(
                "Qubits argument must be a None or a list of length two or less")
        self._qidx0 = qubits[0]
        self._qidx1 = qubits[1] if len(qubits) > 1 else 0

    class Shifts(IntEnum):
        """
        Defines the bit index of the of the command subfields.
        """
        OPCODE_TYPE = 63

        OPCODE = 52
        ARG0 = 20
        IDX0 = 0
        ARG1 = 36
        IDX1 = 10

    class Masks(IntEnum):
        """Masks for decoding QHAL binary
        """
        # Relative to entire 64-bit command
        QUBIT0 = 0x3FF
        QUBIT1 = 0xFFC00
        ARG0 = 0xFFFF00000
        ARG1 = 0xFFFF000000000

    def to_binary(self) -> uint64:
        """
        Generate 64-bit binary form of QHAL command
        """
        cmd = (
            (int(self._opcode.value) << self.Shifts.OPCODE)
            | (self._arg0 << self.Shifts.ARG0)
            | (self._arg1 << self.Shifts.ARG1)
            | (self._qidx1 << self.Shifts.IDX1)
            | self._qidx0
        )
        return uint64(cmd)

    @classmethod
    def from_binary(cls, cmd: uint64) -> "QHALCommand":
        """Constructor to create QHALCommand from bitstring

        Parameters
        ----------
        cmd : uint64
            QHAL command bitcode

        Returns
        -------
        QHALCommand
        """
        if not isinstance(cmd, uint64):
            raise TypeError("Command from binary should take uint64")
        cmd = int(cmd)
        op = Opcode(cmd >> (cls.Shifts.OPCODE))

        # Extracting args and qubits
        args = []
        qubits = []

        qubits.append(cmd & cls.Masks.QUBIT0)
        args.append((cmd & cls.Masks.ARG0) >> cls.Shifts.ARG0)
        args.append((cmd & cls.Masks.ARG1) >> cls.Shifts.ARG1)

        if op.is_dual():
            qubits.append(
                (cmd & cls.Masks.QUBIT1) >> cls.Shifts.IDX1)

        return QHALCommand(op, args, qubits)

    def __str__(self) -> str:
        return(f"QHALCommand({self._opcode}: args=[{self._arg0}, {self._arg1}], "+
                f"qubits=[{self._qidx0}, {self._qidx1}])")

    def __eq__(self, other: "QHALCommand") -> bool:
        return (self.opcode == other.opcode and
                self.args == other.args and
                self.qubits == other.qubits)

    @property
    def opcode(self) -> Opcode:
        "Get opcode"
        return self._opcode

    @property
    def qubits(self) -> List[int]:
        "Get qubit indicies"
        return [self._qidx0, self._qidx1]

    @property
    def args(self) -> List[int]:
        "Get arguments"
        return [self._arg0, self._arg1]


def command_creator(
        op: str, args: List[int] = None, qubits: List[int] = None
) -> uint64:
    """Helper function to create HAL commands.

    Parameters
    ----------
    op : str
        Name of opcode.
    args : List[int]
        List of integer representation of argument value [arg0, arg1]
    qubit : List[int]
        List of integer representation of qubit address [qidx0, qidx1]
    Returns
    -------
    uint64
        64-bit (8 bytes) HAL command.
    """
    warnings.warn("This interface is now deprecated. "
                  "Please use the new QHALCommand and Opcode classes.",
                  DeprecationWarning)
    return QHALCommand(Opcode[op], args=args, qubits=qubits).to_binary()


def command_unpacker(
    cmd: uint64
) -> Tuple[str, str, List[int], List[int]]:
    """Helper function to unpack HAL commands.

    Parameters
    ----------
    cmd: uint64
    64-bit(8 bytes) HAL command.

    Returns
    -------
    op: str
    Name of opcode.
    cmd_type: str
    Type of opcode.
    arguments: List[int]
    List of integer representation of argument value(s).
    qubit_indexes: List[int]
    List of integer representation of qubit addresses.
    """
    warnings.warn("This interface is now deprecated. "
                    "Please use the new QHALCommand and Opcode classes.", 
                    DeprecationWarning)

    cmd = QHALCommand.from_binary(cmd)

    return (cmd.opcode.name, 
            "DUAL" if cmd.opcode.is_dual() else "SINGLE", 
            cmd.args, 
            cmd.qubits)
