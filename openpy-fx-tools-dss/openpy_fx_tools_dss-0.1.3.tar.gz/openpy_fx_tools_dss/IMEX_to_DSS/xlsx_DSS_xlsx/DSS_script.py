# -*- coding: utf-8 -*-
# @Time    : 26/10/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import logging
import pandas as pd
from io import open
import numpy as np
import openpyxl
import os
import glob
import shutil
from openpy_fx_tools_dss.logg_print_alert import logg_alert
from ...helper_functions import is_float

log_py = logging.getLogger(__name__)



def create_scrips_base_dss(name_dss: str, xlsx_file: str, path_save: str, add_path: bool, coords: str):
    """
    function that creates the OpenDSS scripts with the information from the database.

    :param name_dss:
    :param xlsx_file:
    :param path_save:
    :param add_path:
    :param coords:
    :return: OpenDSS scripts in the specified path_save
    """
    delete_all_files(path_save)
    create_master_base_dss(name_dss, xlsx_file, path_save, add_path, coords)
    for element in check_BBDD(xlsx_file):
        create_element_base_dss(name_dss, element, xlsx_file, coords)
    logg_alert.update_logg_file('_' * 64, 1)
    logg_alert.update_logg_file('Data loaded and .DSS files created', 2, log_py)


def create_cases(name_dss: str, file_BBDD: str, root_path: str, name_folder: str):
    """

    :param name_dss:
    :param file_BBDD:
    :param root_path:
    :param name_folder:
    :return:
    """
    indicator = os.path.exists(name_folder)

    if indicator:
        shutil.rmtree(name_folder)
        create_folder(name_folder)
        delete_files_DSS()
        root_file_path = root_path+f'/{file_BBDD}'
        root_file_path_csv = root_path + f'/Buscoords_{name_dss}.csv'
        name_dss_aux = name_dss + f'_{name_folder}'
        create_scrips_dss(name_dss_aux, file_BBDD, root_file_path)
        move_files_DSS(root_path, root_path + f'/{name_folder}')
        shutil.copy(src=root_file_path, dst=root_path + f'/{name_folder}')
        shutil.copy(src=root_file_path_csv, dst=root_path + f'/{name_folder}')
        os.rename(root_path + f'/{name_folder}' + f'/{file_BBDD}', root_path+ f'/{name_folder}' + f'/BBDD_{name_folder}.xlsx')
        os.rename(root_path + f'/{name_folder}' + f'/Buscoords_{name_dss}.csv', root_path + f'/{name_folder}' + f'/Buscoords_{name_dss}_{name_folder}.csv')

    elif not indicator:
        create_folder(name_folder)
        delete_files_DSS()
        root_file_path = root_path + f'/{file_BBDD}'
        root_file_path_csv = root_path + f'/Buscoords_{name_dss}.csv'
        name_dss_aux = name_dss + f'_{name_folder}'
        create_scrips_dss(name_dss_aux, file_BBDD, root_file_path)
        move_files_DSS(root_path, root_path + f'/{name_folder}')
        shutil.copy(src=root_file_path, dst=root_path + f'/{name_folder}')
        shutil.copy(src=root_file_path_csv, dst=root_path + f'/{name_folder}')
        os.rename(root_path + f'/{name_folder}' + f'/{file_BBDD}', root_path + f'/{name_folder}' + f'/BBDD_{name_folder}.xlsx')
        os.rename(root_path + f'/{name_folder}' + f'/Buscoords_{name_dss}.csv', root_path + f'/{name_folder}' + f'/Buscoords_{name_dss}_{name_folder}.csv')

    else:
        print('Cannot perform the operation try another name')

def create_folder(name_folder: str):
    os.mkdir(name_folder)

def file_path(workbook):
    return read_direction()+workbook

def read_direction():
    file_path = os.path.dirname(os.path.abspath(__file__))
    file_path = file_path.replace("\\", "/")
    return file_path

def move_files_DSS(source_address, destination_address):
    """
    :return:
    Delete existing .DSS files in the specified path_save
    """
    direction = read_direction()
    dss_files = glob.glob(direction+'/*.dss')
    dss_files2 = glob.glob('/*.dss')
    for dss_file in dss_files:
        shutil.move(dss_file, destination_address)

