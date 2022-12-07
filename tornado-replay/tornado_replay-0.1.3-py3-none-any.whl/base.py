import uuid
from typing import Optional
from urllib.parse import parse_qs

import tornado.web

from tornado_replay.models import RequestContainer, ResponseContainer, RequestRecord
from tornado_replay.queue import global_inspect_buffer


class BaseRequestHandler(tornado.web.RequestHandler):  # NOQA

    def _retrieve_request_info(self) -> RequestContainer:
        return RequestContainer(
            queries=parse_qs(self.request.query, keep_blank_values=True),
            headers={k: v for k, v in self.request.headers.items()},
            body_in_byte=self.request.body,
        )

    def _retrieve_response_info(self) -> ResponseContainer:
        return ResponseContainer(
            headers={k: v for k, v in self._headers.items()},
            body_in_byte=b''.join(self._write_buffer),
        )

    def flush(self, include_footers: bool = False):
        # can't wrap in `finish` in case of using `finish` to send chunk
        # can't wrap in `on_finish` cause :meth: `flush` will truncate `_buffer`
        self.request_record: Optional[RequestRecord] = None
        # record request derived from `BaseRequestHandler`
        if isinstance(self, BaseRequestHandler):
            self.request_record = RequestRecord(  # NOQA
                request_id=str(uuid.uuid4()),
                protocol=self.request.protocol, method=self.request.method.upper(),
                host=self.request.host, path=self.request.path,
                uri=self.request.uri, remote_ip=self.request.remote_ip,
                http_version=self.request.version,
                status_code=self.get_status(), reason=self._reason,
            )
            self.request_record.request = self._retrieve_request_info()
            self.request_record.response = self._retrieve_response_info()
            self.request_record.status_code = self.get_status()
            self.request_record.reason = self._reason
            self.request_record.time_elapsed = round(self.request.request_time() * 1000, 2)  # ms
            global_inspect_buffer.add_record(self.request_record)

        super(BaseRequestHandler, self).flush(include_footers)


class NotFoundRequestHandler(BaseRequestHandler):  # NOQA
    # To record 404 Response
    ...
