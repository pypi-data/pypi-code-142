import pandas as pd
import numpy as np

def Convert(lst):
    res_dct = map(lambda i: (lst[i], lst[i+1]), range(len(lst)-1)[::2])
    return dict(res_dct)

def get_index(x_data):
    try:
        column_name  =list(x_data.columns)
        index_list_len =lambda columns:len(columns)*2
        lst = []
        for i in range(0,index_list_len(column_name)):
            if i%2 != 0:
                lst.append(i)
    except Exception as e:
        Warning(e)
        print(e)
    return lst,column_name

def df_to_dictionary(x_data,y_data,x_data_len):
    try:
        indexs,column_name = get_index(x_data)
        ydata = []
        xdata = []
        for i in y_data:
            ydata.append(i)
        for i in range(0,x_data_len):
            col = x_data.iloc[i,]
            number = 0
            for num in col:
                column_name.insert(indexs[number],col[number])
                number +=1

            xdata.append(Convert(column_name))
    except Exception as e:
        Warning(e)
        print(e)
    return xdata,ydata
