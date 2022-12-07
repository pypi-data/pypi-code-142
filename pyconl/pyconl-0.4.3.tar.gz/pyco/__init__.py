# afhankelijke externe bibliotheken
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


###############################################################################


import pyco.basis
BasisObject = pyco.basis.BasisObject

import pyco.waarde
Waarde = pyco.waarde.Waarde

import pyco.lijst
Lijst = pyco.lijst.Lijst

import pyco.data
Data = pyco.data.Data

import pyco.knoop
Knoop = pyco.knoop.Knoop

import pyco.lijn
Lijn = pyco.lijn.Lijn

import pyco.vorm
Vorm = pyco.vorm.Vorm

if True:
    import pyco.rechthoek
    Rechthoek = pyco.rechthoek.Rechthoek

    import pyco.cirkel
    Cirkel = pyco.cirkel.Cirkel
    
import pyco.venster
TekstVenster = pyco.venster.TekstVenster
FiguurVenster = pyco.venster.FiguurVenster
BestandsnaamVenster = pyco.venster.BestandsnaamVenster

import pyco.figuur
Figuur = pyco.figuur.Figuur

import pyco.materiaal
Materiaal = pyco.materiaal.Materiaal


###############################################################################


def functies_print_help():
    print("""
    
+-------------------------------------------+
|  algemene pyco functies en eigenschappen  |
+-------------------------------------------+

ALGEMEEN GEBRUIK VAN FUNCTIES         alle namen met () erachter zijn functies
    pc.wortel(9) == 3.0               direct aan te roepen vanuit pc object
    
ALGEMEEN GEBRUIK VAN EIGENSCHAPPEN
    pc.pi == 3.141592653589793        direct aan te roepen vanuit pc object

WISKUNDIGE FUNCTIES                   (geïmporteerd uit Numpy module)
    invoerwaarden:  int, float, np.array, Waarde of Lijst
    sin(x)                            sinus
    cos(x)                            cosinus
    tan(x)                            tangens
    asin(x)                           arcsinus (omgekeerde sin)
    acos(x)                           arccosinus (omgekeerde cos)
    atan(x)                           arctangens (omgekeerde tan)
    hypot(a, b)                       hypotenuse (c in: a^2 + b^c = c^2)
    graden(rad)                       van radialen naar graden
    radialen(deg)                     van graden naar radialen
    sinh(x)                           hyperbolische sinus
    cosh(x)                           hyperbolische cosinus
    tanh(x)                           hyperbolische tangens
    asinh(x)                          arc hyperb. sinus (omgekeerde sinh)
    acosh(x)                          arc hyperb. cosinus (omgekeerde cosh)
    atanh(x)                          arc hyperb. tangens (omgekeerde tanh)
    afronden(x, n)                    rond af op n decimalen (standaard 0)
    plafond(x)                        rond af naar boven (geheel getal)
    vloer(x)                          rond af naar beneden (geheel getal)
    plafond_0_vloer(x)                rond af richting 0 (geheel getal)
    som(lijst)                        de som van de elementen
    product(lijst)                    het product van de elementen
    verschil(lijst)                   lijst met verschillen tussen elementen
    optellen(a, b)                    a + b
    aftrekken(a, b)                   a - b
    vermenigvuldigen(a, b)            a * b
    delen(a, b)                       a / b
    delen_aantal(a, b)                delen afgerond naar beneden
    delen_rest(a, b)                  restant na afronden naar beneden
    macht(a, n)                       a ** n
    reciproke(x)                      1 / x
    negatief(x)                       -x
    kruisproduct(lijst_a, lijst_b)    a x b: staat loodrecht op vector a en b
    inwendigproduct(lijst_a, lijst_b) a . b: is |a| * |b| * cos(theta)
    exp(x)                            exponentieel: berekent e^x
    ln(x)                             natuurlijke logaritme (grondgetal e)
    log(x)                            logaritme met grondgetal 10
    kleinste_gemene_veelvoud(a, b)    kleinste gemene veelvoud: a=12 b=20: 60
    grootste_gemene_deler(a, b)       grootste gemene deler: a=12 b=20: 4
    min(lijst)                        bepaalt minimum waarde lijst
    max(lijst)                        bepaalt maximum waarde lijst
    bijsnijden(lijst, min, max)       snij alle elementen af tot minmax bereik
    wortel(x)                         vierkantswortel
    wortel3(x)                        kubieke wortel
    absoluut(x)                       absolute waarde (altijd positief)
    teken(x)                          positief getal: 1.0   negatief: -1.0 
    kopieer_teken(a, b)               neem getal a, met het teken (+-) van b
    is_positief(a, b)                 stap functie:a<0 -> 0, a=0 -> b, a>0 -> 1 
    verwijder_nan(lijst)              verwijder niet-getallen (not a number)
    getal_nan_inf(lijst)              vervang: nan=0, inf=1.7e+308 (heel groot)
    interpoleer(x, array_x, array_y)  interpoleer x in y; array_x MOET oplopen
    van_totmet_n(van, tot_met, n)     genereert vast aantal getallen (incl. t/m)
    van_tot_stap(van, tot, stap)      genereert vaste stappen (excl. tot)
    gemiddelde(lijst)                 bepaalt het gemiddelde
    stdafw_pop(lijst)                 bepaalt standaardafwijking voor populatie
    stdafw_n(lijst)                   bepaalt standaardafwijking steekproef
    mediaan(lijst)                    bepaalt de mediaan
    percentiel(lijst, percentage)     percentage getal tussen 0 en 100
    correlatie(lijst_a, lijst_b)      bepaalt correlatie matrix
    sorteer(lijst)                    sorteert een lijst van klein naar groot
    omdraaien(lijst)                  draai de volgorde van de lijst om
    is_nan(x)                         bepaalt of waarde een niet-getal is
    is_inf(x)                         bepaalt of waarde oneindig is
    gelijk(lijst_a, lijst_b)          per element kijken of waarden gelijk zijn
    niet_gelijk(lijst_a, lijst_b)     per element kijken of waarden gelijk verschillen
    groter(lijst_a, lijst_b)          per element kijken of waarde groter dan
    groter_gelijk(lijst_a, lijst_b)   idem, maar dan ook gelijk
    kleiner(lijst_a, lijst_b)         per element kijken of waarde kleiner dan
    kleiner_gelijk(lijst_a, lijst_b)  idem, maar dan ook gelijk
    alle(lijst)                       kijkt of alle elementen True zijn
    sommige(lijst)                    kijkt of er minimaal 1 element True is
    niet_alle(lijst)                  kijkt of er minimaal 1 element False is
    geen(lijst)                       kijkt of alle elementen False zijn
    of(a, b)                          kijkt of a of b True is
    en(a, b)                          kijkt of a en b True is
    niet(x)                           omdraaien van True naar False en andersom
    xof(a, b)                         True als a of b True is, en niet beide
    
WISKUNDIGE EIGENSCHAPPEN              (gebaseerd op Numpy module)
    nan                               float die geen getal is (not a number)
    inf                               oneindig groot
    pi                                3.141592653589793
    e                                 2.718281828459045

    """.strip())
    
    
