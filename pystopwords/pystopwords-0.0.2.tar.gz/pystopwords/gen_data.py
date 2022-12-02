"""
从原始数据处理成txt
"""

import os
import yaml
import json


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
RAW_DATA_DIR = os.path.join(CURRENT_DIR, '../data-raw')
DATA_DIR = os.path.join(CURRENT_DIR, './data')

word_set = set()

def dfs_yaml(info):
    """
    获取到yaml叶子结点的内容
    """
    if isinstance(info, str):
        return [info]
    res = []
    if isinstance(info, list):
        for elem in info:
            res += dfs_yaml(elem)
    if isinstance(info, dict):
        for key in info:
            res += dfs_yaml(info[key])
    return res



def format_file(input_file, output_file, input_format):
    with open(input_file) as f, open(output_file, 'w') as fout:

        if input_format == 'yaml':
            info_list = dfs_yaml(yaml.safe_load(f))
        elif input_format == 'json':
            info_list = json.load(f)['zh']
        elif input_format == 'txt':
            info_list = f.readlines()
    
        for elem in info_list:
            elem = elem.strip('\r\n')
            if not elem:
                continue
            fout.write(elem)
            word_set.add(elem)
            fout.write("\n")


# 中科院计算所
format_file(os.path.join(RAW_DATA_DIR, 'ict/stopWord.txt'),
            os.path.join(DATA_DIR, 'stopwords.zh.ict.txt'), 'txt')

# 百度
format_file(os.path.join(RAW_DATA_DIR, 'baidu/百度停用词表.txt'),
            os.path.join(DATA_DIR, 'stopwords.zh.baidu.txt'), 'txt')

# 哈工大
format_file(os.path.join(RAW_DATA_DIR, 'hit/哈工大停用词表.txt'),
            os.path.join(DATA_DIR, 'stopwords.zh.hit.txt'), 'txt')

# 川大
format_file(os.path.join(RAW_DATA_DIR, 'scu/四川大学机器智能实验室停用词库.txt'),
            os.path.join(DATA_DIR, 'stopwords.zh.scu.txt'), 'txt')

# 中文
format_file(os.path.join(RAW_DATA_DIR, 'cn/中文停用词表.txt'),
            os.path.join(DATA_DIR, 'stopwords.zh.cn.txt'), 'txt')


# process marimo
format_file(os.path.join(RAW_DATA_DIR, 'marimo/stopwords_zh_simplified.yml'),
            os.path.join(DATA_DIR, 'stopwords.zh.marimo.txt'), 'yaml')

# process stopwords-iso
format_file(os.path.join(RAW_DATA_DIR, 'stopwords-iso/stopwords-iso.json'),
            os.path.join(DATA_DIR, 'stopwords.zh.iso.txt'), 'json')


# write all
with open(os.path.join(DATA_DIR, 'stopwords.zh.all.txt'), 'w') as fout:

    for elem in word_set:
        elem = elem.strip('\r\n')
        if not elem:
            continue
        fout.write(elem)
        fout.write("\n")




