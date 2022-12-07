import requests
import logging.handlers
from typing import Literal

WIDGET_MODES = Literal["live_chart", "boolean", "knob", "area_chart"]
WIDGET_LABELS = Literal["hourly", "daily", "instant"]

DEVICE_STATUS = Literal["active", "inactive"]
ELEMENT_TYPE = Literal["device", "sensor", "widget"]


class ZebraClient:
    def __init__(self, sensor_id: str, server_address: str, schema: str = "http"):
        self.sens_id = sensor_id
        self.server = server_address
        self.schema = schema
        self.sens_url = f"{schema}://{server_address}/log/set_data/"

    def send(self, value):
        try:
            requests.post(
                url=self.sens_url,
                data={
                    "value": value,
                    "sens_id": self.sens_id
                }
            )
        except:
            pass

    def get_handler(self, name=None, level=4):
        logger = logging.getLogger(name=name)
        http_handler = logging.handlers.HTTPHandler(
            self.server,
            '/log/set/',
            method='POST'
        )
        logger.setLevel(level)
        logger.addHandler(http_handler)
        return logger

    def create_widget(self, mode: WIDGET_MODES, labels: WIDGET_LABELS, dataset_label: str):
        try:
            data = {
                "mode": mode,
                "labels": labels,
                "dataset_label": dataset_label
            }
            return requests.post(f"{self.schema}://{self.server}/api/create_widget/",
                                 data=data).json()["id"]
        except Exception as e:
            raise Exception(e)

    def create_sensor(self, name: str, chart_id: str, widget_id):
        try:
            data = {
                "name": name,
                "chart_id": chart_id,
                "widget_id": widget_id
            }
            return requests.post(f"{self.schema}://{self.server}/api/create_sensor/",
                                 data=data).json()["id"]
        except Exception as e:
            raise Exception(e)

    def create_device(self, name: str, address: str, status: DEVICE_STATUS, sensors: list):
        try:
            data = {
                "name": name,
                "address": address,
                "status": status,
                "sensors[]": sensors
            }
            return requests.post(f"{self.schema}://{self.server}/api/create_device/",
                                 data=data).json()["id"]
        except Exception as e:
            raise Exception(e)

    def delete(self, element_type: ELEMENT_TYPE, element_id: int):
        try:
            data = {
                "id": element_id
            }
            if element_type == "device":
                url = f"{self.schema}://{self.server}/api/delete_device/"
            elif element_type == "sensor":
                url = f"{self.schema}://{self.server}/api/delete_sensor/"
            else:
                url = f"{self.schema}://{self.server}/api/delete_widget/"

            return requests.post(url, data=data).json()
        except Exception as e:
            raise Exception(e)
