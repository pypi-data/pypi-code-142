

import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta

def mtable(prescriptions_data,propensity_data,ndc2_data):
  prescriptions_data_demo=prescriptions_data[['subject_id','starttime','stoptime','ndc','doses_per_24_hrs']].drop_duplicates()#Removed duplicates 
  propensity_data_demo=propensity_data[['subject_id','hadm_id','admittime','dischtime']].drop_duplicates()#Removed duplicates
  ndc2_data=ndc2_data.drop_duplicates()#Removed duplicates
  ndc2_data=ndc2_data.dropna(subset=['MED_THERAPEUTIC_CLASS_DESCRIPTION'])
  first_merge=pd.merge(prescriptions_data_demo,ndc2_data,left_on='ndc',right_on='NDC_MEDICATION_CODE',how='left')#Merging 'MED_THERAPEUTIC_CLASS_DESCRIPTION' column with prescriptions_data
  first_merge=first_merge.dropna(subset=['MED_THERAPEUTIC_CLASS_DESCRIPTION'])#Droping 'MED_THERAPEUTIC_CLASS_DESCRIPTION' column's nan value only
  first_merge= first_merge.drop("NDC_MEDICATION_CODE", axis='columns')
  second_merge=pd.merge(first_merge,propensity_data_demo,on='subject_id',how='left')#Merging first_merge_2 dataframe with propensity_data using subject_id
  second_merge=second_merge.dropna(subset=['admittime'])#Droping 'admittime' column's nan value only
  second_merge['starttime'] =  pd.to_datetime(second_merge['starttime'], infer_datetime_format=True)#Converting this column into datetime
  second_merge['stoptime'] =  pd.to_datetime(second_merge['stoptime'], infer_datetime_format=True)#Converting this column into datetime
  second_merge['admittime'] =  pd.to_datetime(second_merge['admittime'], infer_datetime_format=True)#Converting this column into datetime
  second_merge['dischtime'] =  pd.to_datetime(second_merge['dischtime'], infer_datetime_format=True)#Converting this column into datetime
  second_merge['Timeperiod']=np.nan#Creating and assigning null value to Timeperiod column
  second_merge.loc[(second_merge['starttime'] >= second_merge['admittime']) & (second_merge['starttime'] <= second_merge['dischtime']),['Timeperiod']]='Valid' #valid when starttime is in between admittime and dischtime
  second_merge=second_merge.dropna(subset=['Timeperiod'])#Droping 'Timeperiod' column's nan value only
  second_merge['ndc']=1
  table = pd.pivot_table(second_merge, values='ndc', index=['subject_id','hadm_id','admittime','dischtime'],columns=['MED_THERAPEUTIC_CLASS_DESCRIPTION'], aggfunc='sum')
  final_df = pd.DataFrame(table.to_records())
  return final_df