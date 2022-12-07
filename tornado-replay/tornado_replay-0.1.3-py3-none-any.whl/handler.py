import asyncio
import logging
import os
from typing import Union, Optional, Awaitable

import tornado.web
import tornado.escape
from tornado.concurrent import Future
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

from tornado_replay.queue import global_inspect_buffer


class _BaseInspectHandler(tornado.web.RequestHandler):
    """inner inspect request SHOULD inherit from this. To avoid circle
    capture permanently!
    """

    def get_template_path(self) -> Optional[str]:
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), 'templates'
            )
        )

    async def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        return super(_BaseInspectHandler, self).data_received(chunk)

    async def prepare(self):
        self.json = {}
        if self.request.headers.get('Content-Type', '').startswith('application/json'):
            self.json = tornado.escape.json_decode(
                self.request.body.decode('utf-8')
            ) if self.request.body else {}


class InspectHttpLiveHandler(_BaseInspectHandler):
    """Long-polling request for new request coming
    """

    async def post(self):
        last_request_id = self.json.get("last_request_id", "")
        records = global_inspect_buffer.get_record_after_request_id(last_request_id)
        while not records:
            # Save the Future returned here, so we can cancel it in on_connection_close.
            self.wait_future = global_inspect_buffer.cond.wait()  # NOQA
            try:
                await self.wait_future
            except asyncio.CancelledError:
                return
            records = global_inspect_buffer.get_record_after_request_id(last_request_id)
        if self.request.connection.stream.closed():  # NOQA
            return
        self.write({
            'data': [
                {
                    'request_id': record.request_id,
                    'html': tornado.escape.to_unicode(self.render_string("record_template.html", record=record))
                } for record in records
            ],
            'limit': global_inspect_buffer.cache_size,
        })

    def on_connection_close(self):
        self.wait_future.cancel()


class InspectHttpIndexHandler(_BaseInspectHandler):
    async def get(self):
        await self.render("index.html")

    async def delete(self):
        """Clear records is the buffer
        """
        global_inspect_buffer.clear()
        self.write({})


class InspectHttpRecordHandler(_BaseInspectHandler):

    async def get(self, request_id: str):
        """Get detail of one record
        """
        record = global_inspect_buffer.get_record_by_request_id(request_id)
        if not record:
            return self.write({})
        data = record.to_dict()
        data['detail'] = tornado.escape.to_unicode(
            self.render_string("record_detail_template.html", record=record)
        )
        self.write({
            'data': data,
        })

    async def post(self, request_id: str):
        """Do Request Replay
        """
        record = global_inspect_buffer.get_record_by_request_id(request_id)
        if not record:
            return self.write({})
        url = f'{record.protocol}://{record.host}{record.uri}'
        await self.async_replay(
            method=record.method, url=url,
            body=record.request.body_in_byte,
            headers=record.request.headers,
        )

    @staticmethod
    async def async_replay(method: str, url: str, body: Union[str, bytes, None], **kwargs):
        req: HTTPRequest = HTTPRequest(
            method=method, url=url, body=body, **kwargs,
            allow_nonstandard_methods=True,
        )
        http_client = AsyncHTTPClient()
        my_future = Future()
        fetch_future = http_client.fetch(req)
        try:
            fetch_future.add_done_callback(lambda f: my_future.set_result(f.result()))
        except Exception as e:
            logging.warning(e)
        return my_future
