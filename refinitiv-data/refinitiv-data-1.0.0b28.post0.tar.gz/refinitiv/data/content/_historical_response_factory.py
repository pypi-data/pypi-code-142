from typing import TYPE_CHECKING

from .._core.session import Session
from ..delivery._data._data_provider import ResponseFactory

if TYPE_CHECKING:
    from ..delivery._data._data_provider import ParsedData

response_errors = {
    "default": "{error_message}. Requested ric: {rics}. Requested fields: {fields}",
    "TS.Intraday.UserRequestError.90001": "{rics} - The universe is not found",
    "TS.Intraday.Warning.95004": "{rics} - Trades interleaving with corrections is currently not supported. Corrections will not be returned.",
    "TS.Intraday.UserRequestError.90006": "{error_message} Requested ric: {rics}",
}


class HistoricalResponseFactory(ResponseFactory):
    def get_raw(self, data: "ParsedData"):
        raw = {}
        if data.content_data:
            raw = data.content_data[0]
        return raw

    def create_success(self, data: "ParsedData", session: "Session" = None, **kwargs):
        raw = self.get_raw(data)
        error_code = raw.get("status").get("code") if raw.get("status") else None
        if error_code:
            self._compile_error_message(error_code, data, **kwargs)
        return super().create_success(data, **kwargs)

    def create_fail(self, data: "ParsedData", **kwargs):
        raw = self.get_raw(data)
        status = raw.get("status", {})
        error_code = data.first_error_code or status.get("code")
        self._compile_error_message(error_code, data, **kwargs)
        return super().create_fail(data, **kwargs)

    def _compile_error_message(
        self, error_code: str, data: "ParsedData", universe=None, fields=None, **kwargs
    ):
        """Compile error message in human readable format."""
        content_data = self.get_raw(data) if data.content_data else {}
        error_message = data.first_error_message or content_data.get("status", {}).get(
            "message"
        )
        rics = content_data.get("universe").get("ric") if content_data else universe

        if error_code not in response_errors.keys():
            # Need to add error_code to data because different structure of responses
            data.error_codes = error_code
            data.error_messages = response_errors["default"].format(
                error_message=error_message, rics=rics, fields=fields
            )
        else:
            data.error_codes = error_code
            data.error_messages = response_errors[error_code].format(
                rics=rics, error_message=error_message
            )
