# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Other_elem_DSS.py
# @Software: PyCharm

import pandas as pd
from openpy_fx_tools_dss.interface_dss import dss
from openpy_fx_tools_dss.NameClass_columns import dict_Other
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.fx_objects import _COL_MTY, _COL_ORD

list_Other_DSS = ['Vsource', 'Fault', 'GICsource', 'Isource']

def Other_ORD(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:
    if name_class == 'Vsource':
        return _COL_ORD(dict_Other, DF_elem_DSS, name_class)

    elif name_class == 'Fault':
        return _COL_ORD(dict_Other, DF_elem_DSS, name_class)

    elif name_class == 'GICsource':
        return _COL_ORD(dict_Other, DF_elem_DSS, name_class)

    elif name_class == 'Isource':
        return _COL_ORD(dict_Other, DF_elem_DSS, name_class)

    else:
        return DF_elem_DSS

def Other_Def_Value(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:
    if name_class == 'Vsource':
        if not DF_elem_DSS.empty:
            for index, row in DF_elem_DSS.iterrows():
                if DF_elem_DSS['MVAsc3'][index] != '' and DF_elem_DSS['MVAsc1'][index] != '':
                    list_Vs = ['x1r1', 'x0r0',
                               'Isc3', 'Isc1',
                               'R1', 'X1', 'R0', 'X0', 'Z1', 'Z0', 'Z2',
                               'puZ1', 'puZ0', 'puZ2']
                    for m in list_Vs:
                        DF_elem_DSS[m][index] = ''

                if DF_elem_DSS['Isc3'][index] != '' and DF_elem_DSS['Isc1'][index] != '':
                    list_Vs = ['x1r1', 'x0r0',
                               'MVAsc3', 'MVAsc1',
                               'R1', 'X1', 'R0', 'X0', 'Z1', 'Z0', 'Z2',
                               'puZ1', 'puZ0', 'puZ2']
                    for m in list_Vs:
                        DF_elem_DSS[m][index] = ''

                if DF_elem_DSS['x1r1'][index] != '' and DF_elem_DSS['x0r0'][index] != '':
                    list_Vs = ['Isc3', 'Isc1',
                               'MVAsc3', 'MVAsc1',
                               'R1', 'X1', 'R0', 'X0', 'Z1', 'Z0', 'Z2',
                               'puZ1', 'puZ0', 'puZ2']
                    for m in list_Vs:
                        DF_elem_DSS[m][index] = ''


                row_aux = [
                    'frequency', 'MVAsc3', 'MVAsc1', 'x1r1', 'x0r0', 'Isc3', 'Isc1', 'R1', 'X1', 'R0', 'X0',
                    'ScanType', 'Sequence', 'bus2', 'baseMVA', 'Model', 'puZideal', 'spectrum', 'enabled', 'basefreq']
                
                value_aux = [
                    'base frequency', 2000, 2100, 4, 3, 1000, 10500, 1.65, 6.6, 1.9, 5.7, 'Positive', 'Positive',
                    'Bus1.0.0.0', 100, 'Thevenin', '[1e-06, 0.001]', 'defaultvsource', 'Yes', 'base frequency']

                for x in zip(row_aux, value_aux):
                    if DF_elem_DSS[x[0]][index] == dss.solution_read_frequency():
                        DF_elem_DSS[x[0]][index] = ''

                    if DF_elem_DSS[x[0]][index] == x[1]:
                        DF_elem_DSS[x[0]][index] = ''

                    if DF_elem_DSS[x[0]][index] == f'{DF_elem_DSS["bus1"][index]}.0.0.0':
                        DF_elem_DSS[x[0]][index] = ''

                    if DF_elem_DSS[x[0]][index] == f'{DF_elem_DSS["bus1"][index]}.0.0':
                        DF_elem_DSS[x[0]][index] = ''


        return DF_elem_DSS

    elif name_class == 'Fault':
        if not DF_elem_DSS.empty:
            pass

        return DF_elem_DSS

    elif name_class == 'GICsource':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'Isource':
        if not DF_elem_DSS.empty:
            pass

        return DF_elem_DSS

    else:
        return DF_elem_DSS

def Other_MTY(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):
    #list_property = dss.dsselement_all_property_names()
    list_property = dict_Other[name_class]

    if name_class == 'Vsource':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Fault':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'GICsource':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Isource':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    else:
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)