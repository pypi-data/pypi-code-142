import random
from time import sleep

from client import ZebraClient

if __name__ == '__main__':
    cli = ZebraClient(
        sensor_id="1",
        server_address="3.142.187.132:8000",
        schema="http"
    )
    a = 0
    while a < 100:
        sleep(1)
        handler = cli.get_handler()
        handler.info("hi")
        a += 1

