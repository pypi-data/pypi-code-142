def adds(a, b *args, **kwargs):
    '''
    sumation
        
    '''
    #1. create copy of dataframe
    import numpy as np
    import pandas as pd

    
    try:
        return a+b
    except:
        print("Something else went wrong")
