import os
import sys
from datetime import datetime, timedelta
import traceback
import logging
import json
import time
import paho.mqtt.publish as publish

class MqttNotificationMessageMalformedException(Exception):
    pass

class Mqtt_publisher():
    def __init__(self, host, port, subject, topics:dict, logger=None):
        if logger:
            self.logger = logger
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s')
            self.logger = logging.getLogger(__name__)
        self.host = host
        self.port = port
        self.topics = topics
        if "notification" in topics:
            self.topic_notification = self.topics["notification"]
        else:
            self.logger.warning("notification topic not defined")
            self.topic_notification = None

        if "timeseries" in topics:
            self.topic_base_timeseries = self.topics["timeseries"]
        else:
            self.logger.warning("timeseries topic not defined")
            self.topic_base_timeseries = None

        if "state" in topics:
            self.topic_state = self.topics["state"]
        else:
            self.logger.warning("state topic not defined")
            self.topic_state = None

        self.subject = subject

    #TODO annotation retry
    def __send(self, topic, payload, retain=False):
        """
        publish a MQTT message containing the payload to the given topic
        :param topic:
        :param payload:
        :param retain: if True, the flag retain is added
        :return:
        """
        self.logger.debug(f"[MQTT __send] mqtt_host: {self.host}:{self.port} - topic: {topic} - payload: {payload}")
        res = publish.single(hostname=self.host, port=self.port, topic=topic, payload=payload)
        return res

    def send_notification(self, notification_message: dict) -> int:
        """
        send a mqtt message to the notification topic
        :param notification_message:
        :return: the result of paho mqtt publish.single and -1 if the topic notification is not set
        """
        if self.topic_notification:
            topic = f"{self.topic_notification}"
            #if ("channel" not in notification_message) or ("msg" not in notification_message):
            #    raise MqttNotificationMessageMalformedException("[MQTT send_notification] malformed notification_message")
            self.logger.debug(f"[MQTT send_notification] topic: {topic} - notification_message: {notification_message}")
            res = self.__send(self.topic_notification, json.dumps(notification_message))
        else:
           self.logger.warning(f"[MQTT send_notification] no timeseries notification_message defined")
           res = -1
        return res


    def send_values_to_timeseries(self, values_message: dict):
        """
        send a mqtt message to the timeseries topic
        :param values_message:
        :return:
        """
        if self.topic_base_timeseries:
            topic = f"{self.topic_base_timeseries}/{self.subject}"
            self.logger.debug(f"[MQTT send_values_to_timeseries] topic: {topic} - data_dict: {values_message}")
            res = self.__send(topic, json.dumps(values_message))
        else:
            self.logger.warning(f"[MQTT send_values_to_timeseries] no timeseries topic defined - data_dict: {values_message}")
            res = -1
        return res


    def send_values_to_state(self, data_label: str, data_value: float):
        """
        send a mqtt message to the state topic : <state> / <subject> / <data_label>
        :param data_label: the last item of the topic
        :param data_value: the float value to publish
        :return:
        """
        if self.topic_state:
            topic = f"{self.topic_state}/{self.subject}/{data_label}"
            self.logger.debug(f"[MQTT send_values_to_state] topic: {topic} - data_value: {data_value}")
            res = self.__send(f"{topic}", data_value, retain=True)
        else:
            self.logger.warning(f"[MQTT send_values_to_state] no state topic defined - data_value: {data_value}")
            res = -1
        return res