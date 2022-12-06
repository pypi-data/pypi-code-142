from rest_framework import status as st
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


class JsonSerializer:
    MODEL = None
    DATA = None
    OPTIONS = None
    MAX_LENGTH = None
    UNDEFINED_FIELD = False
    MODEL_TYPE = [int, str, float, bool, list, dict, tuple, set, "ANY"]

    def __init__(self, data=None):
        self.load_data(data)

    def load_data(self, data):
        self.body = None if data == b'' else json.loads(data.decode('utf-8'))

    def check_configurations(self):
        if self.MODEL is not None:
            if not isinstance(self.MODEL, dict):
                raise Exception(f"{self.MODEL}\nMODEL must be dict")
            for mdl in self.MODEL:
                if self.MODEL[mdl] not in self.MODEL_TYPE:
                    raise Exception(
                        f"{self.MODEL}\nModel type must be in {self.MODEL_TYPE}")
            if self.OPTIONS is not None:
                if not isinstance(self.OPTIONS, dict):
                    raise Exception(f"{self.OPTIONS}\nOPTIONS must be dict")
                for opt in self.OPTIONS:
                    if self.MODEL.get(opt) is None:
                        raise Exception(
                            f"{self.MODEL}\n{self.OPTIONS}\nOption key must be in model")
                    if not isinstance(self.OPTIONS[opt], list):
                        raise Exception(
                            f"{self.OPTIONS}\nOptions value must be list")
            if self.MAX_LENGTH is not None:
                if not isinstance(self.MAX_LENGTH, dict):
                    raise Exception(
                        f"{self.MAX_LENGTH}\nMAX_LENGTH must be dict")
                for lngth in self.MAX_LENGTH:
                    if self.MODEL.get(lngth) is None:
                        raise Exception(
                            f"{self.MODEL}\n{self.MAX_LENGTH}\nMax length key must be in model")
                    if not self.MODEL[lngth] is str:
                        raise Exception(
                            f"{self.MODEL}\n{self.MAX_LENGTH}\nMax length key just str")
                    if not isinstance(self.MAX_LENGTH[lngth], int):
                        raise Exception(
                            f"{self.MAX_LENGTH}\nMax length value must be int")
            return True
        raise Exception("Model is not defined")

    def check_field(self):
        if self.check_configurations():
            if not self.UNDEFINED_FIELD:
                if not len(self.MODEL) == len(self.body):
                    return False
            for mdl in self.MODEL:
                if mdl not in self.body:
                    return False
                if not self.MODEL[mdl] == "ANY":
                    if not isinstance(self.body[mdl], self.MODEL[mdl]):
                        return False
                if self.OPTIONS is not None:
                    if mdl in self.OPTIONS:
                        if self.body[mdl] not in self.OPTIONS[mdl]:
                            return False
                if self.MAX_LENGTH is not None:
                    if mdl in self.MAX_LENGTH:
                        if len(self.body[mdl]) > self.MAX_LENGTH[mdl]:
                            return False
            self.DATA = self.body
            self.body = None
            return True

    def is_valid(self):
        if self.body:
            return self.check_field()
        raise Exception(
            "Body is empty if using is_valid method body data must be")

    @staticmethod
    def response(data=None, status=st.HTTP_200_OK):
        return Response(data=data, status=status)

    @staticmethod
    def lazy_response(function, parameters: set, data=None, status=st.HTTP_200_OK):
        return LazyResponse(data=data, then_callback=function, status=status, parameters=parameters)

    @staticmethod
    def http_100_continue(data=None):
        return Response(data=data, status=st.HTTP_100_CONTINUE)

    @staticmethod
    def http_101_switching_protocols(data=None):
        return Response(data=data, status=st.HTTP_101_SWITCHING_PROTOCOLS)

    @staticmethod
    def http_102_processing(data=None):
        return Response(data=data, status=st.HTTP_102_PROCESSING)

    @staticmethod
    def http_103_early_hints(data=None):
        return Response(data=data, status=st.HTTP_103_EARLY_HINTS)

    @staticmethod
    def http_200_ok(data=None):
        return Response(data=data, status=st.HTTP_200_OK)

    @staticmethod
    def http_201_created(data=None):
        return Response(data=data, status=st.HTTP_201_CREATED)

    @staticmethod
    def http_202_accepted(data=None):
        return Response(data=data, status=st.HTTP_202_ACCEPTED)

    @staticmethod
    def http_203_non_authoritative_information(data=None):
        return Response(data=data, status=st.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    @staticmethod
    def http_204_no_content(data=None):
        return Response(data=data, status=st.HTTP_204_NO_CONTENT)

    @staticmethod
    def http_205_reset_content(data=None):
        return Response(data=data, status=st.HTTP_205_RESET_CONTENT)

    @staticmethod
    def http_206_partial_content(data=None):
        return Response(data=data, status=st.HTTP_206_PARTIAL_CONTENT)

    @staticmethod
    def http_207_multi_status(data=None):
        return Response(data=data, status=st.HTTP_207_MULTI_STATUS)

    @staticmethod
    def http_208_already_reported(data=None):
        return Response(data=data, status=st.HTTP_208_ALREADY_REPORTED)

    @staticmethod
    def http_226_im_used(data=None):
        return Response(data=data, status=st.HTTP_226_IM_USED)

    @staticmethod
    def http_300_multiple_choices(data=None):
        return Response(data=data, status=st.HTTP_300_MULTIPLE_CHOICES)

    @staticmethod
    def http_301_moved_permanently(data=None):
        return Response(data=data, status=st.HTTP_301_MOVED_PERMANENTLY)

    @staticmethod
    def http_302_found(data=None):
        return Response(data=data, status=st.HTTP_302_FOUND)

    @staticmethod
    def http_303_see_other(data=None):
        return Response(data=data, status=st.HTTP_303_SEE_OTHER)

    @staticmethod
    def http_304_not_modified(data=None):
        return Response(data=data, status=st.HTTP_304_NOT_MODIFIED)

    @staticmethod
    def http_305_use_proxy(data=None):
        return Response(data=data, status=st.HTTP_305_USE_PROXY)

    @staticmethod
    def http_306_switch_proxy(data=None):
        return Response(data=data, status=st.HTTP_306_RESERVED)

    @staticmethod
    def http_307_temporary_redirect(data=None):
        return Response(data=data, status=st.HTTP_307_TEMPORARY_REDIRECT)

    @staticmethod
    def http_308_permanent_redirect(data=None):
        return Response(data=data, status=st.HTTP_308_PERMANENT_REDIRECT)

    @staticmethod
    def http_400_bad_request(data=None):
        return Response(data=data, status=st.HTTP_400_BAD_REQUEST)

    @staticmethod
    def http_401_unauthorized(data=None):
        return Response(data=data, status=st.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def http_402_payment_required(data=None):
        return Response(data=data, status=st.HTTP_402_PAYMENT_REQUIRED)

    @staticmethod
    def http_403_forbidden(data=None):
        return Response(data=data, status=st.HTTP_403_FORBIDDEN)

    @staticmethod
    def http_404_not_found(data=None):
        return Response(data=data, status=st.HTTP_404_NOT_FOUND)

    @staticmethod
    def http_405_method_not_allowed(data=None):
        return Response(data=data, status=st.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    def http_406_not_acceptable(data=None):
        return Response(data=data, status=st.HTTP_406_NOT_ACCEPTABLE)

    @staticmethod
    def http_407_proxy_authentication_required(data=None):
        return Response(data=data, status=st.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)

    @staticmethod
    def http_408_request_timeout(data=None):
        return Response(data=data, status=st.HTTP_408_REQUEST_TIMEOUT)

    @staticmethod
    def http_409_conflict(data=None):
        return Response(data=data, status=st.HTTP_409_CONFLICT)

    @staticmethod
    def http_410_gone(data=None):
        return Response(data=data, status=st.HTTP_410_GONE)

    @staticmethod
    def http_411_length_required(data=None):
        return Response(data=data, status=st.HTTP_411_LENGTH_REQUIRED)

    @staticmethod
    def http_412_precondition_failed(data=None):
        return Response(data=data, status=st.HTTP_412_PRECONDITION_FAILED)

    @staticmethod
    def http_413_payload_too_large(data=None):
        return Response(data=data, status=st.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

    @staticmethod
    def http_414_uri_too_long(data=None):
        return Response(data=data, status=st.HTTP_414_REQUEST_URI_TOO_LONG)

    @staticmethod
    def http_415_unsupported_media_type(data=None):
        return Response(data=data, status=st.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    @staticmethod
    def http_416_requested_range_not_satisfiable(data=None):
        return Response(data=data, status=st.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE)

    @staticmethod
    def http_417_expectation_failed(data=None):
        return Response(data=data, status=st.HTTP_417_EXPECTATION_FAILED)

    @staticmethod
    def http_418_im_a_teapot(data=None):
        return Response(data=data, status=st.HTTP_418_IM_A_TEAPOT)

    @staticmethod
    def http_421_misdirected_request(data=None):
        return Response(data=data, status=st.HTTP_421_MISDIRECTED_REQUEST)

    @staticmethod
    def http_422_unprocessable_entity(data=None):
        return Response(data=data, status=st.HTTP_422_UNPROCESSABLE_ENTITY)

    @staticmethod
    def http_423_locked(data=None):
        return Response(data=data, status=st.HTTP_423_LOCKED)

    @staticmethod
    def http_424_failed_dependency(data=None):
        return Response(data=data, status=st.HTTP_424_FAILED_DEPENDENCY)

    @staticmethod
    def http_426_upgrade_required(data=None):
        return Response(data=data, status=st.HTTP_426_UPGRADE_REQUIRED)

    @staticmethod
    def http_428_precondition_required(data=None):
        return Response(data=data, status=st.HTTP_428_PRECONDITION_REQUIRED)

    @staticmethod
    def http_429_too_many_requests(data=None):
        return Response(data=data, status=st.HTTP_429_TOO_MANY_REQUESTS)

    @staticmethod
    def http_431_request_header_fields_too_large(data=None):
        return Response(data=data, status=st.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE)

    @staticmethod
    def http_451_unavailable_for_legal_reasons(data=None):
        return Response(data=data, status=st.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)

    @staticmethod
    def http_500_internal_server_error(data=None):
        return Response(data=data, status=st.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def http_501_not_implemented(data=None):
        return Response(data=data, status=st.HTTP_501_NOT_IMPLEMENTED)

    @staticmethod
    def http_502_bad_gateway(data=None):
        return Response(data=data, status=st.HTTP_502_BAD_GATEWAY)

    @staticmethod
    def http_503_service_unavailable(data=None):
        return Response(data=data, status=st.HTTP_503_SERVICE_UNAVAILABLE)

    @staticmethod
    def http_504_gateway_timeout(data=None):
        return Response(data=data, status=st.HTTP_504_GATEWAY_TIMEOUT)

    @staticmethod
    def http_505_http_version_not_supported(data=None):
        return Response(data=data, status=st.HTTP_505_HTTP_VERSION_NOT_SUPPORTED)

    @staticmethod
    def http_506_variant_also_negotiates(data=None):
        return Response(data=data, status=st.HTTP_506_VARIANT_ALSO_NEGOTIATES)

    @staticmethod
    def http_507_insufficient_storage(data=None):
        return Response(data=data, status=st.HTTP_507_INSUFFICIENT_STORAGE)

    @staticmethod
    def http_508_loop_detected(data=None):
        return Response(data=data, status=st.HTTP_508_LOOP_DETECTED)

    @staticmethod
    def http_510_not_extended(data=None):
        return Response(data=data, status=st.HTTP_510_NOT_EXTENDED)

    @staticmethod
    def http_511_network_authentication_required(data=None):
        return Response(data=data, status=st.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)


class LazyResponse(Response):
    def __init__(self, data, then_callback, parameters, **kwargs):
        super().__init__(data, **kwargs)
        self.then_callback = then_callback
        self.parameters = parameters

    def close(self):
        super().close()
        self.then_callback(*self.parameters)

