from typing import AnyStr
import uuid
import random   


def generate_id():
    return str(uuid.uuid4())

def remove_last_slash(str: AnyStr):
    return (str).strip("/")

def get_dict_attr(dict_object, attr_name, default_value = None):
 
    if attr_name in dict_object:
        return dict_object[attr_name]
    else:
        return default_value    

def get_random(min, max):
  return random.randint(min, max)

def get_attr(object, attr_name, default_value = None):

    if (type(object) is dict):
        #it is a dictionary
        if attr_name in object:
            return object[attr_name]
        else:
            return default_value    
    else:
        #it is a python object
        if hasattr(object, attr_name):
            return getattr(object, attr_name) 
        else:
            return default_value 

def get_value_by_attrs(object, attr_names, default_value = None):
    value = None
    for field in attr_names:
        value = get_attr(object, field, default_value)
        if (value != None):
            return value, field
    return value, field
    

def has_attr(object, attr_name):

    if (type(object) is dict):
        #it is a dictionary
        if attr_name in object:
            return True
        else:
            return False    
    else:
        #it is a python object
        if hasattr(object, attr_name):
            return True
        else:
            return False   

def has_attr_and_value(object, attr_name, reject_empty = False):

   has_att = has_attr(object, attr_name)
   if (has_att == True):
       value = get_attr(object, attr_name)
       if (reject_empty == False):
            return value!=None
       else:
           if (value == None):
               return False
           else:
               return (len(str(value)) > 0)

   else:
       return None    


def check_type(obj, _type):
    return isinstance(obj, _type)            

        
