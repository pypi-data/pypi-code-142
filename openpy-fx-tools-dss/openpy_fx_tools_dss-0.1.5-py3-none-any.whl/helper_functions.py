# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import pandas as pd
import os.path
import openpyxl
import logging


def characters_delete(DataFrame: pd.DataFrame, column: str) -> object:
    """
    Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS

    :param DataFrame: Name of the selected dataFrame
    :param column: Column name of the selected dataFrame
    :return:
    """
    characters_delete_space = [' ', '  ', '   ']
    for i in characters_delete_space:
        DataFrame[column] = DataFrame[column].apply(str).str.replace(i, '', regex=True)

    characters_delete = ['-', '/', '*', '.', '(', ')', 'á', 'é', 'í', 'ó', 'ú']
    for k in characters_delete:
        DataFrame[column] = DataFrame[column].apply(str).str.replace(k, '_', regex=True)
        # DataFrame[column] = DataFrame[column].str.replace(k, '', regex=True)


def characters_delete_phase(DataFrame: pd.DataFrame, column: str):
    DataFrame[column] = DataFrame[column].astype(str)
    DataFrame[column] = DataFrame[column].str.replace('.1', '')
    DataFrame[column] = DataFrame[column].str.replace('.2', '')
    DataFrame[column] = DataFrame[column].str.replace('.3', '')
    DataFrame[column] = DataFrame[column].str.replace('.4', '')


def characters_delete_phase_2(DataFrame: pd.DataFrame, column: str):
    characters_delete = ['.1', '.2', '.3', '.4']
    # characters_delete = ['.1.2.3.4', '.1.2.3', '.1', '.2', '.3', '.4']
    for k in characters_delete:
        DataFrame[column] = DataFrame[column].str.replace(k, '')
        # DataFrame[column] = DataFrame[column].str.replace(k, '', regex=True)
        # DataFrame[column] = DataFrame[column].apply(str).str.replace(k, '', regex=True)


def clean_database(filename: str, path_open: str, path_save: str):
    if not os.path.isfile(filename):
        return None
    xls = pd.ExcelFile(filename)
    sheets = xls.sheet_names
    book = openpyxl.load_workbook(path_open)
    for i in sheets:
        sheet = book[i]
        sheet.delete_rows(2, sheet.max_row - 1)
    book.save(path_save)


def readAllSheets(filename: str):
    """
    Read the .xls file. Store the DataFrame in a dictionary and retrieve all the names of the sheets

    :param filename: DigSilent database file in xls format
    :return: results, sheets
    """

    if not os.path.isfile(filename):
        return None
    xls = pd.ExcelFile(filename)
    sheets = xls.sheet_names
    results = {}
    for sheet in sheets:
        results[sheet] = xls.parse(sheet)
    xls.close()
    return results, sheets

def is_float(variable):
	try:
		float(variable)
		return True
	except:
		return False

def _save_BBDD_temp_xlsx(workbook_DSS: str, elem_select: list, BBDD_OpenDSS: dict, out_path: str, all_elem_DSS: bool):
    """
    Generates the .xlsx file, with xlsx_data format for OpenDSS

    :param workbook_DSS:
    :param elem_select:
    :param BBDD_OpenDSS:
    :param out_path:
    :return:
    """
    if len(elem_select) != 0:
        all_elem_DSS = False
        elem_select.append('Buscoords')

    with pd.ExcelWriter(f'{out_path}\{workbook_DSS}') as writer:
        for elem_name, DF_elem_DSS in BBDD_OpenDSS.items():
            if all_elem_DSS:
                DF_elem_DSS.to_excel(writer, sheet_name=elem_name, index=False)
            else:
                for elem_aux in elem_select:
                    if elem_aux == elem_name:
                        DF_elem_DSS.to_excel(writer, sheet_name=elem_name, index=False)
                if DF_elem_DSS.empty:
                    pass
                else:
                    DF_elem_DSS.to_excel(writer, sheet_name=elem_name, index=False)


