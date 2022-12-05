import pandas as pd
import dask
import dask.dataframe as dd



def dask_read(ReaderFunc,l:list,npart = 10,output_lazy = 0):
    '''
    Input a Function and the input
    Now input only for reader so only a list named 'l'
    '''
    delayed_df=[dask.delayed(ReaderFunc)(f) for f in l]
    ddf=dd.from_delayed(delayed_df)
    if output_lazy == 1:
        return ddf
    ddf=ddf.repartition(npartitions=npart)
    df = ddf.compute()
    return df