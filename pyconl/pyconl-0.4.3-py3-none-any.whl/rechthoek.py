from typing import Union

import pyco.waarde
import pyco.lijn
import pyco.vorm

class pc:
    Waarde = pyco.waarde.Waarde
    Lijn = pyco.lijn.Lijn
    Vorm = pyco.vorm.Vorm

    
class Rechthoek(pc.Vorm):
    """
    Creeert een rechthoekig Vorm object.
    
    AANMAKEN RECHTHOEK
        r = Rechthoek(breedte=Waarde(300).mm, hoogte=Waarde(500).mm)
        
    Verder zijn alle eigenschappen van toepassing als van een Vorm object. 
    """

    def __init__(self,
                 breedte:Union[pc.Waarde, float, int],
                 hoogte:Union[pc.Waarde, float, int]):

        eenheid = None
        if isinstance(breedte, pc.Waarde):
            eenheid = breedte.eenheid
        b = float(breedte)

        if isinstance(hoogte, pc.Waarde):
            hoogte.eenheid = eenheid
        h = float(hoogte)

        lijn = pc.Lijn([
                [-1/2 * b, -1/2 * h],
                [-1/2 * b,  1/2 * h],
                [ 1/2 * b,  1/2 * h],
                [ 1/2 * b, -1/2 * h],
            ])
        lijn.eenheid = eenheid

        super().__init__(lijn)
