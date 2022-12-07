from typing import Dict

from kafka import KafkaProducer, KafkaConsumer
from json import dumps


class KafkaController:
    """
    UR implementation to Kafka controller.
    we are using kafka-python library for this controller.
    """

    def __init__(self, bootstrap_servers: str, topic: str, **kwargs: None):
        """
        :param bootstrap_servers: server address to connect.
        :param topic: topic to store the messages
        """
        self.topics = topic
        try:
            self.consumer = KafkaConsumer(topic)
            self.producer = KafkaProducer(bootstrap_servers=[bootstrap_servers],
                                          value_serializer=lambda x:
                                          dumps(x).encode('utf-8'))
            if self.producer.bootstrap_connected() is False or self.consumer.bootstrap_connected() is False:
                raise Exception('Could not connect')

        except Exception as e:
            print(f'error: {e}')

    def __del__(self):
        try:
            self.consumer.close()
            self.producer.close()
        except Exception as e:
            print("Exception")

    def send_message(self, message: Dict):
        """
        Send a message to Kafka
        :param message: data to send to Kafka.
        """
        self.producer.send(self.topics, value=message)

    def get_message(self, topic: str):
        pass

