from cloudpickle import load as pickle_load, dump
from torch.jit import load as torchscript_load
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper
import os
import re
import tempfile
import zipfile
import requests
import json
from xgboost import XGBClassifier
from torch import Tensor, device
from torch.cuda import is_available
from numpy import atleast_2d, ndarray

from cerebrium.flow import CerebriumFlow, ModelType, _check_flow_type
from cerebrium.models.torch import TorchModel
from cerebrium.models.xgboost import XGBClassfierModel

REGEX_NAME_PATTERN = "^[a-z0-9-]*$"
class Conduit:
    """
    The Conduit class encompasses the logic required to create a computational graph from a given model flow, as well as the logic required to run the graph on a given input.
    """

    def __init__(self, name: str, api_key: str, flow: CerebriumFlow = []):
        # Check that the flow name is valid
        if len(name) > 20:
            raise ValueError("Conduit name must be less than 20 characters")
        if not bool(re.match(REGEX_NAME_PATTERN, name)):
            raise ValueError(
                "Conduit name can only contain lowercase alphanumeric characters and hyphens"
            )
        self.name = name
        self.api_key = api_key
        if flow is not None:
            self.flow = _check_flow_type(flow)
        self.flow = flow
        self.graph = []
        self.ready = False

    def load(self, directory: str = "/cache/", direct_from_flow: bool = False):
        """
        Load the Conduit components from the stored Model Flow into the computation graph.

        Args:
            directory (str): The directory to load the Conduit components from.
        """
        if self.flow == []:
            raise ValueError("Conduit is empty. Please add models to the Conduit flow.")
        else:
            self.device = device('cuda' if is_available() else 'cpu')
            for model_type, model_path, _ in self.flow:
                if direct_from_flow:
                    model_path = os.path.abspath(model_path)
                else:
                    model_path = directory + model_path.split("/")[-1]
                if model_type == ModelType.TORCH:
                    if model_path.endswith(".pt"):
                        model = torchscript_load(model_path)
                    else:
                        with open(model_path, "rb") as f:
                            model = pickle_load(f)
                    model.to(self.device)
                    self.graph.append(TorchModel(model))
                elif model_type == ModelType.XGBOOST_CLASSIFIER:
                    if model_path.endswith("json"):
                        model = XGBClassifier()
                        model.load_model(model_path)
                    else:
                        with open(model_path, "rb") as f:
                            model = pickle_load(f)
                    self.graph.append(XGBClassfierModel(model))
            self.ready = True

    def run(self, data: list):
        """
        Run the Conduit on the given input with the stored computational graph.

        Args:
            data (list): The input data to run the Conduit on.
        """
        if not self.ready:
            return "Conduit not ready. Please load the Conduit components with conduit.load()."
        else:
            if self.flow[0][0] == ModelType.TORCH:
                data = Tensor(atleast_2d(data)).to(self.device)
            else:
                data = atleast_2d(data)

            for ((model_type, _, postprocessor), (model)) in zip(self.flow, self.graph):
                # Ensure that the input data is the correct type
                if model_type == ModelType.TORCH and not isinstance(data, Tensor):
                    data = Tensor(data).to(self.device)
                elif model_type != ModelType.TORCH and isinstance(data, Tensor):
                    data = data.detach().numpy()
                
                # Run the model
                if model_type == ModelType.SKLEARN_PREPROCESSOR:
                    data = model.transform(data)
                else:
                    data = model.predict(data)
                
                # Run the postprocessor
                if postprocessor:
                    data = postprocessor(data)

            # Ensure that final output is a list
            if isinstance(data, Tensor):
                data = data.detach().numpy().tolist()
            elif isinstance(data, ndarray):
                data = data.tolist()
            
            # If the output is not a list or dict, throw an error
            if not isinstance(data, list) and not isinstance(data, dict):
                raise ValueError("Conduit output must be a list or dictionary. Please check your final postprocessor's output.")
            return data

    def add_model(self, model_type, model_path, postprocessor=None):
        self.flow.append((model_type, model_path, postprocessor))

    def _upload(self, url):
        """
        Upload the Conduit to Cerebrium.

        Args:
            url (str): The upload URL.

        Returns:
            dict ('status_code': int, 'data': dict): The response code and data. 'data' contains the flow token if successful.
        """
        if self.flow == []:
            raise ValueError("Conduit is empty. Please add models to the Conduit.")
        else:
            # Create a temporary directory to store the Conduit zip
            with tempfile.TemporaryDirectory() as tmpdir:
                # Create a zip file of the Conduit, writing the model files and Conduit object to the zip
                with zipfile.ZipFile(tmpdir + f"/{self.name}.zip", "w") as zip:
                    for (_, model_path, _) in self.flow:
                        true_path = os.path.abspath(model_path)
                        print(os.path.basename(true_path))
                        print(true_path)
                        zip.write(true_path, os.path.basename(true_path))
                    with open("conduit.pkl", "wb") as f:
                        c = Conduit(self.name, self.api_key, self.flow)
                        dump(c, f)
                    zip.write("conduit.pkl")
                # Upload the Conduit zip, chunking with tqdm for progress bar
                with open(tmpdir + f"/{self.name}.zip", "rb") as f:
                    headers = {
                        "Content-Type": "application/zip",
                    }
                    with tqdm(
                        total=os.path.getsize(tmpdir + f"/{self.name}.zip"),
                        unit="B",
                        unit_scale=True,
                        unit_divisor=1024,
                        colour="#EB3A6F",
                    ) as pbar:
                        wrapped_f = CallbackIOWrapper(pbar.update, f, "read")
                        response = requests.put(
                            url,
                            headers=headers,
                            data=wrapped_f,
                            timeout=60,
                            stream=True,
                        )
                    data = {} if not response.text else json.loads(response.text)
                    return {"status_code": response.status_code, "data": data}
