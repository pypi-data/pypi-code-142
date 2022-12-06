# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : PC_elements_MTY.py
# @Software: PyCharm

import pandas as pd
from openpy_fx_tools_dss.interface_dss import dss
from openpy_fx_tools_dss.NameClass_columns import dict_Meters
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.fx_objects import _COL_ORD, _COL_MTY

list_Meters_DSS = ['EnergyMeter', 'FMonitor', 'Monitor', 'Sensor']

def Meters_Def_Value(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:

    if name_class == 'EnergyMeter':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'FMonitor':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'Monitor':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'Sensor':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    else:
        return DF_elem_DSS

def Meters_ORD(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:

    if name_class == 'EnergyMeter':
        return _COL_ORD(dict_Meters, DF_elem_DSS, name_class)
    elif name_class == 'FMonitor':
        return _COL_ORD(dict_Meters, DF_elem_DSS, name_class)
    elif name_class == 'Monitor':
        return _COL_ORD(dict_Meters, DF_elem_DSS, name_class)
    elif name_class == 'Sensor':
        return _COL_ORD(dict_Meters, DF_elem_DSS, name_class)
    else:
        return DF_elem_DSS

def Meters_MTY(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):
    #list_property = dss.dsselement_all_property_names()
    list_property = dict_Meters[name_class]

    if name_class == 'EnergyMeter':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'FMonitor':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Monitor':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Sensor':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    else:
        return BBDD_elem_DSS, DSS_elem_list


