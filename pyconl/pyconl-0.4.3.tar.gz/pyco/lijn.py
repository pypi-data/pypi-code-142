from typing import Union

import numpy as np
import matplotlib.pyplot as plt

import pyco.basis
import pyco.waarde
import pyco.knoop
import pyco.lijst

class pc:
    BasisObject = pyco.basis.BasisObject
    Waarde = pyco.waarde.Waarde
    Lijst = pyco.lijst.Lijst
    Knoop = pyco.knoop.Knoop


class Lijn(pc.BasisObject):
    """Bevat een collectie met knopen, waartussen zich rechte lijnen bevinden.

    AANMAKEN LIJN               invoeren van één of meedere Knoop objecten
        Lijn(Knoop(Waarde(1).cm, Waarde(2).cm)))    begin Knoop object
        Lijn([1,2]) of Lijn((1,2))                  alleen begincoordinaat
        Lijn((1,2), (3,4), (5,6))                   alle knoopcoordinaten

    AANPASSEN EENHEID
        l = Lijn((1,2), (3,4))
        l.eenheid               opvragen huidige eenheid; in dit geval None
        l.eenheid = 'm'         alle waarden in alle knoopobjecten naar 'm'
        l.gebruik_eenheid('m')  zelfde als bovenstaande, retourneert object

    OMZETTEN LIJN NAAR TEKST    resulteert in nieuw string object
        tekst = str(l)          of automatisch met bijvoorbeeld print(l)
        tekst = format(l,'.2f') format configuratie meegeven voor getal

    VERLENGEN LIJN              vanuit laatste knoop (of enige beginknoop)
        l.lijn_recht(naar=(3,4))
            rechte lijn naar een nieuwe knoop

        l.lijn_bezier(richting=(3,4), naar=(5,6), stappen=100)
            (kwadratische) Bezier kromme (met één richtingspunt) naar nieuwe
            knoop waarbij de kromme lijn omgezet wordt in aantal (stappen)
            rechte lijnen; standaard 100 stappen

        l.lijn_cirkelboog(middelpunt=(3,4), gradenhoek=-90, stappen=100)
            cirkelboog met opgegeven cirkel middelpunt over aantal opgegeven
            graden (waarbij 360 is gehele cirkel tekenen; positief is tegen
            klok in; negatief getal is met de klok mee) waarbij kromme lijn
            omgezet wordt in aantal rechte lijnen; standaard 100 stappen

    TRANSFORMEREN LIJN
        l.transformeren(       # standaard zijn alle parameters None
            rotatiepunt=[0,0], # xy Knoop/list; als None dan zwaartepunt vorm
            rotatiehoek=20,    # in graden, positief is tegen de klok in
            schaalfactor=2,  # Waarde/getal: vergrootfactor t.o.v. rotatiepunt
            schaalfactor=[2,3],# of Lijst/list met x-schaalfactor en y-factor
            schaalfactor=[1,-1],# verticaal spiegelen
            schaalfactor=[-1,1],# horizontaal spiegelen
            schaalfactor=[-5,3],# bovenstaande combineren
            translatie=[10,5], # xy verschuiven (na roteren en schalen)
        )

    MOGELIJKE BEWERKINGEN
        waarde = abs(l)         berekent lengte lijnstukken -> Waarde object
        getal = float(l)        berekent lengte lijnstukken -> float object
        for w in v1:            itereert en geeft Knoop object terug
        getal = len(v1)         geeft aantal knopen terug

    NUMPY BEWERKINGEN               gebruikt array object
        2D numpy_array = l1.array   retourneert volledige Numpy array object
                                      (bevat allen getallen, zonder eenheid)
        1D_numpy_array = l1[2]      retourneert knoopcoordinaten op index
        2D_numpy_array = l1[1:3]    retourneert knoopcoordinaten vanuit slice

    WAARDEN VERGELIJKEN         resulteert in een boolean (True/False)
        l1 == l2                is gelijk aan
        l1 != l2                is niet gelijk aan
        l1 &  l2                eenheden zijn zelfde type

    EXTRA OPTIES
        l.plot()                plot simpele 2D weergave van lijn
        l.plot3D()              plot simpele 3D weergave van lijn

        Lijn((4, -5), (-10, 10)).lijn_cirkelboog(middelpunt=(0,0),
            gradenhoek=+220, stappen=50).lijn_recht(naar=(4, 10)).lijn_bezier(
            richting=(-10,-4), naar=(4, -5)).plot()
    """

    def __init__(self, *knopen):
        super().__init__()

        tmp_knopen = []
        self._eenheid = None

        if (len(knopen) == 1
                and (
                    isinstance(knopen[0], list) or
                    isinstance(knopen[0], tuple))
                and len(knopen[0]) > 0
                and (
                    isinstance(knopen[0][0], pc.Knoop) or
                    isinstance(knopen[0][0], list) or
                    isinstance(knopen[0][0], tuple))):
            knopen = knopen[0]

        if len(knopen) < 1:
            raise ValueError('voer minimaal één knoop in')

        for i, knoop in enumerate(knopen):
            if not (isinstance(knoop, pc.Knoop)
                    or isinstance(knoop, list) or isinstance(knoop, tuple)):
                raise TypeError('opgegeven argument is geen Knoop object of lijst met getallen/Waardes')
            if not isinstance(knoop, pc.Knoop):
                knoop = pc.Knoop(knoop)
            if i > 0:
                if ((self._eenheid is None and knoop.eenheid is not None)
                        or (self._eenheid is not None and knoop.eenheid is None)):
                    raise ValueError('knopen moeten zelfde type eenheid hebben')
                knoop.eenheid = self._eenheid
            if i == 0 or (i > 0 and tmp_knopen[-1] != knoop.array.tolist()):
                tmp_knopen.append(knoop.array.tolist())
            if i == 0:
                self._eenheid = knoop.eenheid

        self._array = np.array(tmp_knopen, dtype='float64')

    @property
    def eenheid(self) -> str:
        """Geeft eenheid van Waarde. 'None' als geen eenheid."""
        return self._eenheid

    @eenheid.setter
    def eenheid(self, eenheid:str):
        """Zet knopen om naar nieuwe eenheid."""
        tmp_knopen = []
        oude_eenheid = self._eenheid

        for k_array in self.array:
            k = pc.Knoop(k_array.tolist())
            k.eenheid = oude_eenheid
            k.eenheid = eenheid
            tmp_knopen.append(k.array.tolist())

        self._array = np.array(tmp_knopen, dtype='float64')
        self._eenheid = eenheid

    def gebruik_eenheid(self, eenheid:str):
        """Zet knopen om naar nieuwe eenheid en retourneert object."""
        self.eenheid = eenheid
        return self

    @property
    def array(self) -> np.array:
        """Retourneert Numpy array object met alle getallen (zonder eenheid)."""
        return self._array

    def lijn_recht(self, naar:pc.Knoop):
        """Verlengt lijn object met een extra rechte lijn naar opgegeven knoop."""
        if not (isinstance(naar, pc.Knoop)
                or isinstance(naar, list) or isinstance(naar, tuple)):
            raise TypeError('opgegeven argument is geen Knoop object of lijst met getallen/Waardes')

        if not isinstance(naar, pc.Knoop):
            naar = pc.Knoop(naar)

        if ((self.eenheid is None and naar.eenheid is not None)
                or (self.eenheid is not None and naar.eenheid is None)):
            raise ValueError('knopen moeten zelfde type eenheid hebben')
        naar.eenheid = self.eenheid

        if self[-1].tolist() != naar.array.tolist():
            self._array = np.append(self.array, [naar.array.tolist()], axis=0)
        return self

    def lijn_bezier(self, richting:pc.Knoop, naar:pc.Knoop, stappen:int=100):
        """Verlengt lijn object als kwadratische Bezier kromme naar opgegeven knoop. Hierbij worden <aantal stappen> rechte lijnen gemaakt."""
        if not (isinstance(richting, pc.Knoop)
                or isinstance(richting, list) or isinstance(richting, tuple)):
            raise TypeError('opgegeven richting-knoop is geen Knoop object of lijst met getallen/Waardes')
        if not (isinstance(naar, pc.Knoop)
                or isinstance(naar, list) or isinstance(naar, tuple)):
            raise TypeError('opgegeven naar-knoop is geen Knoop object of lijst met getallen/Waardes')

        if not isinstance(richting, pc.Knoop):
            richting = pc.Knoop(richting)
        if not isinstance(naar, pc.Knoop):
            naar = pc.Knoop(naar)

        if ((self.eenheid is None and richting.eenheid is not None)
                or (self.eenheid is not None and richting.eenheid is None)):
            raise ValueError('knopen moeten zelfde type eenheid hebben')
        richting.eenheid = self.eenheid
        if ((self.eenheid is None and naar.eenheid is not None)
                or (self.eenheid is not None and naar.eenheid is None)):
            raise ValueError('knopen moeten zelfde type eenheid hebben')
        naar.eenheid = self.eenheid

        start = pc.Knoop(self[-1].tolist())
        start.eenheid = self.eenheid

        tt = np.linspace(0, 1, num=stappen+1)
        P1 = start[:]
        P2 = richting[:]
        P3 = naar[:]

        extra_knopen=[]
        for t in tt[1:]:
            # kwadratische Bezier kromme:
            extra_knoop = (1 - t**2)*P1 + 2*t*(1-t)*P2 + t**2*P3
            extra_knopen.append(extra_knoop.tolist())

        self._array = np.append(self.array, extra_knopen, axis=0)
        return self

    def lijn_cirkelboog(self, middelpunt:pc.Knoop, gradenhoek:float, stappen:int=100):
        """Verlengt lijn object als cirkel met middelpunt over x aantal graden. Hierbij worden <aantal stappen> rechte lijnen gemaakt. Positief is tegen klok in, negatief is met de klok mee."""
        if not (isinstance(middelpunt, pc.Knoop)
                or isinstance(middelpunt, list) or isinstance(middelpunt, tuple)):
            raise TypeError('opgegeven middelpunt-knoop is geen Knoop object of lijst met getallen/Waardes')

        if not isinstance(middelpunt, pc.Knoop):
            middelpunt = pc.Knoop(middelpunt)

        if ((self.eenheid is None and middelpunt.eenheid is not None)
                or (self.eenheid is not None and middelpunt.eenheid is None)):
            raise ValueError('knopen moeten zelfde type eenheid hebben')
        middelpunt.eenheid = self.eenheid

        start = pc.Knoop(self[-1].tolist())
        start.eenheid = self.eenheid

        P1 = start[:]
        M = middelpunt[:]
        straal = np.linalg.norm(M - P1)
        hoek = gradenhoek%360 if gradenhoek >= 0 else -1*((-1*gradenhoek)%360)
        hoek = 360 if hoek == 0 else hoek
        start_hoek = (270-np.rad2deg(np.arctan2(M[0]-P1[0], M[1]-P1[1])))%360
        eind_hoek = start_hoek + hoek

        tt = np.linspace(np.deg2rad(start_hoek), np.deg2rad(eind_hoek), num=stappen+1)
        extra_knopen=[]
        for t in tt[1:]:
            extra_knoop = [M[0] + straal*np.cos(t), M[1] + straal*np.sin(t)]
            extra_knopen.append(extra_knoop)

        self._array = np.append(self.array, extra_knopen, axis=0)
        return self

    def transformeren(self,
                      rotatiepunt:pc.Knoop=None,
                      rotatiehoek:Union[pc.Waarde, float, int]=None,
                      schaalfactor:Union[pc.Waarde, float, int,
                                         pc.Lijst, list, tuple]=None,
                      translatie:Union[pc.Lijst, list, tuple]=None):
        """Verplaatst, roteert en/of verschaalt de lijn."""

        if rotatiepunt is not None and isinstance(rotatiepunt, pc.Knoop):
            rotatiepunt = rotatiepunt.array.tolist()
        elif (rotatiepunt is not None
                and (isinstance(rotatiepunt, tuple)
                or isinstance(rotatiepunt, list))):
            rotatiepunt = [rotatiepunt[0], rotatiepunt[1]]
        else:
            # als geen geldige coordinaten, dan bereken zwaartepunt
            Xi = self.array[:,0]
            Yi = self.array[:,1]
            Xii = np.delete(np.hstack((Xi, np.array([Xi[0]]))), 0)
            Yii = np.delete(np.hstack((Yi, np.array([Yi[0]]))), 0)
            determinant = Xi*Yii - Xii*Yi
            A = 1/2 * sum(determinant)
            if not A:
                return
            teken = 1.0 if A > 0 else -1.0
            A_ = float(teken * A)
            ncx = float(teken * 1/6/A_ * sum((Xi + Xii) * determinant))
            ncy = float(teken * 1/6/A_ * sum((Yi + Yii) * determinant))
            rotatiepunt = [ncx, ncy]

        if rotatiehoek is not None:
            tmp_array = self.array - rotatiepunt

            rh = np.radians(float(rotatiehoek))
            rotatie_matrix = np.array([[np.cos(rh), -np.sin(rh)],
                                       [np.sin(rh),  np.cos(rh)]])
            tmp_array = np.matmul(rotatie_matrix, tmp_array.T).T

            self._array = tmp_array + rotatiepunt

        if schaalfactor is not None:
            tmp_array = self.array - rotatiepunt

            if ((isinstance(schaalfactor, list)
                    or isinstance(schaalfactor, tuple)
                    or isinstance(schaalfactor, pc.Lijst))
                    and len(schaalfactor) >= 2):
                sf1 = float(schaalfactor[0])
                sf2 = float(schaalfactor[1])
            else:
                sf1 = float(schaalfactor)
                sf2 = float(schaalfactor)

            schaal_matrix = np.array([[sf1,  0],
                                      [ 0, sf2]])
            tmp_array = np.matmul(schaal_matrix, tmp_array.T).T

            self._array = tmp_array + rotatiepunt

        if translatie is not None and len(translatie) >= 2:
            self._array = self.array + np.array(
                    [translatie[0], translatie[1]])

        return self

    def plot(self):
        """Teken simpele plot van lijn (met 2 dimensies)."""
        plt.plot(self.array[:,0], self.array[:,1])
        plt.axis('equal')
        plt.show()
        
    def plot3D(self):
        """Teken simpele plot van lijn (met 3 dimensies)."""
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = Axes3D(fig)
        plt.plot(self.array[:,0], self.array[:,1], self.array[:,2])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    def __eq__ (self, andere):
        """Vergelijkt twee Lijn objecten."""
        if len(self) != len(andere):
            return False
        return all(s == a for s, a in zip(self, andere))

    def __neq__ (self, andere):
        """Vergelijkt negatief twee Lijn objecten."""
        return not self == andere

    def __and__(self, andere):
        """Controleert of Lijn zelfde type eenheid heeft als andere."""
        if not isinstance(andere, pc.Lijn):
            raise TypeError('tweede waarde is geen Lijn object')
        return pc.Waarde(1, self.eenheid) & Waarde(1, andere.eenheid)

    def __iter__(self):
        """Itereert over knopen en geeft Knoop objecten terug."""
        for k_array in self.array:
            k = pc.Knoop(k_array.tolist())
            k.eenheid = self.eenheid
            yield k

    def __getitem__(self, index):
        """Retourneert subset Numpy array object met getallen (zonder eenheid)."""
        return self.array[index]

    def __len__(self):
        """Geeft aantal knopen."""
        return len(self.array)

    def __float__(self):
        """Berekent de totale lengte van de lijnstukken als float object."""
        if len(self) < 2:
            return 0.0
        laatste_kn_arr = self[0]
        lengte = 0.0
        for kn_arr in self[1:]:
            x1 = laatste_kn_arr[0]
            x2 = kn_arr[0]
            y1 = laatste_kn_arr[1]
            y2 = kn_arr[1]
            lengte += np.sqrt((x2-x1)**2 + (y2-y1)**2)
            laatste_kn_arr = kn_arr
        return lengte

    def __abs__(self):
        """Berekent de totale lengte van de lijnstukken als Waarde object."""
        return pc.Waarde(float(self), self.eenheid)

    def __format__(self, config:str=None):
        """Geeft tekst met geformatteerd getal en eenheid."""
        if config is None:
            return str(self)
        knopen = ', '.join(format(k, config).rsplit(')', 1)[0]+')' for k in self)
        eenheid = self.eenheid if self.eenheid is not None else ''
        return '({}) {}'.format(knopen, eenheid).strip()

    def __repr__(self):
        cls_naam = type(self).__name__
        knopen = ', '.join(repr(k) for k in self)
        return '{}({})'.format(cls_naam, knopen)

    def __str__(self):
        knopen = ', '.join(str(k).rsplit(')', 1)[0]+')' for k in self)
        eenheid = self.eenheid if self.eenheid is not None else ''
        return '({}) {}'.format(knopen, eenheid).strip()
