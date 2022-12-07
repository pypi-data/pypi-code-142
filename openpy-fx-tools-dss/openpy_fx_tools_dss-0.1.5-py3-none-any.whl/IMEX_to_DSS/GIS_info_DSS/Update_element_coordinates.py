# -*- coding: utf-8 -*-
# @Time    : 27/06/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import pandas as pd
from openpy_fx_tools_dss.interface_dss import dss

def from_to_bus(type_element, num_cond, node_order, bus1, bus2):
    if type_element == True:
        if num_cond == 1:
            aux1 = bus1.find('.' + str(node_order[0]))
            if aux1 == -1:
                from_bus = bus1
            else:
                from_bus = bus1[:aux1]
            to_bus = ''
        elif num_cond == 2:
            aux1 = bus1.find('.' + str(node_order[0]))
            if aux1 == -1:
                from_bus = bus1
            else:
                from_bus = bus1[:aux1]
            to_bus = ''
        elif num_cond == 3:
            aux1 = bus1.find('.' + str(node_order[0]))
            if aux1 == -1:
                from_bus = bus1
            else:
                from_bus = bus1[:aux1]
            to_bus = ''
        elif num_cond == 4:
            aux1 = bus1.find('.' + str(node_order[0]))
            if aux1 == -1:
                from_bus = bus1
            else:
                from_bus = bus1[:aux1]
            to_bus = ''

    else:
        if num_cond == 1:
            aux1 = bus1.find('.' + str(node_order[0]))
            aux2 = bus2.find('.' + str(node_order[1]))
            if aux1 == -1:
                from_bus = bus1
            else:
                from_bus = bus1[:aux1]

            if aux2 == -1:
                to_bus = bus2
            else:
                to_bus = bus2[:aux2]
        elif num_cond == 2:
            aux1 = bus1.find('.' + str(node_order[0]))
            aux2 = bus2.find('.' + str(node_order[2]))
            if aux1 == -1:
                from_bus = bus1
            else:
                from_bus = bus1[:aux1]

            if aux2 == -1:
                to_bus = bus2
            else:
                to_bus = bus2[:aux2]

        elif num_cond == 3:
            aux1 = bus1.find('.' + str(node_order[0]))
            aux2 = bus2.find('.' + str(node_order[3]))
            if aux1 == -1:
                from_bus = bus1
            else:
                from_bus = bus1[:aux1]

            if aux2 == -1:
                to_bus = bus2
            else:
                to_bus = bus2[:aux2]
        elif num_cond == 4:
            aux1 = bus1.find('.' + str(node_order[0]))
            aux2 = bus2.find('.' + str(node_order[4]))
            if aux1 == -1:
                from_bus = bus1
            else:
                from_bus = bus1[:aux1]
            if aux2 == -1:
                to_bus = bus2
            else:
                to_bus = bus2[:aux2]

    return from_bus, to_bus

def characters_delete(DataFrame: pd.DataFrame, column: str) -> object:
    """
    Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS

    :param DataFrame: Name of the selected dataFrame
    :param column: Column name of the selected dataFrame
    :return:
    """
    characters_delete_space = ['.1', '.2', '.3', '.4']
    for i in characters_delete_space:
        DataFrame[column] = DataFrame[column].replace({i: ''}, regex=True)

def save_BBDD_xlsx(workbook_DSS: str, elements_OpenDSS: list, BBDD_OpenDSS: dict, out_path:str):
    """
    Generates the .xlsx file, with xlsx_data format for OpenDSS

    :param workbook_DSS:
    :param elements_OpenDSS:
    :param BBDD_OpenDSS:
    :param out_path:
    :return:
    """

    writer = pd.ExcelWriter(f'{out_path}\{workbook_DSS}')
    for name in elements_OpenDSS:
        BBDD_OpenDSS[name].to_excel(writer, sheet_name=name, index=False)
    writer.save()
    writer.close()

