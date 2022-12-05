# -*- coding: utf-8 -*-
# @Time    : 16/11/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Voltagebases_DSS.py
# @Software: PyCharm


import warnings
import pandas as pd
from openpy_fx_tools_dss.interface_dss import dss

warnings.simplefilter(action='ignore', category=Warning)

def Voltagebases_DSS() -> pd.DataFrame:
    list_aux = dss.settings_read_voltage_bases()
    data = str(list_aux).replace("[", "").replace("]", "")
    dic = {'Id_Voltagebases': data}
    df_VoltBase_DSS = pd.DataFrame(columns=['Id_Voltagebases'])
    df_VoltBase_DSS = df_VoltBase_DSS.append({'Id_Voltagebases': list_aux}, ignore_index=True)

    return df_VoltBase_DSS

