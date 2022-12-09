import os

from unidev.model_utils.model import Model


class ModelLoader:
    DEFAULT_DIR = "models/"
    FILE_EXTENSION = ".model"

    device_list = {}

    data_file = None
    data_dump = None

    def __init__(self, directory=DEFAULT_DIR):
        file_list = os.listdir(directory)
        for file in file_list:
            if not file.endswith(self.FILE_EXTENSION):
                file_list.remove(file)
            else:
                self.device_list[file.strip(self.FILE_EXTENSION)] = directory + file

    def load_model(self, device_name=None, path=None):
        model_path = None

        if device_name is not None:
            model_path = self.device_list.get(device_name)
        if path is not None:
            model_path = path

        model: Model = Model(model_path)
        return model

    def get_device_list(self):
        return self.device_list.keys()











