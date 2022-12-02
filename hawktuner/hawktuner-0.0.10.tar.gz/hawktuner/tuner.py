import json
import tqdm
import random
from multiprocessing import Pool
import multiprocessing
import uuid
from pathlib import Path
import torch
from typing import Dict, NamedTuple, Union, List, Tuple
import pickle


# from model.utils import ResultRecord

class NNParmSpace(NamedTuple):
    layers: Union[List, Tuple]
    dropout: Union[List, Tuple]
    activation: Union[List, Tuple]
    unit: Union[List, Tuple]
    other_parm: Dict
    input_size: int


class Tuner:
    def __init__(self, search_space, metrics: Dict[str, str], model_type='ml', train_func=None,
                 normalize_file_name=None, normalize_output_folder=None, is_save_model: bool = False,
                 model_key: str = None, model_folder=None):
        self.search_space = search_space
        self.train_func = train_func
        self.result_record = {}
        self.__cpu_count = multiprocessing.cpu_count()
        self.results = []
        self.metrics = metrics
        self.output = Path("output_log/")
        self.model_type = model_type
        self.normalize_file_name = normalize_file_name
        self.normalize_output_folder = Path(normalize_output_folder) if normalize_output_folder else Path(
            "normalize_data")
        self.normalize_output_folder.mkdir(exist_ok=True)
        self.model_folder = Path(model_folder) if model_folder else Path("model_set")
        self.model_folder.mkdir(exist_ok=True)
        self.model_key = model_key
        self.is_save_model = is_save_model

    def set_random_seed(self, seed=0):
        random.seed(seed)

    def get_rand_parm_from_space(self, space):
        if type(space) == tuple:
            parm = random.uniform(space[0], space[1])
        elif type(space) == list:
            parm = random.choice(space)
        return parm

    def nn_rand_parameter(self):
        result_parameter = {}
        ac_name = self.get_rand_parm_from_space(self.search_space.activation)
        layers_count = self.get_rand_parm_from_space(self.search_space.layers)
        drop_list = self.search_space.dropout
        unit_list = self.search_space.unit
        result_parameter['layer_count'] = layers_count
        layer_list = []
        result_parameter['activation'] = ac_name
        is_shrink = random.choice([True, False])
        pre_unit = self.search_space.input_size
        max_unit = max(unit_list)
        for i in range(layers_count):
            layer_info = {}
            if i == layers_count - 1:
                layer_info['in'] = pre_unit
                layer_info['out'] = 1
                layer_info['drop'] = 0
            else:
                if is_shrink:
                    # current_unit = max([unit for unit in unit_list if unit < pre_unit])
                    current_unit = int(pre_unit/2)
                    drop_unit = random.choice(drop_list)
                    layer_info['in'] = pre_unit
                    layer_info['out'] = current_unit
                    layer_info['drop'] = drop_unit
                    pre_unit = current_unit
                else:
                    drop_unit = random.choice(drop_list)
                    layer_info['in'] = pre_unit
                    layer_info['out'] = max_unit
                    layer_info['drop'] = drop_unit
                    pre_unit = max_unit
                    is_shrink = True
            layer_list.append(layer_info)
        result_parameter['layers'] = layer_list
        for name, space in self.search_space.other_parm.items():
            if type(space) == tuple:
                result_parameter[name] = random.uniform(space[0], space[1])
            elif type(space) == list:
                result_parameter[name] = random.choice(space)
        return result_parameter

    def rand_parameter(self):
        result_parameter = {}
        if self.model_type != 'ml':
            result_parameter = self.nn_rand_parameter()
        else:
            for k, v in self.search_space.items():
                result_parameter[k] = self.get_rand_parm_from_space(v)
            result_parameter['id'] = str(uuid.uuid4())
        return result_parameter

    def set_cpu(self, cpu_count):
        self.__cpu_count = cpu_count

    def tune(self, num_parameter, is_nn=False, input_parm=None, output_normalize_data=True):
        if is_nn:
            mp = torch.multiprocessing.get_context('spawn')
            pool = mp.Pool(self.__cpu_count)
        else:
            pool = Pool(self.__cpu_count)
        if len(input_parm) == 0:
            results = pool.map(self.train_func, [(self.rand_parameter()) for _ in range(num_parameter)])
        else:
            results = pool.starmap(self.train_func,
                                   tqdm.tqdm([input_parm + (self.rand_parameter(),) for _ in range(num_parameter)],
                                             total=num_parameter))
        # results_list = self.output_generalize(results)
        self.results = results
        res = self.get_best_result()
        self.save_log(res)
        if output_normalize_data:
            # self.output_normalize(res)
            pass
        if self.is_save_model:
            self.save_model()

    def get_best_result(self, metrics: Dict[str, str] = None):
        metrics_key_dict = metrics if metrics else self.metrics
        result_dict = {}
        for metrics, key in metrics_key_dict.items():
            if key.lower() == "min":
                res = min(self.results, key=lambda i: i[metrics])
            elif key == "max":
                res = max(self.results, key=lambda i: i[metrics])
            result_dict[metrics] = res
        return result_dict

    def save_log(self, res):
        res_dict = {k: v['parm'] for k, v in res.items()}
        json_object = json.dumps(res_dict, indent=4)
        self.output.mkdir(exist_ok=True)
        output_path = self.output / "hyper_parm.json"
        with open(output_path, "w") as outfile:
            outfile.write(json_object)

    def output_normalize(self, best_res):
        with open(self.normalize_output_folder / self.normalize_file_name + "_mean.json", "w") as f:
            json.dump(dict(best_res['mean']), f, indent=4)
        with open(self.normalize_output_folder / self.normalize_file_name + "_std.json", "w") as f:
            json.dump(dict(best_res['std']), f, indent=4)

    def save_model(self):
        for metrics, key in self.metrics.items():
            if key.lower() == "min":
                res = min(self.results, key=lambda i: i[metrics])
            elif key == "max":
                res = max(self.results, key=lambda i: i[metrics])
            model = res[self.model_key]
            model_name = metrics + "_model"
            with open(self.model_folder / model_name, 'wb') as f:
                pickle.dump(model, f)
