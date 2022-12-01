import numpy as np
import pandas as pd
from copy import deepcopy
import numpy_groupies as npg
import time
from collections import defaultdict
import numba as nb
# import numpy_helper as nph

int_array = nb.types.int64[:]
int_list = nb.types.ListType(nb.types.int64)

@nb.jit(nopython=True)
def ordered_clusters_group_by(l,current_type):
    indices = nb.typed.Dict.empty(
        key_type=current_type,
        value_type=int_list
    )

    for i in np.arange(l.shape[0]):
        try:
            indices[l[i]].append(i)
        except:
            indices[l[i]] = nb.typed.List([i])

    indices_list = np.empty_like(l,np.int64)
    i = 0
    ks = np.empty(len(indices.keys()))
    for k in indices.keys():
        ks[i] = k
        for h in indices[k]:
            indices_list[h] = i
        i += 1
    return ks,indices_list


class DataFrame:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self):
        super(DataFrame, self).__setattr__('__d__', {})
        super(DataFrame, self).__setattr__('__ncol__', 0)
        super(DataFrame, self).__setattr__('__nrow__', 0)
        super(DataFrame, self).__setattr__('shape', (0,0))
        super(DataFrame, self).__setattr__('columns', [])
        super(DataFrame, self).__setattr__('__current_mode__', "ndarray")
        super(DataFrame, self).__setattr__('__max_row_print__', 1000)
        super(DataFrame, self).__setattr__('nan_int', -9223372036854775808)
        
    def __repr__(self):
        df = DataFrame.to_pandas(self.head())
        return df.__repr__()
    def __str__(self):
        df = DataFrame.to_pandas(self.head())
        return df.__str__()
    def __getattr__(self, key):        
        if (type(key) == int or type(key) == np.int64):
            key = list(self.__d__.keys())[key]
        return self.__d__[key]
    def __setattr__(self, name, value):
        if (type(name) == int or type(name) == np.int64):
            name = list(self.__d__.keys())[name]
        if type(value) == dict:
            raise Exception("Cannot insert a dictionary")            
        if type(value) == range:
            value = [*value]
        if type(value) == list:
            try:
                value = np.array(value)
            except:
                value = np.array(value,dtype=object)
        if type(value) != np.ndarray:
            value = np.array([value])
        self.__d__[name] = value
        self.names()
        super(DataFrame, self).__setattr__('__ncol__', len(self.__d__.keys()))
        if self.__nrow__ == 0:
            super(DataFrame, self).__setattr__('__nrow__', len(value))
        super(DataFrame, self).__setattr__('shape', (len(self.__d__[list(self.__d__.keys())[0]]),len(self.__d__.keys())))
    def __getitem__(self,args):
        if type(args) == tuple:
            rows,key=args
            if (type(rows) == int or type(rows) == np.int64):
                rows = [rows]
            if type(key) == slice:
                
                if key.start is None:
                    start = 0
                else:
                    start = key.start
                if key.stop is None:
                    stop = len(self.__d__.keys())
                else:
                    stop = key.stop
                if key.step is None:
                    step = 1                    
                else:
                    step = key.step
                return DataFrame.__getitem__(self,(rows,range(start,stop,step)))
            else:
                if type(key) == str:
                    return self.__d__[key][rows]
                else:
                    if type(key) == list or type(key) == np.array or type(key) == range:                    
                            t_ = DataFrame()
                            for k in key:
                                if (type(k) == int or type(k) == np.int64):
                                    k = list(self.__d__.keys())[k]
                                DataFrame.__setattr__(t_,k,self.__d__[k][rows])
                            return t_
                    elif (type(key) == int or type(key) == np.int64):
                        k = list(self.__d__.keys())[key]
                        return self.__d__[k][rows]
        else:
            key = args
            if type(key) == slice:
                if key.start is None:
                    start = 0
                else:
                    start = key.start
                if key.stop is None:
                    stop = len(self.__d__.keys())
                else:
                    stop = key.stop
                if key.step is None:
                    step = 1                    
                else:
                    step = key.step                
                return DataFrame.__getitem__(self,(rows,range(start,stop,step)))
            else:
                if type(key) == str:
                    return self.__d__[key]
                else:
                    if type(key) == list or type(key) == np.array or type(key) == range:                    
                            t_ = DataFrame()
                            for k in key:
                                if (type(k) == int or type(k) == np.int64):
                                    k = list(self.__d__.keys())[k]
                                DataFrame.__setattr__(t_,k,self.__d__[k])
                            return t_
                    elif (type(key) == int or type(key) == np.int64):
                        k = list(self.__d__.keys())[key]
                        return self.__d__[k]
    def __setitem__(self,args,values):
        if type(args) == tuple:
            rows,key = args
            if (type(rows) == int or type(rows) == np.int64):
                rows = [rows]
            if type(key) == str or (type(key) == int or type(key) == np.int64):
                if (type(key) == int or type(key) == np.int64):
                    key = list(self.__d__.keys())[key]
                self.__d__[key][rows] = values
            else:
                if type(key) == slice:
                    if key.start is None:
                        start = 0
                    else:
                        start = key.start
                    if key.stop is None:
                        stop = len(self.__d__.keys())
                    else:
                        stop = key.stop
                    if key.step is None:
                        step = 1                    
                    else:
                        step = key.step      
                    return DataFrame.__setitem__(self,(rows,range(start,stop,step)))                    
                    
                else:
                    if len(key) == 1:                    
                        for k in key:
                            if (type(k) == int or type(k) == np.int64):
                                k = list(self.__d__.keys())[k]
                            self.__d__[k][rows] = values
                    else:
                        raise Exception("Cannot only set 1 column at the moment.")
        else:
            if type(args) == str or (type(args) == int or type(args) == np.int64):
                if (type(args) == int or type(args) == np.int64):
                    key = list(self.__d__.keys())[args]
                DataFrame.__setattr__(self,args,values)
            else:
                if len(args) == 1:
                    for k in args:
                        if (type(k) == int or type(k) == np.int64):
                            k = list(self.__d__.keys())[k]
                        self.__d__[k] = values
                else:
                    raise Exception("Cannot set more than row")

        self.names()

    # def append(self,key,value):
    #     if self.__current_mode__ != "list":
    #         self.__current_mode__ = "list"
    #         for name in self.columns:
    #             self[name] = self[name].tolist()
    #     self[key].append(value)
    # def extend(self,key,list):
    #     if self.__current_mode__ != "list":
    #         self.__current_mode__ = "list"
    #         for name in self.columns:
    #             self[name] = self[name].tolist()
    #     self[key].extend(list)

    def __stop_appending__(self):
        if self.__current_mode__ == "list":
            self.__current_mode__ = "ndarray"
            for name in self.columns:
                self[name] = np.array(self[name])

    def rename(self,keys,new_keys):
        self.__stop_appending__()        
        new_d = {}
        if type(keys) == str or (type(keys) == int or type(keys) == np.int64):
            if (type(keys) == int or type(keys) == np.int64):
                keys = [self.columns[keys]]
            else:
                keys = [keys]
        else:
            keys_ = []
            for k in keys:
                if (type(k) == int or type(k) == np.int64):
                    k = self.columns[k]
                keys_.append(k)
            keys = keys_
        if type(new_keys) == str:
            new_keys = [new_keys]
        
        failed = False
        for name in self.columns:
            if name in keys:
                
                index = int(np.where(np.array(keys) == name)[0][0])
                if not new_keys[index] in self.columns or new_keys[index] == name:
                    new_d[new_keys[index]] = self.__d__[name]
                else:
                    failed = True
                    print("Keys not unique. This operation would delete an existing column, aborting")
                    break
                    
            else:
                new_d[name] = self.__d__[name]
        if not failed:
            super(DataFrame, self).__setattr__('d', new_d)
            self.names()

    def __shape__(self):
        self.__stop_appending__()
        if len(self.__d__.keys()) > 0:
            shape = (len(self.__d__[list(self.__d__.keys())[0]]),len(self.__d__.keys()))
        else:
            shape = (0,0)
        
        return shape

    def sort(self,order):
        self.__stop_appending__()
        for k in self.__d__.keys():
            self.__d__[k] = self.__d__[k][order]

    def sort_by(self,name):
        self.__stop_appending__()
        order = np.argsort(self.__d__[name])
        self.sort(order)
        return self
    def __temp_sort_by_column__(self,name):
        self.__stop_appending__()
        order = np.argsort(self.__d__[name])
        super(DataFrame, self).__setattr__('order_', order[order])
        self.sort(order)
    def __unsort_temp_order__(self):
        self.__stop_appending__()
        self.sort(self.order_)

    def group_by(self,keys):
        self.__stop_appending__()
        # thanks to gg349 and Trenton McKinney https://stackoverflow.com/questions/30003068/how-to-get-a-list-of-all-indices-of-repeated-elements-in-a-numpy-array
        # create a test array
        records_array = self.__d__[keys]

        # creates an array of indices, sorted by unique element
        idx_sort = np.argsort(records_array,kind='mergesort')

        # sorts records array so all unique elements are together
        sorted_records_array = records_array[idx_sort]

        # returns the unique values, the index of the first occurrence of a value, and the count for each element
        # vals, idx_start, count = np.unique(sorted_records_array, return_counts=True, return_index=True)
        vals, idx_start= np.unique(sorted_records_array, return_index=True)

        # splits the indices into separate arrays
        res = np.split(idx_sort, idx_start[1:])
        return vals,res
    def aggregate(self,key,columns,function,args = [],kargs = {}):
        self.__stop_appending__()
        t_ = DataFrame()
        keys_values = []
        values = []
        names_columns = []
        val,groups = self.group_by(key)
        for column in columns:
            values.append([])
            if (type(column) == int or type(column) == np.int64):
                name = list(self.__d__.keys())[column]
            else:
                name = column            
            names_columns.append(name)
        for group in groups:
            for column_index in range(len(columns)):
                column = columns[column_index]
                if args != [] and kargs != {}:
                    result = function(self[column][group],*args,**kargs)
                elif args != []:
                    result = function(self[column][group],*args)
                elif kargs != {}:
                    result = function(self[column][group],**kargs)
                else:
                    result = function(self[column][group])
                values[column_index].append(result)

        t_[key] = val
        for i in range(len(names_columns)):
            t_[names_columns[i]] = values[i]
        return t_
    def apply(self,column,function,args = [],kargs = {}):
        self.__stop_appending__()
        if args != [] and kargs != {}:
            values = np.array([function(x,*args,**kargs) for x in self.__d__[column]])
        elif args != []:
            values = np.array([function(x,*args) for x in self.__d__[column]])
        elif kargs != {}:
            values = np.array([function(x,**kargs) for x in self.__d__[column]])
        else:
            values = np.array([function(x) for x in self.__d__[column]])
        
        return values


    def unique(self,key):
        self.__stop_appending__()
        return np.unique(self.__d__[key])
        
    def all_in(self,values,key):
        self.__stop_appending__()
        current = True
        for val in values:
            current = current and any(self.__d__[key] == val)
        return current
    def any_in(self,values,key):
        self.__stop_appending__()
        current = False
        for val in values:
            current = current or any(self.__d__[key] == val)
            if current:
                break
        return current
    def indices_in(self,values,key):
        self.__stop_appending__()
        current = np.zeros(self.__d__[key].shape[0],dtype=bool)
        for val in values:    
            current = current | (self.__d__[key] == val)
        return np.where(current)
    def which_in(self,values,key):
        self.__stop_appending__()
        if type(values) == list:
            values = np.array(values)
        result = [any(x == self.__d__[key]) for x in values]
        return values[result]
    def is_in(self,values,key):
        self.__stop_appending__()
        result = [any(x == self.__d__[key]) for x in values]
        return np.array(result)
    def names(self):
        self.__stop_appending__()
        super(DataFrame, self).__setattr__('columns', np.array(list(self.__d__.keys())))
        return self.columns
    
    def from_pandas(self,df):
        self.__stop_appending__()     
        for name in df.columns:
            if df[name].values.dtype == np.dtype('O'):
                df[name] = df[name].fillna('')
            DataFrame.__setattr__(self,name , df[name].values)
        return self
    def where(self,boolean_array):
        self.__stop_appending__()
        indices = np.where(boolean_array)[0]
        return self[indices,:]

    def indices(self,boolean_array):
        self.__stop_appending__()
        indices = np.where(boolean_array)[0]
        return indices
    
    def to_pandas(self):
        self.__stop_appending__()
        df = pd.DataFrame()
        for k in self.__d__.keys():
            df[k] = self.__d__[k]
        
        return df

    def head(self,n=-1):
        if (n == -1):
            n = self.__max_row_print__
        self.__stop_appending__()
        return self[0:n,:]

    def to_csv(self,path):
        self.__stop_appending__()
        df = self.to_pandas()
        df.to_csv(path,index = False)
    
    def read_csv(self,path,skip_blank_lines = False,keep_default_na=False):
        self.__stop_appending__()
        df = pd.read_csv(path,skip_blank_lines = skip_blank_lines,keep_default_na=keep_default_na)

        return self.from_pandas(df)

    def to_float(self,column):
       values = self.__d__[column]
       is_null = (values == "NULL") | (values == "") | (values == "nan") | (values == "NAN") | (values == "NaN") | (values == "Nan") | (values == "null") | (values == " ") | (values == ".")
       self.__d__[column][is_null] = np.nan
       self.__d__[column] = values.astype(float)

    def to_int(self,column,nan_value = np.nan):
       self.to_float(column)              
       self.__d__[column] = np.round(self.__d__[column]).astype(int)
    #    self.__d__[column][self.__d__[column] == self.nan_int] = np.nan

    def round(self,column,nan_value = np.nan):
        #this operation can handle nans
       self.to_float(column)              
       self.__d__[column] = np.round(self.__d__[column])
    #    self.__d__[column][self.__d__[column] == self.nan_int] = np.nan

    
    def to_str(self,column):
        values = self.__d__[column]
    #    is_null = values == "NULL"
    #    values[is_null] = np.nan
        self.__d__[column] = values.astype(str)

        # values = [str(x) for x in list(values)]
        # self.__d__[column] = np.array(values)


def from_pandas(df):                  
    t = DataFrame()
    t.from_pandas(df)
    return t

def read_csv(path,skip_blank_lines = False,keep_default_na=False):
    df = pd.read_csv(path,skip_blank_lines = skip_blank_lines,keep_default_na=keep_default_na)
    return from_pandas(df)