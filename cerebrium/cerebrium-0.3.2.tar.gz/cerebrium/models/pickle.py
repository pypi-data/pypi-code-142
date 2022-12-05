from pipeline import (
    PipelineFile,
    pipeline_function,
    pipeline_model,
)
from cloudpickle import load as pickle_load
from numpy import atleast_2d


@pipeline_model
class PickleModel:
    def __init__(self):
        self.model = None

    @pipeline_function(run_once=True, on_startup=True)
    def load(self, model_file: PipelineFile) -> bool:
        try:
            self.model = pickle_load(open(model_file.path, "rb"))
            return True
        except Exception as e:
            print(e)
            return False

    @pipeline_function
    def predict(self, input_list: list) -> list:
        array = atleast_2d(input_list)
        return self.model.predict(array).tolist()


@pipeline_model
class PickleClassifierModel:
    def __init__(self):
        self.model = None

    @pipeline_function(run_once=True, on_startup=True)
    def load(self, model_file: PipelineFile) -> bool:
        try:
            self.model = pickle_load(open(model_file.path, "rb"))
            return True
        except Exception as e:
            print(e)
            return False

    @pipeline_function
    def predict(self, input_list: list) -> list:
        array = atleast_2d(input_list)
        return self.model.predict_proba(array).tolist()


@pipeline_model
class PicklePreprocessorModel:
    def __init__(self):
        self.model = None

    @pipeline_function(run_once=True, on_startup=True)
    def load(self, model_file: PipelineFile) -> bool:
        try:
            self.model = pickle_load(open(model_file.path, "rb"))
            return True
        except Exception as e:
            print(e)
            return False

    @pipeline_function
    def predict(self, input_list: list) -> list:
        array = atleast_2d(input_list)
        return self.model.transform(array).tolist()