def _save_BBDD_xlsx(workbook_DSS: str, BBDD_OpenDSS: dict, out_path: str, add_empty: bool):
    """
    Generates the .xlsx file, with xlsx_data format for OpenDSS

    :param workbook_DSS:
    :param elements_OpenDSS:
    :param BBDD_OpenDSS:
    :param out_path:
    :return:
    """
    try:
        with pd.ExcelWriter(f'{out_path}\{workbook_DSS}') as writer:
            for elem_name, DF_elem_DSS in BBDD_OpenDSS.items():
                if add_empty:
                    DF_elem_DSS.to_excel(writer, sheet_name=elem_name, index=False)
                else:
                    if DF_elem_DSS.empty:
                        pass
                    else:
                        DF_elem_DSS.to_excel(writer, sheet_name=elem_name, index=False)
    except PermissionError:

        writer = pd.ExcelWriter(f'{out_path}\{workbook_DSS}')
        writer.close()


def check_if_element_exists(BBDD_elem_DigS: dict, name_sheets: list):
    """
    According to a list of elements, it checks if they are found in the DigSilent database

    :param BBDD_elem_DigS: DigSilent database file in xls format
    :param name_sheets: List of sheets from DigSilent
    :return: BBDD_DigS
    """
    message = '\n'
    list_DSS = ['General', 'BlkDef', 'ChaRef', 'ElmComp', 'ElmCoup', 'ElmDsl', 'ElmFeeder', 'ElmLne', 'ElmLod',
                'ElmSubstat',
                'ElmNet', 'ElmShnt', 'ElmSym', 'ElmTerm', 'ElmTr2', 'ElmTr3', 'ElmXnet', 'IntFolder', 'IntGrf',
                'IntGrfcon', 'IntGrfnet', 'StaCubic', 'StaSwitch', 'TypGeo', 'TypCon', 'TypLne', 'TypLod', 'TypSym',
                'TypTow', 'TypTr2', 'TypTr3', 'RelFuse', 'IntFolder']

    for name_sheet in list_DSS:
        if len([x for x in [name_sheet] if x in name_sheets]) == 1:
            print(f'Loading {name_sheet} file: With xlsx_data')
            message = message + f'Loading {name_sheet} file: With xlsx_data\n'
        else:
            message = message + f'Loading {name_sheet} file: With xlsx_data\n'
            print(f'Loading {name_sheet} file: Empty')
            if name_sheet == 'General':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(columns=['ID(a:40)', 'Descr(a:40)', 'Val(a:40)'])

            elif name_sheet == 'BlkDef':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)'])

            elif name_sheet == 'ChaRef':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)'])

            elif name_sheet == 'ElmComp':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'outserv(i)',
                             'typ_id(p)'])

            elif name_sheet == 'ElmCoup':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'typ_id(p)',
                             'on_off(i)', 'aUsage(a:4)', 'chr_name(a:20)'])

            elif name_sheet == 'ElmDsl':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'typ_id(p)', 'outserv(i)'])

            elif name_sheet == 'ElmFeeder':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'obj_id(p)',
                             'iorient(i)', 'i_scale(i)', 'Iset(r)', 'icolor(i)',
                             'outserv(i)'])

            elif name_sheet == 'ElmLne':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'bus1(p)', 'bus2(p)', 'fold_id(p)', 'typ_id(p)', 'dline(r)',
                             'chr_name(a:20)', 'Inom(r)', 'Inom_a(r)', 'outserv(i)', 'rearth(r)', 'c_pcond(p)',
                             'c_ptow(p)', 'c_pcoup(p)', 'cpBranch(p)', 'for_name(a:40)', 'Unom(r)', 'R1(r)', 'X1(r)',
                             'R0(r)', 'X0(r)', 'C1(r)', 'C0(r)', 'B1(r)', 'B0(r)', 'G1(r)', 'G0(r)'])

            elif name_sheet == 'ElmLod':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'typ_id(p)', 'chr_name(a:20)',
                             'plini(r)', 'qlini(r)', 'scale0(r)'])

            elif name_sheet == 'ElmLod':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'typ_id(p)', 'chr_name(a:20)',
                             'plini(r)', 'qlini(r)', 'scale0(r)'])

            elif name_sheet == 'ElmNet':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'frnom(r)'])

            elif name_sheet == 'ElmShnt':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'chr_name(a:20)', 'shtype(i)', 'ushnm(r)',
                             'qcapn(r)', 'ncapx(i)', 'ncapa(i)', 'outserv(i)'])

            elif name_sheet == 'ElmSym':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'typ_id(p)',
                             'ngnum(i)', 'i_mot(i)', 'chr_name(a:20)', 'outserv(i)',
                             'pgini(r)', 'qgini(r)', 'usetp(r)', 'iv_mode(i)',
                             'q_min(r)',
                             'q_max(r)'])

            elif name_sheet == 'ElmTerm':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'typ_id(p)', 'iUsage(i)', 'uknom(r)',
                             'chr_name(a:20)', 'outserv(i)', 'GPSlat(r)', 'GPSlon(r)', 'cDisplayName(a)', 'NodeName(a)',
                             'cpBranch(p)', 'cpZone(p)', 'cpArea(p)', 'cpSubstat(p)', 'systype(i)', 'phtech(i)',
                             'unknom(r)', 'cPosLne(r)', 'iminus(i)', 'iEarth(i)', 'cStatName(a)', 'UcteNodeName(a)',
                             'cpGrid(p)', 'cpOwner(p)', 'cpOperator(p)', 'cpSite(p)', 'cpMeteostat(p)', 'cpHeadFold(p)',
                             'ciOutaged(i)', 'ciEnergized(i)', 'ciEarthed(i)', 'cpSupplyTransformer(p)',
                             'cpSupplyTrfStation(p)', 'cpSupplySubstation(p)'])

            elif name_sheet == 'ElmTr2':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'typ_id(p)',
                             'outserv(i)', 'nntap(i)', 'sernum(a:20)', 'constr(i)',
                             'chr_name(a:20)'])

            elif name_sheet == 'ElmTr3':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'typ_id(p)',
                             'outserv(i)', 'nntap(i)', 'sernum(a:20)', 'constr(i)',
                             'chr_name(a:20)'])

            elif name_sheet == 'ElmXnet':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'outserv(i)', 'snss(r)', 'rntxn(r)',
                             'z2tz1(r)', 'snssmin(r)', 'rntxnmin(r)', 'z2tz1min(r)', 'chr_name(a:20)', 'bustp(a:2)',
                             'pgini(r)', 'qgini(r)', 'phiini(r)', 'usetp(r)'])

            elif name_sheet == 'IntFolder':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)'])

            elif name_sheet == 'IntGrf':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'iCol(i)',
                             'iVis(i)', 'iLevel(i)', 'rCenterX(r)', 'rCenterY(r)',
                             'sSymNam(a:40)',
                             'pDataObj(p)', 'iRot(i)', 'rSizeX(r)', 'rSizeY(r)'])

            elif name_sheet == 'IntGrfcon':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'rX:SIZEROW(i)', 'rX:0(r)', 'rX:1(r)',
                             'rX:2(r)', 'rY:SIZEROW(i)', 'rY:0(r)', 'rY:1(r)', 'rY:2(r)'])

            elif name_sheet == 'IntGrfnet':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'snap_on(i)',
                             'grid_on(i)', 'ortho_on(i)'])

            elif name_sheet == 'StaCubic':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'chr_name(a:20)',
                             'obj_bus(i)', 'obj_id(p)', 'it2p1(i)', 'it2p2(i)', 'it2p3(i)',
                             'cPhInfo(a)', 'nphase(i)'])

            elif name_sheet == 'StaSwitch':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'on_off(i)', 'typ_id(p)', 'iUse(i)'])

            elif name_sheet == 'TypCon':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'uline(r)',
                             'sline(r)', 'ncsub(i)', 'dsubc(r)', 'rpha(r)', 'diaco(r)',
                             'erpha(r)'])

            elif name_sheet == 'TypLne':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'uline(r)', 'sline(r)', 'aohl_(a:3)',
                             'rline(r)', 'xline(r)', 'cline(r)', 'rline0(r)', 'xline0(r)', 'cline0(r)', 'rtemp(r)',
                             'Ithr(r)', 'chr_name(a:20)'])

            elif name_sheet == 'TypLod':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'phtech(i)', 'kpu(r)', 'kqu(r)', 'systp(i)',
                             'aP(r)', 'bP(r)', 'cP(r)', 'aQ(r)', 'bQ(r)', 'cQ(r)', 'kpu0(r)', 'kpu1(r)', 'kqu0(r)',
                             'kqu1(r)', 'chr_name(a:20)'])

            elif name_sheet == 'TypSym':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'sgn(r)', 'ugn(r)', 'cosn(r)', 'xd(r)',
                             'xq(r)', 'xdsss(r)', 'rstr(r)', 'xdsat(r)', 'satur(i)'])

            elif name_sheet == 'TypTow':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'frnom(r)',
                             'nlear(i)', 'nlcir(i)', 'gearth(r)', 'i_mode(i)'])

            elif name_sheet == 'TypTr2':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'strn(r)', 'frnom(r)', 'utrn_h(r)',
                             'utrn_l(r)', 'uktr(r)', 'pcutr(r)', 'uk0tr(r)', 'ur0tr(r)', 'tr2cn_h(a:2)', 'tr2cn_l(a:2)',
                             'nt2ag(r)', 'curmg(r)', 'pfe(r)', 'zx0hl_n(r)', 'tap_side(i)', 'dutap(r)', 'phitr(r)',
                             'nntap0(i)', 'ntpmn(i)', 'ntpmx(i)', 'manuf(a:20)', 'chr_name(a:20)'])

            elif name_sheet == 'TypTr3':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'strn(r)', 'frnom(r)', 'utrn_h(r)',
                             'utrn_l(r)', 'uktr(r)', 'pcutr(r)', 'uk0tr(r)', 'ur0tr(r)', 'tr2cn_h(a:2)', 'tr2cn_l(a:2)',
                             'nt2ag(r)', 'curmg(r)', 'pfe(r)', 'zx0hl_n(r)', 'tap_side(i)', 'dutap(r)', 'phitr(r)',
                             'nntap0(i)', 'ntpmn(i)', 'ntpmx(i)', 'manuf(a:20)', 'chr_name(a:20)'])

            elif name_sheet == 'RelFuse':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'typ_id(p)', 'on_off(i)', 'aUsage(a:4)',
                             'chr_name(a:20)', 'outserv(i)', 'bus1(p)', 'bus2(p)', 'nphase(i)', 'nneutral(i)',
                             'c_type(a)', 'cpOperator(p)', 'ciEnergized(i)'])


            elif name_sheet == 'TypGeo':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'nlear(i)', 'nlcir(i)', 'xy_e:SIZEROW(i)',
                             'xy_e:SIZECOL(i)', 'xy_c:SIZEROW(i)', 'xy_c:SIZECOL(i)', 'xy_c:0:0(r)', 'xy_c:0:1(r)',
                             'xy_c:0:2(r)', 'xy_c:0:3(r)', 'xy_c:0:4(r)', 'xy_c:0:5(r)', 'xy_c:0:6(r)'])


            elif name_sheet == 'ElmSubstat':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'sShort(a:6)', 'Unom(r)', 'GPSlat(r)',
                             'GPSlon(r)'])

            elif name_sheet == 'IntFolder':
                BBDD_elem_DigS[name_sheet] = pd.DataFrame(
                    columns=['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)'])

    return BBDD_elem_DigS, message


