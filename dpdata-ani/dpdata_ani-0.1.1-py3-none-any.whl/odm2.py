import tempfile
import subprocess as sp
from typing import Tuple

import numpy as np
import dpdata
from dpdata.driver import Driver
from dpdata.periodic_table import Element

unitconv = dpdata.unit.EnergyConversion("kcal_mol", "eV").value()

@Driver.register("mndo/odm2")
class ODM2Driver(Driver):
    def __init__(self, charge: int = 0) -> None:
        self.charge = charge

    def label(self, data):
        nframes = data['coords'].shape[0]

        atomic_z = np.array([Element(xx).Z for xx in data['atom_names']], dtype=int)

        species = np.array(atomic_z[data['atom_types']])

        energies = []
        forces = []
        for ii in range(nframes):
            out = run_odm2_calculation(species, data['coords'][ii], charge=self.charge)
            energy, force = read_output(out)
            if energy is None or force is None:
                energy = np.nan
                force = np.full([species.size ,3], np.nan)
            energies.append(energy)
            forces.append(force)

        data['energies'] = np.array(energies)
        data['forces'] = np.array(forces)
        return data

def run_odm2_calculation(numbers: np.ndarray, coordinates: np.ndarray, charge=0) -> str:
    """Run an ODM2 calculation.
    
    Parameters
    ----------
    numbers : np.ndarray
        Atomic numbers.
    coordinates : np.ndarray
        Atomic coordinates.
    
    Returns
    -------
    str
        The output of the ODM2 calculation.
    """

    buff = []
    buff.append('jop=-2 +')
    buff.append('iop=-22 igeom=1 iform=1 immdp=-1 +')
    buff.append('icuts=-1 icutg=-1 kitscf=9999 iscf=9 iplscf=9 +')
    buff.append('iprint=-1 kprint=-5 lprint=-2 mprint=0 jprint=-1 +')
    buff.append('kharge=%d imult=0 nprint=-1\n\n' % charge)
    for j in range(len(numbers)):
        buff.append('%2s     %12.8f %3d     %12.8f %3d     %12.8f %3d' %(
            numbers[j],
            coordinates[j][0],
            0,
            coordinates[j][1],
            0,
            coordinates[j][2],
            0,
        ))
    buff.append('')
    buff.append('')
    with tempfile.SpooledTemporaryFile(mode='w+') as f:
        f.write("\n".join(buff))
        f.seek(0)
        out = sp.check_output(
            ['mndo'],
            stdin=f,
            ).decode('utf-8')
    return out


def read_output(output: str) -> Tuple[float, np.ndarray]:
    """Read the output of an ODM2 calculation.
    
    Parameters
    ----------
    output : str
        The output of an ODM2 calculation.
    
    Returns
    -------
    float
        The energy.
    np.ndarray
        The forces.
    """

    energy = None
    forces = None
    for line in output.splitlines():
        if 'SCF TOTAL ENERGY' in line:
            # eV
            energy = float(line.split()[3])
            continue
        if 'I   NI          X           Y           Z                X           Y           Z' in line:
            forces = []
            continue
        if forces is not None:
            if 'CARTESIAN GRADIENT NORM' in line:
                forces = np.array(forces)
                # kcal/mol/Angstrom -> eV/Angstrom
                forces *= -unitconv
                break
            if line.strip() and len(line.split()) == 8:
                forces.append([float(x) for x in line.split()[5:8]])
    return energy, forces
