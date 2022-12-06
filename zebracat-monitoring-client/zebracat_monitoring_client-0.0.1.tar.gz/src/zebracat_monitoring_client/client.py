import requests
import logging.handlers


class ZebraClient:
    def __init__(self, sensor_id: str, server_address: str, schema: str = "http"):
        self.sens_id = sensor_id
        self.server = server_address
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

    def get_handler(self, name=None):
        logger = logging.getLogger(name=name)
        http_handler = logging.handlers.HTTPHandler(
            self.server,
            '/log/set/',
            method='POST'
        )
        logger.addHandler(http_handler)
        return logger