def merge_ElmTerm_StaCubic(DataFrame_ElmTerm: pd.DataFrame, DataFrame_StaCubic: pd.DataFrame) -> pd.DataFrame:
    """
    Join ElmTerm and StaCubic

    :param DataFrame_ElmTerm:Excel sheet named ElmTerm from the Digsilent database, stored in a DataFrame
    :param DataFrame_StaCubic:Excel sheet named StaCubic from the Digsilent database, stored in a DataFrame
    :return: merge_StaCubic_ElmTerm
    """
    'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
    characters_delete(DataFrame_ElmTerm, 'loc_name(a:40)')

    keys_DataFrame_ElmTerm = DataFrame_ElmTerm.loc[:, ['ID(a:40)', 'loc_name(a:40)', 'uknom(r)', 'ciEnergized(i)']]
    keys_DataFrame_ElmTerm = keys_DataFrame_ElmTerm[
        keys_DataFrame_ElmTerm['ciEnergized(i)'] == 1]  # Filters energized elements

    keys_DataFrame_StaCubic = DataFrame_StaCubic.loc[:, ['ID(a:40)', 'fold_id(p)', 'nphase(i)', 'phase_DSS']]

    'Join the DataFrame_ElmTerm and DataFrame_StaCubic with the key'
    merge_StaCubic_ElmTerm = pd.merge(keys_DataFrame_ElmTerm, keys_DataFrame_StaCubic, how='inner', left_on='ID(a:40)',
                                      right_on='fold_id(p)')
    merge_StaCubic_ElmTerm['Bus_name_DSS'] = merge_StaCubic_ElmTerm['loc_name(a:40)'] + merge_StaCubic_ElmTerm[
        'phase_DSS']
    merge_StaCubic_ElmTerm = merge_StaCubic_ElmTerm[
        ['ID(a:40)_y', 'fold_id(p)', 'loc_name(a:40)', 'uknom(r)', 'nphase(i)', 'Bus_name_DSS', 'phase_DSS']]
    merge_StaCubic_ElmTerm = merge_StaCubic_ElmTerm.rename(columns={'ID(a:40)_y': 'ID(a:40)'})

    return merge_StaCubic_ElmTerm


