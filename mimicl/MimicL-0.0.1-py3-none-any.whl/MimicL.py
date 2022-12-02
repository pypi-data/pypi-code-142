
import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta

def ltable(labevents_data,propensity_data,labitems_data):
  labevents_data_demo=labevents_data[['subject_id','charttime','storetime','itemid']].drop_duplicates()
  propensity_data_demo=propensity_data[['subject_id','hadm_id','admittime','dischtime']].drop_duplicates()
  labitems_data_demo=labitems_data[['itemid','label']].drop_duplicates()
  labitems_data_demo['label'].replace(' ', np.nan, inplace=True)
  labitems_data_demo=labitems_data_demo.dropna(subset=['label'])
  selected_lebel=pd.DataFrame({
    'label':["Glucose, POCT",
    'Hemoglobin',
    'Platelet Count',
    'Hematocrit',
    'Erythrocytes',
    'Leukocytes',
    'Potassium',
    'Sodium',
    'Creatinine',
    'Bicarbonate',
    'Chloride',
    'Anion Gap',
    "Calcium, Total",
    'Glucose',
    "Bld Urea Nitrog(BUN)",
    'Lymphocytes',
    'Monocytes',
    'Neutrophils',
    'Eosinophils',
    'Basophils',
    'pH',
    'pCO2',
    'FIO2',
    'pO2',
    'Lactate',
    "Troponin T, 6 hr, 5th gen",
    "Troponin T, 2 hr, 5th gen",
    "Troponin T, Baseline, 5th gen",
    'Venous pH',
    'Venous pCO2',
    'Venous pO2']
    })
  labitems_data_demo=pd.merge(selected_lebel,labitems_data_demo,on='label',how='left')
  labitems_data_demo=labitems_data_demo.dropna(subset=['itemid'])
  first_merge=pd.merge(labevents_data_demo,labitems_data_demo,on='itemid',how='left')
  first_merge_1=first_merge.dropna(subset=['label'])
  second_merge=pd.merge(first_merge_1,propensity_data_demo,on='subject_id',how='left')
  second_merge_1=second_merge.dropna(subset=['admittime'])
  second_merge_1['charttime'] =  pd.to_datetime(second_merge_1['charttime'], infer_datetime_format=True)#Converting this column into datetime
  second_merge_1['storetime'] =  pd.to_datetime(second_merge_1['storetime'], infer_datetime_format=True)#Converting this column into datetime
  second_merge_1['admittime'] =  pd.to_datetime(second_merge_1['admittime'], infer_datetime_format=True)#Converting this column into datetime
  second_merge_1['dischtime'] =  pd.to_datetime(second_merge_1['dischtime'], infer_datetime_format=True)#Converting this column into datetime
  base_data=second_merge_1.copy()
  base_data['Timeperiod']=np.nan#Creating and assigning null value to Timeperiod column
  base_data.loc[(base_data['charttime'] >= base_data['admittime']) & (base_data['charttime'] <= base_data['dischtime']),['Timeperiod']]='Valid' #valid when starttime is in between admittime and dischtime
  final_base_data=base_data.dropna(subset=['Timeperiod'])#Droping 'Timeperiod' column's nan value only
  final_base_data['cnt']=1
  table = pd.pivot_table(final_base_data, values='cnt', index=['subject_id','hadm_id','admittime','dischtime'],columns=['label'], aggfunc='sum')
  pivot_columns=(table.columns).to_list()
  all_columns=selected_lebel['label'].to_list()
  result=list(set(all_columns)-set(pivot_columns))
  for item in result:
    table[item]=0
  final_df = pd.DataFrame(table.to_records())
  return final_df