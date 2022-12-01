import random
import uuid
from pika import BasicProperties
from pika import DeliveryMode
from .logger import logger
from .utils import (
    get_partition_queue_name,
    serialize_content,
    get_suffixed_queue_name,
)
from .rabbit_store import RabbitStore, reconnect


class Producer(RabbitStore):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @reconnect
    def produce(
        self,
        queue,
        content,
        correlation_id=None,
        message_id=None,
        queue_options=None,
        exchange_options=None,
    ):
        if queue_options is None:
            queue_options = {}
        queue_options = self._queue_options | queue_options

        if exchange_options is None:
            exchange_options = {}
        exchange_options = self._exchange_options | exchange_options

        if queue not in self._declared_logical_queues:
            self._declare_queue(
                queue,
                queue_options=queue_options,
            )

        if message_id is None:
            message_id = str(uuid.uuid4())

        # Uniform distribution of messages across the queue partitions
        partition = random.randint(0, self._partitions - 1)
        partition_queue_name = get_partition_queue_name(queue, partition)

        backup_queue_name = get_suffixed_queue_name(
            get_suffixed_queue_name(queue,
                                    'backup'),
            partition
        )

        queue_names = (
            [partition_queue_name,
             backup_queue_name]
            if queue_options['backup'] else [partition_queue_name]
        )

        properties = BasicProperties(
            message_id=message_id,
            correlation_id=correlation_id,
            delivery_mode=DeliveryMode.Transient
        )

        try:
            serialized_content = serialize_content(content)

            logger.debug(
                'Producing message... ',
                exchange=self._exchange,
                queue=partition_queue_name,
            )

            for queue_name in queue_names:
                self._channels[0].basic_publish(
                    exchange=self._exchange,
                    routing_key=queue_name,
                    body=serialized_content,
                    properties=properties,
                    mandatory=True
                )
        except Exception as error:
            logger.exception(
                exchange=self._exchange,
                queue=partition_queue_name,
                content=serialized_content,
            )
            raise error

        logger.debug(
            'Message published.',
            exchange=self._exchange,
            queue=partition_queue_name,
        )
