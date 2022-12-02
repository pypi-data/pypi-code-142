import sys
import os.path

from .script_utils import (
    script,
    error,
    positional,
    flag,
    optional,
    error_catch,
)


@script(
    positional("CHGCAR", help="file to extract data from"),
    flag("--split", help="split CHGCAR into up and down channels"),
    flag("--spin", help="extract the spin density"),
    flag("--total", help="extract the total density"),
)
def charge_extract(opts):
    from .charge_utils import Charge

    if opts.chgcar == "-":
        chg = Charge.from_file(sys.stdin)
        name = "CHGCAR"
    else:
        with open(opts.chgcar) as f:
            chg = Charge.read_from(f)
        name = opts.chgcar

    out_prefix = name

    if opts.split:
        if chg.dif_part is None:
            error("There is spin data available in the input file.")

        up, down = chg.split()
        with open(out_prefix + ".up", "w") as f:
            up.write_to(f)

        with open(out_prefix + ".down", "w") as f:
            down.write_to(f)

    elif opts.spin:
        if chg.dif_part is None:
            error("There is spin data available in the input file.")

        with open(out_prefix + ".spin", "w") as f:
            chg.dif_part.write_to(f)

    elif opts.total:
        with open(out_prefix + ".total", "w") as f:
            chg.total_only().write_to(f)

    else:
        error("No action required.")


@script(
    positional("COEF_A", type=float, help="coeficient for the first file"),
    positional("CHGCAR_A", help="first file to extract data from"),
    positional("COEF_B", type=float, help="coeficient for the second file"),
    positional("CHGCAR_B", help="second file to extract data from"),
)
def charge_combine(opts):
    from .charge_utils import Charge

    if opts.chgcar_a == "-":
        chg_a = Charge.from_file(sys.stdin)
        name = "CHGCAR"
    else:
        with open(opts.chgcar_a) as f:
            chg_a = Charge.read_from(f)
        name = opts.chgcar_a

    prefix_out = name

    if opts.chgcar_b == "-":
        chg_b = Charge.from_file(sys.stdin)
    else:
        with open(opts.chgcar_b) as f:
            chg_b = Charge.read_from(f)

    chg_sum = opts.coef_a * chg_a + opts.coef_b * chg_b

    with open(prefix_out + ".sum", "w") as f:
        chg_sum.write_to(f)


@script(
    positional("OUTCAR", default="OUTCAR", type=str, help="VASP output file"),
    optional(
        "--tol",
        type=float,
        default=None,
        help="Maximum converged force ampliture (A/eV)",
    ),
    flag("--silent", "-q", help="quite mode, just use the return code"),
)
def check_forces(opts):
    import numpy as np
    from .forces import read_forces

    with error_catch(), open(opts.outcar) as f:
        species, forces, tol = read_forces(f)

    if opts.tol is not None:
        tol = opts.tol

    of = 0

    norms = np.linalg.norm(forces, axis=-1)
    (non_conv_where,) = np.where(norms > tol)
    non_conv_where = set(non_conv_where)

    if not opts.silent:
        for sp, n in species:
            print(f"{sp:2} {n:3}")

    if not opts.silent:
        print("       ---        X          Y          Z")
        print("===========================================")
        for sp, n in species:
            for j, (x, y, z) in enumerate(forces[of : of + n], start=of):
                if j in non_conv_where:
                    m = [" ", " ", " "]
                    m[np.argmax(np.abs([x, y, z]))] = "<"
                    print(
                        f"{sp:2} {j+1:3} >>> {x: .05f} {m[0]} {y: .05f} {m[1]} {z: .05f} {m[2]}"
                    )
                else:
                    print(f"{sp:2} {j+1:3}     {x: .05f}   {y: .05f}   {z: .05f}  ")
            of += n

    if non_conv_where:
        if not opts.silent:
            print(
                f"Convergence not reached: max force {np.max(norms):.05} eV/A > {tol:.02}."
            )
        return 1
    else:
        if not opts.silent:
            print("Convergence reached.")
        return 0


@script(
    positional("OUTCAR", default="OUTCAR", type=str, help="VASP output file"),
    flag("--silent", "-q", help="quite mode, just use the return code"),
)
def check_end(opts):
    from .outcar import normal_end

    with error_catch(), open(opts.outcar) as f:
        res = normal_end(f)

    if not opts.silent:
        if res:
            print("Computation ended normally.")
        else:
            print("Computation ended early.")

    return 0 if res else 1


@script(
    positional("DIR", default=".", type=str, help="VASP computation directory"),
    flag("--silent", "-q", help="quite mode, just use the return code"),
    optional("--osz", type=str, default=None, help="path to the OSZICAR file."),
    optional("--out", type=str, default=None, help="path to the OUTCAR file."),
    optional(
        "--tol", type=float, default=1.0e-7, help="Tolerance on the energy residue."
    ),
)
def check_conv(opts):
    from .outcar import converged

    if opts.osz is None:
        osz = os.path.join(opts.dir, "OSZICAR")
    else:
        osz = opts.osz

    if opts.out is None:
        out = os.path.join(opts.dir, "OUTCAR")
    else:
        out = opts.out

    with error_catch():
        res = converged(osz, out, tol=opts.tol)

    if not opts.silent:
        if res:
            print("Computation converged.")
        else:
            print("Computation did not converge.")

    return 0 if res else 1
