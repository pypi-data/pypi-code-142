from typing import Union
import itertools
import numpy as np

import pyco.basis
import pyco.waarde

class pc:
    BasisObject = pyco.basis.BasisObject
    Waarde = pyco.waarde.Waarde

class Vector(pc.BasisObject):
    """
    Bevat een lijst van getallen of Waarde objecten met allen dezelfde eenheid.

    AANMAKEN VECTOR             eenheid van 1e component, geldt voor geheel
        v = Vector(waarde1, waarde2, ...)          waarde: float, int of Waarde
        v = Vector([waarde1, waarde2, ...])              
        v = Vector(numpy_array)             array wordt indien nodig 1D gemaakt

    AANPASSEN EENHEID           omzetten van eenheid naar andere eenheid
        v.eenheid               huidige eenheid opvragen (tekst of None)
        v.eenheid = 'N/mm2'     eenheid aanpassen
        v.gebruik_eenheid('m')  eenheid aanpassen, retourneert object
        v.eh('m')               eenheid aanpassen, retourneert object
        v = v.N_mm2             kan voor een aantal standaard gevallen (zie lijst onderaan)

    OMZETTEN VECTOR NAAR TEKST  resulteert in nieuw string object
        tekst = str(v)          of automatisch met bijvoorbeeld print(w)
        tekst = format(v,'.2f') format configuratie meegeven voor getal

    MOGELIJKE BEWERKINGEN       resulteert in nieuw Vector object
        v3 = v1 + v2            vector optellen bij vector
        v3 = v1 - v2            vector aftrekken van vector
        getal = v1 * v2         vector vermenigvuldigen met vector (inproduct)
        getal = v1 / v2         vector delen door vector (inverse inproduct)
        v2 = n * v1             getal vermenigvuldigen met vector
        v2 = v1 * n             vector vermenigvuldigen met getal
        v2 = n / v1             getal delen door vector
        v2 = v1 / n             vector delen door getal
        waarde = v1 ** n        vector tot de macht een geheel getal
        waarde = abs(v1)        berekent lengte van vector -> Waarde object
        getal = float(v1)       berekent lengte van vector -> float object
        v2 = +v1                behoud teken
        v2 = -v1                verander teken (positief vs. negatief)
        for w in v1:            itereert en geeft float/Waarde object terug
        getal = len(v1)         geeft aantal elementen (dimensies) van vector

    NUMPY BEWERKINGEN           gebruikt array object
        numpy_array = v1.array  retourneert Numpy array object
                                    (bevat allen getallen, zonder eenheid)
        getal = v1[2]           retourneert getal (zonder eenheid) op index
        numpy_array = v1[1:3]   retourneert Numpy array object vanuit slice

    WAARDEN VERGELIJKEN         resulteert in een boolean (True/False)
        v1 == v2                is gelijk aan
        v1 != v2                is niet gelijk aan
        v1 >  v2                de lengte van vector is groter dan
        v1 <  v2                de lengte van vector is kleiner dan
        v1 >= v2                de lengte van vector is groter dan of gelijk aan
        v1 <= v2                de lengte van vector is kleiner dan of gelijk aan
        v1 &  v2                eenheden zijn zelfde type
        
    BESCHIKBARE EIGENSCHAPPEN   voor snel toekennen van eenheid aan waarde
    <object>.<eigenschap>       bijvoorbeeld toekennen inhoud: v.dm3
    a ag am attos bbl C ca cg cl cl_d cl_h cl_j cl_min cl_s cm cm2 cm3 cm3_d
    cm3_h cm3_j cm3_min cm3_s cm4 cm_d cm_h cm_j cm_min cm_s cs cup d dal dam
    das deg dg dl dl_d dl_h dl_j dl_min dl_s dm dm2 dm3 dm3_d dm3_h dm3_j
    dm3_min dm3_s dm4 dm_d dm_h dm_j dm_min dm_s ds Eg Em Es F fg floz fm fs ft
    g gallon Gg Gm GN gon GPa grain Gs h ha hg hl hm hm2 hm3 hs inch K kg kip
    kl km km2 km3 km3_d km3_h km3_j km3_min km3_s km4 km_d km_h km_j km_min
    km_s kN kNm kNmm kN_m kN_mm kN_m2 kN_mm2 kPa ks kton l l_d l_h l_j l_min
    l_s m m2 m3 m3_d m3_h m3_j m3_min m3_s m4 Mg mg mijl minuut ml ml_d ml_h
    ml_j ml_min ml_s Mm mm mm2 mm3 mm3_d mm3_h mm3_j mm3_min mm3_s mm4 mm_d
    mm_h mm_j mm_min mm_s MN MNm MNmm MN_m2 MN_mm2 MPa Ms ms Mton mug mum mus
    m_d m_h m_j m_min m_s N ng Nm nm Nmm ns N_m N_mm N_m2 N_mm2 ounce Pa Pg pg
    pint Pm pm pound Ps ps rad s stone tbs Tg Tm TN ton TPa Ts tsp yard zeemijl
    """

    def __init__(self, *waardes:Union[pc.Waarde, int, float]):
        super().__init__()

        self._eenheid = None

        if len(waardes) < 1:
            raise ValueError('Er moet minimaal één waarde worden opgegeven.')

        if len(waardes) == 1 and \
                (isinstance(waardes[0], list) or isinstance(waardes[0], tuple)):
            waardes = waardes[0]

        if len(waardes) == 1 and isinstance(waardes[0], type(np.array([]))):
            self._array = np.array(waardes[0].flatten(), dtype='float64') # flatten nD to 1D array
            return
        
        if len(waardes) == 1 and isinstance(waardes[0], self.__class__):
            self._array = waardes[0].array
            self._eenheid = waardes[0].eenheid
            return
        
        tmp_waardes = []
        for i, waarde in enumerate(waardes):
            if i == 0:
                # eerste waarde
                if isinstance(waarde, pc.Waarde):
                    _, eenheid = tuple(waarde)
                    if eenheid != '':
                        self._eenheid = eenheid
            else:
                # volgende waardes
                if isinstance(waarde, pc.Waarde):
                    # check of type eenheid zelfde is
                    if not waarde & pc.Waarde(1, self._eenheid):
                        raise TypeError('type eenheid komt niet overeen met 1e waarde: {}'.format(waarde))
                    # eenheden omzetten naar eerste eenheid
                    waarde = waarde[self._eenheid]
                elif isinstance(waarde, float) or isinstance(waarde, int):
                    if self._eenheid is not None:
                        raise TypeError('type eenheid komt niet overeen met 1e waarde: {}'.format(waarde))
            # waardes toevoegen aan self._array
            if isinstance(waarde, pc.Waarde):
                getal, _ = tuple(waarde)
                if isinstance(getal, float) or isinstance(getal, int):
                    tmp_waardes.append(getal)
                else:
                    raise TypeError('waarde in Waarde object is geen getal')
            elif isinstance(waarde, float) or isinstance(waarde, int):
                tmp_waardes.append(float(waarde))
            else:
                raise TypeError('waarde is geen Waarde/float/int: {}'.format(waarde))

        self._array = np.array(tmp_waardes, dtype='float64')
        
    def _verander_eenheid(self, eenheid:str):
        """Zet Vector om naar nieuwe eenheid."""
        if self._eenheid is None:
            self._eenheid = eenheid
        else:
            tmp_waardes = []
            oude_eenheid = self._eenheid
            for w in self:
                w = float(pc.Waarde(float(w), oude_eenheid)[eenheid])
                tmp_waardes.append(w)
            self._array = np.array(tmp_waardes, dtype='float64')
            self._eenheid = eenheid
        return self

    @property
    def eenheid(self):
        """Geeft eenheid van Waarde. 'None' als geen eenheid."""
        return self._eenheid

    @eenheid.setter
    def eenheid(self, eenheid:str):
        """Zet Vector om naar nieuwe eenheid."""
        self._verander_eenheid(eenheid)

    def gebruik_eenheid(self, eenheid:str):
        """Zet om naar nieuwe eenheid en retourneert object."""
        self._verander_eenheid(eenheid)
        return self
    
    def eh(self, eenheid:str):
        """Zet om naar nieuwe eenheid en retourneert object."""
        self._verander_eenheid(eenheid)
        return self

    @property
    def array(self):
        """Retourneert Numpy array object met alle getallen (zonder eenheid)."""
        return self._array

    def __add__(self, andere):
        """Telt waarden bij elkaar op."""
        if not isinstance(andere, Vector):
            raise TypeError('tweede waarde is geen Vector object')
        pairs = itertools.zip_longest(self, andere, fillvalue=0.0)
        cls = type(self)
        return cls([a + b for a, b in pairs])

    def __sub__(self, andere):
        """Trekt waarde van elkaar af"""
        if not isinstance(andere, Vector):
            raise TypeError('tweede waarde is geen Vector object')
        pairs = itertools.zip_longest(self, andere, fillvalue=0.0)
        cls = type(self)
        return cls([a - b for a, b in pairs])

    def __mul__(self, andere):
        """Vermenigvuldigd Vector met andere Vector (inproduct) of scalar getal."""
        if isinstance(andere, Vector):
            pairs = itertools.zip_longest(self, andere, fillvalue=0.0)
            for i, (a, b) in enumerate(pairs):
                if i == 0:
                    product = a * b
                else:
                    product += a * b
            return product
        elif isinstance(andere, int) or isinstance(andere, float):
            cls = type(self)
            return cls([w * andere for w in self])
        else:
            raise TypeError('tweede waarde is geen Vector object of getal')

    #def __matmul__(self, andere):
    #    @ operator -> gebruiken voor kruisproduct? (en niet inproduct); vanaf python 3.5

    def __truediv__(self, andere):
        """Deelt Vector met andere Vector (inproduct) of scalar getal."""
        if isinstance(andere, Vector):
            pairs = itertools.zip_longest(self, andere, fillvalue=0.0)
            for i, (a, b) in enumerate(pairs):
                if i == 0:
                    product = (a / b)
                else:
                    product += (a / b)
            return product
        elif isinstance(andere, int) or isinstance(andere, float):
            cls = type(self)
            return cls([w / andere for w in self])
        else:
            raise TypeError('tweede waarde is geen Vector object of getal')

    def __pow__(self, macht):
        """Doet Vector tot de macht een geheel getal > 1."""
        if isinstance(macht, int) and macht > 1:
            resultaat = self
            for i in range(2, macht+1):
                resultaat = resultaat * resultaat
            return resultaat
        else:
            raise ValueError('macht moet geheel getal zijn groter dan 1')

    def __rmul__(self, andere):
        """Vermenigvuldigd scalar getal met Vector."""
        return self * andere

    def __rtruediv__(self, andere):
        """Deelt scalar met eenheidsloze Vector."""
        if (isinstance(andere, int) or isinstance(andere, float)) and \
                self.eenheid is None:
            cls = type(self)
            return cls([andere / w for w in self])
        else:
            raise TypeError('kan alleen getal delen door eenheidsloze Vector')

    def __eq__(self, andere):
        """Vergelijkt Vector met andere Vector."""
        if not isinstance(andere, Vector):
            raise TypeError('tweede waarde is geen Vector object')
        if len(self) != len(andere):
            return False
        if self.eenheid is None and andere.eenheid is not None:
            return False
        if self.eenheid is not None and andere.eenheid is None:
            return False
        if not W(1, self.eenheid) & W(1, andere.eenheid):
            # ander type eenheid
            return False
        for w1, w2 in zip(self, andere):
            if self.eenheid is None:
                # w is float object
                if round(w1*pc.Waarde._AFRONDEN_BIJ_VERGELIJKEN) != round(w2*pc.Waarde._AFRONDEN_BIJ_VERGELIJKEN):
                    return False
            else:
                # w is Waarde object
                if w1 != w2:
                    return False
        return True

    def __neq__(self, andere):
        """Vergelijkt Vector negatief met andere Vector"""
        return not self.__eq__(andere)

    def __lt__(self, andere):
        """Kijkt of absolute waarde (lengte vector) kleiner is dan andere Vector."""
        if not isinstance(andere, Vector):
            raise TypeError('tweede waarde is geen Vector object')
        if len(self) != len(andere):
            raise TypeError('tweede vector heeft niet zelfde dimensie')
        if self.eenheid is None and andere.eenheid is not None:
            raise TypeError('tweede vector heeft niet zelfde eenheid')
        if self.eenheid is not None and andere.eenheid is None:
            raise TypeError('tweede vector heeft niet zelfde eenheid')
        if not pc.Waarde(1, self.eenheid) & pc.Waarde(1, andere.eenheid):
            raise TypeError('tweede vector heeft niet zelfde type eenheid')
        return abs(self) < abs(andere)

    def __gt__(self, andere):
        """Kijkt of absolute waarde (lengte vector) groter is dan andere Vector."""
        if not isinstance(andere, Vector):
            raise TypeError('tweede waarde is geen Vector object')
        if len(self) != len(andere):
            raise TypeError('tweede vector heeft niet zelfde dimensie')
        if self.eenheid is None and andere.eenheid is not None:
            raise TypeError('tweede vector heeft niet zelfde eenheid')
        if self.eenheid is not None and andere.eenheid is None:
            raise TypeError('tweede vector heeft niet zelfde eenheid')
        if not pc.Waarde(1, self.eenheid) & pc.Waarde(1, andere.eenheid):
            raise TypeError('tweede vector heeft niet zelfde type eenheid')
        return abs(self) > abs(andere)

    def __le__(self, andere):
        """Kijkt of absolute waarde (lengte vector) kleiner dan of gelijk is aan andere Vector."""
        if self.__lt__(andere):
            return True
        else:
            return abs(self) == abs(andere)

    def __ge__(self, andere):
        """Kijkt of absolute waarde (lengte vector) groter dan of gelijk is aan andere Vector."""
        if self.__gt__(andere):
            return True
        else:
            return abs(self) == abs(andere)

    def __and__(self, andere):
        """Controleert of Vector zelfde type eenheid heeft als andere."""
        if not isinstance(andere, Vector):
            raise TypeError('tweede waarde is geen Vector object')
        return pc.Waarde(1, self.eenheid) & pc.Waarde(1, andere.eenheid)

    def __float__(self):
        """Berekent de lengte van de vector als float object."""
        return np.linalg.norm(self.array)

    def __abs__(self):
        """Berekent de lengte van de vector als Waarde object."""
        return pc.Waarde(float(self), self.eenheid)

    def __pos__(self):
        """Behoud teken (positief = positief, negatief = negatief)."""
        self._array *= 1  # moet met underscore
        return self

    def __neg__(self):
        """Verander teken (positief = negatief, negatief = postief)."""
        self._array *= -1  # moet met underscore
        return self

    def __bool__(self):
        """Geeft False als lengte Vector == 0. Anders True."""
        length = float(self)
        return not (length < 1/W._AFRONDEN_BIJ_VERGELIJKEN and length > -1/W._AFRONDEN_BIJ_VERGELIJKEN)

    def __iter__(self):
        """Itereert over waardes. Als geen eenheid: floats. Als wel eenheid dan Waarde objecten."""
        eenheid = self.eenheid
        for w in self.array:
            if eenheid is None:
                yield w
            else:
                yield pc.Waarde(w, eenheid)

    def __len__(self):
        """Geeft aantal dimensies (waarden) van vector."""
        return len(self.array)

    def __format__(self, config:str=None):
        """Geeft tekst met geformatteerd getal en eenheid."""
        if config is None:
            return str(self)
        format_str = '{:' + config + '}'
        waardes = ', '.join(format_str.format(float(w)) for w in self)
        eenheid = self.eenheid if self.eenheid is not None else ''
        return '({}) {}'.format(waardes, eenheid).strip()

    def __repr__(self):
        """Geeft representatie object."""
        cls_naam = type(self).__name__
        if self.eenheid is None:
            waardes = ', '.join(str(float(w)) for w in self)
        else:
            waardes = ', '.join(repr(pc.Waarde(float(w), self.eenheid)) for w in self)
        return '{}({})'.format(cls_naam, waardes)

    def __str__(self):
        """Geeft tekst met vector en eenheid"""
        waardes = ', '.join(str(float(w)) for w in self)
        eenheid = self.eenheid if self.eenheid is not None else ''
        return '({}) {}'.format(waardes, eenheid).strip()

    def __getitem__(self, subset):
        """Geeft subset van numpy array met waarden."""
        return self.array[subset]

        # """Retourneer subset van waardes (floats of Waarde objecten).
        # Als slice dan wordt er nieuw Vector object gegenereert"""
        # waardes = [w for w in self]
        # if isinstance(subset, int):
        #     return waardes[subset]
        # elif isinstance(subset, slice):
        #     cls = type(self)
        #     return cls(waardes[subset])
        # else:
        #     raise TypeError('index moet geheel getal of slice zijn')

        
        
