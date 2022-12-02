import pandas as pd
import os
# IMPORTANT! pip install openpyxl

##INTERNAL Function, not meant for programmer's usage
def checkdir(modelname):
    rootPath = os.path.expanduser('~\.cache/')
    if not os.path.isdir(rootPath):
        os.makedirs(os.getcwd()+'/.cache/randomlib/'+modelname,exist_ok=True)
        return os.getcwd()
    else:
        rootPath = os.path.expanduser('~\.cache/')
        os.chdir(rootPath)
        os.makedirs('randomlib/'+modelname,exist_ok=True)
        return '~'

##INTERNAL Function, not meant for programmer's usage
def downloadMahasent():
    dataset_type = {
        'tweets-train.csv': 'https://raw.githubusercontent.com/l3cube-pune/MarathiNLP/main/L3CubeMahaSent%20Dataset/tweets-train.csv',
        'tweets-test.csv': 'https://raw.githubusercontent.com/l3cube-pune/MarathiNLP/main/L3CubeMahaSent%20Dataset/tweets-test.csv',
        'tweets-valid.csv': 'https://raw.githubusercontent.com/l3cube-pune/MarathiNLP/main/L3CubeMahaSent%20Dataset/tweets-valid.csv',
        'tweets-extra.csv': 'https://raw.githubusercontent.com/l3cube-pune/MarathiNLP/main/L3CubeMahaSent%20Dataset/tweets-extra.csv'
    }
    result = {}
    rootPath = os.path.expanduser(checkdir('mahaSent'))
    childPath = os.path.expanduser(rootPath+'/.cache/randomlib/mahaSent')
    os.chdir(childPath)
    for key in dataset_type:
        df = pd.read_csv(dataset_type[key])
        csv_df = df.to_csv(key, index=False, encoding='UTF-16')
        result[key.split(".")[0]] = df  # add df to an dictionary
    os.chdir(rootPath)
    return result

##INTERNAL Function, not meant for programmer's usage
def downloadMahaner():
    iob = {
        'train_iob.txt': 'https://github.com/l3cube-pune/MarathiNLP/blob/main/L3Cube-MahaNER/IOB/train_iob.txt?raw=true',
        'test_iob.txt': 'https://raw.githubusercontent.com/l3cube-pune/MarathiNLP/main/L3Cube-MahaNER/IOB/test_iob.txt',
        'valid_iob.txt': 'https://raw.githubusercontent.com/l3cube-pune/MarathiNLP/main/L3Cube-MahaNER/IOB/valid_iob.txt',
    }
    non_iob = {
        'train_noniob.txt': 'https://github.com/l3cube-pune/MarathiNLP/blob/main/L3Cube-MahaNER/NON_IOB/train_noniob.txt?raw=true',
        'test_noniob.txt': 'https://raw.githubusercontent.com/l3cube-pune/MarathiNLP/main/L3Cube-MahaNER/NON_IOB/test_noniob.txt',
        'valid_noniob.txt': 'https://raw.githubusercontent.com/l3cube-pune/MarathiNLP/main/L3Cube-MahaNER/NON_IOB/valid_noniob.txt',
    }
    result = {'iob': {}, 'non_iob': {}}

    rootPath = os.path.expanduser(checkdir('mahaNER/IOB'))
    rootPath = os.path.expanduser(checkdir('mahaNER/NON_IOB'))

    childPath = os.path.expanduser(rootPath+'/.cache/randomlib/mahaNER/IOB')
    os.chdir(childPath)
    for key in iob:
        df = pd.read_csv(iob[key], sep=" ")
        txt_df = df.to_csv(key, index=False, encoding='UTF-16')
        result['iob'][key.split(".")[0]] = df  # add df to an dictionary

    childPath = os.path.expanduser(rootPath+'/.cache/randomlib/mahaNER/NON_IOB')
    os.chdir(childPath)
    for key in non_iob:
        df = pd.read_csv(non_iob[key], sep="\t")
        txt_df = df.to_csv(key, index=False, encoding='UTF-16', sep="\t")
        result['non_iob'][key.split(".")[0]] = df  # add df to an dictionary
    
    os.chdir(rootPath)
    return result

##INTERNAL Function, not meant for programmer's usage
def downloadMahahate():
    class_2 = {
        'hate_bin_train.xlsx': 'https://github.com/l3cube-pune/MarathiNLP/blob/main/L3Cube-MahaHate/2-class/hate_bin_train.xlsx?raw=true',
        'hate_bin_test.xlsx': 'https://github.com/l3cube-pune/MarathiNLP/blob/main/L3Cube-MahaHate/2-class/hate_bin_test.xlsx?raw=true',
        'hate_bin_valid.xlsx': 'https://github.com/l3cube-pune/MarathiNLP/blob/main/L3Cube-MahaHate/2-class/hate_bin_valid.xlsx?raw=true',
    }
    class_4 = {
        'hate_train.xlsx': 'https://github.com/l3cube-pune/MarathiNLP/blob/main/L3Cube-MahaHate/4-class/hate_train.xlsx?raw=true',
        'hate_test.xlsx': 'https://github.com/l3cube-pune/MarathiNLP/blob/main/L3Cube-MahaHate/4-class/hate_test.xlsx?raw=true',
        'hate_valid.xlsx': 'https://github.com/l3cube-pune/MarathiNLP/blob/main/L3Cube-MahaHate/4-class/hate_valid.xlsx?raw=true',
    }
    result = {'2-class': {}, '4-class': {}}

    rootPath = os.path.expanduser(checkdir('mahaHate/2-class'))
    rootPath = os.path.expanduser(checkdir('mahaHate/4-class'))

    childPath = os.path.expanduser(rootPath+'/.cache/randomlib/mahaHate/2-class')
    os.chdir(childPath)
    for key in class_2:
        df = pd.read_excel(class_2[key])
        xlsx_df = df.to_excel(key, index=False, encoding='UTF-16')
        result['2-class'][key.split(".")[0]] = df  # add df to an dictionary

    childPath = os.path.expanduser(rootPath+'/.cache/randomlib/mahaHate/4-class')
    os.chdir(childPath)
    for key in class_4:
        df = pd.read_excel(class_4[key])
        xlsx_df = df.to_excel(key, index=False, encoding='UTF-16')
        result['4-class'][key.split(".")[0]] = df  # add df to an dictionary
    os.chdir(rootPath)
    return result


def loadDatasets(name):

    if name == 'mahaSent':
        res_dict = downloadMahasent()
        return res_dict
    elif name == 'mahaHate':
        res_dict = downloadMahahate()
        return res_dict
    elif name == 'mahaNER':
        res_dict = downloadMahaner()
        return res_dict
