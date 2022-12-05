from typing import List
import requests
import pandas as pd
import json
import data_model as data_model
from api_time import int_to_datetime, datetime_to_int


BASE_URL = "http://api.exdelphi.com"
HEADERS = {"Content-Type": "application/json", "Authorization": ""}


def authorize(username: str, password: str) -> None:
    """Sets headers to contain authorization token generated from given username and password"""
    response = requests.post(
        url=f"{BASE_URL}/token",
        data={"username": username, "password": password},
    )
    response_content = json.loads(response.text)
    token = response_content["access_token"]
    HEADERS["Authorization"] = f"Bearer {token}"
    print(f"Authenticated {username} at {BASE_URL}")


def get_product_list() -> List[data_model.Product]:
    """Returns list of all products available to authorized user"""
    response = requests.get(url=f"{BASE_URL}/products/", headers=HEADERS)
    return [data_model.Product.parse_obj(item) for item in json.loads(response.text)]


def get_data_sets_for_product(product_id) -> List[data_model.Dataset]:
    """Returns list of datasets from given product available to authorized user"""
    response = requests.get(url=f"{BASE_URL}/data_sets/{product_id}", headers=HEADERS)
    return [data_model.Dataset.parse_obj(item) for item in json.loads(response.text)]


def get_data(data_set_id: int) -> pd.DataFrame:
    """Returns data set with given ID to authorized user"""
    request = requests.get(url=f"{BASE_URL}/data/{data_set_id}", headers=HEADERS)
    result = json.loads(request.text)
    data = pd.DataFrame(result)
    data.set_index("t", inplace=True)
    return data


def convert_to_timestamp(data: pd.DataFrame) -> pd.DataFrame:
    """Converts time column `t` from int representation to time stamps"""
    data.index = data.index.map(lambda t: int_to_datetime(t))
    return data


def convert_to_int(data: pd.DataFrame) -> pd.DataFrame:
    """Converts time column `t` from time stamps representation to int"""
    data["t"] = data["t"].map(lambda t: datetime_to_int(t))
    return data


def upload_data(product_id: int, start_time: int, data: pd.DataFrame) -> None:
    """ "Convert pandas DataFrame with columns 't' and 'v' to json and upload to database"""
    _prepare_time_column(data)
    data_as_json = data.to_json(orient="records")
    print(data_as_json)
    requests.put(
        url=f"{BASE_URL}/data/?product_id={product_id}&start_time={start_time}",
        headers=HEADERS,
        data=f"{data_as_json}",
    )


def _prepare_time_column(data):
    if data.index.name == "t":
        data["t"] = data.index
    if "t" not in data:
        raise ValueError("time t is missing in data")
    if "v" not in data:
        raise ValueError("value v is missing in data")
    try:
        data = convert_to_int(data)
    except AttributeError:
        pass
    if data["t"].dtype != int:
        raise ValueError("data['t'] must be of type int")
