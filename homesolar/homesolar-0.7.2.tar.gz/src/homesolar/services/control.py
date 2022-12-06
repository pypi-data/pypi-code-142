import time

from loguru import logger


def control_loop(timeout):
    logger.debug("Controls Started")
    try:
        elapsed_time = 0
        while True:
            if time.perf_counter() - elapsed_time >= timeout:
                elapsed_time = time.perf_counter()
                check_controls()
    except Exception as e:
        logger.exception(f"Something went wrong when looping through controls [{e}]")


def check_controls():
    conditions = get_conditions()
    for condition in conditions:
        parameters = condition.parameters
        for parameter in parameters:
            check_parameter(parameter, get_sensor_data())


def get_conditions():
    return []

def get_sensor_data():
    return 0

def check_parameter(parameter, sensor_data):
    pass
