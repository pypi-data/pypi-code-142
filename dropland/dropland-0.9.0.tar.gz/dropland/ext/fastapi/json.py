from typing import Any

from fastapi import Request
from fastapi.responses import ORJSONResponse
from orjson import orjson


class JsonResponse(ORJSONResponse):
    use_indent: bool = False
    sort_keys: bool = False

    def render(self, content: Any) -> bytes:
        option = orjson.OPT_SERIALIZE_UUID
        if self.use_indent:
            option |= orjson.OPT_INDENT_2
        if self.sort_keys:
            option |= orjson.OPT_SORT_KEYS
        return orjson.dumps(content, option=option)


class JsonRequest(Request):
    # noinspection PyAttributeOutsideInit
    async def json(self) -> bytes:
        if not hasattr(self, '_json'):
            body = await self.body()
            self._json = orjson.loads(body)
        return self._json
