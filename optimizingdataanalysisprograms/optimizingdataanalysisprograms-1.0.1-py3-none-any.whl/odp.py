import pandas as pd
from scipy import stats as ss
from scipy import stats
import numpy as np

class get_odp :

    def get_corr_analysis(df, label1, label2) :
        """
         Maker - RAY, FINE \n
         Dates - 2022-11-26 \n
         Needs - dataframe, column name 1, target column name 2
        """

        segment_df = df[[label1, label2]].copy()
        segment_df['conX'] = 0
        segment_df['conY'] = 0
        segment_df['conXY'] = 0


        for i in range( len(segment_df) ) :
            segment_df['conX'][i] = pow((df[label1][i]-np.mean(df[label1])), 2)
            segment_df['conY'][i] = pow((df[label2][i]-np.mean(df[label2])), 2)
            segment_df['conXY'][i] = (df[label1][i]-np.mean(df[label1])) * (df[label2][i]-np.mean(df[label2]))
        
        correlation_value = sum(segment_df['conXY']) / np.sqrt( sum(segment_df['conX']) * sum(segment_df['conY']) )

        significance = 1-0.95 # 유의수준
        tDistribution = len(segment_df)-2 # t분포의 자유도
        threshold = ss.t.ppf(significance/2, tDistribution) # 임계값
        tValue = correlation_value * np.sqrt( tDistribution / (1-pow(correlation_value, 2)) ) # t 값

        if tValue > threshold or tValue < threshold : # 연구가설 : label1과 label2 는 상관관계가 있다.
            return 'correlation coefficient : {}% / adoption of a new hypothesis / Correlated'.format( round(correlation_value*100, 1) )
        else : # 귀무가설 : label1과 label2 는 상관관계가 없다.
            return 'correlation coefficient : {}% / Adopting an Existing Hypothesis / No correlation'.format( round(correlation_value*100, 1) )



    def get_zscoreformula_analysis(df, label1, conf) :
        """
         Maker - RAY, FINE \n
         Dates - 2022-11-26 \n
         Needs - dataframe, target column name 1, confidence interval
        """

        segment_df = df[[label1]].copy()

        dicts = { 80:1.28155, 90:1.64485, 95:1.95996, 99:2.57583 }

        for i in range( len(dicts) ) :
            if conf == list(dicts.keys())[i] :
                upper = np.mean(segment_df[label1])-(list(dicts.values())[i]*np.std(segment_df[label1]))
                lower = np.mean(segment_df[label1])+(list(dicts.values())[i]*np.std(segment_df[label1]))

                return "{} values forecasting is {} ~ {}".format(label1, round(lower, 1), round(upper, 1) )