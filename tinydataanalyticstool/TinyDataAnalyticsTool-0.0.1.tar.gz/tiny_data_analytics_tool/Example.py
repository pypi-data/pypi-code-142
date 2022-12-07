# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:31:17 2020

@author: pahis
"""

import pandas as pd
from TinyDataAnalyticsTool import TinyDataAnalyticsTool
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

def myFunc(*args, **kwargs):
    # Nested dictionary of User Input including Tkinter Objects for further manipulations if required
    user_inputs : dict = kwargs.get('user_inputs') 
    # Trimmed only if User did NOT select option 'All' 
    trimmed_data_based_on_user_input :pd.DataFrame = kwargs.get('data') 
    print(user_inputs)
    print(trimmed_data_based_on_user_input)
    plt.hist(trimmed_data_based_on_user_input["Column1"])
    plt.show()

def main():                      
    #Import: Use the function name (e.g. myFunc) consistent 

    # Read your Data as Pandas Data Frame
    data = pd.DataFrame({'Column1': [1,2,3,4,5],'Column2':[5,4,3,2,1]})

    #Here you give as parameter your Data
    dict_data = {'myFunc' : data}

    #Here you specify the function which shall be called in the Analytics Class above
    func_dict = {"myFunc" : myFunc}

    #Here you specify special options for your DropDown menu, for example if the analysis should be based on relative or absoloute values
    #You can pass multiple special dicts in form of a nested dict
    dict_special_dropdown_options = {'myFunc' : {'Method (Parameters to choose from as a User not in dataset)' : ['Mean' , 'Median', 'Standarddeviation']}}

    #Here you specify Parameters which correspond to the column names in the dataFrame
    option_parameters_from_dataset_columns = {"myFunc" : ['Column1', 'Column2']}

    #here you can change the name of the column names for aesthetic reasons.
    func_parameters_desc = {"myFunc" : {'Column1' : 'Choice 1', 'Column2' : 'Choice 2'}}
    
    #Create the Gui and insert the parameters
    TinyDataAnalyticsTool(func_dict, option_parameters_from_dataset_columns, dict_data = dict_data,
            func_parameters_display_descr=func_parameters_desc,
            dict_special_dropdown_options=dict_special_dropdown_options)

if __name__ == '__main__':
    main()
