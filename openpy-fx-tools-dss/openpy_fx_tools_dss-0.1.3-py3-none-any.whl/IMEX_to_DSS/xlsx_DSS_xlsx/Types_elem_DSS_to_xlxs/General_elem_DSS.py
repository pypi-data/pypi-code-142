# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : General_elem_DSS.py
# @Software: PyCharm

import pandas as pd
from openpy_fx_tools_dss.interface_dss import dss
from openpy_fx_tools_dss.NameClass_columns import dict_General
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.fx_objects import _COL_ORD, _COL_MTY

list_General_DSS = ['WireData', 'LineSpacing', 'LineGeometry', 'LineCode', 'XfmrCode', 'CNData', 'GrowthShape',
                    'LoadShape', 'PriceShape', 'Spectrum', 'TCC_Curve', 'TSData', 'TShape', 'XYcurve']

def General_ORD(DF_elem_DSS: pd.DataFrame, name_class: str):

    if name_class == 'LineCode':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'LoadShape':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'TShape':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'PriceShape':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'XYcurve':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'GrowthShape':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'TCC_Curve':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'Spectrum':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'WireData':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'CNData':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'TSData':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'LineGeometry':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'LineSpacing':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    elif name_class == 'XfmrCode':
        return _COL_ORD(dict_General, DF_elem_DSS, name_class)
    else:
        return DF_elem_DSS

def General_Def_Value(DF_elem_DSS: pd.DataFrame, name_class: str):
    if name_class == 'LineCode':
        if not DF_elem_DSS.empty:
            for index, row in DF_elem_DSS.iterrows():
                row_aux = ['units', 'Kron', 'Rg', 'Xg', 'rho', 'neutral', 'LineType']
                value_aux = ['none', 'No', 0.01805, 0.155081, 100, 'nphases', 'value', 'OH']
                for x in zip(row_aux, value_aux):
                    if DF_elem_DSS[x[0]][index] == x[1]:
                        DF_elem_DSS[x[0]][index] = ''
                    if x[1] == 'nphases':
                        if DF_elem_DSS[x[0]][index] == DF_elem_DSS[x[1]][index]:
                            DF_elem_DSS[x[0]][index] = ''

        return DF_elem_DSS

    elif name_class == 'LoadShape':
        if not DF_elem_DSS.empty:
            for index, row in DF_elem_DSS.iterrows():
                if DF_elem_DSS['mult'][index] == DF_elem_DSS['Pmult'][index]:
                    DF_elem_DSS['Pmult'][index] = ''

                if DF_elem_DSS['Pmax'][index] == 1:
                    DF_elem_DSS['Pmax'][index] = ''
                if DF_elem_DSS['sinterval'][index] == 3600:
                    DF_elem_DSS['sinterval'][index] = ''
                if DF_elem_DSS['minterval'][index] == 60:
                    DF_elem_DSS['minterval'][index] = ''
        return DF_elem_DSS

    elif name_class == 'TShape':
        if not DF_elem_DSS.empty:
            pass

        return DF_elem_DSS

    elif name_class == 'PriceShape':
        if not DF_elem_DSS.empty:
            pass

        return DF_elem_DSS

    elif name_class == 'XYcurve':
        if not DF_elem_DSS.empty:
            pass

        return DF_elem_DSS

    elif name_class == 'GrowthShape':
        if not DF_elem_DSS.empty:
            pass

        return DF_elem_DSS

    elif name_class == 'TCC_Curve':
        if not DF_elem_DSS.empty:
            pass

        return DF_elem_DSS

    elif name_class == 'Spectrum':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'WireData':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'CNData':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'TSData':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'LineGeometry':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'LineSpacing':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'XfmrCode':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    else:
        return DF_elem_DSS


def General_MTY(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):

    #dss.circuit_set_active_class(name_class)
    #list_property_dss = dss.dsselement_all_property_names()
    list_property = dict_General[name_class]

    if name_class == 'LineCode':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'LoadShape':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'TShape':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'PriceShape':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'XYcurve':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'GrowthShape':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'TCC_Curve':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Spectrum':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'WireData':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'CNData':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'TSData':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'LineGeometry':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'LineSpacing':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'XfmrCode':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    else:
        return BBDD_elem_DSS, DSS_elem_list


