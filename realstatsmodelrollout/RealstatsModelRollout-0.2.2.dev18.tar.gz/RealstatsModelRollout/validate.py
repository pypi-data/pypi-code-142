from .settings import Settings
from six import string_types
from .model import Model
from .versioning import Versioning
from .global_functions import globalFunctions as gf
import pandas as pd
from datetime import date
from github import Github
import os
import json


class Validate:
    def __init__(self, id="Optional"):
        self._id = id
        self._mae_value = 0
        self._mae_expected_value = 0
        self._mae_deviation_percentage = 0
        self._r2_value = 0
        self._r2_expected_value = 0
        self._r2_deviation_percentage = 0
        self._mape_value = 0
        self._mape_expected_value = 0
        self._mape_deviation_percentage = 0
        self._mae_valid = False
        self._r2_valid = False
        self._mape_valid = False
        self._model_features = ""
        self._param_settings = {}
        self._target = ""

    # MAE values
    @property
    def MAE_Deviation_percentage(self):
        """
        :type: float
        """
        return self._mae_deviation_percentage

    @MAE_Deviation_percentage.setter
    def MAE_Deviation_percentage(self, value):
        """
        :type: float
        """
        self._mae_deviation_percentage = value

    @property
    def MAE_expected_value(self):
        """
        :type: float
        """
        return self._mae_expected_value

    @MAE_expected_value.setter
    def MAE_expected_value(self, value):
        """
        :type: float
        """
        self._mae_expected_value = value

    # R2 values
    @property
    def R2_Deviation_percentage(self):
        """
        :type: float
        """
        return self._r2_deviation_percentage

    @R2_Deviation_percentage.setter
    def R2_Deviation_percentage(self, value):
        """
        :type: float
        """
        self._r2_deviation_percentage = value

    @property
    def R2_expected_value(self):
        """
        :type: float
        """
        return self._r2_expected_value

    @R2_expected_value.setter
    def R2_expected_value(self, value):
        """
        :type: float
        """
        self._r2_expected_value = value

    # MAPE values
    @property
    def MAPE_Deviation_percentage(self):
        """
        :type: float
        """
        return self._mape_deviation_percentage

    @MAPE_Deviation_percentage.setter
    def MAPE_Deviation_percentage(self, value):
        """
        :type: float
        """
        self._mape_deviation_percentage = value

    @property
    def MAPE_expected_value(self):
        """
        :type: float
        """
        return self._mape_expected_value

    @MAPE_expected_value.setter
    def MAPE_expected_value(self, value):
        """
        :type: float
        """
        self._mape_expected_value = value

    # Features
    @property
    def Feature_array(self):
        """
        :type: list
        """
        return self._model_features

    @Feature_array.setter
    def Feature_array(self, value):
        """
        :type: list
        """
        self._model_features = value

    # target
    @property
    def Model_target(self):
        """
        :type: string
        """
        return self._target

    @Model_target.setter
    def Model_target(self, value):
        """
        :type: string
        """
        self._target = value

    # Param
    @property
    def Model_parameters(self):
        """
        :type: object
        """
        return self._param_settings

    @Model_parameters.setter
    def Model_parameters(self, value):
        """
        :type: object
        """
        self._param_settings = value

    def Start_validation(self, Gitaccestoken="Optional", localpath="Optional", model_url="Optional", model_port="Optional", repo_name="Optional"):
        if localpath == "Optional":
            localpath = gf.Path_is_dir(
                Settings.Base_path + Settings.Enviroment_name + "/")
        else:
            localpath = gf.Path_is_dir(localpath)

        if Gitaccestoken != "Optional":
            Settings.Gitaccesstoken = Gitaccestoken

        # Get Values from model
        model = Model()
        if model_url != "Optional":
            model.Model_URL = model_url
        if model_port != "Optional":
            model.Model_port = model_port

        load = {
            "feature_array": self._model_features,
            "param_values": self._param_settings,
            "target": self._target,
            "localpath": localpath
        }

        print("Starting validation...")
        response = model.Validate_request(payload=load)
        response_json = response.json()
        self._mae_value = response_json["mae_value"]
        self._r2_value = response_json["r2_value"] * 100
        self._mape_value = response_json["mape_value"]

        # Calculate max MAE and min MAE
        print("Starting calculation of results...")
        max_mae = self._mae_expected_value + \
            ((self._mae_expected_value / 100) * self._mae_deviation_percentage)
        min_mae = self._mae_expected_value - \
            ((self._mae_expected_value / 100) * self._mae_deviation_percentage)

        # check if MAE value is within range
        if self._mae_value >= min_mae and self._mae_value <= max_mae:
            print("MAE value is within range")
            self._mae_valid = True
        else:
            print("MAE value is not within range")

        # Calculate max MAPE and min MAPE
        max_mape = self._mape_expected_value + \
            ((self._mape_expected_value / 100) * self._mape_deviation_percentage)
        min_mape = self._mape_expected_value - \
            ((self._mape_expected_value / 100) * self._mape_deviation_percentage)

        # check if MAPE value is within range
        if self._mape_value >= min_mape and self._mape_value <= max_mape:
            print("Mape value is within range")
            self._mape_valid = True
        else:
            print("Mape value is not within range")

        # Calculate max R2% and min R2%
        max_r2 = self._r2_expected_value + \
            ((self._r2_expected_value / 100) * self._r2_deviation_percentage)
        min_r2 = self._r2_expected_value - \
            ((self._r2_expected_value / 100) * self._r2_deviation_percentage)

        # check if R2 value is within range
        if self._r2_value >= min_r2 and self._r2_value <= max_r2:
            print("R2 value is within range")
            self._r2_valid = True
        else:
            print("R2 value is not within range")

        print("Writing validation data to: " + localpath)
        self.Save_validation_results(localpath)
        print("Done writing validation results")

        if self._mae_valid and self._r2_valid and self._mape_valid and repo_name != "Optional":
            version = Versioning()
            version.Repo_name = repo_name
            version.Upload_enviroment()

    def Save_validation_results(self, localpath):
        git = Github(Settings.Gitaccesstoken)
        git_user = git.get_user()
        git_user_data = git_user.get_emails()

        # Create validation documentation
        validation_json = {
            "validation_date": date.today().strftime("%d-%m-%Y"),
            "validation_by": git_user_data[0].email,
            "expected_mae_value": self._mae_expected_value,
            "mae_deviation_percentage": self._mae_deviation_percentage,
            "actual_mae_value": self._mae_value,
            "expected_R2_value": self._r2_expected_value,
            "R2_deviation_percentage": self._r2_deviation_percentage,
            "actual_R2_value": self._r2_value,
            "expected_mape_value": self._mape_expected_value,
            "mape_deviation_percentage": self._mape_deviation_percentage,
            "actual_mape_value": self._mape_value,
            "mae_within_expected_range": self._mae_valid,
            "r2_within_expected_range": self._r2_valid,
            "mape_within_expected_range": self._mape_valid,
            "used_model_features": self._model_features
        }

        path = localpath + "/validation_data/validation_data.json"

        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(json.dumps(validation_json))

        return True