def Update_coordinates_for_GIS(prj_name: str, DSS_file: str, save_path: str):
    '''
    Function that generates a .xlsx file with the coordinates for GIS of a circuit modeled in OpenDSS

    :param prj_name: Name of the new .xlsx file
    :param DSS_file: path_save where the OpenDSS file is located
    :param save_path: path_save where it is going to save
    :return:
    '''

    element_list = list()
    BBDD_Buscoords = dict()

    dss.text("ClearAll")
    dss.text(f"compile [{DSS_file}]")
    dss.solution_solve()

    df_Buscoords = pd.DataFrame(columns=['Id_node', 'GPSlat(r)', 'GPSlon(r)'])
    df_Vsource = pd.DataFrame(columns=['Id_Vsource', 'bus1'])
    df_Transformer = pd.DataFrame(columns=['Id_Transformer', 'bushv', 'buslv'])
    df_Load = pd.DataFrame(columns=['Id_Load', 'bus1'])
    df_Capacitor = pd.DataFrame(columns=['Id_Capacitor', 'bus1'])
    df_Line = pd.DataFrame(columns=['Id_Line', 'bus1', 'bus2'])
    df_Switch = pd.DataFrame(columns=['Id_Switch', 'bus1', 'bus2'])
    df_PVSystem = pd.DataFrame(columns=['Id_PVSystem', 'bus1'])

    list_bus_names = dss.circuit_all_bus_names()
    for bus in list_bus_names:
        dss.circuit_set_active_bus(bus)
        longitude = dss.bus_read_y()
        latitud = dss.bus_read_x()
        df_Buscoords = df_Buscoords.append(
            {'Id_node': bus, 'GPSlat(r)': latitud, 'GPSlon(r)': longitude}, ignore_index=True)
    elements = ['vsources', 'transformers', 'lines', 'loads', 'capacitors']
    BBDD_Buscoords['Buscoords'] = df_Buscoords
    element_list.append('Buscoords')

    'Vsource'
    num_element = dss.vsources_count()
    dss.vsources_first()
    for num in range(num_element):
        name = dss.vsources_read_name()
        bus_name = dss.cktelement_read_bus_names()
        num_cond, node_order, bus1, bus2 = \
            dss.cktelement_num_conductors(), \
            dss.cktelement_node_order(), \
            dss.cktelement_read_bus_names()[0], ''
        from_bus, to_bus = from_to_bus(False, num_cond, node_order, bus1, bus2)

        df_Vsource = df_Vsource.append({'Id_Vsource': name, 'bus1': from_bus}, ignore_index=True)

    df_Vsource = pd.merge(df_Vsource, df_Buscoords, how='left', left_on='bus1', right_on='Id_node').rename(
        columns={'GPSlat(r)': 'GPSlat(r)_bus1', 'GPSlon(r)': 'GPSlon(r)_bus1'})
    df_Vsource = df_Vsource[['Id_Vsource', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1']]

    BBDD_Buscoords['Vsource'] = df_Vsource
    element_list.append('Vsource')

    'transformers'
    num_element = dss.transformers_count()
    dss.transformers_first()
    for num in range(num_element):
        name = dss.vsources_read_name()
        bus_name = dss.cktelement_read_bus_names()
        num_cond, node_order, bus1, bus2 = dss.cktelement_num_conductors(), dss.cktelement_node_order(), \
                                           dss.cktelement_read_bus_names()[0], dss.cktelement_read_bus_names()[1]
        from_bus, to_bus = from_to_bus(False, num_cond, node_order, bus1, bus2)

        df_Transformer = df_Transformer.append(
            {'Id_Transformer': name, 'bushv': from_bus, 'buslv': to_bus}, ignore_index=True)

        dss.transformers_next()

    df_Transformer = pd.merge(df_Transformer, df_Buscoords, how='left', left_on='bushv', right_on='Id_node')
    df_Transformer = pd.merge(df_Transformer, df_Buscoords, how='left', left_on='buslv', right_on='Id_node').rename(
        columns={'GPSlat(r)_x': 'GPSlat(r)_bushv', 'GPSlon(r)_x': 'GPSlon(r)_bushv',
                 'GPSlat(r)_y': 'GPSlat(r)_buslv', 'GPSlon(r)_y': 'GPSlon(r)_buslv'})

    df_Transformer = df_Transformer[
        ['Id_Transformer', 'bushv', 'GPSlat(r)_bushv', 'GPSlon(r)_bushv', 'buslv', 'GPSlat(r)_buslv', 'GPSlon(r)_buslv']
    ]

    BBDD_Buscoords['Transformer'] = df_Transformer
    element_list.append('Transformer')

    'Load'
    num_element = dss.loads_count()
    dss.loads_first()
    for num in range(num_element):
        name = dss.loads_read_name()
        bus_name = dss.cktelement_read_bus_names()
        num_cond, node_order, bus1, bus2 = dss.cktelement_num_conductors(), dss.cktelement_node_order(), \
                                           dss.cktelement_read_bus_names()[0], ''
        from_bus, to_bus = from_to_bus(True, num_cond, node_order, bus1, bus2)
        df_Load = df_Load.append({'Id_Load': name, 'bus1': from_bus}, ignore_index=True)
        dss.loads_next()

    df_Load = pd.merge(df_Load, df_Buscoords, how='left', left_on='bus1', right_on='Id_node').rename(
        columns={'GPSlat(r)': 'GPSlat(r)_bus1', 'GPSlon(r)': 'GPSlon(r)_bus1'})
    df_Load = df_Load[['Id_Load', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1']]

    BBDD_Buscoords['Load'] = df_Load
    element_list.append('Load')

    'Capacitor'
    num_element = dss.capacitors_count()
    dss.capacitors_first()
    for num in range(num_element):
        name = dss.capacitors_read_name()
        bus_name = dss.cktelement_read_bus_names()
        num_cond, node_order, bus1, bus2 = dss.cktelement_num_conductors(), dss.cktelement_node_order(), \
                                           dss.cktelement_read_bus_names()[0], ''
        from_bus, to_bus = from_to_bus(False, num_cond, node_order, bus1, bus2)
        df_Capacitor = df_Capacitor.append({'Id_Capacitor': name, 'bus1': from_bus}, ignore_index=True)
        dss.capacitors_next()

    df_Capacitor = pd.merge(df_Capacitor, df_Buscoords, how='left', left_on='bus1', right_on='Id_node').rename(
        columns={'GPSlat(r)': 'GPSlat(r)_bus1', 'GPSlon(r)': 'GPSlon(r)_bus1'})
    df_Capacitor = df_Capacitor[['Id_Capacitor', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1']]

    BBDD_Buscoords['Capacitor'] = df_Capacitor
    element_list.append('Capacitor')

    'Line'
    num_element = dss.lines_count()
    dss.lines_first()
    for num in range(num_element):
        name = dss.lines_read_name()
        bus_name = dss.cktelement_read_bus_names()
        num_cond, node_order, bus1, bus2 = dss.cktelement_num_conductors(), dss.cktelement_node_order(), \
                                           dss.cktelement_read_bus_names()[0], dss.cktelement_read_bus_names()[1]
        from_bus, to_bus = from_to_bus(False, num_cond, node_order, bus1, bus2)

        switch = dss.dssproperties_read_value('15')
        if switch == 'False':
            df_Line = df_Line.append(
                {'Id_Line': name, 'bus1': from_bus, 'bus2': to_bus}, ignore_index=True)

        if switch == 'True':
            df_Switch = df_Switch.append(
                {'Id_Switch': name, 'bus1': from_bus, 'bus2': to_bus}, ignore_index=True)

        dss.lines_next()
    df_Line = pd.merge(df_Line, df_Buscoords, how='left', left_on='bus1', right_on='Id_node')
    df_Line = pd.merge(df_Line, df_Buscoords, how='left', left_on='bus2', right_on='Id_node').rename(
        columns={'GPSlat(r)_x': 'GPSlat(r)_bus1', 'GPSlon(r)_x': 'GPSlon(r)_bus1',
                 'GPSlat(r)_y': 'GPSlat(r)_bus2', 'GPSlon(r)_y': 'GPSlon(r)_bus2'})

    df_Line = df_Line[['Id_Line',
                       'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1',
                       'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2']]

    BBDD_Buscoords['Line'] = df_Line
    element_list.append('Line')

    df_Switch = pd.merge(df_Switch, df_Buscoords, how='left', left_on='bus1', right_on='Id_node')
    df_Switch = pd.merge(df_Switch, df_Buscoords, how='left', left_on='bus2', right_on='Id_node').rename(
        columns={'GPSlat(r)_x': 'GPSlat(r)_bus1', 'GPSlon(r)_x': 'GPSlon(r)_bus1',
                 'GPSlat(r)_y': 'GPSlat(r)_bus2', 'GPSlon(r)_y': 'GPSlon(r)_bus2'})

    df_Switch = df_Switch[['Id_Switch',
                           'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1',
                           'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2']]
    BBDD_Buscoords['Switch'] = df_Switch
    element_list.append('Switch')

    'PVSystem'
    num_element = dss.pvsystems_count()
    dss.pvsystems_first()
    for num in range(num_element):
        name = dss.pvsystems_read_name()
        bus_name = dss.cktelement_read_bus_names()
        num_cond, node_order, bus1, bus2 = dss.cktelement_num_conductors(), dss.cktelement_node_order(), \
                                           dss.cktelement_read_bus_names()[0], ''
        from_bus, to_bus = from_to_bus(False, num_cond, node_order, bus1, bus2)
        df_PVSystem = df_PVSystem.append({'Id_PVSystem': name, 'bus1': from_bus}, ignore_index=True)
        dss.pvsystems_next()

    df_PVSystem = pd.merge(df_PVSystem, df_Buscoords, how='left', left_on='bus1', right_on='Id_node').rename(
        columns={'GPSlat(r)': 'GPSlat(r)_bus1', 'GPSlon(r)': 'GPSlon(r)_bus1'})
    df_PVSystem = df_PVSystem[['Id_PVSystem', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1']]

    BBDD_Buscoords['PVSystem'] = df_PVSystem
    element_list.append('PVSystem')

    workbook_aux = f'BBDD_Buscoords_{prj_name}.xlsx'
    save_BBDD_xlsx(workbook_DSS=workbook_aux, elements_OpenDSS=element_list,
                   BBDD_OpenDSS=BBDD_Buscoords, out_path=save_path)



