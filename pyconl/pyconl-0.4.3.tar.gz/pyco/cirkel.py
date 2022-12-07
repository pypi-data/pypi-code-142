from typing import Union
import math

import pyco.waarde
import pyco.lijn
import pyco.vorm

class pc:
    Waarde = pyco.waarde.Waarde
    Lijn = pyco.lijn.Lijn
    Vorm = pyco.vorm.Vorm

    
class Cirkel(pc.Vorm):
    """
    Creeert een cirkelvormig Vorm object.
    
    AANMAKEN CIRKEL
        c = Cirkel(straal=Waarde(3).mm)
        
    Vormeigenschappen worden exact bepaald, daar waar een Vorm object een ronde
    rand benadert met kleine rechte lijnen.
    
    Verder zijn alle eigenschappen en methoden van toepassing als van een
    Vorm object.
    """

    def __init__(self,
                 straal:Union[float, int]):

        eenheid = None
        if isinstance(straal, pc.Waarde):
            eenheid = straal.eenheid
        r = float(straal)

        lijn = pc.Lijn([-1*r, 0]).lijn_cirkelboog(
                    middelpunt=(0,0),
                    gradenhoek=360,
                    stappen=200,
                )
        lijn.eenheid = eenheid

        super().__init__(lijn)

        # corrigeer benadering cirkel met polygoon door exacte waarde
        self.O = 2 * math.pi * r
        self.A = math.pi * r**2
        self.xmin = -r
        self.xmax = r
        self.ymin = -r
        self.ymax = r
        self.Ixx = 1/4 * math.pi * r**4
        self.Iyy = self.Ixx
        self.Ixy = 0.0
        self.I1 = self.Ixx
        self.I2 = self.Ixx
        self.alpha = 0.0
        self.Wxmin = self.Ixx / r
        self.Wxmax = self.Wxmin
        self.Wymin = self.Wxmin
        self.Wymax = self.Wxmin
        self.kxmin = -r / 4
        self.kxmax = r / 4
        self.kymin = self.kxmin
        self.kymax = self.kxmax

        self._bereken_waardes()
