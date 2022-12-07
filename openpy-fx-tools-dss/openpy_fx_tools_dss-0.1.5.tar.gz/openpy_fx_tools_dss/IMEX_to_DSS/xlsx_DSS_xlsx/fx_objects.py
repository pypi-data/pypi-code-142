# -*- coding: utf-8 -*-
# @Time    : 15/11/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : General_elem_DSS.py
# @Software: PyCharm

import pandas as pd

def _COL_ORD(dict_obj: dict, DF_elem_DSS: pd.DataFrame, name_class: str):
    list_aux = [f'Id_{name_class}']
    list_aux = list_aux + dict_obj[name_class]
    DF_elem_DSS = DF_elem_DSS[list_aux]
    return DF_elem_DSS

def _COL_MTY(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str, list_property: list):
    list_aux = [f'Id_{name_class}']
    list_aux = list_aux + list_property
    df_elem_DSS = pd.DataFrame(columns=list_aux)
    BBDD_elem_DSS[name_class] = df_elem_DSS
    DSS_elem_list.append(name_class)
    return BBDD_elem_DSS, DSS_elem_list