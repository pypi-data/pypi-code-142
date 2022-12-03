import dpdata
from dpdata.driver import Driver
from dpdata.plugins.ase import ASEDriver

unitconv = dpdata.unit.EnergyConversion("kcal_mol", "eV").value()

@Driver.register("dftd4")
class DFTD4Driver(ASEDriver):
    def __init__(self, method) -> None:
        from dftd4.ase import DFTD4

        dftd4 = DFTD4(method=method)
        super().__init__(dftd4)
