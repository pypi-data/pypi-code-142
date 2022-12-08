import json
import os
from types import SimpleNamespace


def from_json(file):
    f = open(file)
    data = json.load(f)
    return data

def to_json(file, data):
  os.makedirs(os.path.dirname(file), exist_ok=True)
  with open(file, 'w+', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
   
  return data  

def dumps(data):
  
  def get_dict(data):
    try:
      return data.__dict__
    except Exception as err:
      print(err)
      pass

  return json.dumps(data, default=lambda data: get_dict(data), sort_keys=True, indent=4)

def loads(data):
  return json.loads(data, object_hook=lambda d: SimpleNamespace(**d)) 