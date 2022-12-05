# -*- coding: utf-8 -*-
# @Time    : 26/08/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : load_examples.py
# @Software: PyCharm

import logging
import os
import pathlib
from openpy_fx_tools_dss.logg_print_alert import logg_alert
log_py = logging.getLogger(__name__)


class examples_lib:

    def load_examples_DSS(self, Option: int = None, case: str = None) -> dict:
        """
        Within the module, look for the selected option in the examples tab. Return a dictionary with the keys
        ['DSS_path'], ['path_save'] and ['prj_name'].

        :param Option: Option select. Default is None.
        :param case:

        :return: dict_DSS
        """
        dict_DSS = _test_DSS_files(Opt=Option, case=case)

        return dict_DSS

    def load_examples_xlsx(self, Option: int = None) -> dict:
        """
        Within the module, look for the selected option in the examples tab. Return a dictionary with the keys
        ['xlsx_path'], ['path_save'] and ['prj_name'].

        :param Option: Option select. Default is None.
        :return: dict_xlsx
        """
        dict_xlsx = _test_xlsx_files(Opt=Option)

        return dict_xlsx

def _test_DSS_files(Opt: int, case: str):
    script_path = os.path.dirname(os.path.abspath(__file__))
    DSS_info = dict()
    if case == None:
        case = "."
    else:
        case = case + '_files'

    if Opt == 1:
        DSS_info['DSS_path'] = pathlib.Path(script_path).joinpath(
            "./Examples", "13Bus", "DSS_files", "IEEE13Nodeckt.dss")
        DSS_info['path_save'] = pathlib.Path(script_path).joinpath(
            "./Examples", "13Bus", case)
        DSS_info['prj_name'] = '13BusIEEE'

    if Opt == 2:
        DSS_info['DSS_path'] = pathlib.Path(script_path).joinpath(
            "./Examples", "37Bus", "DSS_files", "ieee37.dss")
        DSS_info['path_save'] = pathlib.Path(script_path).joinpath(
            "./Examples", "37Bus", case)
        DSS_info['prj_name'] = '37BusIEEE'

    if Opt == 3:
        DSS_info['DSS_path'] = pathlib.Path(script_path).joinpath(
            "./Examples", "123Bus", "DSS_files", "IEEE123Master")
        DSS_info['path_save'] = pathlib.Path(script_path).joinpath(
            "./Examples", "123Bus", case)
        DSS_info['prj_name'] = '123BusIEEE'

    res = not DSS_info
    if res:
        logg_alert.update_logg_file('Select an uploaded example, see documentation', 4, log_py)
        exit()

    return DSS_info


def _test_xlsx_files(Opt: int) -> object:
    script_path = os.path.dirname(os.path.abspath(__file__))
    xlsx_info = dict()
    if Opt == 1:
        xlsx_info['path_save'] = pathlib.Path(script_path).joinpath(
            "./Examples", "13Bus", "xlsx_files", "DSS_files_from_xlsx")
        xlsx_info['xlsx_path'] = pathlib.Path(script_path).joinpath(
            "./Examples", "13Bus", "xlsx_files", "BBDD_DSS_13BusIEEE.xlsx")

    if Opt == 2:
        xlsx_info['path_save'] = pathlib.Path(script_path).joinpath(
            "./Examples", "37Bus", "xlsx_files", "DSS_files_from_xlsx")
        xlsx_info['xlsx_path'] = pathlib.Path(script_path).joinpath(
            "./Examples", "37Bus", "xlsx_files", "BBDD_DSS_37BusIEEE.xlsx")

    if Opt == 3:
        xlsx_info['path_save'] = pathlib.Path(script_path).joinpath(
            "./Examples", "123Bus", "xlsx_files", "DSS_files_from_xlsx")
        xlsx_info['xlsx_path'] = pathlib.Path(script_path).joinpath(
            "./Examples", "123Bus", "xlsx_files", "BBDD_DSS_123BusIEEE.xlsx")

    res = not xlsx_info
    if res:
        logg_alert.update_logg_file('Select an uploaded example, see documentation', 4, log_py)
        exit()

    return xlsx_info


