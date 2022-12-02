#https://www.w3schools.com/python/python_datatypes.asp

data=[
    {'key': "<class 'str'>", "type":"str"},#
    {'key': "<class 'int'>", "type":"int"},#
    {'key': "<class 'float'>", "type":"float"},#
    {'key': "<class 'complex'>", "type":"complex"},#
    {'key': "<class 'bool'>", "type":"bool"},#
    {'key': "<class 'list'>", "type":"list"},#
    {'key': "<class 'tuple'>", "type":"tuple"},#
    {'key': "<class 'dict'>", "type":"dict"},#
    {'key': "<class 'set'>", "type":"set"},#
    {'key': "<class 'frozenset'>", "type":"frozenset"},#
    {'key': "<class 'bytes'>", "type":"bytes"},#
    {'key': "<class 'bytearray'>", "type":"bytearray"},#
    {'key': "<class 'memoryview'>", "type":"memoryview"},
    {'key': "<class 'NoneType'>", "type":"None"},#
    {'key': "class", "type":"class"}#
]




def find_type(type_object) -> str:
    """It returns the type in str format
    when doesn't find it, it returns an empty str"""

    key_str = str(type(type_object))
    for a in data:
        if a['key'] == key_str:
            return a['type']
    
    #detect class

    if key_str.find('class'):
        return data[14]['type']
    return ''

def str_wrapper(key_str:str, value:str, final_json = False):
    if key_str == '':
        return '"' + value + '"'
    res = '"' + key_str + '":"' + value + '"'
    if final_json:
        return final_wrapper(res)
    else:
        return res

def int_wrapper(key_str:str, value:int, final_json = False):
    if key_str == '':
        return str(value)
    res = '"' + key_str + '":' + str(value)
    if final_json:
        return final_wrapper(res)
    else:
        return res

def float_wrapper(key_str:str, value:float, final_json = False):
    if key_str == '':
        return str(value)
    res = '"' + key_str + '":' + str(value)
    if final_json:
        return final_wrapper(res)
    else:
        return res

def complex_wrapper(key_str:str, value:complex, final_json = False):
    if key_str == '':
        return '"' + str(value) + '"'
    res = '"' + key_str + '":"' + str(value) + '"'
    if final_json:
        return final_wrapper(res)
    else:
        return res

def bool_wrapper(key_str:str, value:bool, final_json = False):
    if key_str == '':
        return str(value)
    res = '"' + key_str + '":' + str(value)
    if final_json:
        return final_wrapper(res)
    else:
        return res

def list_wrapper(key_str:str,value:list,final_json = False):
    if key_str == '':
        res = '['
    else:
        res = '"' + key_str + '":['
    if len(value) > 0:
        for a in value:    
            res += jsonwhatever('',a,False) + ','
        res = res[:-1] + ']'
    else:
        res += ']'
    if final_json:
        return final_wrapper(res)
    else:
        return res

def dict_wrapper(key_str:str,value:dict,final_json = False):
    res = ''
    if len(value) > 0:
        for key in value:    
            value_dict = value[key]
            
            res += jsonwhatever(key_str=key,value=value_dict,final_json=False) + ','
        res = res[:-1]
    
    return final_wrapper(res)

def bytes_wrapper(key_str:str, value:bytes, final_json = False):
    if key_str == '':
        return str(value)
    res = '"' + key_str + '":' + '"' + str(value) + '"'
    if final_json:
        return final_wrapper(res)
    else:
        return res

def none_wrapper(key_str:str,final_json = False):
    res =  '"' + key_str + '":null'
    if final_json:
        return final_wrapper(res)
    else:
        return res

def class_wrapper(key_str:str,value:dict,final_json = False):
    return dict_wrapper(key_str=key_str,value=value.__dict__,final_json=False)

def final_wrapper(data:str):
    return '{' + data + '}'


def jsonwhatever(key_str:str, value, final_json = True):
    type_str = find_type(value)

    if type_str == data[0]['type']:#str
        return str_wrapper(key_str=key_str,value=value,final_json=final_json)

    if type_str == data[1]['type']:#int
        return int_wrapper(key_str=key_str,value=value,final_json=final_json)
    
    if type_str == data[2]['type']:#float
        return float_wrapper(key_str=key_str,value=value,final_json=final_json)
    
    if type_str == data[3]['type']:#complex
        return complex_wrapper(key_str=key_str,value=value,final_json=final_json)
    
    if type_str == data[4]['type']:#bool
        return bool_wrapper(key_str=key_str,value=value,final_json=final_json)

    if type_str == data[5]['type']:#list
        return list_wrapper(key_str=key_str,value=value,final_json=final_json)
    
    if type_str == data[6]['type']:#tuple
        return list_wrapper(key_str=key_str,value=list(value),final_json=final_json)

    if type_str == data[7]['type']:#dictionary
        return dict_wrapper(key_str=key_str,value=value,final_json=final_json)

    if type_str == data[8]['type']:#set
        return list_wrapper(key_str=key_str,value=list(value),final_json=final_json)
    
    if type_str == data[9]['type']:#fronzenset
        return list_wrapper(key_str=key_str,value=list(value),final_json=final_json)

    if type_str == data[10]['type']:#bytes
        return bytes_wrapper(key_str=key_str,value=value,final_json=final_json)
    
    if type_str == data[11]['type']:#bytearray
        return bytes_wrapper(key_str=key_str,value=bytes(value),final_json=final_json)
        
    if type_str == data[13]['type']:#nonetype
        return none_wrapper(key_str=key_str,final_json=final_json)

    if type_str == data[14]['type']:#object class
        return class_wrapper(key_str=key_str,value=value,final_json=final_json)
    