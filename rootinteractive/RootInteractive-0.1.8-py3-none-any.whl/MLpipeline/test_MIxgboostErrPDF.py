#  from RootInteractive.MLpipeline.test_MIxgboostErrPDF import *
import pandas as pd
import numpy as np
import pickle
from RootInteractive.InteractiveDrawing.bokeh.bokehDrawSA import *
from RootInteractive.MLpipeline.NDFunctionInterface import *
#from bokeh.io import output_notebook
from RootInteractive.MLpipeline.RandoForestErrPDF import *
from RootInteractive.MLpipeline.MIForestErrPDF import *
from RootInteractive.MLpipeline.local_linear_forest import LocalLinearForestRegressor
import pdb;
import sys
import os;
import xgboost as xgb
from RootInteractive.MLpipeline.MIxgboostErrPDF import *

sys.path.insert(1, os.environ[f"RootInteractive"]+'/RootInteractive/MLpipeline/') # enable debug symbols in path

widgetParams = [
    ['range', ['A']],
    ['range', ['B']],
    ['range', ['C']],
    ['range', ['D']],
    ['range', ['csin']],
    ['range', ['ccos']],
]
widgetLayoutDesc = [[0, 1, 2], [3, 4,5], {'sizing_mode': 'scale_width'}]
tooltips = [("A", "@A"), ("B", "@B"), ("C", "@C"), ("RF", "@RF")]
methods = ['RF']
rfErrPDF=0
df=0



def generateF1(nPoints, n, outFraction,stdIn):
    """
    Generate random panda+tree random vectors A,B,C,D  - A and C used to define function
        * generate function value = 2*A*sin(n*2*pi*C) + noise
        * generate noise vector
        * calculate local gradient of function
    """
    df = pd.DataFrame(np.random.random_sample(size=(nPoints, 4)), columns=list('ABCD'))
    df["B"]=df["B"]+0.5
    df["noise"] = np.random.normal(0, stdIn, nPoints)
    df["noise"] += (np.random.random(nPoints)<outFraction)*np.random.normal(0, 2, nPoints)
    df["csin"] = np.sin(n*6.28 * df["C"])
    df["ccos"] = np.cos(n*6.28 * df["C"])
    df["valueOrig"] = 2*df["A"]*df["csin"]
    df["value"] = df["valueOrig"] + df["noise"]
    df["gradA"] = df["csin"]
    df["gradC"] = df["A"]*df["ccos"]*n*6.28
    df["grad"]  =np.sqrt(df["gradA"]**2+df["gradC"]**2)
    # df["value"] = df["valueOrig"] + df["noise"]
    return df



def test_MIXGBoostErrPDF(df, nPoints=100000,outFraction=0.1,n_jobs=2):
    varFit = 'value'
    variableX = ['A', "B", "C"]
    #paramTrain = {'learning_rate':0.1, 'max_depth':8,"n_estimators":100,"subsample":0.50,"coeff_learning_rate":0.3}
    paramTrain = {'learning_rate':0.1, 'max_depth':10,"n_estimators":150,"subsample":0.50,"coeff_learning_rate":0.3,"max_learning_rate":0.2}
    xgbErrPDF=MIxgboostErrPDF(paramTrain)
    xgbErrPDF.fit3Fold(df[variableX].to_numpy(),df["value"].to_numpy(),df["value"])
    Xin=df[variableX]

    xgbErrPDF.fitReducible()
    return xgbErrPDF

def test_MIXGBoostErrPDF(df, nPoints=100000,outFraction=0.1,n_jobs=2):
    varFit = 'value'
    variableX = ['A', "B", "C", ]
    paramTrain = {'learning_rate':[0.2,0.05,0.01], 'max_depth':8,"n_estimators":100,"subsample":0.50}
    xgbErrPDF=MIxgboostErrPDFv2(paramTrain)
    xgbErrPDF.fit3Fold(df[variableX].to_numpy(),df["value"].to_numpy(),df["value"])
    Xin=df[variableX]
    return xgbErrPDF

#    return miErrPDF,df, df[variableX]






#%%time
nPoints=300000; outFraction=0.0; n_jobs=16;stdIn=0.1; n=2
df   =generateF1(nPoints, n=n, outFraction=outFraction,stdIn=stdIn)
dfRef=generateF1(nPoints, n=n, outFraction=outFraction,stdIn=stdIn)
dfRef1=generateF1(nPoints, n=n, outFraction=outFraction,stdIn=stdIn)
dfRef2=generateF1(nPoints, n=n, outFraction=outFraction,stdIn=stdIn)
dfRef3=generateF1(nPoints, n=n, outFraction=outFraction,stdIn=stdIn)
