# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 10:55:48 2022

@author: Hedi
"""

import json
import os


class _schema_obj:
    def __init__(self, dict_):
            self.__dict__.update(dict_)
class obj:
    def __init__(self):
        for k,v in self.schema.__dict__.items():
                setattr(self,k,v.default)    
    @property
    def type(self):
        return type(self).__name__
    @property
    def schema(self):
        return getattr(_schema,self.type)
    
def load_json(fname):
    return json.loads(json.dumps(json.
                                 loads(open (os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                 fname+".json"), "r").read()),), object_hook=_schema_obj,)
_schema = load_json("moist_air")

class moist_air(obj):
    def __init__(self,**args):
        self.auto_calcul=False
        super().__init__()
        for k,v in args.items():
            if hasattr(self,k):
                setattr(self,k,v)