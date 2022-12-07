# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:08:02 2020

@author: pahis
"""

#Variables needed for creating intelligent dropdown menu in GUI.py
gui_input_variable = 'gui_input_variable'
gui_tk_variable = 'gui_tk_variable'
gui_tk_variable_last = 'gui_tk_variable_last'
gui_tk_w = 'gui_tk_w'
gui_tk_options = 'gui_tk_options'
gui_special_options_dropdown = 'gui_special_options_dropdown'

gui_tk_alle = 'All'
guit_tk_choose = 'Please Select'

list_gui_params = [gui_input_variable, gui_tk_variable, gui_tk_variable_last, gui_tk_w, gui_tk_options, gui_special_options_dropdown]


def prepend(elem, mylist):
    mylist = [elem] + mylist
    return mylist

def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
