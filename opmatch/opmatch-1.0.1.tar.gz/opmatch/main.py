from typing import List
import pandas as pd
from opmatch.util import variable_ratio_match, entire_number_match

def match(df:pd.DataFrame, matching_ratio:int=None, min_mr:int=None, 
         max_mr:int=None, n_controls:int=None, metric:str='PS',
         var_cols:List[str]=None, case_col:str='case',matching_type:str='const')->dict:
    """
    df: has to contain 'case' column, 
        matching dictionary will be returned with dataframe indices
    matching_type: var, const, full, entire_number
    min_mr: minimum number of controls per case
    max_mr: maximum number of controls per case

    n_controls: total number of controls, if constant matching ratio c desired:
        min_mr=max_mr=c, n_controls=c*n_cases
    metric: PS or check https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html#scipy.spatial.distance.cdist
        distances
    var_cols: if Mahalanobis or Euclidian, columns that will be used for matching
    
    returns:
        {case0_id:[control00_id, control01_id,...], 
        case1_id:[control10_id, control11_id, ...]}
    """
    df[case_col] = df[case_col].astype(bool)
    if matching_type=='const':
        assert isinstance(matching_ratio, int), 'Pass an integer to matching_ratio'
        n_case = len(df[(df.case==1)])
        matching_dic = variable_ratio_match.match(df, min_mr=matching_ratio, 
            max_mr=matching_ratio, n_controls=n_case*matching_ratio, 
            metric=metric, var_cols=var_cols, case_col=case_col)
        return matching_dic
    elif matching_type=='var':
        matching_dic = variable_ratio_match.match(df, min_mr, 
            max_mr, n_controls, metric, var_cols, case_col)
        return matching_dic
    elif matching_type=='entire_number':
        assert metric=='PS', 'For entire number matching the metric must be PS'
        entire_number_match.match(df)
        