def merge_ElmTerm_StaCubic_orig(DataFrame_ElmTerm: pd.DataFrame, DataFrame_StaCubic: pd.DataFrame) -> pd.DataFrame:
    """
    Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS

    :param DataFrame_ElmTerm: Excel sheet named ElmTerm from the Digsilent database, stored in a DataFrame
    :param DataFrame_StaCubic: Excel sheet named StaCubic from the Digsilent database, stored in a DataFrame
    :return: merge_StaCubic_ElmTerm
    """
    'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
    characters_delete(DataFrame_ElmTerm, 'loc_name(a:40)')

    keys_DataFrame_ElmTerm = DataFrame_ElmTerm.loc[:, ['ID(a:40)', 'loc_name(a:40)', 'uknom(r)']]
    keys_DataFrame_StaCubic = DataFrame_StaCubic.loc[:, ['ID(a:40)', 'fold_id(p)', 'nphase(i)', 'phase_DSS']]

    'Join the DataFrame_ElmTerm and DataFrame_StaCubic with the key'
    merge_StaCubic_ElmTerm = pd.merge(keys_DataFrame_ElmTerm, keys_DataFrame_StaCubic, how='inner', left_on='ID(a:40)',
                                      right_on='fold_id(p)')
    merge_StaCubic_ElmTerm['Bus_name_DSS'] = merge_StaCubic_ElmTerm["loc_name(a:40)"] + merge_StaCubic_ElmTerm[
        "phase_DSS"]
    merge_StaCubic_ElmTerm = merge_StaCubic_ElmTerm[
        ['ID(a:40)_y', 'fold_id(p)', 'loc_name(a:40)', 'uknom(r)', 'nphase(i)', 'Bus_name_DSS']]
    merge_StaCubic_ElmTerm = merge_StaCubic_ElmTerm.rename(columns={'ID(a:40)_y': 'ID(a:40)'})

    return merge_StaCubic_ElmTerm


