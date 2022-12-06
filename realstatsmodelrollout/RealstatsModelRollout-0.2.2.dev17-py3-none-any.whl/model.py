from .global_functions import globalFunctions as GF
import requests


class Model:
    def __init__(self):
        self._model_port = "8000"
        self._modelURL = "http://127.0.0.1"

    # Port that is being used by the virtual env #
    @property
    def Model_port(self):
        """
        :type: string
        """
        return self._model_port

    @Model_port.setter
    def Model_port(self, value):
        """
        :type: string
        """
        self._model_port = GF.Check_instance(check=value, instance_type="string")

    # URL to model #
    @property
    def Model_URL(self):
        """
        :type: string
        """
        return self._modelURL

    @Model_URL.setter
    def Model_URL(self, value):
        """
        :type: string
        """
        self._modelURL = GF.Check_instance(check=value, instance_type="string")

    def Info_request(self):
        response = ""
        try:
            response = requests.get(
                url=self._modelURL + ':' + self._model_port + "/info")
        except Exception as e:
            print(e)
            return Exception("Not able to get data from URL please check if model is running or online")
        return response

    def Predict_request(self, json_data=''):
        response = ""
        try:
            response = requests.post(
                url=self._modelURL + ':' + self._model_port + "/predict",
                json=json_data)
        except Exception as e:
            print(e)
            return Exception("Not able to get data from URL please check if model is running or online")
        return response

    def Validate_request(self, payload):
        response = ""
        try:
            response = requests.put(
                url=self._modelURL + ':' + self._model_port + "/validate",
                json=payload)
        except Exception as e:
            print(e)
            return Exception("Not able to get data from URL please check if model is running or online")
        return response

    def Load_model(self):
        response = ""
        try:
            response = requests.put(
                url=self._modelURL + ':' + self._model_port + "/loadmodel")
        except Exception as e:
            print(e)
            return Exception("Not able to get data from URL please check if model is running or online")
        return response

    def Custom_request(self, request_type="", pathing="", json_data='Development'):
        request_type = request_type.lower()
        response = ""

        if request_type == "post":
            response = requests.post(
                url=self._modelURL + ':' + self._model_port + "/" + pathing,
                json=json_data)
            return response
        elif request_type == "put":
            response = requests.put(
                url=self._modelURL + ':' + self._model_port + "/" + pathing,
                json=json_data)
            return response
        elif request_type == "get":
            response = requests.get(
                url=self._modelURL + ':' + self._model_port + "/" + pathing,
                json=json_data)
            return response
        else:
            return Exception("Request type not found please the following: get, put, post")
