# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : PD_elements_MTY.py
# @Software: PyCharm

import pandas as pd
from openpy_fx_tools_dss.interface_dss import dss
from openpy_fx_tools_dss.NameClass_columns import dict_PD_elem
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.fx_objects import _COL_ORD, _COL_MTY

list_PD_elements_DSS = ['Transformer', 'Line', 'Capacitor', 'AutoTrans', 'GICTransformer', 'Reactor']

def PD_elem_Def_Value(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:

    if name_class == 'Transformer':
        if not DF_elem_DSS.empty:
            for index, row in DF_elem_DSS.iterrows():
                if DF_elem_DSS['windings'][index] == 2:
                    if DF_elem_DSS['XHL'][index] != '':
                        row_aux = ['XHT', 'XLT', 'X12', 'X13', 'X23']
                        for x in row_aux:
                            DF_elem_DSS[x][index] = ''
                if DF_elem_DSS['windings'][index] == 3:
                    if DF_elem_DSS['XHL'][index] != '':
                        row_aux = ['X12', 'X13', 'X23']
                        for x in row_aux:
                            DF_elem_DSS[x][index] = ''
                row_aux = ['wdg', 'bus', 'conn', 'kV', 'kVA', 'tap', '%R']
                for x in row_aux:
                    DF_elem_DSS[x][index] = ''
                row_aux = [
                    'Rneut', 'flrise', 'hsrise', '%noloadloss', 'normhkVA', 'emerghkVA',
                    'sub', 'MaxTap', 'MinTap', 'NumTaps', 'subname', '%imag', 'ppm_antifloat', 'XRConst', 'LeadLag',
                    'RdcOhms', 'faultrate', 'basefreq', 'enabled', 'Seasons', 'Ratings', 'n', 'm', 'thermal']

                value_aux = [
                    -1, 65, 15, 0, '110% of kVA rating of Winding 1', '150% of kVA rating of Winding 1', 'No',
                    1.1, 0.9, 32, 'null', 0, 1, 'No', 'Lag', '85% of %R', 0.007, 'basefreq', 'Yes', 1, '[1100.0]',
                    0.8, 0.8, 2]

                for x in zip(row_aux, value_aux):

                    if DF_elem_DSS[x[0]][index] == dss.solution_read_frequency():
                        DF_elem_DSS[x[0]][index] = ''

                    if DF_elem_DSS[x[0]][index] == x[1]:
                        DF_elem_DSS[x[0]][index] = ''
        return DF_elem_DSS
    elif name_class == 'Line':
        if not DF_elem_DSS.empty:
            for index, row in DF_elem_DSS.iterrows():
                if DF_elem_DSS['linecode'][index] != '':
                    list_Line = ['rmatrix', 'xmatrix', 'cmatrix']
                    for m in list_Line:
                        DF_elem_DSS[m][index] = ''
                if DF_elem_DSS['Switch'][index] == 'Yes':
                    list_Line = [
                        'r1', 'x1', 'r0', 'x0', 'C1', 'C0', 'rmatrix', 'xmatrix', 'cmatrix', 'Rg', 'Xg', 'rho',
                        'geometry', 'units', 'spacing', 'wires', 'EarthModel', 'cncables', 'tscables', 'B1', 'B0',
                        'Seasons', 'Ratings', 'LineType', 'normamps', 'emergamps', 'faultrate', 'pctperm', 'repair',
                        'basefreq', 'enabled', 'like']
                    for m in list_Line:
                        DF_elem_DSS[m][index] = ''
                    colum_aux = ['r1', 'r0', 'x1', 'x0', 'C1', 'C0']
                    Value = [0.0001, 0.0001, 0, 0, 0, 0]
                    for x in zip(colum_aux, Value):
                        DF_elem_DSS[x[0]][index] = x[1]
                row_aux = [
                    'linecode', 'length', 'Switch', 'Rg', 'Xg', 'rho', 'units', 'EarthModel', 'LineType', 'faultrate',
                    'pctperm', 'repair', 'enabled', 'basefreq']
                value_aux = [
                    '336 MCM ACSR on 4 ft spacing', 1, 'no', 0.01805, 0.155081, 100, 'None', 'Deri', 'OH', 0.1, 20, 3,
                    'Yes', 'base frequency']
                for x in zip(row_aux, value_aux):
                    if DF_elem_DSS[x[0]][index] == dss.solution_read_frequency():
                        DF_elem_DSS[x[0]][index] = ''
                    if DF_elem_DSS[x[0]][index] == x[1]:
                        DF_elem_DSS[x[0]][index] = ''
        return DF_elem_DSS

    elif name_class == 'Capacitor':
        if not DF_elem_DSS.empty:
            for index, row in DF_elem_DSS.iterrows():
                row_aux = [
                    'bus2', 'R', 'Harm', 'Numsteps', 'states', 'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled']

                value_aux = [
                    'bus1.0', 0, 0, 1, '[1.0]', 0.0005, 100, 3, 'BaseFreq', 'Yes']

                for x in zip(row_aux, value_aux):

                    if DF_elem_DSS[x[0]][index] == dss.solution_read_frequency():
                        DF_elem_DSS[x[0]][index] = ''

                    if DF_elem_DSS[x[0]][index] == x[1]:
                        DF_elem_DSS[x[0]][index] = ''


        return DF_elem_DSS

    elif name_class == 'AutoTrans':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'GICTransformer':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'Reactor':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    else:
        return DF_elem_DSS

def PD_elements_ORD(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:

    if name_class == 'Transformer':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    elif name_class == 'Line':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    elif name_class == 'Capacitor':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    elif name_class == 'AutoTrans':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    elif name_class == 'GICTransformer':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    elif name_class == 'Reactor':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    else:
        return DF_elem_DSS

def PD_elements_MTY(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):

    #list_property = dss.dsselement_all_property_names()
    list_property = dict_PD_elem[name_class]

    if name_class == 'Transformer':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Line':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Capacitor':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'AutoTrans':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'GICTransformer':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Reactor':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    else:
        return BBDD_elem_DSS, DSS_elem_list