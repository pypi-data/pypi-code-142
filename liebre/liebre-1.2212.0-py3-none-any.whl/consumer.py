import json
from time import sleep
from pika import BasicProperties
from threading import Thread
from .utils import (
    get_partition_queue_name,
    deserialize_content,
    serialize_content,
)
from .logger import logger
from .rabbit_store import RabbitStore, reconnect
from .message import Message


class Consumer(RabbitStore):
    def __init__(self, queue, **kwargs):
        super().__init__(**kwargs)
        self._queue = queue
        self._callbacks = {}
        self._channel_by_message = {}
        self._threads = []
        self._shall_die = False
        self._first_queue = True

    @property
    def threads(self):
        return self._threads

    def _send_to_bottom(self, message: Message):
        message_id = message.properties.message_id
        channel = self._channel_by_message[message_id]
        channel.basic_publish(
            exchange=self._exchange,
            routing_key=self._queue,
            body=serialize_content(message.content),
            properties=message.properties,
            mandatory=True
        )

        if self._auto_ack:
            self.commit(message)
        self._increment_message_retries(message_id)

    def _handle_message(
        self,
        channel,
        callback,
        properties,
        message,
        queue_options=None,
    ):
        if queue_options is None:
            queue_options = {}
        queue_options = self._queue_options | queue_options

        try:
            content = deserialize_content(message)
            message_id = properties.message_id
            retries = self._get_message_retries(message_id)

            if (queue_options['dead_letters'] and self._max_retries
                    and retries >= self._max_retries):
                logger.error(
                    f'Message rejected after {self._max_retries} retries.',
                    queue=self._queue,
                )
                channel.basic_reject(
                    delivery_tag=callback.delivery_tag,
                    requeue=False
                )

            else:
                if (retries > 0):
                    sleep(self._sleep_seconds_on_retry)

                try:
                    callback_message = Message(content, properties, callback)
                    self._channel_by_message[message_id] = channel
                    self._callbacks[self._queue]['callback'](callback_message)

                    if self._auto_ack:
                        self.commit(callback_message)
                    self._remove_message_retries(message_id)

                except Exception as error:
                    logger.exception(
                        f'Callback error ({retries + 1}/{self._max_retries}).',
                        error=error,
                        exchange=self._exchange,
                        queue=self._queue,
                        content=content,
                    )

                    if not queue_options['quorum']:
                        try:
                            self._send_to_bottom(callback_message)
                        except Exception:
                            logger.error(
                                'Error sending message to bottom ',
                                f'({retries + 1}/{self._max_retries}).',
                                exchange=self._exchange,
                                queue=self._queue,
                                content=content,
                            )

        except Exception:
            logger.exception('Could not process the message.')
            channel.basic_nack(
                delivery_tag=callback.delivery_tag,
                requeue=True,
            )

    def consume(
        self,
        queue,
        callback,
        exchange_options=None,
        queue_options=None,
    ):
        if queue_options is None:
            queue_options = {}
        queue_options = self._queue_options | queue_options

        if exchange_options is None:
            exchange_options = {}
        exchange_options = self._exchange_options | exchange_options

        if self._first_queue:
            channel = self._channels[0]
            self._first_queue = False
        else:
            channel = self._get_channel()
            self._channels.append(channel)

        thread = Thread(
            target=self._consume_target,
            daemon=True,
            kwargs={
                'channel': channel,
                'queue': queue,
                'callback': callback,
                'queue_options': queue_options,
                'exchange_options': exchange_options,
            },
        )
        self._threads.append(thread)
        thread.start()

    @reconnect
    def _consume_target(
        self,
        channel,
        queue,
        callback,
        queue_options=None,
        exchange_options=None,
    ):
        while not self._shall_die:
            self._callbacks[queue] = {'callback': callback}

            if queue not in self._declared_logical_queues:
                self._declare_queue(
                    queue,
                    queue_options=queue_options,
                    exchange_options=exchange_options,
                    channel=channel
                )

            for partition in range(self._partitions):
                queue_name = get_partition_queue_name(queue, partition)
                channel.basic_consume(
                    queue=queue_name,
                    auto_ack=False,
                    on_message_callback=lambda *args,
                    **kwargs: self._handle_message(
                        *args,
                        **kwargs,
                        queue_options=queue_options,
                    )
                )

                # Log before start consuming since method is blocking
                logger.info(
                    'Waiting for messages...',
                    queue=queue_name,
                    exchange=self._exchange,
                )

                channel.start_consuming()

    @reconnect
    def commit(self, message):
        message_id = message.properties.message_id
        if message_id not in self._channel_by_message:
            raise ValueError('Unknown message_id.')

        channel = self._channel_by_message[message_id]
        channel.basic_ack(delivery_tag=message.method.delivery_tag)
        del self._channel_by_message[message_id]

    def status(self):
        for thread in self._threads:
            if not thread.is_alive():
                return False
        return True

    def start(self):
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()

    def stop(self):
        self._shall_die = True
