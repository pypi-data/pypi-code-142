from typing import Union
import itertools
import numpy as np

import pyco.basis
import pyco.waarde

class pc:
    BasisObject = pyco.basis.BasisObject
    Waarde = pyco.waarde.Waarde

class Lijst(pc.BasisObject):
    """
    Bevat een aantal getallen of Waarde objecten met allen dezelfde eenheid.

    AANMAKEN LIJST              eenheid van 1e component, geldt voor geheel
        l = Lijst(waarde1, waarde2, ...)          waarde: float, int of Waarde
        l = Lijst([waarde1, waarde2, ...])              
        l = Lijst(numpy_array)             array wordt indien nodig 1D gemaakt
        l2 = l.kopie()          maak een kopie (nieuw object) met zelfde eigenschappen 

    AANPASSEN EENHEID           omzetten van eenheid naar andere eenheid
        l.eenheid               huidige eenheid opvragen (tekst of None)
        l.eenheid = 'N/mm2'     eenheid aanpassen
        l.gebruik_eenheid('m')  eenheid aanpassen, retourneert object
        l.eh('m')               eenheid aanpassen, retourneert object
        l = l.N_mm2             kan voor een aantal standaard gevallen (zie lijst onderaan)

    OMZETTEN LIJST NAAR TEKST   resulteert in nieuw string object
        tekst = str(l)          of automatisch met bijvoorbeeld print(l)
        tekst = format(l, '.2f') format configuratie meegeven voor getal
              = l.format('.2f')

    MOGELIJKE BEWERKINGEN       resulteert in nieuw Lijst object
        l3 = l1 + l2            lijst optellen bij lijst
        l3 = l1 - l2            lijst aftrekken van lijst
        getal = l1 * l2         lijst vermenigvuldigen met lijst (inproduct)
        getal = l1 / l2         lijst delen door lijst (inverse inproduct)
        l2 = n * l1             getal vermenigvuldigen met lijst
        l2 = l1 * n             lijst vermenigvuldigen met getal
        l2 = n / l1             getal delen door lijst
        l2 = l1 / n             lijst delen door getal
        l2 = l1 ** n            lijst tot de macht een geheel getal
        waarde = abs(l1)        berekent lengte van lijst -> Waarde object
        getal = float(l1)       berekent lengte van lijst -> float object
        l2 = +l1                behoud teken
        l2 = -l1                verander teken (positief vs. negatief)
        for w in l1:            itereert en geeft float/Waarde object terug
        getal = len(l1)         geeft aantal elementen (dimensies) van lijst

    NUMPY BEWERKINGEN           gebruikt array object
        numpy_array = l1.array  retourneert Numpy array object
                                    (bevat allen getallen, zonder eenheid)
        getal = l1[2]           retourneert getal (zonder eenheid) op index
        numpy_array = l1[1:3]   retourneert Numpy array object vanuit slice

    WAARDEN VERGELIJKEN         resulteert in een boolean (True/False)
        l1 == l2                de totale lijst is gelijk aan
        l1 != l2                de totale lijst is niet gelijk aan
        l1 >  l2                de absolute waarde van lijst is groter dan
        l1 <  l2                de absolute waarde van lijst is kleiner dan
        l1 >= l2                de absolute waarde van lijst is groter dan of gelijk aan
        l1 <= l2                de absolute waarde van lijst is kleiner dan of gelijk aan
        l1 &  l2                eenheden zijn zelfde type
        
    WISKUNDIGE FUNCTIES         
        l.sin()                 sinus (alleen getallen en hoeken)
        l.cos()                 cosinus (alleen getallen en hoeken)
        l.tan()                 tangens (alleen getallen en hoeken)
        l.asin()                arcsinus (omgekeerde sin, alleen getallen)
        l.acos()                arccosinus (omgekeerde cos, alleen getallen)
        l.atan()                arctangens (omgekeerde tan, alleen getallen)
        l.sinh()                hyperbolische sinus (getallen en hoeken)
        l.cosh()                hyperbolische cosinus (getallen en hoeken)
        l.tanh()                hyperbolische tangens (getallen en hoeken)
        l.asinh()               arcsinus hyperb. (omgekeerde asinh, getallen)
        l.acosh()               arccosinus hyperb. (omgekeerde acosh, getallen)
        l.atanh()               arctangens hyperb. (omgekeerde atanh, getallen)
        l.afronden(n)           rond af op n decimalen (standaard 0)
        l.plafond()             rond af naar boven (geheel getal)
        l.vloer()               rond af naar beneden (geheel getal)
        l.plafond_0_vloer()     rond af richting 0 (geheel getal)
        l.som()                 de som van de elementen
        l.product()             het product van de elementen
        l.verschil()            lijst met verschillen tussen elementen
        l1.optellen(l2)         l1 + l2
        l1.aftrekken(l2)        l1 - l2
        l1.vermenigvuldigen(l2) l1 * l2
        l1.delen(l2)            l1 / l2
        l1.delen_aantal(l2)     afgerond naar beneden
        l1.delen_rest(l2)       restant na afronden naar beneden
        l.macht(n)              l ** n
        l.reciproke()           1 / l
        l.negatief()            -l
        l1.kruisproduct(l2)     l1 x l2: staat loodrecht op vector l1 en l2
        l1.inwendigproduct(l2)  l1 . l2: is |l1| * |l2| * cos(theta)
        l.exp()                 exponentieel: berekent e^l
        l.ln()                  natuurlijke logaritme (grondgetal e)
        l.log()                 logaritme met grondgetal 10
        l.bijsnijden(min, max)  snij alle elementen af tot minmax bereik
        l.wortel()              vierkantswortel
        l.wortel3()             kubieke wortel
        l.absoluut()            absolute waarde (altijd positief)
        l.teken()               positief getal: 1.0   negatief: -1.0 
        l.kopieer_teken(l2)     neem huidige, met het teken (+-) van l2
        l.is_positief(a)        stap functie: l<0 -> 0, l=0 -> a, l>0 -> 1 
        l.verwijder_nan()       verwijder niet-getallen (not a number)
        l.getal_nan_inf()       vervang: nan=0, inf=1.7e+308 (heel groot)
        l.gemiddelde()          bepaalt het gemiddelde
        l.stdafw_pop()          bepaalt standaardafwijking voor populatie
        l.stdafw_n()            bepaalt standaardafwijking steekproef
        l.mediaan()             bepaalt de mediaan
        l.percentiel(perc)      percentage: getal tussen 0 en 100
        l.correlatie(l2)        bepaalt correlatie matrix
        l.sorteer()             sorteert een lijst van klein naar groot
        l.omdraaien()           draai de volgorde van de lijst om
        l.is_nan()              bepaalt per element of een niet-getal is
        l.is_inf()              bepaalt per element of oneindig is
        l1.gelijk(l2)           per element: w1 == w2
        l1.niet_gelijk(l2)      per element: w1 != w2
        l1.groter(l2)           per element: w1 > w2
        l1.groter_gelijk(l2)    per element: w1 >= w2
        l1.kleiner(l2)          per element: w1 < w2
        l1.kleiner_gelijk(l2)   per element: w1 <= w2
        l.alle()                kijkt of alle elementen True zijn
        l.sommige()             kijkt of er minimaal 1 element True is
        l.niet_alle()           kijkt of er minimaal 1 element False is
        l.geen()                kijkt of alle elementen False zijn
        l.waar()                zet lijst om in list met True/False
        
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
        
    def _verander_eenheid(self, eenheid:str, check_type:bool=True):
        """Zet Lijst om naar nieuwe eenheid."""
        if self._eenheid is None:
            self._eenheid = eenheid
        else:
            tmp_waardes = []
            oude_eenheid = self._eenheid
            for w in self:
                w = float(pc.Waarde(float(w), oude_eenheid).gebruik_eenheid(eenheid, check_type=check_type))
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
        """Zet Lijst om naar nieuwe eenheid."""
        self._verander_eenheid(eenheid)

    def gebruik_eenheid(self, eenheid:str, check_type:bool=True):
        """Zet om naar nieuwe eenheid en retourneert object."""
        self._verander_eenheid(eenheid, check_type)
        return self
    
    def eh(self, eenheid:str, check_type:bool=True):
        """Zet om naar nieuwe eenheid en retourneert object."""
        self._verander_eenheid(eenheid, check_type)
        return self

    @property
    def array(self):
        """Retourneert Numpy array object met alle getallen (zonder eenheid)."""
        return self._array
    
    def kopie(self):
        """Retourneert kopie van zichzelf (nieuw object)."""
        return type(self)(self.array).gebruik_eenheid(self.eenheid)
    
    def format(self, format_str:str=''):
        """Retourneert geformatteerde tekst."""
        return format(self, format_str)
    
    #-----------------------------------------------------------------------------
    
    def sin(self):
        """Sinus"""
        from pyco import sin
        return sin(self)
            
    def cos(self):
        """Cosinus"""
        from pyco import cos
        return cos(self)
            
    def tan(self):
        """Tangens"""
        from pyco import tan
        return tan(self)
            
    def sinh(self):
        """Hyperbolische sinus"""
        from pyco import sinh
        return sinh(self)
            
    def cosh(self):
        """Hyperbolische cosinus"""
        from pyco import cosh
        return cosh(self)
            
    def tanh(self):
        """Hyperbolische tangens"""
        from pyco import tanh
        return tanh(self)
    
    def afronden(self, n=0):
        """Rond af op n decimalen (standaard 0)"""
        from pyco import afronden
        return afronden(self, n)
    
    def plafond(self):
        """Rond af naar boven (geheel getal)"""
        from pyco import plafond
        return plafond(self)
    
    def vloer(self):
        """Rond af naar beneden (geheel getal)"""
        from pyco import vloer
        return vloer(self)
    
    def plafond_0_vloer(self):
        """Rond af richting 0 (geheel getal)"""
        from pyco import plafond_0_vloer
        return plafond_0_vloer(self)
    
    def som(self):
        """De som van de elementen"""
        from pyco import som
        return som(self)
    
    def product(self):
        """Het product van de elementen"""
        from pyco import product
        return product(self)
    
    def verschil(self):
        """Lijst met verschillen tussen elementen"""
        from pyco import verschil
        return verschil(self)
    
    def optellen(self, l):
        """Tel andere lijst op bij deze lijst (per element)"""
        from pyco import optellen
        return optellen(self, l)
    
    def aftrekken(self, w):
        """Haal andere lijst af van deze lijst (per element)"""
        from pyco import aftrekken
        return aftrekken(self, w)
    
    def vermenigvuldigen(self, w):
        """Vermenigvuldig andere lijst met deze lijst (per element)"""
        from pyco import vermenigvuldigen
        return vermenigvuldigen(self, w)
    
    def delen(self, w):
        """Deel lijst door een andere gegeven lijst (per element)"""
        from pyco import delen
        return delen(self, w)
    
    def delen_aantal(self, w):
        """Deel lijst door een andere gegeven lijst en rond af naar beneden (per element)"""
        from pyco import delen_aantal
        return delen_aantal(self, w)
    
    def delen_rest(self, w):
        """Deel lijst door een andere gegeven lijst, rond af naar beneden en retourneer het restant (per element)"""
        from pyco import delen_rest
        return delen_rest(self, w)
    
    def macht(self, n):
        """Bereken deze lijst tot een bepaalde macht (geheel getal) (per element)"""
        from pyco import macht
        return macht(self, n)
    
    def reciproke(self):
        """Bereken de reciproke (1/x) (per element)"""
        from pyco import reciproke
        return reciproke(self)
    
    def negatief(self):
        """Maak van positieve waarde een negatieve en vice versa (per element)"""
        from pyco import negatief
        return negatief(self)
    
    def kruisproduct(self, lijst):
        """Bepaalt het kruispoduct van deze lijst met andere lijst."""
        from pyco import kruisproduct
        return kruisproduct(self, lijst)
    
    def inwendigproduct(self, lijst):
        """Bepaalt het inwendigpoduct van deze lijst met andere lijst."""
        from pyco import inwendigproduct
        return inwendigproduct(self, lijst)
    
    def exp(self):
        """Berekent e^x."""
        from pyco import exp
        return exp(self)
        
    def ln(self):
        """Berekent ln(x)."""
        from pyco import ln
        return ln(self)
        
    def log(self):
        """Berekent log10(x)."""
        from pyco import log
        return log(self)
    
    def bijsnijden(self, min_, max_):
        """Snij alle elementen af tot min-max-bereik"""
        from pyco import bijsnijden
        return bijsnijden(self, min_, max_)
    
    def wortel(self):
        """Berekent vierkantswortel."""
        if any([i < 0 for i in self]):
            raise ValueError('Een negatieve waarde is bij wortel niet toegestaan')
        from pyco import wortel
        return wortel(self)
    
    def wortel3(self):
        """Berekent kubieke wortel."""
        from pyco import wortel3
        return wortel3(self)
    
    def absoluut(self):
        """Berekent absolute waarde (altijd positief)."""
        from pyco import absoluut
        return absoluut(self)
    
    def teken(self):
        """Geeft 1 terug indien positief, -1 indien negatief en 0 indien nul"""
        from pyco import teken
        return teken(self)
    
    def kopieer_teken(self, andere_waarde):
        """Behoudt grootte van huidige waarde, maar met teken (+-) van andere waarde."""
        from pyco import kopieer_teken
        return kopieer_teken(self, andere_waarde)
    
    def is_positief(self, nul_waarde):
        """Stapfunctie: w<0 -> 0, w=0 -> nul_waarde, w>0 -> 1."""
        from pyco import is_positief
        return is_positief(self, nul_waarde)
    
    def verwijder_nan(self):
        """Verwijder niet-getallen (not a number)."""
        from pyco import verwijder_nan
        return verwijder_nan(self)
    
    def getal_nan_inf(self):
        """Vervang: nan=0, inf=1.7e+308 (heel groot)."""
        from pyco import getal_nan_inf
        return getal_nan_inf(self)
    
    def gemiddelde(self):
        """Bepaalt het gemiddelde."""
        from pyco import gemiddelde
        return gemiddelde(self)
    
    def stdafw_pop(self):
        """Bepaalt de standaardafwijking voor populatie (N)."""
        from pyco import stdafw_pop
        return stdafw_pop(self)
    
    def stdafw_n(self):
        """Bepaalt de standaardafwijking voor een steekproef (N-1)."""
        from pyco import stdafw_n
        return stdafw_n(self)
    
    def mediaan(self):
        """Bepaalt de mediaan."""
        from pyco import mediaan
        return mediaan(self)
    
    def percentiel(self, percentage_getal):
        """Bepaalt de percentiel gegeven een percentage (getal tussen 0 en 100)."""
        from pyco import percentiel
        return percentiel(self, percentage_getal)
    
    def correlatie(self, andere_lijst):
        """Bepaalt een correlatie matrix (Pearson product-moment correlation coefficients)."""
        from pyco import correlatie
        return correlatie(self, andere_lijst)
    
    def sorteer(self):
        """Sorteert de lijst van klein naar groot."""
        from pyco import sorteer
        return sorteer(self)
    
    def omdraaien(self):
        """Draait de volgorde van de lijst om."""
        from pyco import omdraaien
        return omdraaien(self)
    
    def is_nan(self):
        """Bepaalt per elment of waarde een niet-getal is (not a number: pc.nan)."""
        from pyco import is_nan
        return is_nan(self)
    
    def is_inf(self):
        """Bepaalt per element of waarde oneindig groot is. (pc.inf)"""
        from pyco import is_inf
        return is_inf(self)
    
    def gelijk(self, andere_lijst):
        """per element: w == andere_lijst"""
        from pyco import gelijk
        return gelijk(self, andere_lijst)
    
    def niet_gelijk(self, andere_lijst):
        """per element: w != andere_lijst"""
        from pyco import niet_gelijk
        return niet_gelijk(self, andere_lijst)
    
    def groter(self, andere_lijst):
        """per element: w > andere_lijst"""
        from pyco import groter
        return groter(self, andere_lijst)
    
    def groter_gelijk(self, andere_lijst):
        """per element: w >= andere_lijst"""
        from pyco import groter_gelijk
        return groter_gelijk(self, andere_lijst)
    
    def kleiner(self, andere_lijst):
        """per element: w < andere_lijst"""
        from pyco import kleiner
        return kleiner(self, andere_lijst)
    
    def kleiner_gelijk(self, andere_lijst):
        """per element: w <= andere_lijst"""
        from pyco import kleiner_gelijk
        return kleiner_gelijk(self, andere_lijst)
    
    def alle(self):
        """Kijkt of alle elementen True zijn"""
        from pyco import alle
        return alle(self)
    
    def sommige(self):
        """Kijkt of er minimaal 1 element True is"""
        from pyco import sommige
        return sommige(self)
    
    def niet_alle(self):
        """Kijkt of er minimaal 1 element False is"""
        from pyco import niet_alle
        return niet_alle(self)
    
    def geen(self):
        """Kijkt of alle elementen False zijn"""
        from pyco import geen
        return geen(self)
    
#-----------------------------------------------------------------------------
    
    def waar(self):
        """Maak een array met True/False per element"""
        return np.array([bool(w) for w in self])

    def __add__(self, andere):
        """Telt waarden bij elkaar op."""
        return self.optellen(andere)

    def __sub__(self, andere):
        """Trekt waarde van elkaar af"""
        return self.aftrekken(andere)

    def __mul__(self, andere):
        """Vermenigvuldigd Lijst met andere Lijst (inproduct) of scalar getal."""
        return self.vermenigvuldigen(andere)

    #def __matmul__(self, andere):
    #    @ operator -> gebruiken voor kruisproduct? (en niet inproduct); vanaf python 3.5

    def __truediv__(self, andere):
        """Deelt Lijst met andere Lijst (inproduct) of scalar getal."""
        return self.delen(andere)

    def __pow__(self, macht):
        """Doet Lijst tot de macht een geheel getal > 1."""
        return self.macht(macht)

    def __rmul__(self, andere):
        """Vermenigvuldigd scalar getal met Lijst."""
        return self.vermenigvuldigen(andere)

    def __rtruediv__(self, andere):
        """Deelt scalar met eenheidsloze Lijst."""
        return self.delen(andere)

    def __eq__(self, andere):
        """Vergelijkt Lijst met andere Lijst."""
        if not isinstance(andere, Lijst):
            raise TypeError('tweede waarde is geen Lijst object')
        if len(self) != len(andere):
            return False
        if self.eenheid is None and andere.eenheid is not None:
            return False
        if self.eenheid is not None and andere.eenheid is None:
            return False
        if not pc.Waarde(1, self.eenheid) & pc.Waarde(1, andere.eenheid):
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
        """Vergelijkt Lijst negatief met andere Lijst"""
        return not self.__eq__(andere)

    def __lt__(self, andere):
        """Kijkt of absolute waarde (lengte lijst) kleiner is dan andere Lijst."""
        if not isinstance(andere, Lijst):
            raise TypeError('tweede waarde is geen Lijst object')
        if len(self) != len(andere):
            raise TypeError('tweede lijst heeft niet zelfde dimensie')
        if self.eenheid is None and andere.eenheid is not None:
            raise TypeError('tweede lijst heeft niet zelfde eenheid')
        if self.eenheid is not None and andere.eenheid is None:
            raise TypeError('tweede lijst heeft niet zelfde eenheid')
        if not pc.Waarde(1, self.eenheid) & pc.Waarde(1, andere.eenheid):
            raise TypeError('tweede lijst heeft niet zelfde type eenheid')
        return abs(self) < abs(andere)

    def __gt__(self, andere):
        """Kijkt of absolute waarde (lengte lijst) groter is dan andere Lijst."""
        if not isinstance(andere, Lijst):
            raise TypeError('tweede waarde is geen Lijst object')
        if len(self) != len(andere):
            raise TypeError('tweede lijst heeft niet zelfde dimensie')
        if self.eenheid is None and andere.eenheid is not None:
            raise TypeError('tweede lijst heeft niet zelfde eenheid')
        if self.eenheid is not None and andere.eenheid is None:
            raise TypeError('tweede lijst heeft niet zelfde eenheid')
        if not pc.Waarde(1, self.eenheid) & pc.Waarde(1, andere.eenheid):
            raise TypeError('tweede lijst heeft niet zelfde type eenheid')
        return abs(self) > abs(andere)

    def __le__(self, andere):
        """Kijkt of absolute waarde (lengte lijst) kleiner dan of gelijk is aan andere Lijst."""
        if self.__lt__(andere):
            return True
        else:
            return abs(self) == abs(andere)

    def __ge__(self, andere):
        """Kijkt of absolute waarde (lengte lijst) groter dan of gelijk is aan andere Lijst."""
        if self.__gt__(andere):
            return True
        else:
            return abs(self) == abs(andere)

    def __and__(self, andere):
        """Controleert of Lijst zelfde type eenheid heeft als andere."""
        if not isinstance(andere, Lijst):
            raise TypeError('tweede waarde is geen Lijst object')
        return pc.Waarde(1, self.eenheid) & pc.Waarde(1, andere.eenheid)

    def __float__(self):
        """Berekent de lengte van de lijst als float object."""
        return np.linalg.norm(self.array)

    def __abs__(self):
        """Berekent de lengte van de lijst als Waarde object."""
        return pc.Waarde(float(self), self.eenheid)

    def __pos__(self):
        """Behoud teken (positief = positief, negatief = negatief)."""
        return self

    def __neg__(self):
        """Verander teken (positief = negatief, negatief = postief)."""
        return self.negatief()

    def __bool__(self):
        """Geeft False als lengte Lijst == 0. Anders True."""
        length = float(self)
        return not (length < 1/pc.Waarde._AFRONDEN_BIJ_VERGELIJKEN and length > -1/pc.Waarde._AFRONDEN_BIJ_VERGELIJKEN)

    def __iter__(self):
        """Itereert over waardes. Als geen eenheid: floats. Als wel eenheid dan Waarde objecten."""
        eenheid = self.eenheid
        for w in self.array:
            if eenheid is None:
                yield w
            else:
                yield pc.Waarde(w, eenheid)

    def __len__(self):
        """Geeft aantal dimensies (waarden) van lijst."""
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
        """Geeft tekst met lijst en eenheid"""
        waardes = ', '.join(str(float(w)) for w in self)
        eenheid = self.eenheid if self.eenheid is not None else ''
        return '({}) {}'.format(waardes, eenheid).strip()

    def __getitem__(self, subset):
        """Geeft subset van numpy array met waarden."""
        return self.array[subset]

        # """Retourneer subset van waardes (floats of Waarde objecten).
        # Als slice dan wordt er nieuw Lijst object gegenereert"""
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