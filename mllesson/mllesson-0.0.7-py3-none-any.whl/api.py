#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests
import json
import os

def getdict():
    '''
    本函数用于调取数据集名称与文件名称的字典，在下载时会被getdataset函数调用。
    '''
    r = requests.get('https://dataset-mllesson-nvxkumssxj.cn-beijing.fcapp.run/getdict')
    return json.loads(r.text)

def getnames():
    '''
    本函数用于查询可下载的数据集名称
    '''
    r = requests.get('https://dataset-mllesson-nvxkumssxj.cn-beijing.fcapp.run/getnames')
    return json.loads(r.text)


def getdataset(name:str, filedir:str='./'):
    '''
    本函数用于下载机器学习数据集
    :param name: 数据集名称，可为iris或fashion-mnist
    :param filedir: 数据集下载后放置的位置
    '''
    filenames = getdict()
    data = {"name": name}
    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    r = requests.post(url='https://dataset-mllesson-nvxkumssxj.cn-beijing.fcapp.run/getdataset',
                      json=json.dumps(data), headers=headers)
    savedir = os.path.join(filedir, filenames[name])

    if r.status_code == 200:
        with open(savedir, 'wb') as file:
            file.write(r.content)
    else:
        print('错误码:{}'.format(r.status_code))
