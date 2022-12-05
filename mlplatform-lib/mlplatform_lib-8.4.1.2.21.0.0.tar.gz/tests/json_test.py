import pandas as pd
import sys
sys.path.append('../')
from mlplatform_lib.dataclass.insert_tuple_object import InsertTupleObject
import json

inference_data = pd.read_csv('adinf750.csv')

insert_tuple_object = InsertTupleObject(
    isTruncated="True",
    targetColNames=inference_data.columns.tolist(),
    tableData=inference_data.values.tolist(),
)
        

test = json.dumps(insert_tuple_object.__dict__)

print(json.dumps(test))