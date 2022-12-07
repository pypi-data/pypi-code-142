import re
import math
import numpy as np
from fractions import Fraction
from typing import Union

import pyco.basis

class pc:
    BasisObject = pyco.basis.BasisObject

class Waarde(pc.BasisObject):
    """
    Bevat een getal en bijhorende eenheid.

    AANMAKEN WAARDE
        w = Waarde(getal)
        w = Waarde(getal, eenheid_tekst)
        w2 = w.kopie()          maak een kopie (nieuw object) met zelfde eigenschappen    

    AANPASSEN EENHEID           omzetten van eenheid naar andere eenheid
        w.eenheid               huidige eenheid opvragen (tekst of None)
        w.eenheid = 'N/mm2'     eenheid aanpassen
        w = w['N/mm2']          eenheid aanpassen, retourneert object
        w.gebruik_eenheid('mm') eenheid aanpassen, retourneert object
        w.eh('mm')              eenheid aanpassen, retourneert object
        w = w.N_mm2             kan voor een aantal standaard gevallen (zie lijst onderaan)

    AANPASSEN AFRONDING         pas afgerond wanneer waarde wordt getoond als tekst
        w = w[0]                kan voor alle gehele getallen
        w = w._0                kan voor 0 t/m 9 (cijfers achter de komma)

    OMZETTEN WAARDE NAAR TEKST  resulteert in nieuw string object
                                    -> gebruikt afronding indien opgegeven
        tekst = str(w)          of automatisch met bijvoorbeeld print(w)
        tekst = format(w,'.2f') format configuratie meegeven voor getal
              = w.format('.2f')

    OMZETTEN WAARDE NAAR GETAL  resulteert in nieuw float object
        getal = float(w)        omzetten met standaard eenheid
        getal = float(w['eh'])  eerst eenheid definiëren voor omzetten waarde

    MOGELIJKE BEWERKINGEN       resulteert in nieuw Waarde object
        w3 = w1 + w2            waarde optellen bij waarde
        w3 = w1 - w2            waarde aftrekken van waarde
        w3 = w1 * w2            waarde vermenigvuldigen met waarde
        w3 = w1 / w2            waarde delen door waarde
        w2 = n * w1             getal vermenigvuldigen met waarde
        w2 = w1 * n             waarde vermenigvuldigen met getal
        w2 = n / w1             getal delen door waarde
        w2 = w1 / n             waarde delen door getal
        w2 = w1 ** n            waarde tot de macht een geheel getal
        w2 = abs(w1)            maakt waarde altijd positief
        w2 = +w1                behoud teken
        w2 = -w1                verander teken (positief vs. negatief)

    WAARDEN VERGELIJKEN         resulteert in een boolean (True/False)
        w1 == w2                is gelijk aan
        w1 == getal             de float() van waarde is gelijk aan getal
        w1 != w2                is niet gelijk aan
        w1 >  w2                is groter dan
        w1 <  w2                is kleiner dan
        w1 >= w2                is groter dan of gelijk aan
        w1 <= w2                is kleiner dan of gelijk aan
        w1 &  w2                eenheden zijn zelfde type
        
    WISKUNDIGE FUNCTIES         
        w.sin()                 sinus (alleen getallen en hoeken)
        w.cos()                 cosinus (alleen getallen en hoeken)
        w.tan()                 tangens (alleen getallen en hoeken)
        w.asin()                arcsinus (omgekeerde sin, alleen getallen)
        w.acos()                arccosinus (omgekeerde cos, alleen getallen)
        w.atan()                arctangens (omgekeerde tan, alleen getallen)
        w.sinh()                hyperbolische sinus (getallen en hoeken)
        w.cosh()                hyperbolische cosinus (getallen en hoeken)
        w.tanh()                hyperbolische tangens (getallen en hoeken)
        w.asinh()               arcsinus hyperb. (omgekeerde asinh, getallen)
        w.acosh()               arccosinus hyperb. (omgekeerde acosh, getallen)
        w.atanh()               arctangens hyperb. (omgekeerde atanh, getallen)
        w.afronden(n)           rond af op n decimalen (standaard 0)
        w.plafond()             rond af naar boven (geheel getal)
        w.vloer()               rond af naar beneden (geheel getal)
        w.plafond_0_vloer()     rond af richting 0 (geheel getal)
        w1.optellen(w2)         w1 + w2
        w1.aftrekken(w2)        w1 - w2
        w1.vermenigvuldigen(w2) w1 * w2
        w1.delen(w2)            w1 / w2
        w1.delen_aantal(w2)     afgerond naar beneden
        w1.delen_rest(w2)       restant na afronden naar beneden
        w.macht(n)              w ** n
        w.reciproke()           1 / w
        w.negatief()            -w
        w.exp()                 exponentieel: berekent e^w
        w.ln()                  natuurlijke logaritme (grondgetal e)
        w.log()                 logaritme met grondgetal 10
        w.wortel()              vierkantswortel
        w.wortel3()             kubieke wortel
        w.absoluut()            absolute waarde (altijd positief)
        w.teken()               positief getal: 1.0, nul: 0.0, negatief: -1.0 
        w.kopieer_teken(w2)     neem huidige, met het teken (+-) van w2
        w.is_positief(a)        stap functie: w<0 -> 0, w=0 -> a, w>0 -> 1 
        w.is_nan()              bepaalt of waarde een niet-getal is
        w.is_inf()              bepaalt of waarde oneindig is

    EENHEID TEKST
        gebruik getal achter standaard eenheid voor 'tot de macht' (bijv. mm3)
        gebruik / (maximaal één keer) om teller en noemer te introduceren
        gebruik * om eenheden te combineren (zowel in teller als noemer)
        bijvoorbeeld: "m3*kPa/s4*m"

    STANDAARD EENHEDEN          deze kan je combineren in een eenheid tekst
        dimensieloos            -
        massa                   ag fg pg ng mug mg cg g hg kg Mg Gg Tg Pg Eg
                                ton kton Mton ounce pound kip stone grain
        lengte                  am fm pm nm mum mm cm dm m dam hm km Mm Gm Tm
                                Pm Em in ft yard zeemijl mijl
        tijd                    as(.attos) fs ps ns mus ms cs ds s das hs ks
                                Ms Gs Ts Ps Es min(.minuut) h d j
        temperatuur             C K F  (als temperatuur in teller, samen met
                                andere eenheden, dan niet om te rekenen)
        hoek                    rad deg gon
        kracht                  N kN MN GN TN  (of massa*lengte/tijd^2)
        spanning                Pa kPa MPa GPa TPa  (of kracht/oppervlakte)
        moment                  Nm kNm MNm Nmm kNmm MNmm  (of kracht*lengte)
        oppervlakte             ca a ha  (of lengte^2)
        inhoud                  ml cl dl l dal hl kl gallon pint floz tbs tsp
                                bbl cup  (of lengte^3)

    BESCHIKBARE EIGENSCHAPPEN   voor snel toekennen van eenheid aan waarde
    <object>.<eigenschap>       bijvoorbeeld toekennen inhoud: w.dm3
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

    # hulp functie om lijst hierboven te gegeneren; hierna nog bepaalde eigenschappen/methodes verwijderen
    # from pyco.model import Waarde
    # ' '.join(sorted([a for a in dir(Waarde) if a[0] != '_' and a not in ['print_help']], key=lambda x:x.upper()))

    # factoren horende bij basiseenheden, om eenheidsbreuk samen te stellen
    # verschillende priemgetallen, zodat product een uniek resultaat geeft
    _BASIS = {
        'DIMENSIELOOS': 1,
        'MASSA': 2,
        'LENGTE': 3,
        'TIJD': 5,
        'TEMPERATUUR': 7,
        'HOEK': 11,
    }

    # unieke eenheidsbreuk dit hoort bij basis- en samengestelde eenheden
    _TYPE = {
        'DIMENSIELOOS': Fraction(
            _BASIS['DIMENSIELOOS']),
        'MASSA': Fraction(
            _BASIS['MASSA']),
        'LENGTE': Fraction(
            _BASIS['LENGTE']),
        'TIJD': Fraction(
            _BASIS['TIJD']),
        'TEMPERATUUR': Fraction(
            _BASIS['TEMPERATUUR']),
        'HOEK': Fraction(
            _BASIS['HOEK']),
        'KRACHT': Fraction(
            _BASIS['MASSA'] * _BASIS['LENGTE'],
            _BASIS['TIJD'] * _BASIS['TIJD']),
        'SPANNING': Fraction(
            _BASIS['MASSA'],
            _BASIS['TIJD'] * _BASIS['TIJD'] * _BASIS['LENGTE']),
        'MOMENT': Fraction(
            _BASIS['MASSA'] * _BASIS['LENGTE'] * _BASIS['LENGTE'],
            _BASIS['TIJD'] * _BASIS['TIJD']),
        'OPPERVLAKTE': Fraction(
            _BASIS['LENGTE'] * _BASIS['LENGTE']),
        'INHOUD': Fraction(
            _BASIS['LENGTE'] * _BASIS['LENGTE'] * _BASIS['LENGTE']),
    }

    # regexp om in naam van eenheid de letters van cijfers te scheiden
    _RE_NAAM_EENHEID = r'^([a-zA-Z\-]+)([0-9]*)$'

    _EENHEID = {
        # 'afkorting': (naam, breuk van basiseenheden, weegfactor)

        # bij niet standaard schaalbare eenheden:
        #   (naam, breuk van basiseenheden,
        #       (weegfunctie, weegfunctie-inverse, weegfunctie-noemerfactor))

        # de weegfactor voor standaard waarde van (niet samengestelde)
        #   basiseenheid MOET gelijk zijn aan 1 (een één: integer, geen float)

        #==============   basis eenheden  ===============

        # DIMENSIELOOS
        '-': ('dimensieloos', _TYPE['DIMENSIELOOS'], 1), # standaard

        # MASSA
        'ag': ('attogram', _TYPE['MASSA'], 1.0e-21),
        'fg': ('femtogram', _TYPE['MASSA'], 1.0e-18),
        'pg': ('picogram',  _TYPE['MASSA'], 1.0e-15),
        'ng': ('nanogram', _TYPE['MASSA'], 1.0e-12),
        'mug': ('mircogram', _TYPE['MASSA'], 1.0e-9),
        'mg': ('milligram', _TYPE['MASSA'], 1.0e-6),
        'cg': ('centigram', _TYPE['MASSA'], 1.0e-5),
        'dg': ('decigram', _TYPE['MASSA'], 1.0e-4),
        'g': ('gram', _TYPE['MASSA'], 1.0e-3),
        #'dag': ('decagram', _TYPE['MASSA'], 1.0e-2),
        'hg': ('hectogram', _TYPE['MASSA'], 1.0e-1),
        'kg': ('kilogram', _TYPE['MASSA'], 1), # standaard
        'Mg': ('megagram', _TYPE['MASSA'], 1.0e3),
        'Gg': ('gigagram', _TYPE['MASSA'], 1.0e6),
        'Tg': ('teragram', _TYPE['MASSA'], 1.0e9),
        'Pg': ('petagram', _TYPE['MASSA'], 1.0e12),
        'Eg': ('exagram', _TYPE['MASSA'], 1.0e15),
        'ton': ('ton', _TYPE['MASSA'], 1.0e3),
        'kton': ('kiloton', _TYPE['MASSA'], 1.0e6),
        'Mton': ('megaton', _TYPE['MASSA'], 1.0e9),
        'ounce': ('ounce', _TYPE['MASSA'], 0.0283495),
        'pound': ('pound', _TYPE['MASSA'], 0.453592),
        'kip': ('kilopound', _TYPE['MASSA'], 453.592),
        'stone': ('stone', _TYPE['MASSA'], 6.35029),
        'grain': ('grain', _TYPE['MASSA'], 0.0000647989),

        # LENGTE
        'am': ('attometer', _TYPE['LENGTE'], 1.0e-18),
        'fm': ('femtometer', _TYPE['LENGTE'], 1.0e-15),
        'pm': ('picometer', _TYPE['LENGTE'], 1.0e-12),
        'nm': ('nanometer', _TYPE['LENGTE'], 1.0e-9),
        'mum': ('micrometer', _TYPE['LENGTE'], 1.0e-6),
        'mm': ('millimeter', _TYPE['LENGTE'], 1.0e-3),
        'cm': ('centimeter', _TYPE['LENGTE'], 1.0e-2),
        'dm': ('decimeter', _TYPE['LENGTE'], 1.0e-1),
        'm': ('meter', _TYPE['LENGTE'], 1),  # standaard
        'dam': ('decameter', _TYPE['LENGTE'], 1.0e1),
        'hm': ('hectometer', _TYPE['LENGTE'], 1.0e2),
        'km': ('kilometer', _TYPE['LENGTE'], 1.0e3),
        'Mm': ('megameter', _TYPE['LENGTE'], 1.0e6),
        'Gm': ('gigameter', _TYPE['LENGTE'], 1.0e9),
        'Tm': ('terameter', _TYPE['LENGTE'], 1.0e12),
        'Pm': ('petameter', _TYPE['LENGTE'], 1.0e15),
        'Em': ('exameter', _TYPE['LENGTE'], 1.0e18),
        'in': ('inch (Waarde.inch)', _TYPE['LENGTE'], 0.0254000), # eigenschap 'in' niet mogelijk -> 'inch'
        'ft': ('feet', _TYPE['LENGTE'], 0.304800),
        'yard': ('yard', _TYPE['LENGTE'], 0.914400),
        'zeemijl': ('zeemijl', _TYPE['LENGTE'], 1852.00),
        'mijl': ('mijl', _TYPE['LENGTE'], 1609.34),

        # TIJD
        'as': ('attoseconde (Waarde.attos)', _TYPE['TIJD'], 1.0e-18), # eigenschap 'as' niet mogelijk -> 'attos'
        'fs': ('femtoseconde', _TYPE['TIJD'], 1.0e-15),
        'ps': ('picoseconde', _TYPE['TIJD'], 1.0e-12),
        'ns': ('nanoseconde', _TYPE['TIJD'], 1.0e-9),
        'mus': ('microseconde', _TYPE['TIJD'], 1.0e-6),
        'ms': ('milliseconde', _TYPE['TIJD'], 1.0e-3),
        'cs': ('centiseconde', _TYPE['TIJD'], 1.0e-2),
        'ds': ('deciseconde', _TYPE['TIJD'], 1.0e-1),
        's': ('seconde', _TYPE['TIJD'], 1),  # standaard
        'das': ('decaseconde', _TYPE['TIJD'], 1.0e1),
        'hs': ('hectoseconde', _TYPE['TIJD'], 1.0e2),
        'ks': ('kiloseconde', _TYPE['TIJD'], 1.0e3),
        'Ms': ('megaseconde', _TYPE['TIJD'], 1.0e6),
        'Gs': ('gigaseconde', _TYPE['TIJD'], 1.0e9),
        'Ts': ('teraseconde', _TYPE['TIJD'], 1.0e12),
        'Ps': ('petaseconde', _TYPE['TIJD'], 1.0e15),
        'Es': ('exaseconde', _TYPE['TIJD'], 1.0e18),
        'min': ('minuut (Waarde.minuut)', _TYPE['TIJD'], 60), # eigenschap 'min' niet mogelijk -> 'minuut'
        'h': ('uur', _TYPE['TIJD'], 3600),
        'd': ('dag', _TYPE['TIJD'], 24*3600),
        'j': ('jaar', _TYPE['TIJD'], 365*24*3600),

        # TEMPERATUUR
        'C': ('graden Celcius', _TYPE['TEMPERATUUR'], 1),  # standaard
        'K': ('graden Kelvin', _TYPE['TEMPERATUUR'],
              (lambda K: K - 273.15,
               lambda C: C + 273.15,
               1.0)),
        # 1 graad C warmer is 1 graad K warmer
        #   -> als temperatuur in noemer van eenheid
        # als temperatuur in teller (samen met andere eenheden),
        #   dan niet om te rekenen
        'F': ('graden Fahrenheit', _TYPE['TEMPERATUUR'],
              (lambda F: (F - 32) / 1.8,
               lambda C: 1.8 * C + 32,
               (1 / 1.8))),
        # 1 graad C warmer is 1.8 graden F warmer
        #   -> als temperatuur in noemer van eenheid
        # als temperatuur in teller (samen met andere eenheden),
        #   dan niet om te rekenen

        # HOEK
        'rad': ('radialen', _TYPE['HOEK'], 1),  # standaard
        'deg': ('graden', _TYPE['HOEK'], ((2 * math.pi) / 360)),
        'gon': ('gon', _TYPE['HOEK'], ((2 * math.pi) / 400)),


        # ==============   samengestelde eenheden  ===============

        # KRACHT  -->  t.o.v. 1 kg*m/s2 (= 1 N)
        'N': ('Newton', _TYPE['KRACHT'], 1),
        'kN': ('kiloNewton', _TYPE['KRACHT'], 1.0e3),
        'MN': ('megaNewton', _TYPE['KRACHT'], 1.0e6),
        'GN': ('gigaNewton', _TYPE['KRACHT'], 1.0e9),
        'TN': ('teraNewton', _TYPE['KRACHT'], 1.0e12),

        # SPANNING  -->  t.o.v. 1 kg/(m*s2) (= 1 N/m2)
        'Pa': ('Pascal', _TYPE['SPANNING'], 1.0),
        'kPa': ('kiloPascal', _TYPE['SPANNING'], 1.0e3),
        'MPa': ('megaPascal', _TYPE['SPANNING'], 1.0e6),
        'GPa': ('gigaPascal', _TYPE['SPANNING'], 1.0e9),
        'TPa': ('teraPascal', _TYPE['SPANNING'], 1.0e12),

        # MOMENT  -->  t.o.v. 1 kg*m2/s2 (= 1 N*m)
        'Nm': ('Newton meter', _TYPE['MOMENT'], 1.0),
        'kNm': ('kiloNewton meter', _TYPE['MOMENT'], 1.0e3),
        'MNm': ('megaNewton meter', _TYPE['MOMENT'], 1.0e6),
        'Nmm': ('Newton millimeter', _TYPE['MOMENT'], 1.0e-3),
        'kNmm': ('kiloNewton millimeter', _TYPE['MOMENT'], 1.0),
        'MNmm': ('megaNewton millimeter', _TYPE['MOMENT'], 1.0e3),

        # OPPERVLAKTE  -->  t.o.v. 1 m2
        'ca': ('centiare', _TYPE['OPPERVLAKTE'], 1.0),
        'a': ('are', _TYPE['OPPERVLAKTE'], 1.0e2),
        'ha': ('hectare', _TYPE['OPPERVLAKTE'], 1.0e4),

        # INHOUD  -->  t.o.v. 1 m3
        'ml': ('milliliter', _TYPE['INHOUD'], 1.0e-6),
        'cl': ('centiliter', _TYPE['INHOUD'], 1.0e-5),
        'dl': ('deciliter', _TYPE['INHOUD'], 1.0e-4),
        'l': ('liter', _TYPE['INHOUD'], 1.0e-3),
        'dal': ('decaliter', _TYPE['INHOUD'], 1.0e-2),
        'hl': ('hectoliter', _TYPE['INHOUD'], 1.0e-1),
        'kl': ('kiloliter', _TYPE['INHOUD'], 1.0),
        'gallon': ('gallon', _TYPE['INHOUD'], 0.00454609),
        'pint': ('pint', _TYPE['INHOUD'], 0.00056826125),
        'floz': ('fluid ounce', _TYPE['INHOUD'], 1.0e-5),
        'tbs': ('eetlepel (tablespoon)', _TYPE['INHOUD'], 1.5e-5),
        'tsp': ('theelepel (teaspoon)', _TYPE['INHOUD'], 5.0e-6),
        'bbl': ('olievat (oil barrel)', _TYPE['INHOUD'], 0.1589873),
        'cup': ('cup (metrisch)', _TYPE['INHOUD'], 0.00025),
    }

    _STANDAARD_AANTAL_DECIMALEN = 2
    _AFRONDEN_BIJ_VERGELIJKEN = 1e12

    def __init__(self, waarde: Union[int, float, str] = 0,
                 eenheid: Union[str, Fraction] = None, config:dict = None):
        super().__init__()

        if not (isinstance(waarde, int) or isinstance(waarde, float)):
            if isinstance(waarde, Waarde):
                if eenheid is None:
                    self._init_waarde_object_zonder_eenheid(waarde)
                else:
                    # omzetten van dimensieloze waarde naar een bepaalde eenheid
                    if isinstance(eenheid, Fraction):
                        self._init_waarde_object_eenheidbreuk(waarde, eenheid)
                    else:
                        if eenheid is None or eenheid == '':
                            eenheid = '-'
                        self._init_waarde_object_eenheidtekst(waarde, eenheid)
            else:
                self._init_waarde_tekst(str(waarde))
        elif isinstance(eenheid, Fraction):
            self._init_waarde_eenheidbreuk(waarde, eenheid)
        elif isinstance(eenheid, str):
            if eenheid is None or eenheid == '':
                eenheid = '-'
            self._init_waarde_eenheidtekst(waarde, eenheid)
        else:
            self._init_waarde_getal(waarde)

        if config is not None and isinstance(config, dict):
            self._config = config

    def _init_waarde_getal(self, waarde: Union[int, float]):
        """Initieert alleen een getal."""
        self._is_getal = True
        self._getal = float(waarde)
        self._eenheidbreuk = Fraction(1)
        self._config = {
            'standaard_eenheid': None,
            'aantal_decimalen': self._STANDAARD_AANTAL_DECIMALEN,
        }

    def _init_waarde_eenheidtekst(self, waarde: Union[int, float], eenheid: str):
        """Initieert een eenheid met tekst."""
        self._is_getal = True
        self.decimalen = self._STANDAARD_AANTAL_DECIMALEN
        self._getal, self._eenheidbreuk = self._bereken_nieuwe_waarde(eenheid, float(waarde))
        self._config = {
            'standaard_eenheid': eenheid if isinstance(eenheid, str) else '-',
            'aantal_decimalen': self._STANDAARD_AANTAL_DECIMALEN,
        }

    def _init_waarde_eenheidbreuk(self, waarde: Union[int, float], eenheid: Fraction):
        """Initieert een eenheid met Fraction breuk object."""
        self._is_getal = True
        self._getal = waarde
        self._eenheidbreuk = eenheid
        self._config = {
            'standaard_eenheid': None,
            'aantal_decimalen': self._STANDAARD_AANTAL_DECIMALEN,
        }

    def _init_waarde_object_eenheidtekst(self, waarde, eenheid: str):
        """Initieert getal met Waarde object en eenheid met tekst."""
        if not isinstance(waarde, Waarde):
            raise TypeError('waarde is niet van type Waarde')
        self._is_getal = True
        self._getal, self._eenheidbreuk = self._bereken_nieuwe_waarde(eenheid, waarde._getal)
        self._config = {
            'standaard_eenheid': None,
            'aantal_decimalen': self._STANDAARD_AANTAL_DECIMALEN,
        }

    def _init_waarde_object_eenheidbreuk(self, waarde, eenheid: Fraction):
        """Initieert getal met Waarde object en eenheid met Fraction breuk object."""
        if not isinstance(waarde, Waarde):
            raise TypeError('waarde is niet van type Waarde')
        self._is_getal = True
        self._eenheidbreuk = eenheid
        self._getal = waarde._export_waarde(self._eenheidnaam)
        self._config = {
            'standaard_eenheid': None,
            'aantal_decimalen': self._STANDAARD_AANTAL_DECIMALEN,
        }

    def _init_waarde_object_zonder_eenheid(self, waarde):
        """Initieert getal met Waarde object zonder eenheid."""
        if not isinstance(waarde, Waarde):
            raise TypeError('waarde is niet van type Waarde')
        self._is_getal = waarde._is_getal
        self._eenheidbreuk = waarde._eenheidbreuk
        self._getal = waarde._getal
        self._config = waarde._config

    def _init_waarde_tekst(self, waarde:str):
        self._is_getal = False
        self._getal = waarde
        self._eenheidbreuk = None
        self._config = {
            'standaard_eenheid': None,
            'aantal_decimalen': None,
        }

    @property
    def _eenheidnaam(self):
        """Genereert een naam voor eenheid op basis van eenheidbreuk."""

        def priem_BASIS(n):
            i = 2
            _BASIS = []
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    _BASIS.append(i)
            if n > 1:
                _BASIS.append(n)
            return tuple(_BASIS)
        
        def verbind_namen(namen):
            nieuwe_namen = []
            vorige_naam = None
            aantal_namen = 0
            for naam in namen:
                if vorige_naam is None:
                    vorige_naam = naam
                    aantal_namen = 1
                else:
                    if naam == vorige_naam:
                        aantal_namen += 1
                    else:
                        if aantal_namen > 1:
                            nieuwe_namen.append(vorige_naam + str(aantal_namen))
                        else:
                            nieuwe_namen.append(vorige_naam)
                        vorige_naam = naam
                        aantal_namen = 1
            if vorige_naam is not None:
                if aantal_namen > 1:
                    nieuwe_namen.append(vorige_naam + str(aantal_namen))
                else:
                    nieuwe_namen.append(vorige_naam)
            return '*'.join(nieuwe_namen)

        if not hasattr(self, '_eenheidbreuk'):
            self._eenheidbreuk = Fraction(1)

        evenredig__BASIS = priem_BASIS(self._eenheidbreuk.numerator)  # teller
        omgekeerd_evenredig__BASIS = priem_BASIS(self._eenheidbreuk.denominator)  # noemer
        evenredig_namen = []
        omgekeerd_evenredig_namen = []

        for factor in evenredig__BASIS:
            for eh_afk, eh_dict in self._EENHEID.items():
                if Fraction(factor) == eh_dict[1] and eh_dict[2] == 1:
                    evenredig_namen.append(eh_afk)
        for factor in omgekeerd_evenredig__BASIS:
            for eh_afk, eh_dict in self._EENHEID.items():
                if Fraction(factor) == eh_dict[1] and eh_dict[2] == 1:
                    omgekeerd_evenredig_namen.append(eh_afk)
        if evenredig_namen and omgekeerd_evenredig_namen:
            omgekeerd_evenredig_namen_str = verbind_namen(omgekeerd_evenredig_namen)
            if '*' in omgekeerd_evenredig_namen_str:
                return '{}/({})'.format(verbind_namen(evenredig_namen),
                                        omgekeerd_evenredig_namen_str)
            else:
                return '{}/{}'.format(verbind_namen(evenredig_namen), omgekeerd_evenredig_namen_str)
        elif evenredig_namen and not omgekeerd_evenredig_namen:
            return '{}'.format(verbind_namen(evenredig_namen))
        elif not evenredig_namen and omgekeerd_evenredig_namen:
            omgekeerd_evenredig_namen_str = verbind_namen(omgekeerd_evenredig_namen)
            if '*' in omgekeerd_evenredig_namen_str:
                return '1/({})'.format(omgekeerd_evenredig_namen_str)
            else:
                return '1/{}'.format(omgekeerd_evenredig_namen_str)
        elif not evenredig_namen and not omgekeerd_evenredig_namen:
            for eh_afk, eh_dict in self._EENHEID.items():
                if Fraction(self._BASIS['DIMENSIELOOS']) == eh_dict[1] and eh_dict[2] == 1:
                    return eh_afk

    def _bereken_nieuwe_waarde(self, eenheid, invoer_getal):
        """Genereert een interne waarde (getal) op basis van eenheid en invoergetal."""
        getal = invoer_getal
        if not isinstance(eenheid, str) or not eenheid:
            raise ValueError('eenheid moet een (niet leeg) stuk tekst zijn')
        eenheidbreuk = Fraction(1)
        breukonderdelen = eenheid.split('/')
        if len(breukonderdelen) > 2:
            raise ValueError('er mag maar één \'/\' in eenheid aanwezig zijn')
        teller = breukonderdelen[0]
        if teller == '1':
            teller = ''
        noemer = breukonderdelen[1].lstrip('(').rstrip(')') if len(breukonderdelen) > 1 else ''
        telleronderdelen = [onderdeel.strip() for onderdeel in teller.split('*')] if teller else []
        noemeronderdelen = [onderdeel.strip() for onderdeel in noemer.split('*')] if noemer else []
        for telleronderdeel in telleronderdelen:
            result = re.search(self._RE_NAAM_EENHEID, telleronderdeel)
            if result is None:
                if telleronderdeel == '1':
                    pass
                else:
                    raise ValueError('telleronderdeel van eenheid heeft ongeldige opmaak: \'{}\''.format(telleronderdeel))
            else:
                eenheid_naam = result.group(1)
                eenheid_aantal = int(result.group(2)) if result.group(2) else 1
                if not eenheid_naam in self._EENHEID:
                    raise ValueError('telleronderdeel van eenheid is onbekend: \'{}\''.format(eenheid_naam))
                for _ in range(eenheid_aantal):
                    weging = self._EENHEID[eenheid_naam][2]
                    if isinstance(weging, float) or isinstance(weging, int):
                        getal = getal * weging
                    elif isinstance(weging, tuple) and len(weging) == 3 \
                            and callable(weging[0]) and callable(weging[1]) \
                            and (isinstance(weging[2], float) or isinstance(weging[2], int)):
                        if len(telleronderdelen) > 1 or len(noemeronderdelen) > 0:
                            raise ValueError('de niet standaard schaalbare sub-eenheid \'{}\' kan enkel worden omgerekend in teller als het als enige onderdeel voorkomt in hele eenheid; in de noemer kan deze eenheid wel worden gecombineerd'.format(eenheid_naam))
                        getal = weging[0](getal)
                    else:
                        raise ValueError('weging basiseenheid heeft verkeerde syntax')
                    subeenheidfactor = self._EENHEID[eenheid_naam][1]
                    eenheidbreuk = eenheidbreuk * subeenheidfactor
        for noemeronderdeel in noemeronderdelen:
            result = re.search(self._RE_NAAM_EENHEID, noemeronderdeel)
            if result is None:
                raise ValueError('noemeronderdeel van eenheid heeft ongeldige opmaak: \'{}\''.format(noemeronderdeel))
            else:
                eenheid_naam = result.group(1)
                eenheid_aantal = int(result.group(2)) if result.group(2) else 1
                if not eenheid_naam in self._EENHEID:
                    raise ValueError('noemeronderdeel van eenheid is onbekend: \'{}\''.format(eenheid_naam))
                for _ in range(eenheid_aantal):
                    weging = self._EENHEID[eenheid_naam][2]
                    if isinstance(weging, float) or isinstance(weging, int):
                        getal = getal / weging
                    elif isinstance(weging, tuple) and len(weging) == 3 \
                            and callable(weging[0]) and callable(weging[1]) \
                            and (isinstance(weging[2], float) or isinstance(weging[2], int)):
                        weging_noemerfactor = weging[2]
                        getal = getal / weging_noemerfactor
                    else:
                        raise ValueError('weging basiseenheid heeft verkeerde syntax')
                    subeenheidfactor = self._EENHEID[eenheid_naam][1]
                    eenheidbreuk = eenheidbreuk / subeenheidfactor
        return getal, eenheidbreuk

    def _bereken_inverse_waarde(self, eenheid, oude_waarde, oude_eenheidbreuk, check_type=True):
        """Genereert een waarde (getal) op basis van een eenheid."""
        waarde = oude_waarde
        if not isinstance(eenheid, str) or not eenheid:
            raise ValueError('eenheid moet een (niet leeg) stuk tekst zijn')
        eenheidbreuk = Fraction(1)
        breukonderdelen = eenheid.split('/')
        if len(breukonderdelen) > 2:
            raise ValueError('er mag maar één \'/\' in eenheid aanwezig zijn')
        teller = breukonderdelen[0]
        noemer = breukonderdelen[1].lstrip('(').rstrip(')') if len(breukonderdelen) > 1 else ''
        telleronderdelen = [onderdeel.strip() for onderdeel in teller.split('*')] if teller else []
        noemeronderdelen = [onderdeel.strip() for onderdeel in noemer.split('*')] if noemer else []
        for telleronderdeel in telleronderdelen:
            result = re.search(self._RE_NAAM_EENHEID, telleronderdeel)
            if result is None:
                if telleronderdeel == '1':
                    pass
                else:
                    raise ValueError('telleronderdeel van eenheid heeft ongeldige opmaak: \'{}\''.format(telleronderdeel))
            else:
                eenheid_naam = result.group(1)
                eenheid_aantal = int(result.group(2)) if result.group(2) else 1
                if not eenheid_naam in self._EENHEID:
                    raise ValueError('telleronderdeel van eenheid is onbekend: \'{}\''.format(eenheid_naam))
                for _ in range(eenheid_aantal):
                    weging = self._EENHEID[eenheid_naam][2]
                    if isinstance(weging, float) or isinstance(weging, int):
                        waarde = waarde / weging
                    elif isinstance(weging, tuple) and len(weging) == 3 \
                            and callable(weging[0]) and callable(weging[1]) \
                            and (isinstance(weging[2], float) or isinstance(weging[2], int)):
                        if len(telleronderdelen) > 1 or len(noemeronderdelen) > 0:
                            raise ValueError('de niet standaard schaalbare sub-eenheid \'{}\' kan enkel worden omgerekend in teller als het als enige onderdeel voorkomt in hele eenheid; in de noemer kan deze eenheid wel worden gecombineerd'.format(eenheid_naam))
                        inverse_weging = weging[1]
                        waarde = inverse_weging(waarde)
                    else:
                        raise ValueError('weging basiseenheid heeft verkeerde syntax')
                    subeenheidfactor = self._EENHEID[eenheid_naam][1]
                    eenheidbreuk = eenheidbreuk * subeenheidfactor
        for noemeronderdeel in noemeronderdelen:
            result = re.search(self._RE_NAAM_EENHEID, noemeronderdeel)
            if result is None:
                raise ValueError('noemeronderdeel van eenheid heeft ongeldige opmaak: \'{}\''.format(noemeronderdeel))
            else:
                eenheid_naam = result.group(1)
                eenheid_aantal = int(result.group(2)) if result.group(2) else 1
                if not eenheid_naam in self._EENHEID:
                    raise ValueError('noemeronderdeel van eenheid is onbekend: \'{}\''.format(eenheid_naam))
                for _ in range(eenheid_aantal):
                    weging = self._EENHEID[eenheid_naam][2]
                    if isinstance(weging, float) or isinstance(weging, int):
                        waarde = waarde * weging
                    elif isinstance(weging, tuple) and len(weging) == 3 \
                            and callable(weging[0]) and callable(weging[1]) \
                            and (isinstance(weging[2], float) or isinstance(weging[2], int)):
                        weging_noemerfactor = weging[2]
                        waarde = waarde * weging_noemerfactor
                    else:
                        raise ValueError('weging basiseenheid heeft verkeerde syntax')
                    subeenheidfactor = self._EENHEID[eenheid_naam][1]
                    eenheidbreuk = eenheidbreuk / subeenheidfactor
        if check_type and eenheidbreuk != oude_eenheidbreuk:
            raise ValueError('type eenheid \'{}\' komt niet overeen met type eenheid van waarde \'{}\''.format(eenheid, self._eenheidnaam))
        return waarde

    def _export_waarde(self, eenheid=None, check_type=True):
        """Exporteert interne waarde (getal) gegeven een eenheid."""
        if eenheid is None or eenheid == '' or eenheid == '-':
            return self._getal
        else:
            return self._bereken_inverse_waarde(eenheid, self._getal, self._eenheidbreuk, check_type)

    def _verander_aantal_decimalen(self, decimalen:int):
        """Helper functie voor eigenschappen qua standaard eenheid."""
        if not isinstance(decimalen, int):
            raise ValueError('aantal decimalen is geen geheel getal')
        self._config['aantal_decimalen'] = decimalen
        return self

    def _verander_eenheid(self, eenheid:str, check_type:bool=True):
        """Helper functie voor eigenschappen qua afronding."""
        if not self._is_getal:
            raise ValueError('huide waarde is geen getal: {}'.format(self._getal))
        if self._eenheidbreuk == Fraction(1):
            # waarde was dimensieloos; dan mogelijk om eenheid te veranderen
            self.__init__(self._getal, eenheid)
        else:
            # waarde had een bepaalde eenheid; moet zelfde soort blijven
            tmp = Waarde(1.0, eenheid)
            if check_type and tmp._eenheidbreuk != self._eenheidbreuk:
                raise ValueError('huidig type eenheid ({}) komt niet overeen met nieuwe eenheid ({})'.format(self._eenheidbreuk, tmp._eenheidbreuk))
            self.__init__(self._export_waarde(eenheid, check_type), eenheid)
        # # return een kopie van object (en niet verandering van object zelf)
        # kopie = type(self)(*tuple(self), config=self._config)
        return self

    @property
    def eenheid(self):
        """Geeft eenheid van Waarde. 'None' als geen eenheid."""
        if 'standaard_eenheid' in self._config \
                and self._config['standaard_eenheid'] is not None \
                and self._config['standaard_eenheid'] != '' \
                and self._config['standaard_eenheid'] != '-':
            waarde_eenheid = self._config['standaard_eenheid']
        elif self._is_getal and self._eenheidbreuk != Fraction(1):
            waarde_eenheid = self._eenheidnaam
        else:
            waarde_eenheid = ''
        waarde_eenheid = None if waarde_eenheid == '' else waarde_eenheid
        return waarde_eenheid

    @eenheid.setter
    def eenheid(self, nieuwe_eenheid:str):
        """Zet Waarde om naar nieuwe eenheid."""
        self._verander_eenheid(nieuwe_eenheid)
    
    def gebruik_eenheid(self, nieuwe_eenheid:str, check_type:bool=True):
        """Zet om naar nieuwe eenheid en retourneert object."""
        self._verander_eenheid(nieuwe_eenheid, check_type)
        return self
    
    def eh(self, nieuwe_eenheid:str, check_type:bool=True):
        """Zet om naar nieuwe eenheid en retourneert object."""
        self._verander_eenheid(nieuwe_eenheid, check_type)
        return self
    
    def kopie(self):
        """Retourneert een kopie van deze waarde (ander object)."""
        return type(self)(*tuple(self), config=self._config)
    
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
    
    def optellen(self, w):
        """Tel andere waarde op bij deze waarde"""
        from pyco import optellen
        return optellen(self, w)
    
    def aftrekken(self, w):
        """Haal andere waarde af van deze waarde"""
        from pyco import aftrekken
        return aftrekken(self, w)
    
    def vermenigvuldigen(self, w):
        """Vermenigvuldig andere waarde met deze waarde"""
        from pyco import vermenigvuldigen
        return vermenigvuldigen(self, w)
    
    def delen(self, w):
        """Deel waarde door een andere gegeven waarde"""
        from pyco import delen
        return delen(self, w)
    
    def delen_aantal(self, w):
        """Deel waarde door een andere gegeven waarde en rond af naar beneden"""
        from pyco import delen_aantal
        return delen_aantal(self, w)
    
    def delen_rest(self, w):
        """Deel waarde door een andere gegeven waarde, rond af naar beneden en retourneer het restant"""
        from pyco import delen_rest
        return delen_rest(self, w)
    
    def macht(self, n):
        """Bereken deze waarde tot een bepaalde macht (geheel getal)"""
        from pyco import macht
        return macht(self, n)
    
    def reciproke(self):
        """Bereken de reciproke (1/x)"""
        from pyco import reciproke
        return reciproke(self)
    
    def negatief(self):
        """Maak van positieve waarde een negatieve en vice versa"""
        from pyco import negatief
        return negatief(self)
    
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
    
    def wortel(self):
        """Berekent vierkantswortel."""
        if self._getal < 0:
            raise ValueError('Negatieve waarde is bij wortel niet toegestaan')
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
    
    def is_nan(self):
        """Bepaalt of waarde een niet-getal is (not a number: pc.nan)."""
        from pyco import is_nan
        return is_nan(self)
    
    def is_inf(self):
        """Bepaalt of waarde oneindig groot is. (pc.inf)"""
        from pyco import is_inf
        return is_inf(self)
    
        
    
    #-----------------------------------------------------------------------------

    def __add__(self, andere_waarde):
        """Telt twee waarden bij elkaar op."""
        return self.optellen(andere_waarde)

    def __sub__(self, andere_waarde):
        """Trekt waarde van andere waarde af."""
        return self.aftrekken(andere_waarde)

    def __mul__(self, andere_waarde):
        """Vermenigvuldigt waarde met andere waarde of getal."""
        return self.vermenigvuldigen(andere_waarde)

    def __truediv__(self, andere_waarde):
        """Deelt waarde door andere waarde of getal."""
        return self.delen(andere_waarde)

    def __pow__(self, macht):
        """Doet waarde tot de macht een andere waarde (geheel getal)."""
        return self.macht(macht)

    def __rmul__(self, scalar):
        """Vermenigvuldigt getal met waarde."""
        return self.vermenigvuldigen(scalar)

    def __rtruediv__(self, scalar):
        """Deelt getal met waarde."""
        return self.delen(scalar)

    def __eq__(self, andere_waarde):
        """Vergelijkt waarde met andere waarde: =="""
        if not isinstance(andere_waarde, Waarde):
            if (isinstance(andere_waarde, int)
                     or isinstance(andere_waarde, float)):
                return round(float(self)*self._AFRONDEN_BIJ_VERGELIJKEN) == round(float(andere_waarde)*self._AFRONDEN_BIJ_VERGELIJKEN)
            else:
                raise TypeError('term is niet van type Waarde, int of float')
        if self._eenheidbreuk != andere_waarde._eenheidbreuk:
            return False
        if self._is_getal:
            return round(self._getal*self._AFRONDEN_BIJ_VERGELIJKEN) == round(andere_waarde._getal*self._AFRONDEN_BIJ_VERGELIJKEN)
        else:
            return self._getal == andere_waarde._getal

    def __ne__(self, andere_waarde):
        """Vergelijkt waarde met andere waarde: !="""
        return not self.__eq__(andere_waarde)

    def __lt__(self, andere_waarde):
        """Vergelijkt waarde met andere waarde: <"""
        if not isinstance(andere_waarde, Waarde):
            if (isinstance(andere_waarde, int)
                     or isinstance(andere_waarde, float)):
                return float(self) < andere_waarde
            else:
                raise TypeError('term is niet van type Waarde')
        if self._eenheidbreuk != andere_waarde._eenheidbreuk:
            raise TypeError('eenheden zijn niet zelfde type: {}, {}'.format(
                self._eenheidnaam, andere_waarde._eenheidnaam))
        return self._getal < andere_waarde._getal

    def __gt__(self, andere_waarde):
        """Vergelijkt waarde met andere waarde: >"""
        if not isinstance(andere_waarde, Waarde):
            if (isinstance(andere_waarde, int)
                     or isinstance(andere_waarde, float)):
                return float(self) > andere_waarde
            else:
                raise TypeError('term is niet van type Waarde')
        if self._eenheidbreuk != andere_waarde._eenheidbreuk:
            raise TypeError('eenheden zijn niet zelfde type: {}, {}'.format(
                self._eenheidnaam, andere_waarde._eenheidnaam))
        return self._getal > andere_waarde._getal

    def __le__(self, andere_waarde):
        """Vergelijkt waarde met andere waarde: <="""
        return self.__lt__(andere_waarde) or self.__eq__(andere_waarde)

    def __ge__(self, andere_waarde):
        """Vergelijkt waarde met andere waarde: >="""
        return self.__gt__(andere_waarde) or self.__eq__(andere_waarde)

    def __and__(self, andere_waarde):
        """Vergelijkt eenheden of deze zelfde type zijn."""
        return self._eenheidbreuk == andere_waarde._eenheidbreuk

    def __float__(self):
        """Zet waarde om een float object gebruik makend van standaard eenheid."""
        if 'standaard_eenheid' in self._config \
                and self._config['standaard_eenheid'] is not None \
                and self._config['standaard_eenheid'] != '' \
                and self._config['standaard_eenheid'] != '-':
            # wel een standaard eenheid
            return float(self._export_waarde(self._config['standaard_eenheid']))
        elif self._is_getal and self._eenheidbreuk != Fraction(1):
            # geen standaard eenheid maar wel een dimensie
            return float(self._export_waarde(self._eenheidnaam))
        else:
            # geen eenheid
            if self._is_getal:
                return float(self._getal)
            else:
                raise ValueError('waarde is geen getal: {}'.format(self._getal))

    def __abs__(self):
        """Absolute waarde: zet negatieve waarden om naar positief."""
        if self._is_getal:
            self._getal = abs(self._getal)
        return self

    def __pos__(self):
        """Behoud teken (positief = positief, negatief = negatief)."""
        return self

    def __neg__(self):
        """Verander teken (positief = negatief, negatief = postief)."""
        return self.negatief()

    def __bool__(self):
        """Genereert een boolean. False wanneer getal 0 of lege tekst."""
        if self._getal == '':
            return False
        elif isinstance(self._getal, str):
            return True
        return not (self._getal < 1/self._AFRONDEN_BIJ_VERGELIJKEN and self._getal > -1/self._AFRONDEN_BIJ_VERGELIJKEN)

    def __iter__(self):
        """Itereert over het getal/tekst en de eenheidtekst."""
        waarde_getal = float(self) if self._is_getal else self._getal
        waarde_eenheid = self.eenheid

        return (x for x in (waarde_getal, waarde_eenheid))

    def __len__(self):
        """Lengte is altijd 2. Twee iter elementen: het getal/tekst en de eenheidtekst."""
        return 2

    def __getitem__(self, param:Union[int, str]):
        """Aanpassen van standaard eenheid of afronding."""
        if isinstance(param, int):
            return self._verander_aantal_decimalen(param)
        elif isinstance(param, str):
            return self._verander_eenheid(param)
        else:
            return self

    def __format__(self, config:str=None):
       """Geeft tekst met geformatteerd getal en eenheid."""
       if config is None:
           return str(self)
       if self._is_getal:
           waarde_getal, waarde_eenheid = tuple(self)
           format_str = '{:' + config + '} {}'
           return format_str.format(waarde_getal,
                            waarde_eenheid).strip().split(' None', 1)[0]
       else:
           waarde_getal, _ = tuple(self)
           format_str = '{:' + config + '}'
           return format_str.format(waarde_getal)

    def __repr__(self):
        """Geeft representatie object."""
        cls_naam = type(self).__name__
        if self._is_getal:
            getal, eenheid = tuple(self)
            eenheid = '' if eenheid is None else eenheid
            if eenheid:
                return '{}({}, \'{}\')'.format(cls_naam, getal, eenheid)
            else:
                return '{}({})'.format(cls_naam, getal)
        else:
            return '{}(\'{}\')'.format(cls_naam, self._getal)

    def __str__(self):
        """Geeft tekst met getal en eenheid."""
        if self._is_getal:
            waarde_getal, waarde_eenheid = tuple(self)
            waarde_eenheid = '' if waarde_eenheid is None else waarde_eenheid
            if 'aantal_decimalen' in self._config \
                    and self._config['aantal_decimalen'] is not None:
                format_str = '{:.' + str(self._config['aantal_decimalen']) + 'f} {}'
            else:
                format_str = '{:.' + str(self._STANDAARD_AANTAL_DECIMALEN) + 'f} {}'
            return format_str.format(waarde_getal, waarde_eenheid).strip()
        else:
            return self._getal

    # AANTAL DECIMALEN

    @property
    def _0(self):
        return self._verander_aantal_decimalen(0)

    @property
    def _1(self):
        return self._verander_aantal_decimalen(1)

    @property
    def _2(self):
        return self._verander_aantal_decimalen(2)

    @property
    def _3(self):
        return self._verander_aantal_decimalen(3)

    @property
    def _4(self):
        return self._verander_aantal_decimalen(4)

    @property
    def _5(self):
        return self._verander_aantal_decimalen(5)

    @property
    def _6(self):
        return self._verander_aantal_decimalen(6)

    @property
    def _7(self):
        return self._verander_aantal_decimalen(7)

    @property
    def _8(self):
        return self._verander_aantal_decimalen(8)

    @property
    def _9(self):
        return self._verander_aantal_decimalen(9)

    
    
###############################################################################
#  ALLES HIERONDER MOET ZELFDE ZIJN ALS BIJ LIJST OBJECT
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
