# -*- coding: utf-8 -*-
# @Time    : 19/10/2021
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import pandas as pd
from io import open
import numpy as np
import openpyxl
import os
import glob
import shutil

def create_folder(name_folder: str):
    os.mkdir(name_folder)

def copy_file(file: str, root_file_path: str, name_folder: str):
    '''
    :param file:
    :param root_file_path:
    :param name_folder:
    :return:
    '''
    shutil.copyfile(src=root_file_path+f'/{file}', dst=root_file_path+f'/{name_folder}')


#def create_DSS(name_dss:str, file_BBDD:str, root_path:str, name_folder:str):+
#create_DSS(name_dss=export_name, file_BBDD=f'{address_saves_DSS_files}\BBDD_DSS_{export_name}.xlsx', path_save=address_saves_DSS_files)

def create_DSS(name_dss: str, address_saves: str):
    """

    :param name_dss:
    :param address_saves:
    :return:
    """
    file_BBDD = f'{address_saves}\BBDD_DSS_{name_dss}.xlsx'
    directory = os.chdir(address_saves)
    create_scrips_base_dss(name_dss=name_dss, workbook=file_BBDD, ruta_archivo=address_saves)

def create_scrips_base_dss(name_dss:str, workbook:str, ruta_archivo:str):
    '''
    :param name_dss:
    :param workbook:
    :param ruta_archivo:
    :return OpenDSS scripts in the specified path_save

    function that creates the OpenDSS scripts with the information from the database
    '''

    delete_all_files(ruta_archivo)
    create_master_base_dss(name_dss, workbook, ruta_archivo)
    for element in check_BBDD(workbook):
        create_element_base_dss(name_dss, element, workbook)
    print('Data loaded and .DSS files created')

def create_cases(name_dss:str, file_BBDD:str, root_path:str,name_folder:str):
    '''
    :param name_dss:
    :param file:
    :param root_path:
    :param name_folder:
    :return:
    '''
    indicator = os.path.exists(name_folder)
    if indicator == True:
        shutil.rmtree(name_folder)
        create_folder(name_folder)
        delete_files_DSS()
        root_file_path = root_path+f'/{file_BBDD}'
        root_file_path_csv = root_path + f'/Buscoods_{name_dss}.csv'
        name_dss_aux = name_dss + f'_{name_folder}'
        create_scrips_dss(name_dss_aux, file_BBDD, root_file_path)
        move_files_DSS(root_path, root_path + f'/{name_folder}')
        shutil.copy(src=root_file_path, dst=root_path + f'/{name_folder}')
        shutil.copy(src=root_file_path_csv, dst=root_path + f'/{name_folder}')
        os.rename(root_path + f'/{name_folder}' + f'/{file_BBDD}', root_path+ f'/{name_folder}' + f'/BBDD_{name_folder}.xlsx')
        os.rename(root_path + f'/{name_folder}' + f'/Buscoods_{name_dss}.csv', root_path + f'/{name_folder}' + f'/Buscoods_{name_dss}_{name_folder}.csv')

    elif indicator == False:
        create_folder(name_folder)
        delete_files_DSS()
        root_file_path = root_path + f'/{file_BBDD}'
        root_file_path_csv = root_path + f'/Buscoods_{name_dss}.csv'
        name_dss_aux = name_dss + f'_{name_folder}'
        create_scrips_dss(name_dss_aux, file_BBDD, root_file_path)
        move_files_DSS(root_path, root_path + f'/{name_folder}')
        shutil.copy(src=root_file_path, dst=root_path + f'/{name_folder}')
        shutil.copy(src=root_file_path_csv, dst=root_path + f'/{name_folder}')
        os.rename(root_path + f'/{name_folder}' + f'/{file_BBDD}', root_path + f'/{name_folder}' + f'/BBDD_{name_folder}.xlsx')
        os.rename(root_path + f'/{name_folder}' + f'/Buscoods_{name_dss}.csv', root_path + f'/{name_folder}' + f'/Buscoods_{name_dss}_{name_folder}.csv')

    else:
        print('Cannot perform the operation try another name')

def file_path(workbook):
    return read_direction()+workbook

