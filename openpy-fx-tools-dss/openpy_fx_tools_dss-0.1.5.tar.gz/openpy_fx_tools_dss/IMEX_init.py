# -*- coding: utf-8 -*-
# @Time    : 26/08/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : IMEX_init.py
# @Software: PyCharm

from .lib_py_base import DSS_xlsx_save
from .IMEX_to_DSS.xlsx_DSS_xlsx.base_xlsx_DSS import class_xlsx_to_DSS
from .logg_print_alert.logg_alert import add_DSS_empty

aux_xlsx = class_xlsx_to_DSS()

class xlsx_DSS_xlsx:
    def create_template_xlsx(
            self, path_save: str = None, prj_name: str = 'default', elem_list: list = [], all_elem: bool = True):
        """
        Generate .xlsx template for OpenDSS xlsx_data entry.

        :param path_save: Path to save the file created. Default is 'None'.
        :param prj_name: Name of the project or case. Default is 'default'.
        :param elem_list: List of OpenDSS elements considered in xlsx template. Default is '[]'.
        :param all_elem: All OpenDSS elements in the xlsx template. Default is 'True'.
        :return: xlsx file
        """
        aux_xlsx._template_xlsx(path_save, prj_name, elem_list, all_elem)

    def xlsx_to_OpenDSS(
            self, xlsx_path: str = None, path_save: str = None, prj_name: str = 'default', add_path: bool = False,
            coords: str = 'LatLong'):
        """
        Generate OpenDSS files, according to the information found in the xlsx template.

        :param xlsx_path: xlsx file path. Default is 'None'.
        :param path_save: Path to save the file created. Default is 'None'
        :param prj_name: Name of the project or case. Default is 'default'
        :param add_path: Add in the OpenDSS Master the path of the file. Default is 'False'
        :param coords: Type of circuit coordinates, can be 'XY' or 'LatLong'. Default is 'XY'
        :return: DSS files
        """
        aux_xlsx._create_DSS_from_xlsx(xlsx_path, path_save, prj_name, add_path, coords)

    def OpenDSS_to_xlsx(
            self, DSS_path: str = None, path_save: str = None, prj_name: str = 'default',
            add_empty: bool = add_DSS_empty, coords: str = 'LatLong'):
        """
        Generates .xlsx template with xlsx_data from OpenDSS scripts

        :param DSS_path: OpenDSS file path. Default is 'None'
        :param path_save: Path to save the file created. Default is 'None'
        :param prj_name: Name of the project or case. Default is 'default'
        :param add_empty: All OpenDSS elements in the xlsx template. Default is 'True'
        :return:
        """
        aux_xlsx._create_from_DSS_scripts_to_xlsx(DSS_path, path_save, prj_name, add_empty, coords)