###############################################################################
#  ALLES HIERONDER MOET ZELFDE ZIJN ALS BIJ WAARDE OBJECT
###############################################################################

    # MASSA

    @property
    def ag(self):
        return self._verander_eenheid('ag')

    @property
    def fg(self):
        return self._verander_eenheid('fg')

    @property
    def pg(self):
        return self._verander_eenheid('pg')

    @property
    def ng(self):
        return self._verander_eenheid('ng')

    @property
    def mug(self):
        return self._verander_eenheid('mug')

    @property
    def mg(self):
        return self._verander_eenheid('mg')

    @property
    def cg(self):
        return self._verander_eenheid('cg')

    @property
    def dg(self):
        return self._verander_eenheid('dg')

    @property
    def g(self):
        return self._verander_eenheid('g')

    @property
    def hg(self):
        return self._verander_eenheid('hg')

    @property
    def kg(self):
        return self._verander_eenheid('kg')

    @property
    def Mg(self):
        return self._verander_eenheid('Mg')

    @property
    def Gg(self):
        return self._verander_eenheid('Gg')

    @property
    def Tg(self):
        return self._verander_eenheid('Tg')

    @property
    def Pg(self):
        return self._verander_eenheid('Pg')

    @property
    def Eg(self):
        return self._verander_eenheid('Eg')

    @property
    def ton(self):
        return self._verander_eenheid('ton')

    @property
    def kton(self):
        return self._verander_eenheid('kton')

    @property
    def Mton(self):
        return self._verander_eenheid('Mton')

    @property
    def ounce(self):
        return self._verander_eenheid('ounce')

    @property
    def pound(self):
        return self._verander_eenheid('pound')

    @property
    def kip(self):
        return self._verander_eenheid('kip')

    @property
    def stone(self):
        return self._verander_eenheid('stone')

    @property
    def grain(self):
        return self._verander_eenheid('grain')

    # LENGTE

    @property
    def am(self):
        return self._verander_eenheid('am')

    @property
    def fm(self):
        return self._verander_eenheid('fm')

    @property
    def pm(self):
        return self._verander_eenheid('pm')

    @property
    def nm(self):
        return self._verander_eenheid('nm')

    @property
    def mum(self):
        return self._verander_eenheid('mum')

    @property
    def mm(self):
        return self._verander_eenheid('mm')

    @property
    def cm(self):
        return self._verander_eenheid('cm')

    @property
    def dm(self):
        return self._verander_eenheid('dm')

    @property
    def m(self):
        return self._verander_eenheid('m')

    @property
    def dam(self):
        return self._verander_eenheid('dam')

    @property
    def hm(self):
        return self._verander_eenheid('hm')

    @property
    def km(self):
        return self._verander_eenheid('km')

    @property
    def Mm(self):
        return self._verander_eenheid('Mm')

    @property
    def Gm(self):
        return self._verander_eenheid('Gm')

    @property
    def Tm(self):
        return self._verander_eenheid('Tm')

    @property
    def Pm(self):
        return self._verander_eenheid('Pm')

    @property
    def Em(self):
        return self._verander_eenheid('Em')

    @property
    def inch(self):
        return self._verander_eenheid('in') # uitzondering

    @property
    def ft(self):
        return self._verander_eenheid('ft')

    @property
    def yard(self):
        return self._verander_eenheid('yard')

    @property
    def zeemijl(self):
        return self._verander_eenheid('zeemijl')

    @property
    def mijl(self):
        return self._verander_eenheid('mijl')

    # TIJD

    @property
    def attos(self):
        return self._verander_eenheid('as') # uitzondering

    @property
    def fs(self):
        return self._verander_eenheid('fs')

    @property
    def ps(self):
        return self._verander_eenheid('ps')

    @property
    def ns(self):
        return self._verander_eenheid('ns')

    @property
    def mus(self):
        return self._verander_eenheid('mus')

    @property
    def ms(self):
        return self._verander_eenheid('ms')

    @property
    def cs(self):
        return self._verander_eenheid('cs')

    @property
    def ds(self):
        return self._verander_eenheid('ds')

    @property
    def s(self):
        return self._verander_eenheid('s')

    @property
    def das(self):
        return self._verander_eenheid('das')

    @property
    def hs(self):
        return self._verander_eenheid('hs')

    @property
    def ks(self):
        return self._verander_eenheid('ks')

    @property
    def Ms(self):
        return self._verander_eenheid('Ms')

    @property
    def Gs(self):
        return self._verander_eenheid('Gs')

    @property
    def Ts(self):
        return self._verander_eenheid('Ts')

    @property
    def Ps(self):
        return self._verander_eenheid('Ps')

    @property
    def Es(self):
        return self._verander_eenheid('Es')

    @property
    def minuut(self):
        return self._verander_eenheid('min')  # uitzondering

    @property
    def h(self):
        return self._verander_eenheid('h')

    @property
    def d(self):
        return self._verander_eenheid('d')

    # TEMPERATUUR

    @property
    def C(self):
        return self._verander_eenheid('C')

    @property
    def K(self):
        return self._verander_eenheid('K')

    @property
    def F(self):
        return self._verander_eenheid('F')

    # HOEK

    @property
    def rad(self):
        return self._verander_eenheid('rad')

    @property
    def deg(self):
        return self._verander_eenheid('deg')

    @property
    def gon(self):
        return self._verander_eenheid('gon')

    # KRACHT

    @property
    def N(self):
        return self._verander_eenheid('N')

    @property
    def kN(self):
        return self._verander_eenheid('kN')

    @property
    def MN(self):
        return self._verander_eenheid('MN')

    @property
    def GN(self):
        return self._verander_eenheid('GN')

    @property
    def TN(self):
        return self._verander_eenheid('TN')

    # SPANNING

    @property
    def N_mm2(self):
        return self._verander_eenheid('N/mm2')

    @property
    def kN_mm2(self):
        return self._verander_eenheid('kN_mm2')

    @property
    def MN_mm2(self):
        return self._verander_eenheid('MN/mm2')

    @property
    def N_m2 (self):
        return self._verander_eenheid('N/m2')

    @property
    def kN_m2(self):
        return self._verander_eenheid('kN/m2')

    @property
    def MN_m2(self):
        return self._verander_eenheid('MN/m2')

    @property
    def Pa(self):
        return self._verander_eenheid('Pa')

    @property
    def kPa(self):
        return self._verander_eenheid('kPa')

    @property
    def MPa(self):
        return self._verander_eenheid('MPa')

    @property
    def GPa(self):
        return self._verander_eenheid('GPa')

    @property
    def TPa(self):
        return self._verander_eenheid('TPa')

    # MOMENT

    @property
    def Nm(self):
        return self._verander_eenheid('Nm')

    @property
    def kNm(self):
        return self._verander_eenheid('kNm')

    @property
    def MNm(self):
        return self._verander_eenheid('MNm')

    @property
    def Nmm(self):
        return self._verander_eenheid('Nmm')

    @property
    def kNmm(self):
        return self._verander_eenheid('kNmm')

    @property
    def MNmm(self):
        return self._verander_eenheid('MNmm')

    # OPPERVLAKTE

    @property
    def km2(self):
        return self._verander_eenheid('km2')

    @property
    def hm2(self):
        return self._verander_eenheid('hm2')

    @property
    def m2(self):
        return self._verander_eenheid('m2')

    @property
    def dm2(self):
        return self._verander_eenheid('dm2')

    @property
    def cm2(self):
        return self._verander_eenheid('cm2')

    @property
    def mm2(self):
        return self._verander_eenheid('mm2')

    @property
    def ca(self):
        return self._verander_eenheid('ca')

    @property
    def a(self):
        return self._verander_eenheid('a')

    @property
    def ha(self):
        return self._verander_eenheid('ha')

    # INHOUD

    @property
    def km3(self):
        return self._verander_eenheid('km3')

    @property
    def hm3(self):
        return self._verander_eenheid('hm3')

    @property
    def m3(self):
        return self._verander_eenheid('m3')

    @property
    def dm3(self):
        return self._verander_eenheid('dm3')

    @property
    def cm3(self):
        return self._verander_eenheid('cm3')

    @property
    def mm3(self):
        return self._verander_eenheid('mm3')

    @property
    def ml(self):
        return self._verander_eenheid('ml')

    @property
    def cl(self):
        return self._verander_eenheid('cl')

    @property
    def dl(self):
        return self._verander_eenheid('dl')

    @property
    def l(self):
        return self._verander_eenheid('l')

    @property
    def dal(self):
        return self._verander_eenheid('dal')

    @property
    def hl(self):
        return self._verander_eenheid('hl')

    @property
    def kl(self):
        return self._verander_eenheid('kl')

    @property
    def gallon(self):
        return self._verander_eenheid('gallon')

    @property
    def pint(self):
        return self._verander_eenheid('pint')

    @property
    def floz(self):
        return self._verander_eenheid('floz')

    @property
    def tbs(self):
        return self._verander_eenheid('tbs')

    @property
    def tsp(self):
        return self._verander_eenheid('tsp')

    @property
    def bbl(self):
        return self._verander_eenheid('bbl')

    @property
    def cup(self):
        return self._verander_eenheid('cup')

    # SNELHEID

    @property
    def km_j(self):
        return self._verander_eenheid('km/j')

    @property
    def km_d(self):
        return self._verander_eenheid('km/d')

    @property
    def km_h(self):
        return self._verander_eenheid('km/h')

    @property
    def km_min(self):
        return self._verander_eenheid('km/min')

    @property
    def km_s(self):
        return self._verander_eenheid('km/s')

    @property
    def m_j(self):
        return self._verander_eenheid('m/j')

    @property
    def m_d(self):
        return self._verander_eenheid('m/d')

    @property
    def m_h(self):
        return self._verander_eenheid('m/h')

    @property
    def m_min(self):
        return self._verander_eenheid('m/min')

    @property
    def m_s(self):
        return self._verander_eenheid('m/s')

    @property
    def dm_j(self):
        return self._verander_eenheid('dm/j')

    @property
    def dm_d(self):
        return self._verander_eenheid('dm/d')

    @property
    def dm_h(self):
        return self._verander_eenheid('dm/h')

    @property
    def dm_min(self):
        return self._verander_eenheid('dm/min')

    @property
    def dm_s(self):
        return self._verander_eenheid('dm/s')

    @property
    def cm_j(self):
        return self._verander_eenheid('cm/j')

    @property
    def cm_d(self):
        return self._verander_eenheid('cm/d')

    @property
    def cm_h(self):
        return self._verander_eenheid('cm/h')

    @property
    def cm_min(self):
        return self._verander_eenheid('cm/min')

    @property
    def cm_s(self):
        return self._verander_eenheid('cm/s')

    @property
    def mm_j(self):
        return self._verander_eenheid('mm/j')

    @property
    def mm_d(self):
        return self._verander_eenheid('mm/d')

    @property
    def mm_h(self):
        return self._verander_eenheid('mm/h')

    @property
    def mm_min(self):
        return self._verander_eenheid('mm/min')

    @property
    def mm_s(self):
        return self._verander_eenheid('mm/s')



    # TRAAGHEIDSMOMENT

    @property
    def km4(self):
        return self._verander_eenheid('km4')

    @property
    def m4(self):
        return self._verander_eenheid('m4')

    @property
    def dm4(self):
        return self._verander_eenheid('dm4')

    @property
    def cm4(self):
        return self._verander_eenheid('cm4')

    @property
    def mm4(self):
        return self._verander_eenheid('mm4')

    # DEBIET

    @property
    def km3_j(self):
        return self._verander_eenheid('km3/j')

    @property
    def km3_d(self):
        return self._verander_eenheid('km3/d')

    @property
    def km3_h(self):
        return self._verander_eenheid('km3/h')

    @property
    def km3_min(self):
        return self._verander_eenheid('km3/min')

    @property
    def km3_s(self):
        return self._verander_eenheid('km3/s')

    @property
    def m3_j(self):
        return self._verander_eenheid('m3/j')

    @property
    def m3_d(self):
        return self._verander_eenheid('m3/d')

    @property
    def m3_h(self):
        return self._verander_eenheid('m3/h')

    @property
    def m3_min(self):
        return self._verander_eenheid('m3/min')

    @property
    def m3_s(self):
        return self._verander_eenheid('m3/s')

    @property
    def dm3_j(self):
        return self._verander_eenheid('dm3/j')

    @property
    def dm3_d(self):
        return self._verander_eenheid('dm3/d')

    @property
    def dm3_h(self):
        return self._verander_eenheid('dm3/h')

    @property
    def dm3_min(self):
        return self._verander_eenheid('dm3/min')

    @property
    def dm3_s(self):
        return self._verander_eenheid('dm3/s')

    @property
    def cm3_j(self):
        return self._verander_eenheid('cm3/j')

    @property
    def cm3_d(self):
        return self._verander_eenheid('cm3/d')

    @property
    def cm3_h(self):
        return self._verander_eenheid('cm3/h')

    @property
    def cm3_min(self):
        return self._verander_eenheid('cm3/min')

    @property
    def cm3_s(self):
        return self._verander_eenheid('cm3/s')

    @property
    def mm3_j(self):
        return self._verander_eenheid('mm3/j')

    @property
    def mm3_d(self):
        return self._verander_eenheid('mm3/d')

    @property
    def mm3_h(self):
        return self._verander_eenheid('mm3/h')

    @property
    def mm3_min(self):
        return self._verander_eenheid('mm3/min')

    @property
    def mm3_s(self):
        return self._verander_eenheid('mm3/s')

    @property
    def l_j(self):
        return self._verander_eenheid('l/j')

    @property
    def l_d(self):
        return self._verander_eenheid('l/d')

    @property
    def l_h(self):
        return self._verander_eenheid('l/h')

    @property
    def l_min(self):
        return self._verander_eenheid('l/min')

    @property
    def l_s(self):
        return self._verander_eenheid('l/s')

    @property
    def dl_j(self):
        return self._verander_eenheid('dl/j')

    @property
    def dl_d(self):
        return self._verander_eenheid('dl/d')

    @property
    def dl_h(self):
        return self._verander_eenheid('dl/h')

    @property
    def dl_min(self):
        return self._verander_eenheid('dl/min')

    @property
    def dl_s(self):
        return self._verander_eenheid('dl/s')

    @property
    def cl_j(self):
        return self._verander_eenheid('cl/j')

    @property
    def cl_d(self):
        return self._verander_eenheid('cl/d')

    @property
    def cl_h(self):
        return self._verander_eenheid('cl/h')

    @property
    def cl_min(self):
        return self._verander_eenheid('cl/min')

    @property
    def cl_s(self):
        return self._verander_eenheid('cl/s')

    @property
    def ml_j(self):
        return self._verander_eenheid('ml/j')

    @property
    def ml_d(self):
        return self._verander_eenheid('ml/d')

    @property
    def ml_h(self):
        return self._verander_eenheid('ml/h')

    @property
    def ml_min(self):
        return self._verander_eenheid('ml/min')

    @property
    def ml_s(self):
        return self._verander_eenheid('ml/s')

    # lijnlast

    @property
    def kN_m(self):
        return self._verander_eenheid('kN/m')

    @property
    def N_m(self):
        return self._verander_eenheid('N/m')

    @property
    def kN_mm(self):
        return self._verander_eenheid('kN/mm')

    @property
    def N_mm(self):
        return self._verander_eenheid('N/mm')