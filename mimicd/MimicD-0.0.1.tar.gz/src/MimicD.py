
import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta

def dtable(icd_10,diagnoses,new_group):
  icd_10=icd_10[['GROUP_DESC','SUBGROUP_DESC','SUBGROUP']]
  icd_10['SUBGROUP']=icd_10['SUBGROUP'].str.replace('A','1').str.replace('B','2').str.replace('C','3').str.replace('D','4').str.replace('E','5').str.replace('F','6').str.replace('G','7').str.replace('H','8').str.replace('I','9').str.replace('J','10').str.replace('K','11').str.replace('L','12').str.replace('M','13').str.replace('N','14').str.replace('O','15').str.replace('P','16').str.replace('Q','17').str.replace('R','18').str.replace('S','19').str.replace('T','20').str.replace('U','21').str.replace('V','22').str.replace('W','23').str.replace('X','24').str.replace('Y','25').str.replace('Z','26')
  icd_10[['start_point','end_point']] = icd_10.SUBGROUP.str.split("-",expand=True)
  icd_10['start_point'] = icd_10['start_point'].astype('int')
  icd_10['end_point'] = icd_10['end_point'].astype('int')
  icd_10['check']=0
  icd_10.loc[(icd_10['start_point'] > icd_10['end_point']) ,['check']]='T1' 
  m = icd_10['check'] == 'T1'
  icd_10.loc[m, ['start_point', 'end_point']] = (icd_10.loc[m, ['end_point', 'start_point']].values)
  icd_10["Icd_range"] = icd_10['start_point'].astype(str) +"-"+ icd_10["end_point"].astype(str)
  result = []
  for ix, row in icd_10.iterrows():
    range_str = row["Icd_range"]
    for range_ in range(int(range_str.split("-")[0]), int(range_str.split("-")[1]) + 1):
      result.append({"GROUP_DESC": row["GROUP_DESC"],"Icd_code": range_})
  clean_group = pd.DataFrame(result)
  diagnoses_9=diagnoses.loc[diagnoses['icd_version'] == 9]
  diagnoses_10=diagnoses.loc[diagnoses['icd_version'] == 10]
  diagnoses_10=diagnoses_10[['subject_id','hadm_id','seq_num','icd_code']]
  new_group=new_group[['icd9cm','icd10cm']]
  merge_df=pd.merge(diagnoses_9,new_group,left_on='icd_code',right_on='icd9cm',how='left')
  merge_df=merge_df[['subject_id','hadm_id','seq_num','icd10cm']]
  merge_df.rename(columns = {'icd10cm':'icd_code'}, inplace = True)
  clean_data=pd.concat([merge_df, diagnoses_10], axis=0)
  clean_data=clean_data.drop_duplicates()
  clean_data['3_digit_code'] = clean_data.icd_code.str[:3]
  clean_data['3_digit_code']=clean_data['3_digit_code'].str.upper()
  clean_data['point']=clean_data['3_digit_code'].str.replace('A','1').str.replace('B','2').str.replace('C','3').str.replace('D','4').str.replace('E','5').str.replace('F','6').str.replace('G','7').str.replace('H','8').str.replace('I','9').str.replace('J','10').str.replace('K','11').str.replace('L','12').str.replace('M','13').str.replace('N','14').str.replace('O','15').str.replace('P','16').str.replace('Q','17').str.replace('R','18').str.replace('S','19').str.replace('T','20').str.replace('U','21').str.replace('V','22').str.replace('W','23').str.replace('X','24').str.replace('Y','25').str.replace('Z','26').str.replace("'",'').str.replace(" ",'')
  clean_data=clean_data.dropna(subset=['point'])
  clean_data['point'] = clean_data['point'].astype('int')
  final_data=pd.merge(clean_data,clean_group,left_on='point',right_on='Icd_code',how='left')
  final_data=final_data.dropna(subset=['GROUP_DESC'])
  final_data=final_data[['subject_id','hadm_id','GROUP_DESC','Icd_code']]
  final_data['cnt']=1
  table = pd.pivot_table(final_data, values='cnt', index=['subject_id','hadm_id'],columns=['GROUP_DESC'], aggfunc='sum')
  final_df = pd.DataFrame(table.to_records())
  return final_df