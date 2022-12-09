import requests
import pandas as pd
from ascendpbm_package.parsers.json import recursive_keys

def drop_frame_dupes(df,
                     add_id=True):
    
    # Drop dupes via type conversion to str
    dff = df.reset_index(drop=True)
    for col in dff.columns:
        dff[col] = dff[col].astype(str)
    dff.drop_duplicates(inplace=True)
    df = df.iloc[dff.index]
    df.reset_index(inplace=True, drop=True)

    # optionally add reset index as id col
    if add_id is True:
        df.loc[:, 'id'] = df.index
    
    return df

def get_classes(search_str,
                base_url='https://rxnav.nlm.nih.gov',
                all_class_url='/REST/rxclass/allClasses.json',
                regex=False,
                case=False,
                output='flat'):
    
    # Get all classes somehow related to cancer by a regex string...
    all_class_url = '/REST/rxclass/allClasses.json'
    full_url = base_url + all_class_url
    class_response = requests.get(full_url)
    class_response_json = class_response.json()
    
    if output == 'flat':
        try:
            class_response_frame = pd.json_normalize(
                class_response_json,
                recursive_keys(class_response_json)
                )
        except Exception as e:
            print(f'Sorry, but {e} occurred during flattening... returning full json instead')
            return class_response_json
    
    else:
        return class_response_json
    
    regex_filter = class_response_frame['className'].str.contains(search_str,
                                                                  case=case,
                                                                  regex=regex)
    filtered_classes = class_response_frame.loc[regex_filter, :]
    
    return filtered_classes

# all current data sources by name/code
def get_all_sources(base_url='https://rxnav.nlm.nih.gov',
                    all_source_url='/REST/rxclass/relaSources.json',
                    output='flat'):
    
    full_url = base_url + all_source_url
    source_response = requests.get(full_url)
    source_response_json = source_response.json()
    
    if output == 'flat':
        try:
            source_response_frame = pd.json_normalize(
                source_response_json,
                recursive_keys(source_response_json)
                )
        except Exception as e:
            print(f'Sorry, but {e} occurred during flattening... returning full json instead')
            return source_response_json
    
    else:
        return source_response_json
    
    return source_response_frame

def get_drug_members(base_url='https://rxnav.nlm.nih.gov',
                     base_class_members='/REST/rxclass/classMembers.json',
                     output='flat',
                     **kwargs
                     ):
    
    # optional paramaters
    if kwargs:
        url_params = '?'
        # this guarantees no user-redefinitions of base_url etc make it into params
        user_keys = set(kwargs.keys()).difference(['base_url',
                                                  'base_class_members',
                                                  'output'])
        user_params = {uk: kwargs[uk] for uk in user_keys}
        for k, v in user_params.items():
            url_params = url_params + str(k) + '=' + str(v) + '&'
        url_params = url_params[:-1]
    else:
        url_params = ''
    
    # final get
    full_url = base_url + base_class_members + url_params
    member_response = requests.get(full_url)
    
    # check for results, and flatten if there are any
    if len(member_response.json()) > 0:
        member_response_json = member_response.json()
        member_response_frame = pd.json_normalize(member_response_json,
                                                  recursive_keys(member_response_json))
        return member_response_frame
    else:
        return None
    
def get_all_properties(rxcui,
                       base_url='https://rxnav.nlm.nih.gov',
                       **kwargs
                       ):

    # optional paramaters
    if kwargs:
        url_params = '?'
        # this guarantees no user-redefinitions of base_url make it into params
        user_keys = set(kwargs.keys()).difference(['base_url'])
        user_params = {uk: kwargs[uk] for uk in user_keys}
        for k, v in user_params.items():
            url_params = url_params + str(k) + '=' + str(v) + '&'
        url_params = url_params[:-1]
    else:
        url_params = ''

    properties_url = f'/REST/rxcui/{rxcui}/allrelated.json'
    full_url = base_url + properties_url + url_params
    properties_response = requests.get(full_url)
    properties_response_json = properties_response.json()
    
    # didn't find an ez pandas way to flatten this, so keeping json for now
    # this shows how making a class with separate methods for flattening,
    # or for parameter addition, could be much more succinct and powerful
    
    return properties_response_json
    
def get_historical_ndc(rxcui,
                       base_url='https://rxnav.nlm.nih.gov',
                       output='flat',
                       **kwargs
                       ):

    # optional paramaters
    if kwargs:
        url_params = '?'
        # this guarantees no user-redefinitions of base_url make it into params
        user_keys = set(kwargs.keys()).difference(['rxcui', 'base_url', 'output'])
        user_params = {uk: kwargs[uk] for uk in user_keys}
        for k, v in user_params.items():
            url_params = url_params + str(k) + '=' + str(v) + '&'
        url_params = url_params[:-1]
    else:
        url_params = ''

    historical_ndc_url = f'/REST/rxcui/{rxcui}/allhistoricalndcs.json'
    full_url = base_url + historical_ndc_url + url_params
    historical_ndc_response = requests.get(full_url)
    historical_ndc_json = historical_ndc_response.json()
    
    if len(historical_ndc_json) > 0:
        if output == 'flat':
            historical_ndc_frame = pd.json_normalize(historical_ndc_json,
                                                     recursive_keys(historical_ndc_json))
            return historical_ndc_frame
        
        else:
            return historical_ndc_json
        
    else:
        return None