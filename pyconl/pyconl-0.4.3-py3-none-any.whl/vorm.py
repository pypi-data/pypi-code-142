from typing import Union
import math

import numpy as np
import matplotlib.pyplot as plt

import pyco.basis
import pyco.waarde
import pyco.knoop
import pyco.lijn

class pc:
    BasisObject = pyco.basis.BasisObject
    Waarde = pyco.waarde.Waarde
    Knoop = pyco.knoop.Knoop
    Lijn = pyco.lijn.Lijn

    
class VormFuncties:
    """Statische hulpfuncties voor uitrekenen eigenschappen vorm."""

    @classmethod
    def punt_aan_linker_zijde(cls, la, lb, p):
        """Checkt of punt p aan linker kant van lijn la-lb ligt."""
        return (((lb[0] - la[0]) * (p[1] - la[1])
                 - (lb[1] - la[1]) * (p[0] - la[0])) > 0)

    @classmethod
    def punt_aan_rechter_zijde(cls, la, lb, p):
        """Checkt of punt p aan rechter kant van lijn la-lb ligt."""
        return (((lb[0] - la[0]) * (p[1] - la[1])
                 - (lb[1] - la[1]) * (p[0] - la[0])) < 0)

    @classmethod
    def punt_op_lijn(cls, la, lb, p):
        """Checkt of punt p op lijn la-lb ligt, tussen la en lb."""
        op_lijn = (((lb[0] - la[0]) * (p[1] - la[1])
                    - (lb[1] - la[1]) * (p[0] - la[0])) == 0)
        if not op_lijn:
            return False
        if la[0] == lb[0]:     # verticale lijn
            return ((p[1] <= lb[1] and p[1] >= la[1]) or
                    (p[1] >= lb[1] and p[1] <= la[1]))
        else:
            return ((p[0] <= lb[0] and p[0] >= la[0]) or
                    (p[0] >= lb[0] and p[0] <= la[0]))

    @classmethod
    def lijn_raakt_lijn(cls, l1a, l1b, l2a, l2b):
        """Checkt of lijn l1a-l1b de lijn l2a-l2b kruist of raakt, op de
        lijnstukken TUSSEN de punten en INCLUSIEF de punten zelf."""
        if (cls.punt_op_lijn(l1a, l1b, l2a) or
                cls.punt_op_lijn(l1a, l1b, l2b) or
                cls.punt_op_lijn(l2a, l2b, l1a) or
                cls.punt_op_lijn(l2a, l2b, l1b)):
            # uiteinde lijn ligt op andere lijn
            return True

        l1xmin = min(l1a[0], l1b[0])
        l1xmax = max(l1a[0], l1b[0])
        l2xmin = min(l2a[0], l2b[0])
        l2xmax = max(l2a[0], l2b[0])
        l1ymin = min(l1a[1], l1b[1])
        l1ymax = max(l1a[1], l1b[1])
        l2ymin = min(l2a[1], l2b[1])
        l2ymax = max(l2a[1], l2b[1])
        if (l1xmin > l2xmax or l2xmin > l1xmax or
                l1ymin > l2ymax or l2ymin > l1ymax):
            # lijn ligt helemaal links/rechts/onder/boven andere lijn
            return False

        # l1 = a * x + b
        # l2 = c * x + d
        if l1b[0] - l1a[0] == 0:        # l1 is een verticale lijn
            x = l1a[0]
            if l2b[0] - l2a[0] == 0: 	# l2 is ook verticaal
                return False
            else:
                c = 1.0 * (l2b[1] - l2a[1]) / (l2b[0] - l2a[0])
                d = l2a[1] - l2a[0] * c
                y = c * x + d
                if ((y >= l1a[1] and y <= l1b[1]) or
                         (y >= l1b[1] and y <= l1a[1])):
                    return True
                else:
                    return False
        elif l2b[0] - l2a[0] == 0:          # l2 is een verticale lijn
            x = l2a[0]
            if l1b[0] - l1a[0] == 0:	    # l1 is ook verticaal
                return False
            else:
                a = 1.0 * (l1b[1] - l1a[1]) / (l1b[0] - l1a[0])
                b = l1a[1] - l1a[0] * a
                y = a * x + b
                if ((y >= l2a[1] and y <= l2b[1]) or
                         (y >= l2b[1] and y <= l2a[1])):
                    return True
                else:
                    return False
        else:                           # beide lijnen zijn diagonaal
            a = 1.0 * (l1b[1] - l1a[1]) / (l1b[0] - l1a[0])
            b = l1a[1] - l1a[0] * a
            c = 1.0 * (l2b[1] - l2a[1]) / (l2b[0] - l2a[0])
            d = l2a[1] - l2a[0] * c
            # l1 gelijk aan l2
            if a - c == 0:              # parallel
                return False
            x = 1.0 * (d - b) / (a - c)
        if x >= l1xmin and x >= l2xmin and x <= l1xmax and x <= l2xmax:
            return True
        else:
            return False

    @classmethod
    def bereken_hoek(cls, p1, p2, p3, clockw=False):
        """Berekent de hoek in graden tussen punten p1, p2 en p3."""
        det = ((p2[0] - p1[0]) * (p3[1] - p1[1])
                   - (p2[1] - p1[1]) * (p3[0] - p1[0]))
        vec1 = [p2[0] - p1[0], p2[1] - p1[1]]
        vec2 = [p3[0] - p2[0], p3[1] - p2[1]]
        product = vec1[0] * vec2[0] + vec1[1] * vec2[1]

        factor = 0.0
        if det != 0:
            factor = 1.0 * product / det
        length1 = math.sqrt(vec1[0]**2 + vec1[1]**2)
        length2 = math.sqrt(vec2[0]**2 + vec2[1]**2)
        denominator = length1 * length2

        angle = 90.0
        if denominator != 0:
            angle = ((math.acos(1.0 * product / denominator)) *
                (360.0 / (2 * math.pi)))

        # angle is defined counter clockwise
        if angle == 0 or angle == 90 or angle == 180:   # angle is orthogonal
            if det == 0:                         # vec2 in line with vec1
                if angle == 180:
                    angle = 0               # 0
                else:
                    angle = 180             # 180
            else:                                # vec2 is not in line with vec1
                if det < 0:                      # p3 is right of vec1
                    angle = 90              # 90
                else:                            # p3 is left of vec1
                    angle = 270             # 270
        else:                                    # angle is not orthogonal
            if det < 0:                          # p3 is right of vec1
                if factor < 0:                   # p3 is further than vec1
                    angle = 180 - angle     # 90-180
                else:                            # p3 is backwards of vec1
                    angle = 180 - angle     # 0-90
            else:                                # p3 is left of vec1
                if factor > 0:                   # p3 is further than vec1
                    angle = 180 + angle     # 180-270
                else:                            # p3 is backwards of vec1
                    angle = 180 + angle     # 270-360
        if clockw:
            angle = (360 - angle) % 360
        return angle

    @classmethod
    def interpoleer_over_lijn(cls, p1, p2, x):
        """Berekent de y-waarde (bij een gegeven x-waarde) over lijn door p1 en p2. Als er geen waarde bepaald kan worden dan: 99999."""
        if p2[0] - p1[0] == 0 or not (
                isinstance(x, int) or isinstance(x, float)):
            return 99999
        else:
            a = 1.0 * (p2[1] - p1[1]) / (p2[0] - p1[0])
            b = 1.0 * p1[1] - p1[0] * a
            return a * x + b

    @classmethod
    def bereken_oppervlakte_driehoek(cls, p1, p2, p3):
        A = (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) +
            p3[0] * (p1[1] - p2[1])) / 2.0
        return abs(A)

    @classmethod
    def bereken_zwaartepunt_driehoek(cls, p1, p2, p3):
        ncx = (p1[0] + p2[0] + p3[0]) / 3.0
        ncy = (p1[1] + p2[1] + p3[1]) / 3.0
        return [ncx, ncy]

    @classmethod
    def bereken_traagheidsmomenten_driehoek(cls, p1, p2, p3):
        nc = cls.bereken_zwaartepunt_driehoek(p1, p2, p3)
        ncx = nc[0]
        ncy = nc[1]
        c = [p1, p2, p3]
        Ixx = 0.0
        Iyy = 0.0
        Ixy = 0.0
        l = len(c)
        for i in range(l):
            p = [c[i][0] - ncx, c[i][1] - ncy]
            p_volgende = [c[(i + 1) % l][0] - ncx,
                          c[(i + 1) % l][1] - ncy]
            a = abs(p[0] * p_volgende[1] - p_volgende[0] * p[1])
            Ixx += (p[0] * p[0] + p[0] * p_volgende[0] +
                    p_volgende[0] * p_volgende[0]) * a
            Iyy += (p[1] * p[1] + p[1] * p_volgende[1] +
                    p_volgende[1] * p_volgende[1]) * a
            Ixy += (p[0] * p_volgende[1] + 2 * p[0] * p[1] +
                2 * p_volgende[0] * p_volgende[1] + p_volgende[0] * p[1]) * a
        Ixx /= 12.0
        Iyy /= 12.0
        Ixy /= 24.0
        return [Ixx, Iyy, Ixy]

    @classmethod
    def genereer_net(cls, np_array):
        """Triangulatie van niet-convexe polygoon."""

        coordinaten = []
        coordinaten_links_rechts = []

        # zorgen dat laatste knoop niet zelfde is als eerste
        if np_array[0].tolist() == np_array[-1].tolist():
            np_array = np.delete(np_array, (-1), axis=0)

        # zorgen dat omtrek lijnen elkaar nergens kruisen/raken
        l = len(np_array)
        for i in range(l):
            # kies een lijn
            p1 = [np_array[i][0], np_array[i][1]]
            p2 = [np_array[(i+1)%l][0], np_array[(i+1)%l][1]]
            for ii in range(i, l):
                # check alle andere lijnen
                if i != (ii-1)%l and i != ii and i != (ii+1)%l:
                    pp1 = [np_array[ii][0], np_array[ii][1]]
                    pp2 = [np_array[(ii+1)%l][0], np_array[(ii+1)%l][1]]
                    if cls.lijn_raakt_lijn(p1, p2, pp1, pp2):
                        raise ValueError('Omtrek van vorm mag zichzelf nergens raken/kruisen. Volgende lijnen doen dat wel: Lijn({}, {}) & Lijn({}, {})'.format(p1, p2, pp1, pp2))

        def verwijder_punt_op_lijn(c):
            nonlocal coordinaten_links_rechts
            punt_op_lijn_gevonden = False
            c = c if (isinstance(c, list) or isinstance(c, tuple)) else []
            n = len(c)

            for i in range(n):
                x = c[i][0]
                y = c[i][1]
                vorige_x = c[(i - 1 + n) % n][0]
                vorige_y = c[(i - 1 + n) % n][1]
                volgende_x = c[(i + 1) % n][0]
                volgende_y = c[(i + 1) % n][1]
                if cls.punt_op_lijn([vorige_x, vorige_y],
                                        [volgende_x, volgende_y], [x, y]):
                    del c[i]
                    punt_op_lijn_gevonden = True
                    break
            if punt_op_lijn_gevonden:
                verwijder_punt_op_lijn(c)
            else:
                n = len(c)
                for i in range(n):
                    coordinaten.append([c[i][0], c[i][1], i])
                coordinaten_links_rechts = sorted(
                        coordinaten, key=lambda x: x[0])

        verwijder_punt_op_lijn(np_array.tolist())

        # uitzoeken of vorm met klok mee gaat of tegen klok in
        linker_c = coordinaten_links_rechts[0]
        l = len(coordinaten)
        volgende_c = coordinaten[(linker_c[2] + 1) % l]
        vorige_c = coordinaten[(linker_c[2] - 1 + l) % l]
        volgende_y = volgende_c[1]
        vorige_y = vorige_c[1]
        coordinaten_met_klok_mee = True
        if volgende_c[0] > vorige_c[0]:
            interpol_y = cls.interpoleer_over_lijn(
                    linker_c, volgende_c, vorige_c[0])
            if interpol_y != 99999:
                volgende_y = interpol_y
        else:
            interpol_y = cls.interpoleer_over_lijn(
                    linker_c, vorige_c, volgende_c[0])
            if interpol_y != 99999:
                vorige_y = interpol_y
        if volgende_y < vorige_y:
            coordinaten_met_klok_mee = False

        # hoek berekenen en toevoegen aan array
        for i in range(l):
            p = coordinaten[i]
            vorige_p = coordinaten[(i - 1 + l) % l]
            volgende_p = coordinaten[(i + 1) % l]
            hoek = cls.bereken_hoek(
                    vorige_p, p, volgende_p,
                    not coordinaten_met_klok_mee)
            coordinaten[i].append(hoek)

        np_array = np.array([[x, y, h] for x, y, _, h in coordinaten])

        driehoeken = []
        driehoeken_lijnen_intern = []

        aantal_iteraties = 0

        def driehoek_iterator(polys):
            nonlocal driehoeken
            nonlocal driehoeken_lijnen_intern
            nonlocal aantal_iteraties

            aantal_iteraties += 1
            if aantal_iteraties > 9999:
                raise RecursionError('maximale aantal iteraties bereikt')

            gevonden = False
            for poly_i, poly in enumerate(polys):
                if gevonden:
                    break
                l = len(poly)
                if l > 3:
                    for i in range(l):
                        p = [poly[i][0], poly[i][1],
                            poly[i][2], poly[i][3]] # x,y,i,angle
                        p_vorige = [poly[(i-1+l)%l][0], poly[(i-1+l)%l][1],
                              poly[(i-1+l)%l][2], poly[(i-1+l)%l][3]]
                        p_volgende = [poly[(i+1)%l][0], poly[(i+1)%l][1],
                            poly[(i+1)%l][2], poly[(i+1)%l][3]]
                        over_lijn = False

                        for i_sub in range(l):
                            p_sub = [poly[i_sub][0], poly[i_sub][1],
                                poly[i_sub][2], poly[i_sub][3]]
                            p_sub_volgende = [poly[(i_sub+1)%l][0],
                                poly[(i_sub+1)%l][1],
                                poly[(i_sub+1)%l][2],
                                poly[(i_sub+1)%l][3]]
                            if (not (p_vorige[0] == p_sub[0]
                                    and p_vorige[1] == p_sub[1])
                                and not (p_vorige[0] == p_sub_volgende[0]
                                    and p_vorige[1] == p_sub_volgende[1])
                                and not (p_volgende[0] == p_sub[0]
                                    and p_volgende[1] == p_sub[1])
                                and not (p_volgende[0] == p_sub_volgende[0]
                                    and p_volgende[1] == p_sub_volgende[1])):
                                if cls.lijn_raakt_lijn(
                                        p_vorige, p_volgende, p_sub,
                                        p_sub_volgende):
                                    over_lijn = True

                        hoek_vorige = cls.bereken_hoek(
                                p_volgende, p_vorige, p,
                                not coordinaten_met_klok_mee)
                        if hoek_vorige > 180:
                            hoek_vorige = 360 - hoek_vorige

                        hoek_volgende = cls.bereken_hoek(
                                p, p_volgende, p_vorige,
                                not coordinaten_met_klok_mee)
                        if hoek_volgende > 180:
                            hoek_volgende = 360 - hoek_volgende

                        if ((not over_lijn) and p[3] < 180
                                and hoek_vorige < p_vorige[3]
                                and hoek_volgende < p_volgende[3]):
                            poly1 = [
                                [p[0], p[1], p[2], p[3]],
                                [p_vorige[0], p_vorige[1],
                                     p_vorige[2], hoek_vorige],
                                [p_volgende[0], p_volgende[1],
                                     p_volgende[2], hoek_volgende]]
                            poly2 = []

                            for i_temp in range(l):
                                p_temp = poly[i_temp]
                                if (not (p[0] == p_temp[0]
                                         and p[1]==p_temp[1])):
                                    if (p_vorige[0] == p_temp[0]
                                             and p_vorige[1] == p_temp[1]):
                                        poly2.append([
                                            p_temp[0],
                                            p_temp[1],
                                            p_temp[2],
                                            (p_temp[3] - hoek_vorige)])
                                    elif (p_volgende[0] == p_temp[0]
                                              and p_volgende[1] == p_temp[1]):
                                        poly2.append([
                                            p_temp[0],
                                            p_temp[1],
                                            p_temp[2],
                                            (p_temp[3] - hoek_volgende)])
                                    else:
                                        poly2.append(p_temp)

                            polys.append(poly1[:])
                            polys.append(poly2[:])
                            driehoeken_lijnen_intern.append([
                                    p_vorige[2], p_volgende[2]])
                            del polys[poly_i]
                            gevonden = True
                            break

                elif l < 3:
                    raise ValueError('opgegeven poly heeft minder dan drie punten')
                else: # l = 3
                    driehoeken.append(poly[:])
                    del polys[poly_i]
                    gevonden = True
                    break

            if gevonden:
                driehoek_iterator(polys)

        coordinaten = [[[x, y, i, h] for i, (x, y, h)
                           in enumerate(np_array.tolist())]]

        driehoek_iterator(coordinaten)

        driehoeken = [[d[0][2], d[1][2], d[2][2]] for d in driehoeken]

        driehoeken, driehoeken_lijnen_intern = \
            cls.optimaliseer_net(np_array, driehoeken, driehoeken_lijnen_intern)

        return np.array(driehoeken), np.array(driehoeken_lijnen_intern)


    @classmethod
    def optimaliseer_net(cls, np_array, driehoeken, driehoeken_lijnen_intern):
        """Triangulatie van niet-convexe polygoon optimatliseren.

        Deze functie wordt gebruikt aan het einde van 'genereer_net' functie.

        Scherpe hoeken kunnen met floating points tot onnauwkeurigheden leiden.
        Als lijn tussen twee driehoeken (vierhoek) een scherpe hoek oplevert,
        dan lijn flippen en andere hoekpunten in deze vierhoek laten verbinden.
        """

        aantal_iteraties = 0

        def iterator_optimaliseren():
            nonlocal driehoeken
            nonlocal driehoeken_lijnen_intern
            nonlocal aantal_iteraties

            aantal_iteraties += 1
            if aantal_iteraties > 9999:
                raise RecursionError('maximale aantal iteraties bereikt')

            gevonden = False
            for i_intern, lijn_intern in enumerate(driehoeken_lijnen_intern):
                # zoek corresponderende driehoeken
                driehoek1 = None
                driehoek2 = None
                for i_driehoek, driehoek in enumerate(driehoeken):
                    if (lijn_intern[0] in driehoek
                            and lijn_intern[1] in driehoek):
                        if driehoek1 is None:
                            driehoek1 = (int(str(i_driehoek)), driehoek[:])
                        else:
                            driehoek2 = (int(str(i_driehoek)), driehoek[:])
                            break
                if driehoek1 is None or driehoek2 is None:
                    continue
                tmp1 = driehoek1[1][:]
                del tmp1[tmp1.index(lijn_intern[0])]
                del tmp1[tmp1.index(lijn_intern[1])]
                tmp2 = driehoek2[1][:]
                del tmp2[tmp2.index(lijn_intern[0])]
                del tmp2[tmp2.index(lijn_intern[1])]

                # zoek waarden van hoekpunten van vierhoek op
                ip1 = lijn_intern[0]
                ip2 = lijn_intern[1]
                ip3 = tmp1[0]
                ip4 = tmp2[0]
                p1 = np_array[ip1][:2].tolist()
                p2 = np_array[ip2][:2].tolist()
                p3 = np_array[ip3][:2].tolist()
                p4 = np_array[ip4][:2].tolist()

                # check of nieuwe diagonaal wel de oude diagonaal kruist
                #    (anders komt nieuwe diagonaal wellicht buiten Vorm
                if not cls.lijn_raakt_lijn(p1, p2, p3, p4):
                    continue

                # bereken hoeken van diagonalen en check of nieuwe groter zijn
                hoek_bestaand_1 = min(cls.bereken_hoek(p1, p2, p3, True),
                                      cls.bereken_hoek(p1, p2, p3, False))
                hoek_bestaand_2 = min(cls.bereken_hoek(p2, p1, p3, True),
                                      cls.bereken_hoek(p2, p1, p3, False))
                hoek_bestaand_3 = min(cls.bereken_hoek(p1, p2, p4, True),
                                      cls.bereken_hoek(p1, p2, p4, False))
                hoek_bestaand_4 = min(cls.bereken_hoek(p2, p1, p4, True),
                                      cls.bereken_hoek(p2, p1, p4, False))
                hoek_nieuw_1 = min(cls.bereken_hoek(p3, p4, p1, True),
                                         cls.bereken_hoek(p3, p4, p1, False))
                hoek_nieuw_2 = min(cls.bereken_hoek(p4, p3, p1, True),
                                         cls.bereken_hoek(p4, p3, p1, False))
                hoek_nieuw_3 = min(cls.bereken_hoek(p3, p4, p2, True),
                                         cls.bereken_hoek(p3, p4, p2, False))
                hoek_nieuw_4 = min(cls.bereken_hoek(p4, p3, p2, True),
                                         cls.bereken_hoek(p4, p3, p2, False))
                min_hoek_bestaand = min(hoek_bestaand_1, hoek_bestaand_2,
                                        hoek_bestaand_3, hoek_bestaand_4)
                min_hoek_nieuw = min(hoek_nieuw_1, hoek_nieuw_2,
                                     hoek_nieuw_3, hoek_nieuw_4)

                if min_hoek_nieuw > min_hoek_bestaand:
                    gevonden = True
                    # vervang huidige driehoeken
                    tmp_driehoeken = []
                    for i, driehoek in enumerate(driehoeken):
                        if i == driehoek1[0]:
                            tmp_driehoeken.append([ip3, ip4, ip1])
                        elif i == driehoek2[0]:
                            tmp_driehoeken.append([ip3, ip4, ip2])
                        else:
                            tmp_driehoeken.append(driehoek)
                    driehoeken = tmp_driehoeken
                    # vervang huidige interne lijn
                    tmp_lijnen_intern = []
                    for i, lijn in enumerate(driehoeken_lijnen_intern):
                        if i == i_intern:
                            tmp_lijnen_intern.append([ip3, ip4])
                        else:
                            tmp_lijnen_intern.append(lijn)
                    driehoeken_lijnen_intern = tmp_lijnen_intern
                    break

            if gevonden:
                iterator_optimaliseren()

        # start proces
        iterator_optimaliseren()

        return driehoeken, driehoeken_lijnen_intern

    
