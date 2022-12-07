import pyco.waarde
import pyco.lijst

class pc:
    BasisObject = pyco.basis.BasisObject
    Waarde = pyco.waarde.Waarde
    Lijst = pyco.lijst.Lijst

class Tabel(pc.BasisObject):
    """
    Een Pandas DataFrame waarbij kolommen gelijk zijn aan Lijst objecten.

    AANMAKEN TABEL               
        t = Tabel({'col1': lijst1, 'col2': lijst2}) 

 
    """

    def __init__(self, lijst_dict):
        super().__init__()


