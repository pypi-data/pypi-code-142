from typing import TYPE_CHECKING, Iterable, Callable, List

from ._data_grid_type import use_field_names_in_headers_arg_parser
from ..._tools import (
    universe_arg_parser,
    fields_arg_parser,
    ADC_TR_PATTERN,
    ADC_FUNC_PATTERN_IN_FIELDS,
    cached_property,
)
from ...delivery._data._data_provider import (
    DataProvider,
    RequestFactory,
    ResponseFactory,
    ContentValidator,
    ValidatorContainer,
    Request,
)
from ...delivery._data import RequestMethod

if TYPE_CHECKING:
    from ..._core.session import Session
    from ...delivery._data._data_provider import ParsedData

# --------------------------------------------------------------------------------------
#   Response
# --------------------------------------------------------------------------------------
response_errors = {
    "default": "{error_message} Requested universes: {universes}. Requested fields: {"
    "fields}",
    412: "Unable to resolve all requested identifiers in {universes}.",
    218: "Unable to resolve all requested fields in {fields}. The formula must "
    "contain at least one field or function.",
}


class DataGridRDPResponseFactory(ResponseFactory):
    def create_success(self, data: "ParsedData", session: "Session" = None, **kwargs):
        inst = super().create_success(data, **kwargs)
        content_data = data.content_data
        descriptions = content_data.get("messages", {}).get("descriptions", [])
        for descr in descriptions:
            code = descr.get("code")
            if code in {416, 413}:
                inst.errors.append((code, descr.get("description")))
        return inst

    def create_fail(self, data: "ParsedData", universe=None, fields=None, **kwargs):
        error_message = data.first_error_message
        error_code = data.first_error_code
        if error_code not in response_errors.keys():
            data.error_messages = response_errors["default"].format(
                error_message=error_message, fields=fields, universes=universe
            )
        else:
            data.error_messages = response_errors[error_code].format(
                fields=fields, universes=universe
            )

        inst = self.response_class(False, data)
        inst.data = self.data_class(data.content_data)
        inst.data._owner = inst
        return inst


class DataGridUDFResponseFactory(ResponseFactory):
    def get_raw(self, data: "ParsedData"):
        content_data = data.content_data
        return content_data.get("responses", [{}])[0]

    def create_success(self, data: "ParsedData", session: "Session" = None, **kwargs):
        inst = super().create_success(data, **kwargs)
        raw = self.get_raw(data)
        error = raw.get("error", [])
        for err in error:
            code = err.get("code")
            if code == 416:
                inst.errors.append((code, err.get("message")))

        return inst

    def create_fail(self, data: "ParsedData", universe=None, fields=None, **kwargs):
        error_code = data.first_error_code
        error_message = data.first_error_message

        if error_code not in response_errors.keys():
            data.error_messages = response_errors["default"].format(
                error_message=error_message, fields=fields, universes=universe
            )

        else:
            data.error_messages = response_errors[error_code].format(
                fields=fields, universes=universe
            )

        inst = self.response_class(False, data)
        inst.data = self.data_class(data.content_data)
        inst.data._owner = inst
        return inst


# --------------------------------------------------------------------------------------
#   Request
# --------------------------------------------------------------------------------------


def validate_correct_format_parameters(*_, **kwargs) -> dict:
    parameters = kwargs.get("parameters")
    extended_params = kwargs.get("extended_params")
    universe = kwargs.get("universe")
    fields = kwargs.get("fields")
    use_field_names_in_headers = kwargs.get("use_field_names_in_headers")

    if parameters is not None and not isinstance(parameters, dict):
        raise ValueError(f"Arg parameters must be a dictionary")

    extended_params = extended_params or {}
    universe = extended_params.get("universe") or universe
    universe = universe_arg_parser.get_list(universe)
    universe = [value.upper() if value.islower() else value for value in universe]
    fields = fields_arg_parser.get_list(fields)
    use_field_names_in_headers = use_field_names_in_headers_arg_parser.get_bool(
        use_field_names_in_headers
    )

    kwargs.update(
        {
            "universe": universe,
            "fields": fields,
            "parameters": parameters,
            "use_field_names_in_headers": use_field_names_in_headers,
            "extended_params": extended_params,
        }
    )
    return kwargs


class DataGridRDPRequestFactory(RequestFactory):
    def get_body_parameters(self, *_, **kwargs) -> dict:
        kwargs = validate_correct_format_parameters(*_, **kwargs)
        body_parameters = {}

        universe = kwargs.get("universe")
        if universe:
            body_parameters["universe"] = universe

        fields = kwargs.get("fields")
        if fields:
            body_parameters["fields"] = fields

        parameters = kwargs.get("parameters")
        if parameters:
            body_parameters["parameters"] = parameters

        layout = kwargs.get("layout")
        if isinstance(layout, dict) and layout.get("output"):
            body_parameters["output"] = layout["output"]

        return body_parameters

    def get_request_method(self, **kwargs) -> RequestMethod:
        return RequestMethod.POST


