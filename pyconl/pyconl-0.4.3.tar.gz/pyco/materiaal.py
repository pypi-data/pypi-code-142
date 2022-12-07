import pyco.basis
import pyco.waarde

class pc:
    BasisObject = pyco.basis.BasisObject
    Waarde = pyco.waarde.Waarde

    
class Materiaal(pc.BasisObject):
    """Betreft een materiaal met diverse eigenschappen.

    AANMAKEN MATERIAAL
        m = Materiaal(E=Waarde(210, 'GPa'),     # elasticiteitsmodulus
                      G=Waarde(75, 'GPa'),      # glijdings(schuif)modulus
                      v=Waarde(0.4),            # dwarscontractiecoëfficiënt
                                                               (Poisson factor)
                      sm=Waarde(7850, 'kg/m3'), # soortelijke massa (dichtheid)
                      sg=Waarde(78.5, 'kN/m3')) # soortelijk gewicht
        
    RELATIE E, G EN v
        Indien E en v bekend zijn, dan wordt G zelf bepaald: G = E/(2(1+v))
        Indien E en G bekend zijn, dan wordt v zelf bepaald: v = (E/2G)-1
        Alledrie grootheden kunnen handmatig worden overschreven.
        
    OPVRAGEN EN AANPASSEN MATERIAALEIGENSCHAPPEN
        m.E                             # retourneert Waarde object
        m.E = Waarde(180).GPa           # past waarde E aan
    """
    
    DEFAULT_E = pc.Waarde(0, 'N/m2') 
    DEFAULT_G =  pc.Waarde(0, 'N/m2')
    DEFAULT_v = pc.Waarde(0) 
    DEFAULT_sm = pc.Waarde(0, 'kg/m3')
    DEFAULT_sg = pc.Waarde(0, 'N/m3')

    def __init__(self, E=None, G=None, v=None, sm=None, sg=None):
        super().__init__()

        self._E = self.DEFAULT_E 
        self._G = self.DEFAULT_G  
        self._v = self.DEFAULT_v  
        self._sm = self.DEFAULT_sm 
        self._sg = self.DEFAULT_sg
        
        if E is not None:
            self.E = E
        if G is not None:
            self.G = G
        if v is not None:
            self.v = v
        if sm is not None:
            self.sm = sm
        if sg is not None:
            self.sg = sg

    def _check_waarde(self, waarde, zelfde_eenheid):
        if not isinstance(waarde, pc.Waarde):
            raise TypeError('parameter is geen waarde object')
        if not waarde & zelfde_eenheid:
            raise ValueError('type eenheid van waarde is incorrect')

    @property
    def E(self):
        """Elasticiteitsmodulus."""
        return self._E
    @E.setter
    def E(self, waarde):
        self._check_waarde(waarde, self.DEFAULT_E)
        self._E = waarde

    @property
    def G(self):
        """Glijdingsmodulus."""
        if (self._G == self.DEFAULT_G
                and self._E != self.DEFAULT_E
                and self._v != self.DEFAULT_v):
            return self.E / (2 * (pc.Waarde(1) + self.v))
        else:
            return self._G
    @G.setter
    def G(self, waarde):
        self._check_waarde(waarde, self.DEFAULT_G)
        self._G = waarde

    @property
    def v(self):
        """Dwarscontractiecoëfficiënt (Poisson factor)."""
        if (self._v == self.DEFAULT_v
                and self._E != self.DEFAULT_E
                and self._G != self.DEFAULT_G):
            return self.E / (2 * self.G) - pc.Waarde(1)
        else:
            return self._v
    @v.setter
    def v(self, waarde):
        self._check_waarde(waarde, self.DEFAULT_v)
        if float(waarde) >= -1.01 and float(waarde) <= -0.99:
            raise ValueError('een dwarscontractiecoefficient van -1 leidt tot een glijdingsmodulus van oneindig groot; deze waarde is niet mogelijk')
        self._v = waarde

    @property
    def sm(self):
        """Soortelijke massa (dichtheid)."""
        return self._sm
    @sm.setter
    def sm(self, waarde):
        self._check_waarde(waarde, self.DEFAULT_sm)
        self._sm = waarde

    @property
    def sg(self):
        """Soortelijk gewicht."""
        return self._sg
    @sg.setter
    def sg(self, waarde):
        self._check_waarde(waarde, self.DEFAULT_sg)
        self._sg = waarde


if __name__ == '__main__':
    m1 = Materiaal()
    print(m1.E, bool(m1.E))
    m1.E = pc.Waarde(2.1e5, 'MPa')
    m1.v = pc.Waarde(0.2)
    m1.sm = pc.Waarde(700e3, 'kg/m3')
    m1.sg = pc.Waarde(75, 'kN/m3')
    print(m1.E, bool(m1.E))
    print(m1.G)
