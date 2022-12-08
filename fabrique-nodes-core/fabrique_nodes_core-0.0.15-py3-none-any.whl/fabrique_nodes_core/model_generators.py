from pathlib import Path
import json
import os
import sys
from pydantic import BaseModel
import typing
from datamodel_code_generator import InputFileType, generate
# import importlib
from importlib.machinery import SourceFileLoader

cur_file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f'{cur_file_dir}/.')

from core import Port, SYS_FIELDS


def data2models(data, input_file_type=InputFileType.Auto, path='.'):
    output = Path(os.path.join(path, 'model.py'))
    full_pth = str(output)
    generate(
        data,
        input_file_type=input_file_type,
        input_filename="example.json",
        output=output,
    )


    #import model  # noqa
    #importlib.reload(model)

    model = SourceFileLoader('model', full_pth).load_module()
    try:
        os.remove(full_pth)
    except OSError:
        pass
    return model


def jsons2model(jsons: typing.List[str], input_file_type=InputFileType.Json, path='.'):
    jsons_str = ',\n'.join(jsons)
    json_data = f"[{jsons_str}]"
    model = data2models(json_data, input_file_type, path)
    return model.ModelItem


def schema2model(json_schema):
    py_dict = json.loads(json_schema)
    py_dict.pop('title', 0)
    schema = json.dumps(py_dict)
    model = data2models(schema, input_file_type=InputFileType.JsonSchema)
    return model.Model


def model2schema(model):
    py_dict = model.schema()
    py_dict.pop('title', 0)
    return json.dumps(py_dict, indent=2)


def field2schema(model, field_name: str):
    type_ = model.__fields__[field_name].type_
    return model2schema(type_)


def is_list(field_cls):
    return typing.get_origin(field_cls.outer_type_) is list


def is_object(field_cls):
    type_ = field_cls.type_
    return issubclass(type_, BaseModel)


def model2ports(Model) -> typing.List[Port]:
    model_type = dict
    if Model.__fields__.get('__root__'):
        model_type = list
    model_port = Port(id_='root', name='root', special=True)
    model_port.type_ = model_type
    model_port.model = Model

    def field2port(key, val):
        code = key
        if key in SYS_FIELDS:
            key += '_'
        type_ = val.type_
        port = Port(id_=key, name=key)
        port.required = Model.__fields__[key].required
        port.code = code
        if is_list(val):
            port.type_ = list
            if is_object(val):
                port.model = type_
        elif is_object(val):
            port.type_ = dict
            port.model = type_
        else:
            port.type_ = type_
        return port

    # ports = [ model2port('root', Model), ]

    ports = [model_port, ] + [field2port(key, val) for key, val in Model.__fields__.items()]
    return ports