###############################################################################

# eigenschappen

nan = np.nan
inf = np.inf
pi = np.pi
e = np.e

    
###############################################################################
    
# functies

_numpy_functions = dict(
    # tuple(n_args, fn, check_type_eenheid, pre_verander_eenheid_fn, post_verander_eenheid_fn, maak_bool)
    sin = (1, np.sin, 'deg', lambda eh, _: 'rad', lambda eh, _: None),
    cos = (1, np.cos, 'deg', lambda eh, _: 'rad', lambda eh, _: None),
    tan = (1, np.tan, 'deg', lambda eh, _: 'rad', lambda eh, _: None),
    asin = (1, np.arcsin, '-', None, lambda eh, _: 'rad'),
    acos = (1, np.arccos, '-', None, lambda eh, _: 'rad'),
    atan = (1, np.arctan, '-', None, lambda eh, _: 'rad'),
    hypot = (2, np.hypot), 
    graden = (1, np.degrees, '-', None, None),
    radialen = (1, np.radians, '-', None, None),
    sinh = (1, np.sinh, 'deg', lambda eh, _: 'rad', lambda eh, _: None),
    cosh = (1, np.cosh, 'deg', lambda eh, _: 'rad', lambda eh, _: None),
    tanh = (1, np.tanh, 'deg', lambda eh, _: 'rad', lambda eh, _: None),
    asinh = (1, np.arcsinh, '-', None, lambda eh, _: 'rad'),
    acosh = (1, np.arccosh, '-', None, lambda eh, _: 'rad'),
    atanh = (1, np.arctanh, '-', None, lambda eh, _: 'rad'),
    afronden = (2, np.round),
    plafond = (1, np.ceil),
    vloer = (1, np.floor),
    plafond_0_vloer = (1, np.fix),
    som = (1, np.sum),
    product = (1, np.prod),
    verschil = (1, np.diff),
    optellen = (2, np.add),
    aftrekken = (2, np.subtract),
    vermenigvuldigen = (2, np.multiply, None,
        lambda eh, _: Waarde(1, (Waarde(1, eh)._eenheidbreuk), config=None).eenheid,           
        lambda eh, args: (
            Waarde(1, (Waarde(1, args[0].eenheid)._eenheidbreuk)*(Waarde(1, args[1].eenheid)._eenheidbreuk), config=None).eenheid 
            if (isinstance(args[0], Waarde) and isinstance(args[1], Waarde))
                  or (isinstance(args[0], Lijst) and isinstance(args[1], Lijst))
            else '@' + eh if eh is not None else None  # @: eenheid naar origineel terugzetten
        )
    ),
    delen = (2, np.divide, None,
        lambda eh, _: Waarde(1, (Waarde(1, eh)._eenheidbreuk), config=None).eenheid,           
        lambda eh, args: (# Waarde/Lijst delen door Waarde/Lijst
              Waarde(1, (Waarde(1, args[0].eenheid)._eenheidbreuk)/(Waarde(1, args[1].eenheid)._eenheidbreuk), config=None).eenheid
              if (isinstance(args[0], Waarde) and isinstance(args[1], Waarde))
                  or (isinstance(args[0], Lijst) and isinstance(args[1], Lijst))
              else (
                  # Waarde/Lijst delen door getal
                  args[0].eenheid
                  if sum(isinstance(args[0], t) for t in (Waarde, Lijst))
                     and not sum(isinstance(args[1], t) for t in (Waarde, Lijst))
                  else (
                      # getal delen door Waarde/Lijst
                      Waarde(1, 1/(Waarde(1, args[1].eenheid)._eenheidbreuk), config=None).eenheid
                      if not sum(isinstance(args[0], t) for t in (Waarde, Lijst))
                          and sum(isinstance(args[1], t) for t in (Waarde, Lijst))
                      else
                          # getal delen door getal
                          None
             )))
    ),
    delen_aantal = (2, np.floor_divide, None,
        lambda eh, _: Waarde(1, (Waarde(1, eh)._eenheidbreuk), config=None).eenheid,           
        lambda eh, args: (# Waarde/Lijst delen door Waarde/Lijst
             Waarde(1, (Waarde(1, args[0].eenheid)._eenheidbreuk)/(Waarde(1, args[1].eenheid)._eenheidbreuk), config=None).eenheid
             if (isinstance(args[0], Waarde) and isinstance(args[1], Waarde))
                 or (isinstance(args[0], Lijst) and isinstance(args[1], Lijst))
             else (
                 # Waarde/Lijst delen door getal
                 args[0].eenheid
                 if sum(isinstance(args[0], t) for t in (Waarde, Lijst))
                    and not sum(isinstance(args[1], t) for t in (Waarde, Lijst))
              else (
                  # getal delen door Waarde/Lijst
                     Waarde(1, 1/(Waarde(1, args[1].eenheid)._eenheidbreuk), config=None).eenheid
                     if not sum(isinstance(args[0], t) for t in (Waarde, Lijst))
                         and sum(isinstance(args[1], t) for t in (Waarde, Lijst))
                     else
                         # getal delen door getal
                         None
            )))
    ),
    delen_rest = (2, np.remainder, None,
        lambda eh, _: Waarde(1, (Waarde(1, eh)._eenheidbreuk), config=None).eenheid,           
        lambda eh, args: (# Waarde/Lijst delen door Waarde/Lijst
             Waarde(1, (Waarde(1, args[0].eenheid)._eenheidbreuk)/(Waarde(1, args[1].eenheid)._eenheidbreuk), config=None).eenheid
             if (isinstance(args[0], Waarde) and isinstance(args[1], Waarde))
                 or (isinstance(args[0], Lijst) and isinstance(args[1], Lijst))
             else (
                 # Waarde/Lijst delen door getal
                 args[0].eenheid
                 if sum(isinstance(args[0], t) for t in (Waarde, Lijst))
                    and not sum(isinstance(args[1], t) for t in (Waarde, Lijst))
              else (
                  # getal delen door Waarde/Lijst
                     Waarde(1, 1/(Waarde(1, args[1].eenheid)._eenheidbreuk), config=None).eenheid
                     if not sum(isinstance(args[0], t) for t in (Waarde, Lijst))
                         and sum(isinstance(args[1], t) for t in (Waarde, Lijst))
                     else
                         # getal delen door getal
                         None
            )))
    ),
    macht = (2, np.power, None, 
        lambda eh, _: Waarde(1, (Waarde(1, eh)._eenheidbreuk), config=None).eenheid,
        lambda eh, args: Waarde(1, (Waarde(1, eh)._eenheidbreuk)**args[1], config=None).eenheid
    ),
    reciproke = (1, np.reciprocal, None,
        lambda eh, _: Waarde(1, (Waarde(1, eh)._eenheidbreuk), config=None).eenheid,
        lambda eh, args: Waarde(1, (1/Waarde(1, eh)._eenheidbreuk), config=None).eenheid),
    negatief = (1, np.negative, None, lambda eh, _: eh, lambda eh, _: eh),
    kruisproduct = (2, np.cross, None,
        lambda eh, _: Waarde(1, (Waarde(1, eh)._eenheidbreuk), config=None).eenheid,           
        lambda eh, args: (
            Waarde(1, (Waarde(1, args[0].eenheid)._eenheidbreuk)*(Waarde(1, args[1].eenheid)._eenheidbreuk), config=None).eenheid 
            if (isinstance(args[0], Waarde) and isinstance(args[1], Waarde))
                  or (isinstance(args[0], Lijst) and isinstance(args[1], Lijst))
            else '@' + eh if eh is not None else None  # @: eenheid naar origineel terugzetten
        )
    ),
    inwendigproduct = (2, np.dot, None,
        lambda eh, _: Waarde(1, (Waarde(1, eh)._eenheidbreuk), config=None).eenheid,           
        lambda eh, args: (
            Waarde(1, (Waarde(1, args[0].eenheid)._eenheidbreuk)*(Waarde(1, args[1].eenheid)._eenheidbreuk), config=None).eenheid 
            if (isinstance(args[0], Waarde) and isinstance(args[1], Waarde))
                  or (isinstance(args[0], Lijst) and isinstance(args[1], Lijst))
            else '@' + eh if eh is not None else None  # @: eenheid naar origineel terugzetten
        )
    ),
    exp = (1, np.exp, None, None, lambda eh, _: None),
    ln = (1, np.log, None, None, lambda eh, _: None),
    log = (1, np.log10, None, None, lambda eh, _: None),
    kleinste_gemene_veelvoud = (2, np.lcm, None, None, lambda eh, _: None),
    grootste_gemene_deler = (2, np.gcd, None, None, lambda eh, _: None),
    bijsnijden = (3, np.clip),
    wortel = (1, np.sqrt, None, None, lambda eh, _: None),
    wortel3 = (1, np.cbrt, None, None, lambda eh, _: None),
    absoluut = (1, np.absolute),
    teken = (1, np.sign, None, None, lambda eh, _: None),
    kopieer_teken = (2, np.copysign),
    is_positief = (2, np.heaviside, None, None, lambda eh, _: None),
    getal_nan_inf = (1, np.nan_to_num),
    verwijder_nan = (1, lambda x: x[np.logical_not(np.isnan(x))]),
    interpoleer = (3, np.interp),
    van_totmet_n = (3, np.linspace),
    van_tot_stap = (3, np.arange),
    gemiddelde = (1, np.mean),
    stdafw_pop = (1, lambda x: np.std(x, ddof=0)),
    stdafw_n = (1, lambda x: np.std(x, ddof=1)),
    mediaan = (1, np.median),
    percentiel = (2, np.percentile),
    correlatie = (2, lambda l1, l2: np.corrcoef(l1, l2)[0, 1], None, None, lambda eh, _: None),
    sorteer = (1, np.sort),
    omdraaien = (1, np.flip),
    is_nan = (1, np.isnan, None, None, lambda eh, _: None, True),
    is_inf = (1, np.isinf, None, None, lambda eh, _: None, True),
    gelijk = (2, np.equal, None, None, lambda eh, _: None, True),
    niet_gelijk = (2, np.not_equal, None, None, lambda eh, _: None, True),
    groter = (2, np.greater, None, None, lambda eh, _: None, True),
    groter_gelijk = (2, np.greater_equal, None, None, lambda eh, _: None, True),
    kleiner = (2, np.less, None, None, lambda eh, _: None, True),
    kleiner_gelijk = (2, np.less_equal, None, None, lambda eh, _: None, True),
    alle = (1, np.all, None, None, lambda eh, _: None, True),
    sommige = (1, np.any, None, None, lambda eh, _: None, True),
    niet_alle = (1, lambda x: ~np.all(x), None, None, lambda eh, _: None, True),
    geen = (1, lambda x: ~np.any(x), None, None, lambda eh, _: None, True),
    of = (2, np.logical_or, None, None, lambda eh, _: None, True),
    en = (2, np.logical_and, None, None, lambda eh, _: None, True),
    niet = (1, np.logical_not, None, None, lambda eh, _: None, True),
    xof = (2, np.logical_xor, None, None, lambda eh, _: None, True),
)
_numpy_functions['min'] = np.amin # reserverd keywords
_numpy_functions['max'] = np.amax
_numpy_functions['abs'] = np.fabs