def name_folders_elements(dict_df_DigS: dict) -> dict:
    '''
    Add to Id_elem the name of the folder that belongs to the Digsilent database

    :param dict_df_DigS:DigSilent database file in xls format
    :return: dict_df_DigS
    '''

    DataFrame_IntFolder = dict_df_DigS['IntFolder']
    if DataFrame_IntFolder.empty == True:
        pass
    else:
        if dict_df_DigS['TypCon'].empty == True:
            pass
        else:
            dict_df_DigS['TypCon'] = merge_name_folders_elements(DataFrame_IntFolder=DataFrame_IntFolder,
                                                                 name_elem='TypCon',
                                                                 dict_df_DigS=dict_df_DigS)
        if dict_df_DigS['TypTow'].empty == True:
            pass
        else:
            dict_df_DigS['TypTow'] = merge_name_folders_elements(DataFrame_IntFolder=DataFrame_IntFolder,
                                                                 name_elem='TypTow',
                                                                 dict_df_DigS=dict_df_DigS)
        if dict_df_DigS['TypGeo'].empty == True:
            pass
        else:
            dict_df_DigS['TypGeo'] = merge_name_folders_elements(DataFrame_IntFolder=DataFrame_IntFolder,
                                                                 name_elem='TypGeo',
                                                                 dict_df_DigS=dict_df_DigS)
        if dict_df_DigS['TypLne'].empty == True:
            pass
        else:
            dict_df_DigS['TypLne'] = merge_name_folders_elements(DataFrame_IntFolder=DataFrame_IntFolder,
                                                                 name_elem='TypLne',
                                                                 dict_df_DigS=dict_df_DigS)
        if dict_df_DigS['TypTr2'].empty == True:
            pass
        else:
            dict_df_DigS['TypTr2'] = merge_name_folders_elements(DataFrame_IntFolder=DataFrame_IntFolder,
                                                                 name_elem='TypTr2',
                                                                 dict_df_DigS=dict_df_DigS)
        if dict_df_DigS['TypTr3'].empty == True:
            pass
        else:
            dict_df_DigS['TypTr3'] = merge_name_folders_elements(DataFrame_IntFolder=DataFrame_IntFolder,
                                                                 name_elem='TypTr3',
                                                                 dict_df_DigS=dict_df_DigS)
    return dict_df_DigS


