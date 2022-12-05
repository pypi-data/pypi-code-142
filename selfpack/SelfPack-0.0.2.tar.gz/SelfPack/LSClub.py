import numpy as np
import pandas as pd
# Personally used for LSClub algorithm to retrieval Soil Moisture


def LoadType(namenpy:str):
    '''
    Used For only load type
    So .... Be carefual when u creat the Div.npy!
    #LoadType('../../div/Div500-1.npy')
    '''
    landtype = np.load(namenpy)#.transpose()
    xlen = np.shape(landtype)[0]
    ylen = np.shape(landtype)[1]
    x = np.arange(xlen)-xlen//2
    y = np.arange(ylen)-ylen//2
    yarr,xarr = np.meshgrid(y,x,sparse=False)
    df_landtype = pd.DataFrame({"x":xarr.reshape(-1),"y":yarr.reshape(-1),"type":landtype.reshape(-1)})
    return df_landtype