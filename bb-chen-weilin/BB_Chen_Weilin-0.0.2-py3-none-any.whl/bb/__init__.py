import random


def name_to_bb_nick_name(name: str):
    name_to_nick_name = {'陈伟林':'handsome boy', '陈渊琪':'老逼', '陈东海':'冬瓜','肖晓红':'小伟红'}
    if name not in name_to_nick_name.keys():
        return '宁您倒底佳宁'
    return name_to_nick_name[name]


def random_bb():
    name_list = ['陈伟林','陈渊琪','陈东海','肖晓红']
    return random.sample(name_list, k=1)[0]