def merge_name_folders_elements(DataFrame_IntFolder: pd.DataFrame, name_elem: str, dict_df_DigS: dict):
    '''
    Join the Id_elem with the name of the folder it belongs to

    :param DataFrame_IntFolder:DataFrame -> IntFolder
    :param name_elem:Type the element
    :param dict_df_DigS:DigSilent database file in xls format
    :return: DataFrame_elem
    '''

    DataFrame_IntFolder = DataFrame_IntFolder[['ID(a:40)', 'loc_name(a:40)']]
    DataFrame_elem = dict_df_DigS[name_elem]
    merge_TypCon_IntFolder = pd.merge(DataFrame_elem[['loc_name(a:40)', 'fold_id(p)']], DataFrame_IntFolder,
                                      how='left', left_on='fold_id(p)', right_on='ID(a:40)',
                                      suffixes=('_x', '_y')).fillna('')

    for index, row in merge_TypCon_IntFolder.iterrows():
        if merge_TypCon_IntFolder['loc_name(a:40)_y'][index] == '':
            DataFrame_elem['loc_name(a:40)'][index] = merge_TypCon_IntFolder['loc_name(a:40)_x'][index]
        else:
            DataFrame_elem['loc_name(a:40)'][index] = merge_TypCon_IntFolder['loc_name(a:40)_x'][index] + f' ' + \
                                                      merge_TypCon_IntFolder['loc_name(a:40)_y'][index]
    return DataFrame_elem


def file_logging_info(logfilename: str, message: str):
    logging.basicConfig(filename=f'{logfilename}.log',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info(message)


def check_version_of_BBDD(BBDD_DigS: dict, name_sheets: list):
    version = int(BBDD_DigS['General']['Val(a:40)'][0])

    if version == 6:
        for name in name_sheets:
            BBDD_DigS[name] = BBDD_DigS[name].rename(columns={'FID(a:40)': 'ID(a:40)'})

    elif version == 5:
        pass
    else:
        print('Export the database in Digsilent in version 5 (recommended) or 6')
        exit()

    return BBDD_DigS, name_sheets
