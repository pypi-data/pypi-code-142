import pickle  # nosec
from typing import Any, Dict
import joblib
from ..object_manager import ModelManager
from ..utils import from_file


class SKLearnModelManager(ModelManager):
    framework = "sklearn"

    def save_object(self, obj: Any):
        joblib.dump(obj, self.object_file_path)

    def load_object(self) -> Any:
        """
        Loads a stored SKLearn model. As the model is stored with pickle and a certain version of SKLearn, there
        may be inconsistencies where different versions of SKLearn are used for pickling and unpickling.
        :return:
        """
        try:
            return joblib.load(self.object_file_path)
        except Exception:
            # fallback on pickle for old filesz
            return pickle.loads(from_file(self.object_file_path, "rb"))  # nosec

    def hash_object(self, obj) -> int:
        return hash(str(obj))

    @staticmethod
    def get_params(model) -> Dict:
        """
        Extracts the parameters of the model.
        :param model: The model
        """

        return model.get_params()
