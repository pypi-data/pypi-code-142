# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : PC_elements_MTY.py
# @Software: PyCharm

import pandas as pd
from openpy_fx_tools_dss.interface_dss import dss
from openpy_fx_tools_dss.NameClass_columns import dict_Control
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.fx_objects import _COL_ORD, _COL_MTY

list_Controls_DSS = ['CapControl', 'ESPVLControl', 'ExpControl', 'Fuse', 'GenDispatcher', 'InvControl', 'Recloser',
                     'RegControl', 'Relay', 'StorageController', 'SwtControl', 'UPFCControl']

def Controls_ORD(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:
    if name_class == 'CapControl':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'ESPVLControl':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'ExpControl':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'Fuse':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'GenDispatcher':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'InvControl':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'Recloser':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'RegControl':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'Relay':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'StorageController':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'SwtControl':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    elif name_class == 'UPFCControl':
        return _COL_ORD(dict_Control, DF_elem_DSS, name_class)
    else:
        return DF_elem_DSS


def Controls_Def_Value(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:
    if name_class == 'CapControl':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'ESPVLControl':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'ExpControl':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'Fuse':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'GenDispatcher':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'InvControl':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'Recloser':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'RegControl':
        if not DF_elem_DSS.empty:
            for index, row in DF_elem_DSS.iterrows():
                row_aux = [
                    'revvreg', 'band', 'ptratio', 'CTprim', 'delay', 'reversible', 'tapdelay', 'debugtrace',
                    'maxtapchange', 'inversetime', 'vlimit', 'PTphase', 'revThreshold', 'revDelay', 'revNeutral',
                    'EventLog', 'TapNum', 'Cogen', 'basefreq', 'enabled', 'revband']

                value_aux = [
                    120, 3, 60, 0.2, 15, 'No', 2, 'No', 16, 'No', 0, 1, 100, 60, 'No', 'Yes', 0, 'No', 'basefreq',
                    'Yes', 3]

                for x in zip(row_aux, value_aux):

                    if DF_elem_DSS[x[0]][index] == dss.solution_read_frequency():
                        DF_elem_DSS[x[0]][index] = ''

                    if DF_elem_DSS[x[0]][index] == x[1]:
                        DF_elem_DSS[x[0]][index] = ''

        return DF_elem_DSS

    elif name_class == 'Relay':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'StorageController':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'SwtControl':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'UPFCControl':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    else:
        return DF_elem_DSS

def Controls_MTY(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):
    # list_property = dss.dsselement_all_property_names()
    list_property = dict_Control[name_class]

    if name_class == 'CapControl':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'ESPVLControl':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'ExpControl':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Fuse':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'GenDispatcher':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'InvControl':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Recloser':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'RegControl':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Relay':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'StorageController':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'SwtControl':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'UPFCControl':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    else:
        return BBDD_elem_DSS, DSS_elem_list


