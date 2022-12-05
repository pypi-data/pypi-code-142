import numpy as np
import pandas as pd

def UBRMSE(*args):
    '''
    Use dataframe and columns name or
    ndarray x and y which have the same length!!!
    Use pd.DataFrame({'a':a,'b':b}),'a','b'
    or np.array([0,1,2,3,4]),np.array([1,2,3,4,5])
    '''
    if len(args) == 3:
        df = args[0]
        x = args[1]
        y = args[2]
        mean1 = df[x].mean()
        mean2 = df[y].mean()
        return np.sqrt(np.sum(pow((df[x]-mean1-(df[y] - mean2)),2))/len(df))
    elif len(args) == 2:
        x = args[0]
        y = args[1]
        mean1 = x.mean()
        mean2 = y.mean()
        return np.sqrt(np.sum(pow((x-mean1-(y - mean2)),2))/len(x))
    else:
        return np.nan
    
def RMSE(*args):
    '''
    Use dataframe and columns name or
    ndarray x and y which have the same length!!!
    Use pd.DataFrame({'a':a,'b':b}),'a','b'
    or np.array([0,1,2,3,4]),np.array([1,2,3,4,5])
    '''
    if len(args) == 3:
        df = args[0]
        x = args[1]
        y = args[2]
        return np.sqrt(np.sum(pow((df[x]-(df[y])),2))/len(df))
    elif len(args) == 2:
        x = args[0]
        y = args[1]
        return np.sqrt(np.sum(pow((x-(y)),2))/len(x))
    else:
        return np.nan
    
    
def MSE(*args):
    '''
    Use dataframe and columns name or
    ndarray x and y which have the same length!!!
    Use pd.DataFrame({'a':a,'b':b}),'a','b'
    or np.array([0,1,2,3,4]),np.array([1,2,3,4,5])
    '''
    if len(args) == 3:
        df = args[0]
        x = args[1]
        y = args[2]
        return np.sum(pow((df[x]-(df[y])),2))/len(df)
    elif len(args) == 2:
        x = args[0]
        y = args[1]
        return np.sum(pow((x-(y)),2))/len(x)
    else:
        return np.nan
    
def SSE(*args):
    '''
    Use dataframe and columns name or
    ndarray x and y which have the same length!!!
    Use pd.DataFrame({'a':a,'b':b}),'a','b'
    or np.array([0,1,2,3,4]),np.array([1,2,3,4,5])
    '''
    if len(args) == 3:
        df = args[0]
        x = args[1]
        y = args[2]
        return np.sum(pow((df[x]-(df[y])),2))
    elif len(args) == 2:
        x = args[0]
        y = args[1]
        return np.sum(pow((x-(y)),2))
    else:
        return np.nan
    
def MAE(*args):
    '''
    Use dataframe and columns name or
    ndarray x and y which have the same length!!!
    Use pd.DataFrame({'a':a,'b':b}),'a','b'
    or np.array([0,1,2,3,4]),np.array([1,2,3,4,5])
    '''
    if len(args) == 3:
        df = args[0]
        x = args[1]
        y = args[2]
        return np.sum(np.abs(df[x]-df[y]))/len(df)
    elif len(args) == 2:
        x = args[0]
        y = args[1]
        return np.sum(np.abs(x-y))/len(x)
    else:
        return np.nan
    
def BIAS(*args):
    '''
    Use dataframe and columns name or
    ndarray x and y which have the same length!!!
    Use pd.DataFrame({'a':a,'b':b}),'a','b'
    or np.array([0,1,2,3,4]),np.array([1,2,3,4,5])
    '''
    if len(args) == 3:
        df = args[0]
        x = args[1]
        y = args[2]
        return np.sum(df[x]-df[y])/len(df)
    elif len(args) == 2:
        x = args[0]
        y = args[1]
        return np.sum(x-y)/len(x)
    else:
        return np.nan