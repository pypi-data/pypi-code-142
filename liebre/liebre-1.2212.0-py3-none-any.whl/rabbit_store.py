from threading import Lock
from .logger import logger
import time
import pika
from .utils import get_partition_queue_name


class RabbitStore:

    EXCHANGE_OPTIONS = {
        'type': 'direct',
        'durable': True,
        'auto_delete': False,
    }

    QUEUE_OPTIONS = {
        'quorum': True,
        'lazy': True,
        'durable': True,
        'auto_delete': False,
        'backup': False,
        'dead_letters': True,
    }

    def __init__(
        self,
        user=None,
        password=None,
        host=None,
        port=None,
        vhost=None,
        exchange=None,
        max_retry_seconds=None,
        max_retries=None,
        sleep_seconds_on_retry=None,
        auto_ack=True,
        prefetch=None,
        partitions=None,
        exchange_options=None,
        queue_options=None,
        logger_options=None,
    ):
        self._reconnect_lock = Lock()

        self._user = user or 'guest'
        self._password = password or 'guest'
        self._host = host or 'localhost'
        self._port = port or 5672
        self._vhost = vhost or '/'
        self._exchange = exchange
        self._max_retry_seconds = max_retry_seconds or 0

        self._sleep_seconds_on_retry = sleep_seconds_on_retry or 1

        self._max_retries = max_retries or (
            self._max_retry_seconds / self._sleep_seconds_on_retry
        )

        self._auto_ack = auto_ack
        self._prefetch = prefetch or 10
        self._partitions = partitions or 1

        if exchange_options is None:
            self._exchange_options = self.__class__.EXCHANGE_OPTIONS.copy()
        else:
            self._exchange_options = self.EXCHANGE_OPTIONS | exchange_options

        if queue_options is None:
            self._queue_options = self.__class__.QUEUE_OPTIONS.copy()
        else:
            self._queue_options = self.QUEUE_OPTIONS | queue_options

        logger.reload(logger_options)

        self._rabbit_url = (
            f'amqp://{self._user}:{self._password }@{self._host}:{self._port}'
        )

        self._declared_logical_queues = set()

        self._channels = [None]

        self._message_retries = {}
        self._connected = False

    def is_rabbitmq_alive(self):
        connection = self._get_connection()
        try:
            # Provide a connection object so it can be closed
            self._get_channel(connection=connection)
            return True
        except Exception:
            return False
        finally:
            try:
                connection.close()
            except Exception:
                pass

    def connect(self, do_wait=True):
        if self._connected:
            return

        done = False
        while not done:
            try:
                self._channels[0] = self._get_channel()
                done = True
            except Exception as error:
                if not do_wait:
                    raise error
                logger.error('Could not connect to RabbitMQ. Retrying...')
                time.sleep(self._sleep_seconds_on_retry)

            if not do_wait:
                break

        self._connected = True

    def _get_connection(self):
        return pika.BlockingConnection(
            pika.ConnectionParameters(
                self._host,
                self._port,
                self._vhost,
                pika.PlainCredentials(
                    self._user,
                    self._password,
                ),
            )
        )

    def _get_channel(
        self,
        prefetch=None,
        connection=None,
    ):
        if prefetch is None:
            prefetch = self._prefetch

        # Pika's connection is not thread-safe, can't be reused.
        # Thus, neither the channels belonging to it.
        if connection is None:
            connection = self._get_connection()

        channel = connection.channel()
        channel.confirm_delivery()
        channel.basic_qos(prefetch_count=prefetch)

        return channel

    def _declare_exchange(
        self,
        exchange,
        exchange_options=None,
    ):
        if exchange_options is None:
            exchange_options = self._exchange_options
        else:
            exchange_options = self._exchange_options | exchange_options

        self._get_channel().exchange_declare(
            exchange=exchange,
            exchange_type=exchange_options['type'],
            durable=exchange_options['durable'],
            auto_delete=exchange_options['auto_delete'],
        )

    def _declare_queue(
        self,
        queue,
        queue_options=None,
        exchange_options=None,
        dead_letter=False,
        channel=None,
    ):
        if queue_options is None:
            queue_options = {}
        queue_options = self._queue_options | queue_options

        if exchange_options is None:
            exchange_options = {}
        exchange_options = self._exchange_options | exchange_options

        if channel is None:
            channel = self._channels[0]

        partitions = 1 if queue_options['dead_letters'] else self._partitions
        data = []
        for partition in range(partitions):
            if dead_letter:
                queue_name = queue
            else:
                queue_name = get_partition_queue_name(queue, partition)

            arguments = {}
            if queue_options['quorum']:
                arguments['x-queue-type'] = 'quorum'
            else:
                arguments['x-queue-type'] = 'classic'
                if queue_options['lazy']:
                    #  Quorum queues cannot be defined as lazy.
                    arguments['x-queue-mode'] = 'lazy'

            if not dead_letter and queue_options['dead_letters']:
                dead_letter_queue_name = f'{queue_name}.dlq'
                self._declare_queue(
                    queue=dead_letter_queue_name,
                    dead_letter=True,
                )

                arguments['x-dead-letter-exchange'] = self._exchange
                arguments['x-dead-letter-routing-key'] = dead_letter_queue_name

            self._declare_exchange(
                self._exchange,
                exchange_options=exchange_options,
            )
            data.append(
                channel.queue_declare(
                    queue_name,
                    durable=queue_options['durable'],
                    auto_delete=queue_options['auto_delete'],
                    arguments=arguments,
                )
            )

            channel.queue_bind(
                exchange=self._exchange,
                queue=queue_name,
                routing_key=queue_name,
            )

            self._declared_logical_queues.add(queue_name)

        return data

    def _get_message_retries(self, message_id):
        if message_id in self._message_retries:
            return self._message_retries[message_id]
        else:
            return 0

    def _increment_message_retries(self, message_id):
        if not message_id:
            return
        self._message_retries[message_id] = (
            self._message_retries[message_id]
            + 1 if message_id in self._message_retries else 1
        )

    def _remove_message_retries(self, message_id):
        if (message_id in self._message_retries):
            del self._message_retries[message_id]


def reconnect(function):
    def _(*args, **kwargs):
        retries = 0

        while True:
            try:
                return function(*args, **kwargs)

            except Exception as error:
                print("reconnect")
                instance = args[0]
                retries += 1
                if (not instance._max_retries
                        or retries >= instance._max_retries):
                    raise error
                logger.error(error=error)

                time.sleep(instance._sleep_seconds_on_retry)

                with instance._reconnect_lock:
                    logger.warning(
                        'Reconnecting... '
                        f'({retries}/{instance._max_retries})',
                        error=error
                    )

                    try:
                        instance.connect(do_wait=False)
                        break
                    except Exception as error:
                        logger.error(
                            'Could not reconnect.',
                            error=error,
                        )

    return _