#1
def delete_all_files(path_save):
    """
    Delete existing .DSS files in the specified path_save
    
    :param path_save:
    :return: 
    """
    dss_files = glob.glob(f'{path_save}/*.dss')
    for dss_file in dss_files:
        try:
            os.remove(dss_file)
        except OSError as e:
            print(f"Error:{e.strerror}")

def delete_files_DSS():
    """
    :return:
    Delete existing .DSS files in the specified path_save
    """
    path_save = read_direction()
    dss_files = glob.glob(f'{path_save}/*.dss')
    for dss_file in dss_files:
        try:
            os.remove(dss_file)
        except OSError as e:
            print(f"Error:{e.strerror}")

def master_content_dir(name_dss: str, list_elements: list, path_save: str, add_path: bool, coords: str):
    """

    :param name_dss:
    :param list_elements:
    :param path_save:
    :param add_path:
    :param coords:
    :return:
    """
    if add_path:
        content = \
            f'set Datapath=({path_save}\)\n'\
            'Clear\n'\
            '\n'\
            f'New Circuit.{name_dss}\n'\
            '\n'
    else:
        content = \
            'Clear\n' \
            '\n' \
            f'New Circuit.{name_dss}\n' \
            '\n'
    aux = ''
    content_aux = ''

    for element in list_elements:
        if element == 'Buscoords':
            pass
        elif element != 'Voltagebases':
            content_aux = f'Redirect {element}_{name_dss}.dss\n'
            aux = aux + content_aux

    aux = content + aux

    aux_0 = '\n'\
            f'Redirect Voltagebases_{name_dss}.dss\n'
    if logg_alert.export_csv:
        if coords == 'XY':
            aux_1 = '\n'\
                    f'Buscoords Buscoords_{name_dss}.csv' \
                    '\n'
        elif coords == 'LatLong':
            aux_1 = '\n'\
                    f'LatLongCoords Buscoords_{name_dss}.csv'\
                    '\n'
        else:
            aux_1 = '\n'
    else:
        if coords == 'XY':
            aux_1 = '\n'\
                    f'Buscoords Buscoords_{name_dss}.dss' \
                    '\n'
        elif coords == 'LatLong':
            aux_1 = '\n'\
                    f'LatLongCoords Buscoords_{name_dss}.dss'\
                    '\n'
        else:
            aux_1 = '\n'

    aux_2 = '\n'\
            'solve'

    aux = aux + aux_0 + aux_1 + aux_2

    return aux


#2
def create_master_base_dss(name_dss: str, xlsx_file: str, path_save: str, add_path: bool, coords: str):
    """

    :param name_dss:
    :param xlsx_file:
    :param path_save:
    :param add_path:
    :param coords:
    :return:
    """
    os.chdir(path_save)
    os.getcwd()
    list_elements = check_BBDD(xlsx_file)
    master_dss = open(f'Master_{name_dss}.dss', 'w')
    content = master_content_dir(name_dss, list_elements, path_save, add_path, coords)
    master_dss.write(content)
    master_dss.close()

def create_master_dss(name_dss: str, xlsx_file: str):

    list_elements = check_BBDD(xlsx_file)
    master_dss = open(f'Master_{name_dss}.dss', 'w')
    content = master_content(name_dss, list_elements)
    master_dss.write(content)
    master_dss.close()

#4
def check_BBDD(xlsx_file: str):
    """
    :param xlsx_file:
    :return:
    """
    workbook = openpyxl.load_workbook(xlsx_file, read_only=True)
    name_sheets = workbook.sheetnames
    list_elements = []
    for name_sheet in name_sheets:
        df_sheet = pd.read_excel(xlsx_file, sheet_name=name_sheet)
        if len(df_sheet) >= 1:
            list_elements.append(name_sheet)
        else:
            pass
    return list_elements

