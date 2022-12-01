import json
import logging
import os
import warnings
from http import HTTPStatus
from queue import Queue

import numpy as np
import requests

from .__consumer import Consumer
from .utils import AGGREGATED_OUTPUT_DIR, FILE_METADATA


class Client:
    def __init__(self,
                 credentials: dict = None,
                 host: str = "https://api.branchkey.com"):

        if credentials is None:
            credentials = dict(leaf_name="guest", leaf_id="guest", leaf_session_token="guest",
                               response_host="response.branchkey.com", port=5672)

        self.__leaf_name = credentials["leaf_name"]
        self.__leaf_id = credentials["leaf_id"]
        self.__leaf_session_token = credentials["leaf_session_token"]
        self.__status = "unauthenticated"

        self.__api_host = host
        # Verify SSL certs
        self.__verify = True

        self.queue = Queue()
        self.__run_status = 'pause'

        self.rabbit_credentials = dict(
            leaf_name=self.__leaf_name, leaf_id=self.__leaf_id, queue_password=self.__leaf_session_token, host=credentials["response_host"])
        self.consumer = None
        return

    def __update_run_status(self, status):
        self.__run_status = status

    def disable_ssl_verification(self, enabled=False):
        warnings.warn(
            "[BranchKey] We highly recommend enabling ssl verification. Use this at your own risk.")
        self.__verify = enabled
        return self.__verify

    def convert_pytorch_numpy(self, model, weighting=1):
        """
        Usage:
        update = convert_pytorch_numpy(model.get_params(), client_samples=5*5)
        :param model: Pytorch model parameters
        :param weighting: Weight given to this update. Usually the number of client samples used to construct the model
        :return: type(np.ndarray) of parameters
        """
        params = []
        for param in model:
            params.append(param[1].data.cpu().detach().numpy())
        numpy = (weighting, params)
        return np.asarray(numpy, dtype=object)

    def validate_weight_shape(self, file):
        """
        Validates that the weights are in the correct shape before being sent to the API
        :param file: file bytes or file path
        :return: True on success, otherwise returns an exception
        """
        array = np.load(file, allow_pickle=True)
        if array.shape[0] != 2:
            raise Exception("[validate_weight_shape] Incorrect shape != 2")
        elif type(array[0]) is not int:
            raise Exception("[validate_weight_shape] Dim 0 not integer")
        elif type(array[1]) is not list:
            raise Exception("[validate_weight_shape] Dim 1 not list")
        elif type(array[1][0]) is not np.ndarray:
            raise Exception("[validate_weight_shape] Dim 1:0 not ndarray")
        else:
            file.seek(0)
            return True

    def authenticate(self):
        try:
            url = self.__api_host + "/v1/leaf/authenticate"
            headers = {"accept": "application/json"}

            resp = requests.get(url, headers=headers,
                                auth=(self.__leaf_id, self.__leaf_session_token), verify=self.__verify)

            print(f"received resp code form auth: {resp.status_code}")
            if resp.status_code != HTTPStatus.OK:
                raise Exception(resp.json())

            authenticate_data = resp.json()["data"]
            try:
                self.__status = "authenticated"
                self.rabbit_credentials["tree_id"] = authenticate_data["tree_id"]
                self.rabbit_credentials["branch_id"] = authenticate_data["branch_id"]
                consumer = Consumer(self.rabbit_credentials,
                                    self.queue, self.__update_run_status)
                self.consumer = consumer.spawn_consumer_thread()
                return True
            except Exception as e:
                raise Exception(
                    f"Failed to parse response from authenticate API: {e}")

        except Exception as e:
            msg = "Authentication failed for leaf {}: {}".format(
                self.__leaf_name, e)
            logging.error(msg)
            return False

    def file_upload(self, file_path):
        if self.__status == "authenticated":
            try:
                with open(file_path, mode="rb") as f:
                    self.validate_weight_shape(f)

                    url = self.__api_host + "/v1/file/upload"
                    headers = {"accept": "application/json"}
                    data = {"data": json.dumps({"leaf_name": self.__leaf_name,
                                                "metadata": FILE_METADATA})}
                    file = {"file": f}

                    resp = requests.post(
                        url, files=file, data=data, headers=headers,
                        auth=(self.__leaf_id, self.__leaf_session_token), verify=self.__verify)
                    f.close()

                    if resp.status_code != HTTPStatus.CREATED:
                        raise Exception(resp.json()["error"])
                    else:
                        return resp.json()["data"]["file_id"]

            except Exception as e:
                msg = "File Upload failed for leaf {} for file {}: {}".format(
                    self.__leaf_name, file_path, e)
                raise Exception(msg)
        else:
            msg = "File Upload failed for leaf {} : {}".format(
                self.__leaf_name, "leaf not authenticated")
            raise Exception(msg)

    def file_download(self, file_id):
        if self.__status == "authenticated":
            try:
                if not os.path.exists(AGGREGATED_OUTPUT_DIR):
                    os.makedirs(AGGREGATED_OUTPUT_DIR)

                url = self.__api_host + "/v1/file/download/" + file_id
                headers = {"accept": "*/*S"}
                resp = requests.get(url, headers=headers,
                                    auth=(self.__leaf_id, self.__leaf_session_token), verify=self.__verify)

                if resp.status_code != HTTPStatus.OK:
                    raise Exception(resp.json()["error"])

                try:
                    download_url = resp.json()["data"]["download_url"]
                except Exception as e:
                    raise Exception(
                        f"Failed to parse response from download API: {resp.json()}")

                resp = requests.get(download_url)
                if len(resp.content) == 0:
                    raise Exception("file not received")

                f = open(AGGREGATED_OUTPUT_DIR +
                         '/' + file_id + ".npy", 'wb')
                f.write(resp.content)
                f.close()
                print(f"downloaded file {file_id}")
                return True

            except Exception as e:
                msg = "File Download failed for leaf {} for file {}: {}".format(
                    self.__leaf_name, file_id, e)
                raise Exception(msg)
        else:
            msg = "File Download failed for leaf {} : {}".format(
                self.__leaf_name, "leaf not authenticated")
            raise Exception(msg)

    @property
    def leaf_id(self):
        return self.__leaf_id

    @property
    def session_token(self):
        return self.__leaf_session_token

    @property
    def is_authenticated(self):
        return self.__status == "authenticated"

    @property
    def run_status(self):
        return self.__run_status
