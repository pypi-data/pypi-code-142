import json
import pulsar

from json.decoder import JSONDecodeError


class Producer:
    def __init__(self, pulsar_connection_file):
        self.pulsar_connection = None
        self.client = None
        self.producer= None

        with pulsar_connection_file.open() as file:
           self.pulsar_connection = file.read()

        try:
            self.pulsar_connection = json.loads(self.pulsar_connection)
        except JSONDecodeError:
            raise Exception('Error parsing Pulsar Connection file')

        self.producer = self._create_producer(self.pulsar_connection)

    def _create_producer(self, config):
        topic = config.get('topic', 'pulsar-producer-default-topic-name')
        url_connection = 'pulsar://{}:{}'.format(
            config.get('host', 'localhost'),
            config.get('port', 6650),
        )

        self.client = pulsar.Client(url_connection)

        return self.client.create_producer(topic)

    def send_message(self, message_file):
        message = None

        try:
            with message_file.open() as file:
                message = file.read()
        except:
            raise Exception('Error reading message file ({})'.format(message_file))

        self.producer.send(message.encode('utf-8'))
        self.client.close()
