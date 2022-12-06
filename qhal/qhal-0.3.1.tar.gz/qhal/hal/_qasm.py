import qiskit
from qiskit.circuit.library import standard_gates as qiskit_gate

from ._commands import Opcode
from ._circuit import QHALCircuit
from ._utils import angle_binary_representation

def insert_barriers_to_qasm(qasm_str: str) -> str:
    """Add barriers in between OpenQASM commands to ensure operation order.
    Only one qreg is supported.

    Parameters
    ----------
    qasm_str : str
        OpenQASM program

    Returns
    -------
    str
        OpenQASM program with barriers
    """
    qregs = [qreg.name for qreg in qiskit.QuantumCircuit.from_qasm_str(
        qasm_str).qregs]
    qasm_cmds = qasm_str.split("\n")
    qreg_cmds = [c for c in qasm_cmds if c.startswith('qreg')]
    qreg_cmd_idx = qasm_cmds.index(qreg_cmds[0])

    barrier_cmd = "barrier " + ", ".join(qregs) + ";"
    qasm_str_w_barriers = f"\n{barrier_cmd}\n".join(
        qasm_cmds[qreg_cmd_idx+1:])
    qasm_str_w_barriers = "\n".join(
        qasm_cmds[:qreg_cmd_idx+1]) + qasm_str_w_barriers
    return qasm_str_w_barriers


def qiskit_instruction_to_qhal_opcode(qi: qiskit.circuit.Instruction) -> Opcode:
    """Convert Qiskit Instruction to QHAL Opcode

    Parameters
    ----------
    qi : qiskit.circuit.Instruction

    Returns
    -------
    Opcode
    """
    if isinstance(qi, qiskit_gate.x.XGate):
        return Opcode.X
    if isinstance(qi, qiskit_gate.y.YGate):
        return Opcode.Y
    if isinstance(qi, qiskit_gate.z.ZGate):
        return Opcode.Z
    if isinstance(qi, qiskit_gate.h.HGate):
        return Opcode.H

    if isinstance(qi, qiskit_gate.t.TGate):
        return Opcode.T
    if isinstance(qi, qiskit_gate.t.TdgGate):
        return Opcode.INVT

    if isinstance(qi, qiskit_gate.s.SGate):
        return Opcode.S
    if isinstance(qi, qiskit_gate.s.SdgGate):
        return Opcode.INVS

    if isinstance(qi, qiskit_gate.sx.SXGate):
        return Opcode.SX
    if isinstance(qi, qiskit_gate.swap.SwapGate):
        return Opcode.SWAP

    if isinstance(qi, qiskit_gate.rx.RXGate):
        return Opcode.RX
    if isinstance(qi, qiskit_gate.ry.RYGate):
        return Opcode.RY
    if isinstance(qi, qiskit_gate.rz.RZGate):
        return Opcode.RZ

    if isinstance(qi, qiskit_gate.p.PhaseGate):
        return Opcode.PHASE

    if isinstance(qi, qiskit_gate.x.CXGate):
        return Opcode.CNOT
    if isinstance(qi, qiskit_gate.rzz.RZZGate):
        return Opcode.RZZ
    if isinstance(qi, qiskit_gate.rxx.RXXGate):
        return Opcode.RXX

    if isinstance(qi, qiskit_gate.i.IGate):
        return Opcode.ID

    if isinstance(qi, qiskit.circuit.measure.Measure): 
        return Opcode.QUBIT_MEASURE

    raise NotImplementedError(
        f"Qiskit operation {qi} was not compiled to QHAL")


# pylint: disable=invalid-name
def qhal_circuit_from_qiskit(qc: qiskit.QuantumCircuit = None) -> QHALCircuit:
    """Generate QHALCircuit from a qiskit.QuantumCircuit

    Parameters
    ----------
    qc : qiskit.QuantumCircuit
        The quantum circuit to be converted

    Returns
    -------
    QHALCircuit
        The equivalent QHAL circuit
    """
    if not isinstance(qc, qiskit.QuantumCircuit):
        raise TypeError("qiskit.QuantumCircuit expected")
    circ = QHALCircuit()

    qubits = qc.qubits
    assert isinstance(qubits, list)
    circ.add_command(Opcode.START_SESSION)
    circ.add_command(Opcode.STATE_PREPARATION_ALL)

    for ins, q, _ in qc.data:
        if len(q) not in [1, 2]:
            raise NotImplementedError(
                f"Operations with {len(q)} qubits not supported")

        if ins.condition is not None:
            raise NotImplementedError(
                "Classical branching is not supported")

        if isinstance(ins, qiskit.circuit.barrier.Barrier):
            continue
        op = qiskit_instruction_to_qhal_opcode(ins)

        args = [0, 0]
        if type(ins) in [qiskit_gate.rx.RXGate,
                         qiskit_gate.ry.RYGate,
                         qiskit_gate.rz.RZGate,
                         qiskit_gate.p.PhaseGate,
                         qiskit_gate.rzz.RZZGate,
                         qiskit_gate.rxx.RXXGate]:
            args[0] = angle_binary_representation(ins.params[0])

        if isinstance(ins, qiskit.circuit.measure.Measure) and len(q) != 1:
            raise NotImplementedError(
                "QHAL QUBIT_MEASURE command only supports one qubit. "
                                      f"Readout of {len(q)} qubits requested.")

        circ.add_command(op, args=args, qubits=[qubits.index(qq) for qq in q])

    circ.add_command(Opcode.END_SESSION)
    return circ


def qhal_from_qasm_file(qasm_file: str) -> QHALCircuit:
    """Converts a QASM file to QHAL

    Parameters
    ----------
    qasm_file : str
        Path to OpenQASM file


    Returns
    -------
    QHALCircuit
    """
    # pylint: disable=unspecified-encoding
    with open(qasm_file, "r") as istream:
        qasm_str = "\n".join(istream.readlines())
    return qhal_from_qasm_str(qasm_str)


def qhal_from_qasm_str(qasm_str: str) -> QHALCircuit:
    """Converts a QASM string to QHAL

    Parameters
    ----------
    qasm_str : 
        The OpenQASM quantum circuit to be converted

    Returns
    -------
    QHALCircuit

    Raises
    ------
    NotImplementedError
        If operations are performed on neither one nor two qubits, 
        or if the OpenQASM to QHAL conversion is not implemented for an operation.
    """
    circ_qiskit = qiskit.QuantumCircuit.from_qasm_str(qasm_str)
    circ_qhal = qhal_circuit_from_qiskit(circ_qiskit)
    return circ_qhal
