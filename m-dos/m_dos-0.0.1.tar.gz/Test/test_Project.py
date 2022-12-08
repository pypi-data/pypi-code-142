#%%
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('../Project')))
from Project.Prediction import ClassModel  as md
from Project.Prediction import DataCollection as dc
import numpy as np
import pandas as pd

def test_Doc():
    test = dc.Data().impo()
    assert  np.shape(test) == (137836, 4)

df = dc.Data().impo()
df.set_index("Time", inplace = True)
df.index = pd.to_datetime(df.index)

def test_Doc():
    test = md.Dos(df, 1,2022,9,2).createFeatures()
    assert  np.shape(test) == (137836, 12)

