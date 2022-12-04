#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests
import json
import os

filenames = {'iris': 'iris.csv', 'fashion-mnist': 'Fashion-Mnist.zip'}


def getdataset(name:str, filedir:str='./'):
    '''
    本函数用于下载机器学习数据集
    :param name: 数据集名称，可为iris或fashion-mnist
    :param filedir: 数据集下载后放置的位置
    '''
    data = {"name": name}
    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    r = requests.post(url='http://at-api-test-sqtvletgcn.cn-beijing.fcapp.run/getdataset',
                      json=json.dumps(data), headers=headers)
    savedir = os.path.join(filedir, filenames[name])

    if r.status_code == 200:
        with open(savedir, 'wb') as file:
            file.write(r.content)
    else:
        print('错误码:{}'.format(r.status_code))
