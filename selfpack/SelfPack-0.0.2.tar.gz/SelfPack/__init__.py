"""
            Self used Model
            ===============
     Part of GNSS-R data deal pack
        ************************
            Version 0.0.1
        Add Bufeng-1 Data Reader
            Version 0.0.2
        Renew BuFeng-1 Reader
       Add GNOS-R Data Reader
       Add ACCcalculator Method
          Add LSClub Method
          ------------------
          >>> Method <<<
          ------------------
        SelfPack.ACCcalculator
        -------------------------
    >> SelfPack.ACCcalculator.UBRMSE(A,B)
    >> SelfPack.ACCcalculator.UBRMSE(df,X,Y)
    >> SelfPack.ACCcalculator.RMSE(A,B)
    >> SelfPack.ACCcalculator.RMSE(df,X,Y)
    >> SelfPack.ACCcalculator.MSE(A,B)
    >> SelfPack.ACCcalculator.MSE(df,X,Y)
    >> SelfPack.ACCcalculator.SSE(A,B)
    >> SelfPack.ACCcalculator.SSE(df,X,Y)
    >> SelfPack.ACCcalculator.MAE(A,B)
    >> SelfPack.ACCcalculator.MAE(df,X,Y)
    >> SelfPack.ACCcalculator.BIAS(A,B)
    >> SelfPack.ACCcalculator.BIAS(df,X,Y)
       --------------------------
      SelfPack.GNSSReader
    >> SelfPack.GNSSReader.ReadBF_L1C(path:str)
    >> SelfPack.GNSSReader.Read_GNOS2_L1(path:str)
       --------------------------
       SelfPack.LSClub
    >> SelfPack.LSClub.LoadType(namenpy:str)
       --------------------------
      SelfPack.Daks_reader
    >> SelfPack.Daks_reader(func,l:list)
"""
import numpy as np
import pandas as pd
import os