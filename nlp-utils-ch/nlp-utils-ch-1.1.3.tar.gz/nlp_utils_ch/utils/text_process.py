#!user/bin/python
# _*_ coding: utf-8 _*_
# @Author      :   Jesper
# @Time        :   2022/11/11  10:45
# @Description :




def delete_tab_line_break(text):
	text = str(text).replace("\n", " ").replace("\r", " ").replace("\t", " ")
	return text
