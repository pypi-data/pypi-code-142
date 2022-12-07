import platform
from .settings import Settings
from .vmachine import Vmachine
from .model import Model
from .versioning import Versioning
from .global_functions import globalFunctions
from .validate import Validate
from .auth import Auth

Settings

Settings.Token = ""
Settings.Package_version = "0.0.1.dev"
Settings.Platform_version = platform.python_version()
Settings.Premade_main_code_data = """
# Local imports
import datetime

# Third party imports
from pydantic import BaseModel, Field

from ms import app
from ms.functions import get_model_response
from ms.train_model import train_model
from ms import Load_model

model_name = "Testing model"
version = "v1.0.0"
localpath = ""

# Input for data validation
class Inputs(BaseModel):
    temp: str
    # TODO

# Ouput for data validation
class Output(BaseModel):
    label: str
    prediction: int

class Validation_input(BaseModel):
    feature_array: list[str]
    param_values: object
    target: str
    localpath: str

class Validation_output(BaseModel):
    mae_value: float
    r2_value: float
    mape_value: float
    features: list[str]

class loaded_output(BaseModel):
    loaded: bool

@app.get('/')
async def help():
    return {
        "name": model_name,
        "version": version,
        "property": "Realstats"
    }

@app.get('/info')
async def model_info():
    return {
        "name": model_name,
        "version": version,
        "creator": "Realstats",
        "information": "Go look at the documentation for what calls to make"
    }

@app.post('/predict', response_model=Output)
async def model_predict(inputs: Inputs):
    response = get_model_response(inputs)
    print(response)
    return response

@app.put('/validate', response_model=Validation_output)
async def model_validate(input: Validation_input):
    response = train_model.Execute_training_testing(feature_array=input.feature_array, param_values=input.param_values, target=input.target, localpath=input.localpath)
    localpath = input.localpath

    Load_model(localpath)
    return response

@app.put('/loadmodel', response_model=loaded_output)
async def model_load():
    try:
        Load_model(localpath)
        return {
            "loaded": True
        }
    except:
        return {
            "loaded": False
        }
"""
Settings.Premade_ms_init_code = """
# Imports
from fastapi import FastAPI
import joblib

model = ""

# Initialize FastAPI app
app = FastAPI()

def Load_model(localpath):
    # Load model
    model = joblib.load(localpath + 'model/trained_model.pkl')

"""
Settings.Premade_ms_train_code = """
# import general packages
import pandas as pd
import os
import joblib
from datetime import date

# import validation functions
from ms.functions import percentage_error
from ms.functions import mean_absolute_percentage_error

# import model training systems
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import train_test_split

# Class for the model and training
class train_model:
    # General function for calling and training model
    def Execute_training_testing(feature_array, param_values, target, localpath):
        # Save locations
        SAVE_MODEL = localpath + 'model/trained_model.pkl'
        train_data = pd.read_pickle(localpath + 'data/train_data_model.pkl')

        # Define features
        features = feature_array

        # Zet feature data types goed
        for i in range(len(features)):
            features[i] = features[i].lower()

        # Corrigeer columns namen
        train_data.columns = train_data.columns.str.lower()
        train_data = train_data.loc[:, ~train_data.columns.duplicated()]

        # Defineer target en relevant columns
        target = [target]

        # Train model
        y = train_data[target]
        X = train_data[features]

        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            train_size=0.75, test_size=0.25,
                                                            random_state=10)

        best_param_values = list(param_values.values())

        if best_param_values[0] == 0:
            boosting_type = 'gbdt'
        else:
            boosting_type = 'dart'

        model = LGBMRegressor(
            learning_rate=best_param_values[2],
            num_leaves=int(best_param_values[5]),
            max_depth=int(best_param_values[3]),
            n_estimators=int(best_param_values[4]),
            boosting_type=boosting_type,
            colsample_bytree=best_param_values[1],
            reg_lambda=best_param_values[6],
            random_state=10
        )

        model.fit(X_train, y_train,
                eval_metric='l1',
                eval_set=[(X_test, y_test)],
                early_stopping_rounds=500,
                verbose=0
                )

        # Get results of the test to check the model functionality these get send back to package
        preds = model.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        mape = mean_absolute_percentage_error(y_test, preds)
        r2 = r2_score(y_test, preds)

        # Retrain model with full dataset for versioning and saving
        model.fit(X, y,
                eval_metric='l1',
                verbose=0)
        joblib.dump(value=model, filename=SAVE_MODEL)

        # Return needed values for the package to continue work
        return {
            "mae_value": mae,
            "r2_value": r2,
            "mape_value": mape,
            "features": features
        }

"""
Settings.Premade_ms_function_code_data = """
import pandas as pd
import numpy as np
from ms import model
from sklearn.metrics import mean_absolute_error

def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction

def get_model_response(input):
    X = pd.json_normalize(input.__dict__)
    prediction = predict(X, model)
    if prediction == 1:
        label = "M"
    else:
        label = "B"
    return {
        'label': label,
        'prediction': int(prediction)
    }

def percentage_error(actual, predicted):
    res = np.empty(actual.shape)
    for j in range(actual.shape[0]):
        if actual[j] != 0:
            res[j] = (actual[j] - predicted[j]) / actual[j]
        else:
            res[j] = predicted[j] / np.mean(actual)
    return res

def mean_absolute_percentage_error(y_true, y_pred):
    return (1 - np.mean(np.abs(percentage_error(np.asarray(y_true), np.asarray(y_pred))))) * 100

"""
Settings.Premade_requirements_data = """
anyio==3.5.0
asgiref==3.5.0
click==8.1.2
cycler==0.11.0
fastapi==0.75.2
fonttools==4.32.0
h11==0.13.0
idna==3.3
joblib==1.1.0
kiwisolver==1.4.2
matplotlib==3.5.1
numpy==1.22.3
packaging==21.3
pandas==1.4.2
Pillow==9.1.0
pydantic==1.9.0
pyparsing==3.0.8
python-dateutil==2.8.2
pytz==2022.1
scikit-learn==1.0.2
scipy==1.8.0
six==1.16.0
sklearn==0.0
sniffio==1.2.0
starlette==0.17.1
threadpoolctl==3.1.0
typing_extensions==4.2.0
uvicorn==0.17.6
lightgbm
"""
Settings.Premade_documentation_data = """
# POST
url = Base_url:8000/predict
body = {

}

# GET
url = Base_url:8000/


# GET
url = Base_url:8000/info

# PUT method
url = Base_url:8000/validate

# Documentation
url = Base_url:8000/docs
"""