#5
def create_element_base_dss(name_dss: str, element: str, direction: str, coords: str):
    """
    :param name_dss:
    :param element:
    :param direction:
    :return:
    """
    df_element = pd.read_excel(direction, sheet_name='{}'.format(element))
    dict_element = df_element.to_dict()
    keys = [*dict_element]
    script = ''
    aux = 0
    list_aux = []

    if element != 'Buscoords':
        for n in range(len(dict_element['Id_{}'.format(element)])):
            for key in keys:
                if key == 'Id_{}'.format(element):
                    if dict_element[key][aux] == 'source':
                        script = 'Edit "{}.{}" '.format(element, dict_element[key][aux])
                    else:
                        if element == 'Switch':
                            element_aux = 'Line'
                            script = 'New "{}.{}" '.format(element_aux, dict_element[key][aux])
                        elif element == 'Voltagebases':
                            script = f'Set Voltagebases = {dict_element[key][aux]}\n calcv\n'
                        else:
                            script = 'New "{}.{}" '.format(element, dict_element[key][aux])

                    list_aux.append(script)
                else:
                    if aux <= len(dict_element[key]):
                        value_DSS = dict_element[key][aux]

                        if str(value_DSS) != 'nan':
                            list_str = ['linecode']
                            if len([x for x in [key] if x in list_str]) == 1:
                                if is_float(dict_element[key][aux]):
                                    value_DSS = str(int(value_DSS))

                            script = '{}={} '.format(key, value_DSS)
                            list_aux.append(script)
                        else:
                            pass
            list_aux.append('\n')

            aux += 1
        element_content = '{}'.format(''.join(list_aux))
        element_dss = open('{}_{}.dss'.format(element, name_dss), 'w')
        element_dss.write(element_content)
        element_dss.close()
    else:
        if coords == 'XY':
            df_element = df_element[['Bus name', 'X', 'Y']]
        elif coords == 'LatLong':
            df_element = df_element[['Bus name', 'Long', 'Lat']]
        else:
            df_element = df_element[['Bus name']]
            df_element['Aux_Y'] = 0
            df_element['Aux_X'] = 0
        element_content = df_element.to_csv(index=False, header=False).replace('\r', '')
        element_dss = open('{}_{}.dss'.format(element, name_dss), 'w')
        element_dss.write(element_content)
        element_dss.close()

def create_element_dss(name_dss: str, element: str, direction: str):
    """
    :param name_dss:
    :param element:
    :param direction:
    :return:
    """
    df_element = pd.read_excel(direction, sheet_name='{}'.format(element))
    dict_element = df_element.to_dict()
    keys = [*dict_element]
    script = ''
    aux = 0
    list_aux = []
    for n in range(len(dict_element['Id_{}'.format(element)])):
        for key in keys:
            if key == 'Id_{}'.format(element):
                if dict_element[key][aux] == 'source':
                    script = 'Edit "{}.{}" '.format(element, dict_element[key][aux])
                else:
                    if element == 'Switch':
                        element_aux = 'Line'
                        script = 'New "{}.{}" '.format(element_aux, dict_element[key][aux])
                    elif element == 'Voltagebases':
                        script = \
                            f'Set Voltagebases = {dict_element[key][aux]}\n'\
                            f'calcv\n'
                    else:
                        script = 'New "{}.{}" '.format(element, dict_element[key][aux])

                list_aux.append(script)
            else:
                if aux <= len(dict_element[key]):
                    if str(dict_element[key][aux]) != 'nan':
                        script = '{}={} '.format(key, dict_element[key][aux])
                        list_aux.append(script)
                    else:
                        pass
        list_aux.append('\n')

        aux += 1
    element_content = '{}'.format(''.join(list_aux))
    element_dss = open('{}_{}.dss'.format(element, name_dss), 'w')
    element_dss.write(element_content)
    element_dss.close()

def create_scrips_dss(name_dss: str, workbook: str, ruta_archivo: str):
    """
    :param name_dss:
    :param workbook:
    :param ruta_archivo:
    :return OpenDSS scripts in the specified path_save

    function that creates the OpenDSS scripts with the information from the database
    """
    delete_files_DSS()
    create_master_dss(name_dss, workbook)
    for element in check_BBDD(workbook):
        create_element_dss(name_dss, element, ruta_archivo)
    print('Data loaded and .DSS files created')

def create_scripts_OpenDSS(name_dss, workbook, ruta_raiz, name_folder):
    create_cases(name_dss, workbook, ruta_raiz, name_folder)