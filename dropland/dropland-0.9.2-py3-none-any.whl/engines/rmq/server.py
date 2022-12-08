from typing import Any, Mapping, Optional

import aio_pika

from dropland.log import logger, tr
from .engine import Connection


class RmqServer:
    def __init__(self, channel: Connection,
                 queue: aio_pika.abc.AbstractRobustQueue,
                 exchange: Optional[aio_pika.RobustExchange] = None,
                 app_id: Optional[str] = None) -> None:
        self._channel = channel
        self._exchange = exchange or channel.default_exchange
        self._queue = queue
        self._app_id = app_id
        self._iter: Optional[aio_pika.abc.AbstractQueueIterator] = None

    def _on_request(self, body: bytes, info: Mapping[str, Any]) -> Optional[bytes]:
        ...

    async def run(self):
        async with self._queue.iterator() as queue_iter:
            self._iter = queue_iter
            message: aio_pika.abc.AbstractIncomingMessage

            async for message in queue_iter:
                try:
                    async with message.process():
                        if response := self._on_request(message.body, message.info()):
                            await self._exchange.publish(
                                aio_pika.Message(
                                    body=response,
                                    correlation_id=message.correlation_id,
                                    delivery_mode=message.delivery_mode,
                                    app_id=self._app_id,
                                ),
                                routing_key=message.reply_to,
                            )
                except Exception as e:
                    logger.exception(tr('dropland.engines.rmq.rpc.exception').format(exc=e))

    async def stop(self):
        if self._iter:
            await self._iter.close()
