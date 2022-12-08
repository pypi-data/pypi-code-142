import asyncio
import uuid
from typing import MutableMapping, Optional, Union

import aio_pika

from dropland.log import logger, tr
from .engine import Connection


class RmqClient:
    def __init__(self, channel: Connection, routing_key: str,
                 exchange: Optional[aio_pika.RobustExchange] = None,
                 app_id: Optional[str] = None, queue_name: Optional[str] = None) -> None:
        self._channel = channel
        self._exchange = exchange or channel.default_exchange
        self._routing_key = routing_key
        self._app_id = app_id
        self._queue_name = queue_name
        self._queue: Optional[aio_pika.abc.AbstractRobustQueue] = None
        self._consumer_tag: Optional[aio_pika.abc.ConsumerTag] = None
        self._futures: MutableMapping[str, asyncio.Future] = dict()
        self._loop = asyncio.get_running_loop()

    async def connect(self):
        if not self._queue:
            self._queue = await self._channel.declare_queue(
                name=self._queue_name, exclusive=True, auto_delete=True
            )
        if not self._consumer_tag:
            self._consumer_tag = await self._queue.consume(self._on_response)
        return self

    async def disconnect(self):
        if self._consumer_tag:
            await self._queue.cancel(self._consumer_tag)
            self._consumer_tag = self._queue = None

    def _on_response(self, message: aio_pika.IncomingMessage) -> None:
        if message.correlation_id is None:
            logger.error(tr('dropland.engines.rmq.rpc.bad-message').format(message=message))
            return

        logger.debug(tr('dropland.engines.rmq.rpc.received').format(info=message.info()))

        if future := self._futures.pop(message.correlation_id, None):
            future.set_result(message.body)
        else:
            logger.error(tr('dropland.engines.rmq.rpc.correlation-not-found').format(id=message.correlation_id))

    async def send(
            self, body: bytes, content_type: Optional[str] = None,
            headers: Optional[aio_pika.abc.HeadersType] = None,
            delivery_mode: Union[aio_pika.abc.DeliveryMode, int, None] = None,
            expiration: Optional[aio_pika.abc.DateType] = None,
            type: Optional[str] = None,
            user_id: Optional[str] = None) -> bytes:
        correlation_id = str(uuid.uuid4())
        future = self._loop.create_future()
        self._futures[correlation_id] = future

        await self._exchange.publish(
            aio_pika.Message(
                body,
                content_type=content_type,
                correlation_id=correlation_id,
                reply_to=self._queue.name,
                headers=headers,
                delivery_mode=delivery_mode,
                expiration=expiration,
                type=type, user_id=user_id, app_id=self._app_id,
            ),
            routing_key=self._routing_key,
        )

        return bytes(await future)