def _wrap_functie(n_args, fn, check_type_eenheid=None, pre_verander_eenheid_fn=None,
                  post_verander_eenheid_fn=None, maak_bool=False):
    def return_fn(*args, **kwargs):
        if n_args is not None:
            if n_args != len(args):
                raise ValueError('Onjuist aantal argumenten gegeven in functie.')
            args = args[0:n_args]
        # pre
        eenheid = None
        originele_eenheid = None
        waarde = False
        nieuwe_args = []
        for iarg, arg in enumerate(args):
            if isinstance(arg, Waarde):
                arg = arg.kopie()
                if (check_type_eenheid is not None
                        and arg.eenheid is not None
                        and arg._eenheidbreuk != Waarde(1)[check_type_eenheid]._eenheidbreuk):
                    raise ValueError('Eenheid \'{}\' in functie \'{}\' is niet geldig. '
                                     'Dit moet bijvoorbeeld \'{}\' zijn.'.format(
                                     arg.eenheid, fn.__name__, check_type_eenheid))
                waarde = True
                originele_eenheid = (arg.eenheid if originele_eenheid is None
                                                 else originele_eenheid)
                if pre_verander_eenheid_fn is not None:
                    eenheid = arg.eenheid if eenheid is None else eenheid
                    eenheid = pre_verander_eenheid_fn(eenheid, args)
                    arg = arg.gebruik_eenheid(eenheid, check_type=False)
                else:
                    if iarg == 0:
                        eenheid = arg.eenheid
                    else:
                        arg = arg.eh(eenheid)
                nieuwe_args.append(float(arg))
            elif isinstance(arg, Lijst):
                arg = arg.kopie()
                arg_w = Waarde(1)[arg.eenheid]
                if (check_type_eenheid is not None
                        and arg.eenheid is not None
                        and arg_w._eenheidbreuk != Waarde(1)[check_type_eenheid]._eenheidbreuk):
                    raise ValueError('Eenheid \'{}\' in functie \'{}\' is niet geldig. '
                                     'Dit moet bijvoorbeeld \'{}\' zijn.'.format(
                                     arg_w.eenheid, fn.__name__, check_type_eenheid))
                originele_eenheid = arg.eenheid if originele_eenheid is None else originele_eenheid
                if pre_verander_eenheid_fn is not None:
                    eenheid = arg.eenheid if eenheid is None else eenheid
                    eenheid = pre_verander_eenheid_fn(eenheid, args)
                    arg = arg.gebruik_eenheid(eenheid, check_type=False)
                else:
                    if iarg == 0:
                        eenheid = arg.eenheid
                    else:
                        arg = arg.eh(eenheid)
                nieuwe_args.append(arg.array)
            else:
                nieuwe_args.append(arg)
            
        # call
        value = fn(*nieuwe_args, **kwargs)
        
        # post
        gebruik_originele_eenheid = False
        if post_verander_eenheid_fn is not None:
            eenheid = post_verander_eenheid_fn(eenheid, args)
            if eenheid is not None and eenheid[0] == '@':
                eenheid = eenheid[1:]
                gebruik_originele_eenheid = True
        if isinstance(value, bool) or 'numpy.bool' in str(type(value)):
            return value
        elif isinstance(value, type(np.array([]))):
            l = Lijst(np.array(value, dtype='float64'))
            if eenheid is not None:
                if post_verander_eenheid_fn is not None:
                    l = l.gebruik_eenheid(eenheid, check_type=False)
                else:
                    l = l.gebruik_eenheid(eenheid)
            if gebruik_originele_eenheid:
                l = l.gebruik_eenheid(originele_eenheid)
            if len(l) == 1:
                l = Waarde(l[0]).gebruik_eenheid(l.eenheid)
            if maak_bool:
                l = l.waar()
            return l
        elif waarde or eenheid:
            w = Waarde(value)
            if eenheid is not None:
                if post_verander_eenheid_fn is not None:
                    w = w.gebruik_eenheid(eenheid, check_type=False)
                else:
                    w = w.gebruik_eenheid(eenheid)
            if gebruik_originele_eenheid:
                w = w.gebruik_eenheid(originele_eenheid)
            if maak_bool:
                w = bool(w)
            return w
        return value
    return return_fn

for fn_name, fn_arg in _numpy_functions.items():
    if callable(fn_arg):
        setattr(pyco, fn_name, _wrap_functie(None, fn_arg))
    elif len(fn_arg) == 2:
        setattr(pyco, fn_name, _wrap_functie(fn_arg[0], fn_arg[1]))
    elif len(fn_arg) == 3:
        setattr(pyco, fn_name, _wrap_functie(fn_arg[0], fn_arg[1], fn_arg[2]))
    elif len(fn_arg) == 4:
        setattr(pyco, fn_name, _wrap_functie(fn_arg[0], fn_arg[1], fn_arg[2], fn_arg[3]))
    elif len(fn_arg) == 5:
        setattr(pyco, fn_name, _wrap_functie(fn_arg[0], fn_arg[1], fn_arg[2], fn_arg[3], fn_arg[4]))
    elif len(fn_arg) == 6:
        setattr(pyco, fn_name, _wrap_functie(fn_arg[0], fn_arg[1], fn_arg[2], fn_arg[3], fn_arg[4], fn_arg[5]))

    
###############################################################################
    
