import sys
import os

import numpy as np
from dpdata.driver import Driver

from .anidriver import ANIDriver, ani_eval


class AIQM1Args:
    mndobin = None
    dftb4bin = None
    xyzfile = None
    d4 = None
    mndokw = None
    yestfile = None
    ygradestfile = None
    hessianestfile = None
    
    def __init__(self, device: str=None, model_index: int=None) -> None:
        self.device = device
        self.model_index = model_index


@Driver.register("aiqm1/nn")
class AIQM1NNDriver(ANIDriver):
    def __init__(self, device: str=None, model_index: int=0, type: str = 'aiqm1dft'):
        assert type in ("aiqm1", "aiqm1dft")

        sys.modules['stopper'] = 0
        os.environ['mndobin'] = 'mndo'
        os.environ['dftd4bin'] = 'dftd4'
        from MLatom.AIQM1 import AIQM1Cls

        aiqm1 = AIQM1Cls([
            type,
            'model_index=%d' % model_index,
            'xyzfile',
            ])
        aiqm1.define_aev()
        aiqm1.load_models()
        if type == 'aiqm1dft':
            self.sae = np.array(aiqm1.ccsae)
        elif type == 'aiqm1dft':
            self.sae = np.array(aiqm1.dftsae)
        else:
            raise
        super().__init__(aiqm1.models[0], device=device)

    def label(self, data):
        from torchani.units import hartree2ev
        nframes = data['coords'].shape[0]
        natoms = data['coords'].shape[1]

        number_dict = {
            'H': 0,
            'C': 1,
            'N': 2,
            'O': 3,
        }
        atomic_types = np.array([number_dict[xx] for xx in data['atom_names']], dtype=int)

        species = np.array(atomic_types[data['atom_types']])
        species = np.tile(species, (nframes, 1))

        energy, force = self.auto_batch_size.execute_all(ani_eval, nframes, natoms, self.model, self.device, data['coords'], species)
        
        bias = hartree2ev(np.sum(self.sae[species]))

        data['energies'] = energy + bias
        data['forces'] = force
        return data


@Driver.register('aiqm1')
class AIQM1Driver(Driver.get_driver("hybrid")):
    """AIQM1."""
    def __init__(self, charge: int = 0, model_index: int = 0) -> None:
        super().__init__([
            {'type': 'aiqm1/nn', 'model_index': model_index},
            {'type': 'mndo/odm2', 'charge': charge},
            {'type': 'dftd4', 'method': 'wb97x'},
            ])

    @property
    def charge(self):
        return self.drivers[1].charge

    @charge.setter
    def charge(self, charge: int = 0) -> None:
        self.drivers[1].charge = charge
