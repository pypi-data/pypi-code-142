import json

try:
    import cysimdjson

    _parser = cysimdjson.JSONParser()

    def loads(raw_input: str | bytes) -> dict:
        if not isinstance(raw_input, (bytes, bytearray)):
            raw_input = str.encode(raw_input)
        resp = _parser.parse(raw_input)
        return resp.export()

except ModuleNotFoundError:
    pass

try:
    import orjson

    ORJSON_EXISTS = True

    def str_dumps(v, *, default):
        return orjson.dumps(v, default=default).decode()

    def byte_dumps(v):
        return orjson.dumps(v)

    if "loads" not in globals():

        def loads(raw_input: str) -> dict:
            return orjson.loads(raw_input)

except ModuleNotFoundError:
    ORJSON_EXISTS = False

if "loads" not in globals():

    def loads(raw_input: str) -> dict:
        return json.loads(raw_input)


if "str_dumps" not in globals():

    def str_dumps(v, *, default=None):
        return json.dumps(v)

    def byte_dumps(v):
        return str.encode(json.dumps(v))
