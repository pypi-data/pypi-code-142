
class JsonWhatEver:
    def __init__(self) -> None:
        self.__recursion_count = 0
        self.__recursion_levels = 800
        self.__data =[
                {'key': "<class 'str'>", "type":"str"},
                {'key': "<class 'int'>", "type":"int"},
                {'key': "<class 'float'>", "type":"float"},
                {'key': "<class 'complex'>", "type":"complex"},
                {'key': "<class 'bool'>", "type":"bool"},
                {'key': "<class 'list'>", "type":"list"},
                {'key': "<class 'tuple'>", "type":"tuple"},
                {'key': "<class 'dict'>", "type":"dict"},
                {'key': "<class 'set'>", "type":"set"},
                {'key': "<class 'frozenset'>", "type":"frozenset"},
                {'key': "<class 'bytes'>", "type":"bytes"},
                {'key': "<class 'bytearray'>", "type":"bytearray"},
                {'key': "<class 'memoryview'>", "type":"memoryview"},
                {'key': "<class 'NoneType'>", "type":"None"},
                {'key': "class", "type":"class"}
            ]
    

    def find_type(self,type_object) -> str:
        """It returns the type in str format
        when doesn't find it, it returns an empty str"""

        key_str = str(type(type_object))
        for a in self.__data:
            if a['key'] == key_str:
                return a['type']
        
        #detect class-object
        if key_str.find('class'):
            return self.__data[14]['type']
        return ''

    """Beyond this point it will start all the string parses"""
    def str_wrapper(self,key_str:str, value:str, final_json = False):
        if key_str == '':
            return '"' + value + '"'
        res = '"' + key_str + '":"' + value + '"'
        if final_json:
            return self.final_wrapper(res)
        else:
            return res

    def int_wrapper(self,key_str:str, value:int, final_json = False):
        if key_str == '':
            return str(value)
        res = '"' + key_str + '":' + str(value)
        if final_json:
            return self.final_wrapper(res)
        else:
            return res

    def float_wrapper(self,key_str:str, value:float, final_json = False):
        if key_str == '':
            return str(value)
        res = '"' + key_str + '":' + str(value)
        if final_json:
            return self.final_wrapper(res)
        else:
            return res

    def complex_wrapper(self, key_str:str, value:complex, final_json = False):
        if key_str == '':
            return '"' + str(value) + '"'
        res = '"' + key_str + '":"' + str(value) + '"'
        if final_json:
            return self.final_wrapper(res)
        else:
            return res

    def bool_wrapper(self,key_str:str, value:bool, final_json = False):
        if key_str == '':
            return str(value)
        res = '"' + key_str + '":' + str(value)
        if final_json:
            return self.final_wrapper(res)
        else:
            return res

    def bytes_wrapper(self,key_str:str, value:bytes, final_json = False):
        if key_str == '':
            return str(value)
        res = '"' + key_str + '":' + '"' + str(value) + '"'
        if final_json:
            return self.final_wrapper(res)
        else:
            return res

    def none_wrapper(self, key_str:str,final_json = False):
        res =  '"' + key_str + '":null'
        if final_json:
            return self.final_wrapper(res)
        else:
            return res

    def class_wrapper(self, key_str:str,value:dict,final_json = False):
        return self.dict_wrapper(key_str=key_str,value=value.__dict__,final_json=False)            

    """Right here starts the array parse"""
    def list_wrapper(self,key_str:str,value:list,final_json = False):
        if key_str == '':
            res = '['
        else:
            res = '"' + key_str + '":['
        if len(value) > 0:
            for a in value:    
                res += self.main_wrapper('',a,False) + ','
            res = res[:-1] + ']'
        else:
            res += ']'
        if final_json:
            return self.final_wrapper(res)
        else:
            return res

    def dict_wrapper(self,key_str:str,value:dict,final_json = False):
        res = ''
        if len(value) > 0:
            for key in value:    
                value_dict = value[key]
                
                res += self.main_wrapper(key_str=key,value=value_dict,final_json=False) + ','
            res = res[:-1]
        
        return self.final_wrapper(res)

    """The final wrapper is use to add {}"""
    def final_wrapper(self, data:str):
        return '{' + data + '}'

    def jsonwhatever(self, key_str:str, value, final_json = True):
        res =  self.main_wrapper(key_str=key_str,value=value,final_json=final_json)
        self.__recursion_count = 0 #in this part, the recursion count, resets
        return res

    def main_wrapper(self, key_str:str, value, final_json = True):
        type_str = self.find_type(value)

        self.__recursion_count += 1

        if self.__recursion_count > self.__recursion_levels:
            raise RecursionError('JsonWhatEver can not go too far in the Recursion by levels')

        if type_str == self.__data[0]['type']:#str
            return self.str_wrapper(key_str=key_str,value=value,final_json=final_json)

        if type_str == self.__data[1]['type']:#int
            return self.int_wrapper(key_str=key_str,value=value,final_json=final_json)
        
        if type_str == self.__data[2]['type']:#float
            return self.float_wrapper(key_str=key_str,value=value,final_json=final_json)
        
        if type_str == self.__data[3]['type']:#complex
            return self.complex_wrapper(key_str=key_str,value=value,final_json=final_json)
        
        if type_str == self.__data[4]['type']:#bool
            return self.bool_wrapper(key_str=key_str,value=value,final_json=final_json)

        if type_str == self.__data[5]['type']:#list
            return self.list_wrapper(key_str=key_str,value=value,final_json=final_json)
        
        if type_str == self.__data[6]['type']:#tuple
            return self.list_wrapper(key_str=key_str,value=list(value),final_json=final_json)

        if type_str == self.__data[7]['type']:#dictionary
            return self.dict_wrapper(key_str=key_str,value=value,final_json=final_json)

        if type_str == self.__data[8]['type']:#set
            return self.list_wrapper(key_str=key_str,value=list(value),final_json=final_json)
        
        if type_str == self.__data[9]['type']:#fronzenset
            return self.list_wrapper(key_str=key_str,value=list(value),final_json=final_json)

        if type_str == self.__data[10]['type']:#bytes
            return self.bytes_wrapper(key_str=key_str,value=value,final_json=final_json)
        
        if type_str == self.__data[11]['type']:#bytearray
            return self.bytes_wrapper(key_str=key_str,value=bytes(value),final_json=final_json)
            
        if type_str == self.__data[13]['type']:#nonetype
            return self.none_wrapper(key_str=key_str,final_json=final_json)

        if type_str == self.__data[14]['type']:#object class
            return self.class_wrapper(key_str=key_str,value=value,final_json=final_json)