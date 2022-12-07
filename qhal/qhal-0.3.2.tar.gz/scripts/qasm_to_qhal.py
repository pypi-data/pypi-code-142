from argparse import ArgumentParser
import pathlib

from qhal.hal import qhal_from_qasm_file


if __name__ == "__main__":
    parser = ArgumentParser("OpenQASM 2 to QHAL converter")
    parser.add_argument('-i', '--qasm', type=str, required=True)
    parser.add_argument('-o', '--qhal', type=str)
    parser.add_argument('-p', '--print', action='store_true')
    options = parser.parse_args()

    if options.qhal is None and not options.print:
        raise RuntimeError("Specify an out file for QHAL or request print!")

    qhal_circuit = qhal_from_qasm_file(
        pathlib.Path(__file__).parent / options.qasm)

    if options.qhal is not None:
        qhal_circuit.to_file(pathlib.Path(__file__).parent / options.qhal)

    if options.print:
        print(qhal_circuit)