###############################################################################
    
    
class Vorm(pc.BasisObject):
    """Betreft een meetkundig 2D vorm met bijbehorende eigenschappen.

    AANMAKEN VORM
        v1 = Vorm(Lijn)                 invoeren van één Lijn object
        v2 = Vorm([(0,0),(1,1),(1,0)])  direct invoeren knoopcoordinaten

    EENHEID
        v.eenheid       opvragen huidige eenheid; of None als alleen getal
        v.eenheid = 'm' alle waarden in alle knoopobjecten naar 'm'
        v.gebruik_eenheid('m')   zelfde als bovenstaande, retourneert object

    EIGENSCHAPPEN       naam + '_'  -->  Waarde object i.p.v. getal
        v.O             omtrek   (bijv. v.O_ geeft omtrek Waarde met eenheid)
        v.A             oppervlakte
        v.xmin v.xmax   minimum en maximum x-waarde
        v.ymin v.ymax   minimum en maximum y-waarde
        v.ncx  v.ncy    x- en y-waarde normaalkrachtencetrum (zwaartepunt)
        v.Ixx  v.Iyy    oppervlakte traagheidsmoment in x- en y-richting
        v.Ixy           traagheidsproduct (is 0 voor symmetrische vormen)
        v.I1   v.I2     hoofdtraagheidsmomenten (1 sterke richting, 2 zwakke)
        v.alpha         hoek (tegen klok in) hoofdtraagheidsassen
        v.Wxmin v.Wxmax weerstandsmoment voor vezel x-minimaal en x-maximaal
        v.Wymin v.Wymax weerstandsmoment voor vezel y-minimaal en y-maximaal
        v.kxmin v.kxmax laagste/hoogste x-waarde van kern
        v.kymin v.kymax laagste/hoogste y-waarde van kern

    KNOOP COORDINATEN
        v.array                 Numpy array met x/y coordinaten
        v.array_gesloten        zelfde, met kopie 1e knoop aan het einde
        v.kern_array            Numpy array met x/y coordinaten van kern
        v.kern_array_gesloten   zelfde, met kopie 1e knoop aan het einde

    LIJN OBJECT
        v.lijn        genereert een Lijn object van vorm omtrek (gesloten)

    BEWERKINGEN
        v[3]          subset Numpy array object met getallen (zonder eenheid)
        len(v)        aantal knopen
        for k in v:   itereert over knopen, geeft Knoop object (met eenheid)

    OVERIG
        v.plot()                Matplotlib plot met vormeigenschappen
        v.print_eigenschappen() print overzicht van eigenschappen
        v.print_eigenschappen(knopen=True)  zelfde, met lijst van knopen
    """

    fn = VormFuncties()

    EIGENSCHAPPEN = ('O A xmin xmax ymin ymax ncx ncy Ixx Iyy Ixy I1 I2 '
                     'alpha Wxmin Wxmax Wymin Wymax kxmin kxmax kymin kymax '
                     ).split()

    AFRONDEN_NAAR_NUL = 1e-13

    def __init__(self, lijn:Union[pc.Lijn, list, tuple]):
        super().__init__()

        if not isinstance(lijn, pc.Lijn):
            lijn = pc.Lijn(*lijn)

        self._eenheid = lijn.eenheid

        # controleer knoop data en maak Numpy array
        self._array = self._check_knopen(lijn.array.copy())

        # aanmaken vorm eigenschappen
        # normaal een float object, met underscore erachter een Waarde object
        self.O = None       # omtrek
        self.O_ = None
        self.A = None       # oppervlakte
        self.A_ = None
        self.xmin = None    # laagste x-waarde (links)
        self.xmin_ = None
        self.xmax = None    # hoogste x-waarde (rechts)
        self.xmax_ = None
        self.ymin = None    # laagste y-waarde (onder)
        self.ymin_ = None
        self.ymax = None    # hoogste y-waarde (boven)
        self.ymax_ = None
        self.ncx = None     # normaalkrachtcentrum x (zwaartepunt horizontaal)
        self.ncx_ = None
        self.ncy = None     # normaalkrachtcentrum y (zwaartepunt verticaal)
        self.ncy_ = None
        self.Ixx = None     # traagheidsmoment xx (buiging belasting x-richting)
        self.Ixx_ = None
        self.Iyy = None     # traagheidsmoment yy (buiging belasting y-richting)
        self.Iyy_ = None
        self.Ixy = None     # wringtraagheidsmoment xy
        self.Ixy_ = None
        self.I1 = None      # hoofdtraagheidsmoment 1 (sterke as)
        self.I1_ = None
        self.I2 = None      # hoofdtraagheidsmoment 2 (zwakke as)
        self.I1_ = None
        self.alpha = None   # hoek van hoofdtraagheidsassen in graden
        self.alpha_ = None
        self.Wxmin = None   # weerstandsmoment t.p.v. laagste x-waarde (links)
        self.Wxmin_ = None
        self.Wxmax = None   # weerstandsmoment t.p.v. hoogste x-waarde (rechts)
        self.Wxmax_ = None
        self.Wymin = None   # weerstandsmoment t.p.v. laagste y-waarde (onder)
        self.Wymin_ = None
        self.Wymax = None   # weerstandsmoment t.p.v. hoogste y-waarde (boven)
        self.Wymax_ = None
        self.kxmin = None   # laagste x-waarde kern (links)
        self.kxmin_ = None
        self.kxmax = None   # hoogste x-waarde kern (rechts)
        self.kxmax_ = None
        self.kymin = None   # laagste y-waarde kern (onder)
        self.kymin_ = None
        self.kymax = None   # hoogste y-waarde kern (boven)
        self.kymax_ = None

        self._bereken_eigenschappen()
        self._bereken_waardes()

        self._kern_array = np.array([])  # xy coordinaten van kern
        self._bereken_kern_array()

    def _check_knopen(self, np_array):
        """Checkt knopen en berekent hoeken."""

        coordinaten = []
        coordinaten_links_rechts = []

        # zorgen dat laatste knoop niet zelfde is als eerste
        if np_array[0].tolist() == np_array[-1].tolist():
            np_array = np.delete(np_array, (-1), axis=0)

        # zorgen dat omtrek lijnen elkaar nergens kruisen/raken
        l = len(np_array)
        for i in range(l):
            # kies een lijn
            p1 = [np_array[i][0], np_array[i][1]]
            p2 = [np_array[(i+1)%l][0], np_array[(i+1)%l][1]]
            for ii in range(i, l):
                # check alle andere lijnen
                if i != (ii-1)%l and i != ii and i != (ii+1)%l:
                    pp1 = [np_array[ii][0], np_array[ii][1]]
                    pp2 = [np_array[(ii+1)%l][0], np_array[(ii+1)%l][1]]
                    if self.fn.lijn_raakt_lijn(p1, p2, pp1, pp2):
                        raise ValueError('Omtrek van vorm mag zichzelf nergens raken/kruisen. Volgende lijnen doen dat wel: Lijn({}, {}) & Lijn({}, {})'.format(p1, p2, pp1, pp2))

        def verwijder_punt_op_lijn(c):
            nonlocal coordinaten_links_rechts
            punt_op_lijn_gevonden = False
            c = c if (isinstance(c, list) or isinstance(c, tuple)) else []
            n = len(c)

            for i in range(n):
                x = c[i][0]
                y = c[i][1]
                vorige_x = c[(i - 1 + n) % n][0]
                vorige_y = c[(i - 1 + n) % n][1]
                volgende_x = c[(i + 1) % n][0]
                volgende_y = c[(i + 1) % n][1]
                if self.fn.punt_op_lijn([vorige_x, vorige_y],
                                        [volgende_x, volgende_y], [x, y]):
                    del c[i]
                    punt_op_lijn_gevonden = True
                    break
            if punt_op_lijn_gevonden:
                verwijder_punt_op_lijn(c)
            else:
                n = len(c)
                for i in range(n):
                    coordinaten.append([c[i][0], c[i][1], i])
                coordinaten_links_rechts = sorted(
                        coordinaten, key=lambda x: x[0])

        verwijder_punt_op_lijn(np_array.tolist())

        if len(np_array) < 3:
            raise ValueError('Vorm moet minimaal drie knopen bevatten (die niet op één lijn liggen).')

        return np_array

    def _float(self, waarde):
        """Zet object om naar een float en rond hele kleine waarden af naar nul."""
        f = float(waarde)
        if f > -1*self.AFRONDEN_NAAR_NUL and f < 1*self.AFRONDEN_NAAR_NUL:
            f = 0.0
        return f

    def _bereken_eigenschappen(self, alleen_A_O_minmax_nc=False):
        """Berekent alle geometrische eigenschappen."""

        arr = self.array
        Xi = arr[:,0]
        Yi = arr[:,1]
        Xii = np.delete(np.hstack((Xi, np.array([Xi[0]]))), 0)
        Yii = np.delete(np.hstack((Yi, np.array([Yi[0]]))), 0)
        determinant = Xi*Yii - Xii*Yi

        A = 1/2 * sum(determinant)
        if not A:
            return

        # als coordinaten tegen de klok in zijn ingevoerd, dan positief
        # als coordinaten met de klok mee zijn ingevoerd, dan negatief
        teken = 1.0 if A > 0 else -1.0

        self.A = self._float(teken * A)
        self.O = self._float(pc.Lijn(self.array_gesloten.tolist()))
        self.xmin = self._float(Xi.min())
        self.xmax = self._float(Xi.max())
        self.ymin = self._float(Yi.min())
        self.ymax = self._float(Yi.max())
        self.ncx = self._float(
            teken * 1/6/self.A * sum((Xi + Xii) * determinant))
        self.ncy = self._float(
            teken * 1/6/self.A * sum((Yi + Yii) * determinant))

        if alleen_A_O_minmax_nc:
            return

        # vanaf nu alle coordinaten t.o.v. zwaartepunt relativeren
        Xi_ = Xi - self.ncx
        Yi_ = Yi - self.ncy
        Xii_ = np.delete(np.hstack((Xi_, np.array([Xi_[0]]))), 0)
        Yii_ = np.delete(np.hstack((Yi_, np.array([Yi_[0]]))), 0)
        determinant_ = Xi_*Yii_ - Xii_*Yi_

        self.Ixx = self._float(
            teken * 1/12 * sum((Xi_**2 + Xi_*Xii_ + Xii_**2) * determinant_))
        self.Iyy = self._float(
            teken * 1/12 * sum((Yi_**2 + Yi_*Yii_ + Yii_**2) * determinant_))
        self.Ixy = self._float(
            teken * 1/24 * sum((Xi_*Yii_ + 2*Xi_*Yi_ + 2*Xii_*Yii_ + Xii_*Yi_) * determinant_))

        self.Wxmin = self._float(self.Ixx / abs(self.ncx - self.xmin))
        self.Wxmax = self._float(self.Ixx / abs(self.ncx - self.xmax))
        self.Wymin = self._float(self.Iyy / abs(self.ncx - self.xmin))
        self.Wymax = self._float(self.Iyy / abs(self.ncx - self.xmax))
        self.kxmin = self._float(-1 * self.Wxmax / self.A)
        self.kxmax = self._float(self.Wxmin / self.A)
        self.kymin = self._float(-1 * self.Wxmax / self.A)
        self.kymax = self._float(self.Wxmin / self.A)
        self.I1 = self._float((self.Ixx + self.Iyy) / 2
                   + np.sqrt((self.Ixx - self.Iyy)**2 + 4*self.Ixy**2)/2)
        self.I2 = self._float((self.Ixx + self.Iyy) / 2
                   - np.sqrt((self.Ixx - self.Iyy)**2 + 4*self.Ixy**2)/2)
        if self.Ixx - self.Iyy != 0:  # kan niet delen door 0
            self.alpha = self._float((math.atan(2 * self.Ixy /
                (self.Ixx - self.Iyy))/2) * (360 / (2 * math.pi)))
        elif self.Ixy == 0: # hor/vert symmetrisch: bijvoorbeeld rechthoek
            self.alpha = 0.0
        else: # Ixx == Iyy, maar niet hor/vert symmetrisch: bijvoorbeeld ruit
            self.alpha = 45.0

    def _bereken_waardes(self):
        # maak Waarde objecten met eenheid
        oppervlakte_eenheid = None
        weerstand_eenheid = None
        traagheid_eenheid = None
        if self.eenheid is not None:
            oppervlakte_eenheid = '{}2'.format(self.eenheid)
            weerstand_eenheid = '{}3'.format(self.eenheid)
            traagheid_eenheid = '{}4'.format(self.eenheid)
        self.O_ = pc.Waarde(self.O, self.eenheid)
        self.A_ = pc.Waarde(self.A, oppervlakte_eenheid)
        self.xmin_ = pc.Waarde(self.xmin, self.eenheid)
        self.xmax_ = pc.Waarde(self.xmax, self.eenheid)
        self.ymin_ = pc.Waarde(self.ymin, self.eenheid)
        self.ymax_ = pc.Waarde(self.ymax, self.eenheid)
        self.ncx_ = pc.Waarde(self.ncx, self.eenheid)
        self.ncy_ = pc.Waarde(self.ncy, self.eenheid)
        self.Ixx_ = pc.Waarde(self.Ixx, traagheid_eenheid)
        self.Iyy_ = pc.Waarde(self.Iyy, traagheid_eenheid)
        self.Ixy_ = pc.Waarde(self.Ixy, traagheid_eenheid)
        self.I1_ = pc.Waarde(self.I1, traagheid_eenheid)
        self.I2_ = pc.Waarde(self.I2, traagheid_eenheid)
        self.alpha_ = pc.Waarde(self.alpha, 'deg')
        self.Wxmin_ = pc.Waarde(self.Wxmin, weerstand_eenheid)
        self.Wxmax_ = pc.Waarde(self.Wxmax, weerstand_eenheid)
        self.Wymin_ = pc.Waarde(self.Wymin, weerstand_eenheid)
        self.Wymax_ = pc.Waarde(self.Wymax, weerstand_eenheid)
        self.kxmin_ = pc.Waarde(self.kxmin, self.eenheid)
        self.kxmax_ = pc.Waarde(self.kxmax, self.eenheid)
        self.kymin_ = pc.Waarde(self.kymin, self.eenheid)
        self.kymax_ = pc.Waarde(self.kymax, self.eenheid)

    def _bereken_kern_array(self):
        """Berekent het gebied daar waar een normaaldrukkracht NIET in trekspanningen resulteert."""
        kernpunten = [] # lijst met xy coordinaten van kern
        elastiek_lijn = [] # lijst met xy coordinaten als elastiek om vorm

        def bereken_geroteerde_coordinaten(p, alpha, z):
            alpha = -alpha
            xrot = (1.0 * math.cos(alpha * (2 * math.pi / 360)) *
                    (p[0] - z[0]) + math.sin(alpha * (2 * math.pi / 360)) *
                    (p[1] - z[1]))
            yrot = (-1.0 * math.sin(alpha * (2 * math.pi / 360)) *
                    (p[0] - z[0]) + math.cos(alpha * (2 * math.pi / 360)) *
                    (p[1] - z[1]))
            return [xrot + z[0], yrot + z[1]]

        def maak_groot_getal(x):
            return math.floor(x * 1e12)

        c = self.array.tolist()
        l = len(c)
        p = [c[0][0], c[0][1]]

        for i in range(l):
            geldig = True
            p_volgende = [c[(i + 1) % l][0], c[(i + 1) % l][1]]
            test_lijn = [p.copy(), p_volgende.copy()]
            if test_lijn[0][0] == test_lijn[1][0]: # verticale lijn
                if (test_lijn[0][0] < self.xmax
                        and test_lijn[0][0] > self.xmin):
                    geldig = False
            else: # horizontaal of diagonaal
                a = (1.0 * (test_lijn[1][1] - test_lijn[0][1]) /
                    (test_lijn[1][0] - test_lijn[0][0]))
                b = 1.0 * test_lijn[0][1] - test_lijn[0][0] * a
                is_hoger = False
                is_lager = False
                for ii in range(l):
                    if (maak_groot_getal(c[ii][1])
                            > maak_groot_getal(a * c[ii][0] + b) + 10):
                        is_hoger = True
                    elif (maak_groot_getal(c[ii][1])
                            < maak_groot_getal(a * c[ii][0] + b) - 10):
                        is_lager = True
                if is_hoger and is_lager:
                    geldig = False
            if geldig:
                elastiek_lijn.append([p.copy(), p_volgende.copy()])
                p = [c[(i + 1) % l][0], c[(i + 1) % l][1]]

        ncx = self.ncx
        ncy = self.ncy
        n = len(elastiek_lijn)
        for i in range(n):
            rand_lijn = elastiek_lijn[i]
            lijn = [[rand_lijn[0][0] - ncx, rand_lijn[0][1] - ncy],
                    [rand_lijn[1][0] - ncx, rand_lijn[1][1] - ncy]]
            inverse_x1 = 0
            inverse_y1 = 0
            if lijn[0][0] == lijn[1][0]: # verticale lijn
                if lijn[0][0] == 0:
                    inverse_x1 = 99e99
                else:
                    inverse_x1 = 1 / lijn[0][0]
                inverse_y1 = 0
            elif lijn[0][1] == lijn[1][1]: # horizontale lijn
                inverse_x1 = 0
                if lijn[0][1] == 0:
                    inverse_y1 = 99e99
                else:
                    inverse_y1 = 1/ lijn[0][1]
            else: # diagonale lijn
                lijn = sorted(lijn, key=lambda x: x[0]) # sorteer op x-waarde
                a = (1.0 * (lijn[1][1] - lijn[0][1])
                     / (lijn[1][0] - lijn[0][0]))
                b = 1.0 * lijn[0][1] - lijn[0][0] * a
                if a == 0 or b == 0:
                    inverse_x1 = 99e99
                else:
                    inverse_x1 = 1/ (-1 * b / a)
                if b == 0:
                    inverse_y1 = 99e99
                else:
                    inverse_y1 = 1 / b
            ex = (-1.0 / self.A * (self.Ixx * inverse_x1
                                   + self.Ixy * inverse_y1))
            ey = (-1.0 / self.A * (self.Ixy * inverse_x1
                                   + self.Iyy * inverse_y1))
            kernpunten.append([ex + ncx, ey + ncy])

        self._kern_array = np.array(kernpunten)

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

        self._array = self._check_knopen(np.array(tmp_knopen, dtype='float64'))
        self._eenheid = eenheid

        self._bereken_eigenschappen()
        self._bereken_waardes()
        self._bereken_kern_array()

    def gebruik_eenheid(self, eenheid:str):
        """Zet knopen om naar nieuwe eenheid en retourneert object."""
        self.eenheid = eenheid
        return self

    @property
    def array(self) -> np.array:
        """Retourneert Numpy array object met alle getallen (zonder eenheid)."""
        return self._array

    @property
    def array_gesloten(self) -> np.array:
        """Retourneert Numpy array object met alle getallen (zonder eenheid) waarbij startpunt OOK als laatste punt wordt aangehouden."""
        if len(self.array) > 0:
            return np.append(self.array, [self[0].tolist()], axis=0)
        else:
            return np.array([])

    @property
    def kern_array(self) -> np.array:
        """Retourneert Numpy array object met alle knopen van kern (zonder eenheid)."""
        return self._kern_array

    @property
    def kern_array_gesloten(self) -> np.array:
        """Retourneert Numpy array object met allen knopen van kern (zonder eenheid) waarbij startpunt OOK als laatste punt wordt aangehouden."""
        if len(self.kern_array) > 0:
            return np.append(self.kern_array,
                         [self.kern_array[0].tolist()], axis=0)
        else:
            return np.array([])

    @property
    def lijn(self) -> pc.Lijn:
        """Retourneert Lijn object dat correspondeert met (gesloten) Vorm."""
        knoop_objecten = [k for k in self]
        return pc.Lijn(knoop_objecten + [knoop_objecten[0]])

    def plot(self):
        """Teken vorm."""
        plt.axis('equal')

        # omtrek vorm
        if len(self.array > 2):
            X = self.array_gesloten[:,0]
            Y = self.array_gesloten[:,1]
            plt.fill(X, Y, 'r', alpha=0.2)
            plt.plot(X, Y, 'r-', lw=2)

        # kern vorm
        if len(self.kern_array > 2):
            X = self.kern_array_gesloten[:,0]
            Y = self.kern_array_gesloten[:,1]
            plt.fill(X, Y, 'b', alpha=0.2)
            plt.plot(X, Y, 'b-', lw=1)

        # hoofdtraagsheidsassens
        marge = 0.1
        hoek = self.alpha / 180 * math.pi
        ymin = self.ymin - (self.ymax - self.ymin) * marge
        ymax = self.ymax + (self.ymax - self.ymin) * marge
        xmin = self.xmin - (self.xmax - self.xmin) * marge
        xmax = self.xmax + (self.xmax - self.xmin) * marge
        x_ymin = self.ncx + (self.ncy - ymin) * math.tan(hoek)
        x_ymax = self.ncx - (ymax - self.ncy) * math.tan(hoek)
        y_xmin = self.ncy - (self.ncx - xmin) * math.tan(hoek)
        y_xmax = self.ncy + (xmax - self.ncx) * math.tan(hoek)
        plt.plot([x_ymin, x_ymax], [ymin, ymax], 'g-', lw=1)
        plt.plot([xmin, xmax], [y_xmin, y_xmax], 'g-', lw=1)

        # zwaartepunt
        plt.plot(self.ncx, self.ncy, 'bo')

        plt.show()

    def print_eigenschappen(self, knopen=False):
        print_queue = []

        if knopen:
            print_queue.append(
                    'knopen (afgerond op 2 decimalen):\n{} {}'.format(
                    [(round(k[0], 2), round(k[1], 2)) for k in self.array],
                    self.eenheid if self.eenheid is not None else '').strip())

            print_queue.append('')

        print_queue.append('\n'.join(['{:>8} = {:.3f}'.format(
                a, getattr(self, a+'_')) for a in self.EIGENSCHAPPEN]))

        print('\n{}\n'.format('\n'.join(print_queue)))

    def __getitem__(self, index) -> np.array:
        """Retourneert subset Numpy array object met getallen (zonder eenheid)."""
        return self.array[index]

    def __len__(self):
        """Geeft aantal knopen."""
        return len(self.array)

    def __iter__(self):
        """Itereert over knopen en geeft Knoop objecten terug."""
        for k_array in self.array:
            k = pc.Knoop(k_array.tolist())
            k.eenheid = self.eenheid
            yield k

    def __repr__(self):
        cls_naam = type(self).__name__
        knopen = ', '.join(repr(k) for k in self)
        return '{}(Lijn({}))'.format(cls_naam, knopen)

    def __str__(self):
        return '{} {}'.format(
                # coordinaten afgerond op twee decimalen
                [(round(k[0], 2), round(k[1], 2)) for k in self.array],
                self.eenheid if self.eenheid is not None else '').strip()


