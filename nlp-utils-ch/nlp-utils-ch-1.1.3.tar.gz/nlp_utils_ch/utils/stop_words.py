#!user/bin/python
# _*_ coding: utf-8 _*_
# @Author      :   Jesper
# @Time        :   2020/11/11 20:31
# @Description :

import os
current_dir = os.path.dirname(__file__)

stop_symbol_path = os.path.join(current_dir, "../resources/symbol.txt")
stop_ch_path = os.path.join(current_dir, "../resources/stopwords.txt")

stop_symbol_chars = list()
stop_ch_chars = list()


with open(stop_symbol_path, "r") as f:
	for line in f.readlines():
		stop_symbol_chars.append(line.strip())

with open(stop_ch_path, "r") as f:
	for line in f.readlines():
		stop_ch_chars.append(line.strip())