def read_direction():
    file_path = os.path.dirname(os.path.abspath(__file__))
    file_path = file_path.replace("\\", "/")
    return file_path

def move_files_DSS(source_address, destination_address):
    '''
    :return:
    Delete existing .DSS files in the specified path_save
    '''
    direction = read_direction()
    dss_files = glob.glob(direction+'/*.dss')
    dss_files2 = glob.glob('/*.dss')
    for dss_file in dss_files:
        shutil.move(dss_file, destination_address)

def delete_all_files(address):
    '''
    :return:
    Delete existing .DSS files in the specified path_save
    '''
    direction = address
    #dss
    dss_files = glob.glob(direction+'/*.dss')
    for dss_file in dss_files:
        try:
            os.remove(dss_file)
        except OSError as e:
            print(f"Error:{e.strerror}")



def delete_files_DSS():
    '''
    :return:
    Delete existing .DSS files in the specified path_save
    '''
    direction = read_direction()
    dss_files = glob.glob(direction+'/*.dss')
    for dss_file in dss_files:
        try:
            os.remove(dss_file)
        except OSError as e:
            print(f"Error:{e.strerror}")

def master_content(name_dss:str, list_elements:list):
    '''
    :param name_dss:
    :param list_elements:
    :return:
    '''
    content = 'Clear\n'\
              '\n'\
              f'New Circuit.{name_dss}\n'\
              '\n'
    aux = ''
    content_aux = ''
    for element in list_elements:
        content_aux = f'Redirect {element}_{name_dss}.dss\n'
        aux = aux + content_aux
    aux = content + aux

    aux_1 = '\n'\
            f'LatLongCoords Buscoods_{name_dss}.csv'\
            '\n'

    aux_2 = '\n'\
            'solve'

    aux = aux + aux_1 + aux_2
    return aux


def create_master_base_dss(name_dss:str, workbook_name:str, dir:str):
    '''
    :param name_dss:
    :param workbook_name:
    :return:
    '''
    os.chdir(dir)
    os.getcwd()
    list_elements = check_BBDD(workbook_name)
    master_dss = open(f'Master_{name_dss}.dss','w')
    content = master_content(name_dss, list_elements)
    master_dss.write(content)
    master_dss.close()

def create_master_dss(name_dss:str, workbook_name:str):
    '''
    :param name_dss:
    :param workbook_name:
    :return:
    '''
    list_elements = check_BBDD(workbook_name)
    master_dss = open(f'Master_{name_dss}.dss','w')
    content = master_content(name_dss, list_elements)
    master_dss.write(content)
    master_dss.close()


def check_BBDD(workbook_name:str):
    '''
    :param workbook_name:
    :return:
    '''
    workbook = openpyxl.load_workbook(workbook_name, read_only=True)
    name_sheets = workbook.sheetnames
    list_elements = []
    for name_sheet in name_sheets:
        df_sheet = pd.read_excel(workbook_name, sheet_name=name_sheet)
        if len(df_sheet) >= 1:
            list_elements.append(name_sheet)
        else:
            pass
    return list_elements

def create_element_base_dss(name_dss:str, element:str, direction:str):
    '''
    :param name_dss:
    :param element:
    :param direction:
    :return:
    '''
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
                        script = f'Set Voltagebases = {dict_element[key][aux]}\n' \
                                 'calcv\n'
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

def create_element_dss(name_dss:str, element:str, direction:str):
    '''
    :param name_dss:
    :param element:
    :param direction:
    :return:
    '''
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
                        script = f'Set Voltagebases = {dict_element[key][aux]}\n' \
                                 'calcv\n'
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


def create_scrips_dss(name_dss:str, workbook:str, ruta_archivo:str):
    '''
    :param name_dss:
    :param workbook:
    :param ruta_archivo:
    :return OpenDSS scripts in the specified path_save

    function that creates the OpenDSS scripts with the information from the database
    '''
    delete_files_DSS()
    create_master_dss(name_dss, workbook)
    for element in check_BBDD(workbook):
        create_element_dss(name_dss, element, ruta_archivo)
    print('Data loaded and .DSS files created')

def create_scripts_OpenDSS(name_dss, workbook, ruta_raiz, name_folder):
    create_cases(name_dss, workbook, ruta_raiz, name_folder)