class DataGridUDFRequestFactory(RequestFactory):
    def create(self, session, *args, **kwargs):
        url_root = session._get_rdp_url_root()
        url = url_root.replace("rdp", "udf")

        method = self.get_request_method(**kwargs)
        header_parameters = kwargs.get("header_parameters") or {}
        extended_params = kwargs.get("extended_params") or {}
        body_parameters = self.get_body_parameters(*args, **kwargs)
        body_parameters = self.extend_body_parameters(body_parameters, extended_params)

        headers = {"Content-Type": "application/json"}
        headers.update(header_parameters)

        return Request(
            url=url,
            method=method,
            headers=headers,
            json={
                "Entity": {
                    "E": "DataGrid_StandardAsync",
                    "W": {"requests": [body_parameters]},
                }
            },
        )

    def get_body_parameters(self, *_, **kwargs) -> dict:
        ticket = kwargs.get("ticket", None)
        if ticket:
            return {"ticket": ticket}

        kwargs = validate_correct_format_parameters(*_, **kwargs)
        body_parameters = {}

        instruments = kwargs.get("universe")
        if instruments:
            body_parameters["instruments"] = instruments

        fields = kwargs.get("fields")
        if fields:
            body_parameters["fields"] = [
                {"name": i}
                for i in fields
                if ADC_TR_PATTERN.match(i) or ADC_FUNC_PATTERN_IN_FIELDS.match(i)
            ]

        parameters = kwargs.get("parameters")
        if parameters:
            body_parameters["parameters"] = parameters

        layout = kwargs.get("layout")
        if isinstance(layout, dict) and layout.get("layout"):
            body_parameters["layout"] = layout["layout"]

        return body_parameters

    def get_request_method(self, **kwargs) -> RequestMethod:
        return RequestMethod.POST


# --------------------------------------------------------------------------------------
#   Content data validator
# --------------------------------------------------------------------------------------


class DataGridContentValidator(ContentValidator):
    @classmethod
    def status_is_not_error(cls, data: "ParsedData") -> bool:
        status_content = data.status.get("content", "")
        if status_content.startswith("Failed"):
            data.error_codes = -1
            data.error_messages = status_content
            return False

        return True


class DataGridRDPContentValidator(DataGridContentValidator):
    @classmethod
    def content_data_has_no_error(cls, data: "ParsedData") -> bool:
        content_data = data.content_data
        error = content_data.get("error")
        if error and not content_data.get("data"):
            data.error_codes = error.get("code", -1)
            data.error_messages = error.get("description")

            if not data.error_messages:
                error_message = error.get("message")
                errors = error.get("errors")

                if isinstance(errors, list):
                    error_message += ":\n"
                    error_message += "\n".join(map(str, errors))

                data.error_messages = error_message

            return False

        return True

    @cached_property
    def validators(self) -> List[Callable[["ParsedData"], bool]]:
        return [
            self.status_is_not_error,
            self.content_data_is_not_none,
            self.content_data_has_no_error,
        ]


class DataGridUDFContentValidator(DataGridContentValidator):
    @classmethod
    def content_data_is_valid_type(cls, data: "ParsedData") -> bool:
        content_data = data.content_data
        if isinstance(content_data, str):
            data.error_codes = -1
            data.error_messages = content_data
            return False

        return True

    @classmethod
    def content_data_has_valid_response(cls, data: "ParsedData") -> bool:
        responses = data.content_data.get("responses", [])
        first_response = responses[0] if responses else {}
        error = first_response.get("error")
        if error and not first_response.get("data"):
            if isinstance(error, dict):
                data.error_codes = error.get("code", -1)
                data.error_messages = error.get("message", error)

            else:
                data.error_codes = -1
                data.error_messages = error

            return False

        return True

    @classmethod
    def content_data_response_has_valid_data(cls, data: "ParsedData") -> bool:
        responses = data.content_data.get("responses", [])
        first_response = responses[0] if responses else {}
        error = first_response.get("error")
        if error and not any(
            any(items[1:]) if isinstance(items, Iterable) else False
            for items in first_response.get("data")
        ):
            first_error = error[0]
            data.error_codes = first_error.get("code", -1)
            data.error_messages = first_error.get("message", first_error)
            return False

        return True

    @cached_property
    def validators(self) -> List[Callable[["ParsedData"], bool]]:
        return [
            self.status_is_not_error,
            self.content_data_is_not_none,
            self.content_data_is_valid_type,
            self.content_data_has_no_error,
            self.content_data_has_valid_response,
            self.content_data_response_has_valid_data,
        ]


# --------------------------------------------------------------------------------------
#   Providers
# --------------------------------------------------------------------------------------


data_grid_rdp_data_provider = DataProvider(
    request=DataGridRDPRequestFactory(),
    response=DataGridRDPResponseFactory(),
    validator=ValidatorContainer(content_validator=DataGridRDPContentValidator()),
)

data_grid_udf_data_provider = DataProvider(
    request=DataGridUDFRequestFactory(),
    response=DataGridUDFResponseFactory(),
    validator=ValidatorContainer(content_validator=DataGridUDFContentValidator()),
)