if __name__ == '__main__':

    print('v1 - lijn met cirkelboog en bezier')
    v1 = Vorm(pc.Lijn(
            (4, -5), (-10, 10)
        ).lijn_cirkelboog(
            middelpunt=(0,0),
            gradenhoek=+220
        ).lijn_recht(
            naar=(4, 10)
        ).lijn_bezier(
            richting=(-10,-4),
            naar=(4, -5)
        ).transformeren(
            rotatiehoek=30,
            translatie=[15, 5],
        ))
    v1.plot()
    v1.print_eigenschappen()

    print('v2 - polygon')
    v2 = Vorm([[0,0], [0,10], [4,10], [4,7], [6,7], [6,10], [10,10], [10,0]])
    v2.plot()
    v2.print_eigenschappen()

    print('v3 - cirkel benaderd d.m.v. een lijn met cirkelboog')
    v3= Vorm(pc.Lijn([-1,0]).lijn_cirkelboog(middelpunt=(0,0), gradenhoek=360))
    v3.plot()
    v3.print_eigenschappen()

    print('v4 - driehoek')
    v4 = Vorm(pc.Lijn([0,0], [6,-3], [10,4]).gebruik_eenheid('cm'))
    v4.plot()
    v4.print_eigenschappen()

    print('v5 - rechthoek met transformatie')
    v5 = Vorm(pc.Lijn([-50,-20], [50,-20], [50,20], [-50, 20]).transformeren(
              rotatiepunt=None, # bij None: neemt zwaartepunt
              rotatiehoek=45, # graden tegen de klok in
              schaalfactor=[1, 1], # vergroten om rotatiepunt; negatief:spiegelen
              translatie=[0, 0] # verplaatsing
        ).gebruik_eenheid('mm'))
    v5.plot()
    v5.print_eigenschappen()

    print('v6 - gedraaide rechthoek met eenheid')
    v6 = Vorm(pc.Lijn([2,0], [0,2], [8,10], [10, 8]).gebruik_eenheid('cm'))
    v6.plot()
    v6.print_eigenschappen()

#     print('v7 - Rechthoek object')
#     v7 = pc.Rechthoek(breedte=30, hoogte=50)
#     v7.plot()
#     v7.print_eigenschappen()

#     print('v8 - Cirkel object')
#     v8 = pc.Cirkel(straal=pc.Waarde(1).dm).gebruik_eenheid('m')
#     v8.plot()
#     v8.print_eigenschappen()
