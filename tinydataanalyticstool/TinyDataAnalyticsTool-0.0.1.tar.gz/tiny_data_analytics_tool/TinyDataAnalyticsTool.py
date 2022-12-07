# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:48:19 2020

@author: pahis
"""

import tkinter as tk
import Settings as st
import pandas as pd

class TinyDataAnalyticsTool:
    
    def __init__(self, func_dict : dict, option_parameters_from_dataset_columns : dict , dict_data:dict = {}, 
                 func_parameters_display_descr :dict = {}, dict_special_dropdown_options:dict = {} , app_icon_path:str = '' , 
                 app_name:str = 'Tiny Data Analytics Tool'):
        self.__app_icon_path = app_icon_path
        self.__app_name = app_name
        self.__func_dict = func_dict
        self.__func_parameters = option_parameters_from_dataset_columns
        self.func_parameters_display_descr = func_parameters_display_descr
        self.__dict_data_backup = self.__dict_data = dict_data
        self.__dict_special_dropdown_options = dict_special_dropdown_options
        self.__dict_special_paramaters = {}
        self.__dict_paramaters = {}
        self.__field_main_view()
    
    def start_func(self, func_name:str, data:pd.DataFrame, drop_down_selected_options):
        self.__func_dict.get(func_name)(data=data, user_inputs=drop_down_selected_options)
        
    def __field_main_view(self):
        self.__tk_root = tk.Tk()
        self.__window_settings(self.__tk_root)
        for func_name, v in self.__func_dict.items():
            self.__create_Buttons(func_name)
        tk.mainloop()
    
    def __window_settings(self, tk_root = True):
        if tk_root:
            if self.__app_icon_path != '':
                try:
                    self.__tk_root.iconbitmap(r"{}".format(self.__app_icon_path))
                except:
                    print('Error 001: Invalid path for app icon')
            self.__tk_root.title(self.__app_name)
        else:
            if self.__app_icon_path != '':
                try:
                    self.tk_master.iconbitmap(r"{}".format(self.__app_icon_path))
                except:
                    print('Error 001: Invalid path for app icon')
            self.tk_master.title(self.__app_name) 
        
    def __create_Buttons(self, func_name):
        button = tk.Button(self.__tk_root, text=func_name)
        button.config(command= lambda func_name = func_name: self.__on_button_click(func_name))
        button.pack()
    
    def __on_button_click(self, func_name):
        self.__func_name = func_name
        self.final_df_for_options_displays = self.__dict_data_backup[func_name]
        self.__analytics_field()
        
    def __create_variables(self, list_parameters, from_data : bool):
        dict_parameters = dict()
        for k in list_parameters:
            dict_parameters.update({k:st.list_gui_params})
        if from_data:
            self.__dict_paramaters = {k:dict(zip(list(map(lambda x : str(x), v)), [-1]*len(v))) for (k,v) in dict_parameters.items()}
        else:
            self.__dict_special_paramaters = {k:dict(zip(list(map(lambda x : str(x), v)), [-1]*len(v))) for (k,v) in dict_parameters.items()}

    def __update_menu(self, param):
        menu = self.__dict_paramaters[param][st.gui_tk_w].children["menu"]
        menu.delete(0, "end")
        for value in self.__dict_paramaters[param][st.gui_tk_options]:
            menu.add_command(label=value, command=lambda v=value: self.__dict_paramaters[param][st.gui_tk_variable].set(v))    

    def __option_changed(self, variable, options):
        if  isinstance(self.tk_master.tk.globalgetvar(variable), int):
            variable = tk.StringVar(value = str(self.tk_master.tk.globalgetvar(variable)))
        else:    
            variable = tk.StringVar(value = self.tk_master.tk.globalgetvar(variable))
        for param,v in self.__dict_paramaters.items():
            if not str(self.__dict_paramaters[param][st.gui_tk_variable_last]) == variable.get() and options == param and not self.__dict_paramaters[param][st.gui_tk_variable_last] == -1:
                self.__dict_paramaters[param][st.gui_tk_variable_last] = variable.get()
                df = self.__dict_data_backup[self.__func_name]
                self.final_df_for_options_displays = df
                df = df.apply(pd.to_numeric, errors='coerce').fillna(df)
                for param2,v2 in self.__dict_paramaters.items():
                    if param != param2:
                        if not self.__dict_paramaters[param2][st.gui_tk_variable_last]  == st.gui_tk_alle and not self.__dict_paramaters[param2][st.gui_tk_variable_last] == -1:
                            try:
                                if not st.represents_int(self.__dict_paramaters[param2][st.gui_tk_variable_last]):
                                    df = df[df[param2] == self.__dict_paramaters[param2][st.gui_tk_variable_last]]
                                    self.final_df_for_options_displays = df
                                else:
                                    df = df[df[param2] == int(self.__dict_paramaters[param2][st.gui_tk_variable_last])]
                                    self.final_df_for_options_displays = df
                            except NameError:
                                print('Error 003: Parameter keys do not correspond to Dataframe colums. Rename Paramater Keys of Parameter dictionary!')
                        elif self.__dict_paramaters[param2][st.gui_tk_variable_last]  == st.gui_tk_alle:
                            self.final_df_for_options_displays = df
        for param,v in self.__dict_paramaters.items():                 
            if param == options:
                df = self.final_df_for_options_displays
                df = df.apply(pd.to_numeric, errors='coerce').fillna(df)
                if st.represents_int(df[param].iloc[0]):
                    if isinstance(df[param].iloc[0], float):
                        df[param] = pd.to_numeric(df[param], errors='coerce')
                        df = df.dropna(subset=[param])
                        df[param] = df[param].apply(lambda x: int(x))
                    self.__dict_paramaters[param][st.gui_tk_options] = st.prepend(st.gui_tk_alle, sorted(set([int(val) for val in df[param] if str(val).isdigit()]))) 
                else:
                    self.__dict_paramaters[param][st.gui_tk_options] = st.prepend(st.gui_tk_alle, sorted(set([val for val in df[param]]))) 
                if not variable.get() == st.gui_tk_alle and not variable.get() is None:
                    if st.represents_int(df[param].iloc[0]): # and not self.__dict_paramaters[param][st.gui_tk_variable_last] == -1:
                        df = df[df[param] == int(variable.get())]
                    else:
                        df = df[df[param] == variable.get()]
                    self.__dict_paramaters[param][st.gui_tk_variable_last] = variable.get()
                for param2,v2 in self.__dict_paramaters.items():
                    if param != param2:
                        if st.represents_int(df[param2].iloc[0]):
                            self.__dict_paramaters[param2][st.gui_tk_options] = st.prepend(st.gui_tk_alle, list((set([val for val in df[param2]if str(val).isdigit()]))))
                        else:
                            self.__dict_paramaters[param2][st.gui_tk_options] = st.prepend(st.gui_tk_alle, list((set([val for val in df[param2]]))))
                for param2,v2 in self.__dict_paramaters.items():
                    if not self.__dict_paramaters[param2][st.gui_tk_w] is None:
                        self.__update_menu(param2)   
                self.final_df_for_options_displays = df
                
    def __quit_master(self):
        self.__dict_data = self.__dict_data_backup 
        self.tk_master.destroy()
        self.__dict_paramaters.clear()
        self.__dict_special_paramaters.clear()
        for k, v in self.__dict_data.items():
            self.final_df_for_options_displays = self.__dict_data[self.__func_name]
    
    def __show_entry_fields(self):
        if self.__func_name in self.__func_parameters or self.__func_name in self.__dict_special_dropdown_options:
            for param,v in self.__dict_special_paramaters.items():
                self.__dict_special_paramaters[param][st.gui_input_variable] = self.__dict_special_paramaters[param][st.gui_tk_variable].get()
        self.start_func(self.__func_name,self.final_df_for_options_displays, self.__dict_special_paramaters)
            
    def __analytics_field(self):
        if self.__func_name in self.__func_parameters or self.__func_name in self.__dict_special_dropdown_options:
            if self.__func_name in self.__func_parameters:
                self.__create_variables(self.__func_parameters[self.__func_name], from_data = True)
            if self.__func_name in self.__dict_special_dropdown_options:
                self.__create_variables(self.__dict_special_dropdown_options[self.__func_name], from_data = False)
            self.tk_master = tk.Tk()
            self.__window_settings(tk_root = False)
            amount_params = len(self.__dict_paramaters) + len(self.__dict_special_paramaters)
            buttons_frame = tk.Frame(self.tk_master)
            buttons_frame.grid(row=amount_params, column=0, columnspan=amount_params+5, rowspan=amount_params+5, sticky=tk.W+tk.E)
            position_row = 0
            for param,v in self.__dict_paramaters.items():
                if bool(self.func_parameters_display_descr):
                    try:
                        tk.Label(self.tk_master, text=self.func_parameters_display_descr[self.__func_name][param]).grid(row = position_row)
                    except:
                        tk.Label(self.tk_master, text=param).grid(row = position_row)
                        print('Error 004: Paramaters does not match with Keys in checkboxes describing dictionary')
                else:
                    tk.Label(self.tk_master, text=param).grid(row = position_row)
                self.__dict_paramaters[param][st.gui_tk_variable] = tk.StringVar(self.tk_master)
                self.__dict_paramaters[param][st.gui_tk_variable].set(st.gui_tk_alle)
                self.__dict_paramaters[param][st.gui_tk_variable].trace_add('write', lambda var_name = self.__dict_paramaters[param][st.gui_tk_variable],*_, var=param: self.__option_changed(var_name, var))
                if st.represents_int(self.final_df_for_options_displays[param].iloc[0]):
                    if isinstance(self.final_df_for_options_displays[param].iloc[0], float):
                       self.final_df_for_options_displays[param] = pd.to_numeric(self.final_df_for_options_displays[param], errors='coerce')
                       self.final_df_for_options_displays = self.final_df_for_options_displays.dropna(subset=[param])
                       self.final_df_for_options_displays[param] = self.final_df_for_options_displays[param].apply(lambda x: int(x))
                    self.__dict_paramaters[param][st.gui_tk_options] = st.prepend(st.gui_tk_alle, sorted(set([int(val) for val in self.final_df_for_options_displays[param] if str(val).isdigit()]))) 
                else:
                    self.__dict_paramaters[param][st.gui_tk_options] = st.prepend(st.gui_tk_alle, sorted(set([val for val in self.final_df_for_options_displays[param]]))) 
                self.__dict_paramaters[param][st.gui_tk_w] = tk.OptionMenu(self.tk_master, self.__dict_paramaters[param][st.gui_tk_variable], *self.__dict_paramaters[param][st.gui_tk_options])
                self.__dict_paramaters[param][st.gui_tk_w].grid(row=position_row, column=1)
                position_row = position_row +1
            for param,v in self.__dict_special_paramaters.items():
                tk.Label(self.tk_master, text=param).grid(row = position_row)
                self.__dict_special_paramaters[param][st.gui_tk_variable] = tk.StringVar(self.tk_master)
                self.__dict_special_paramaters[param][st.gui_tk_variable].set(st.guit_tk_choose)
                self.__dict_special_paramaters[param][st.gui_tk_options] = self.__dict_special_dropdown_options[self.__func_name][param]
                self.__dict_special_paramaters[param][st.gui_tk_w] = tk.OptionMenu(self.tk_master, self.__dict_special_paramaters[param][st.gui_tk_variable], *self.__dict_special_paramaters[param][st.gui_tk_options])
                self.__dict_special_paramaters[param][st.gui_tk_w].grid(row=position_row, column=1)
                position_row = position_row +1
            tk.Button(buttons_frame, text='Quit', command=self.__quit_master).grid(row=amount_params, column=0, sticky=tk.W, pady=4)
            tk.Button(buttons_frame, text='Show', command=self.__show_entry_fields).grid(row=amount_params, column=1, sticky=tk.E, pady=4)
            tk.mainloop()
        else:
            self.__show_entry_fields()