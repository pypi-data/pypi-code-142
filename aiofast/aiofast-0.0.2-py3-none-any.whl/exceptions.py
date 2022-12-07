from pydantic.errors import PydanticErrorMixin


class FastExceptionMixin(PydanticErrorMixin):
    doc_url = ''

    def __str__(self) -> str:
        msg = self.msg_template.format(**self.__dict__)
        return '{} - {}'.format(msg, self.doc_url)


class FastAioException(FastExceptionMixin, Exception):
    pass


class FastAttributeError(FastExceptionMixin, AttributeError):
    pass


class FastTypeError(FastExceptionMixin, TypeError):
    pass


class FastValueError(FastExceptionMixin, ValueError):
    pass


class UntypedAttrFindError(FastTypeError):
    code = 'attr.untyped'
    msg_template = 'missing "{param_name}" parameter type.'
    doc_url = 'https://github.com/fastaio/...'  # TODO


class UnexpectedAttrError(FastAttributeError):
    code = 'attr.unexpected'
    msg_template = 'unexpected "{param_name}" parameter. supported params: "{supported_params}"'
    doc_url = 'https://github.com/fastaio/...'  # TODO


class UnexpectedContentTypeError(FastValueError):
    code = 'body.not_allowed_content_type'
    msg_template = 'cannot fetch body data. Content-Type "{content_type}" not allowed here.'
    doc_url = 'https://github.com/fastaio/...'  # TODO


class MissingContentTypeError(FastValueError):
    code = 'body.missing_content_type'
    msg_template = 'missing Content-Type header'
    doc_url = 'https://github.com/fastaio/...'  # TODO


class UnexpectedHttpCodeTypeError(FastTypeError):
    code = 'response.http_code.type_error'
    msg_template = 'handler result got wrong http_code type. possible type: "{possible_type}"'
    doc_url = 'https://github.com/fastaio/...'  # TODO


class HandlerResultTypeError(FastTypeError):
    code = 'response.type_error'
    msg_template = 'handler result got wrong answer type. possible type: "{possible_type}"'
    doc_url = 'https://github.com/fastaio/...'  # TODO


class NotOriginalResponseError(FastAioException):
    code = 'response.is_not_original'
    msg_template = 'handler must return the original response since it was defined in the attributes'
    doc_url = 'https://github.com/fastaio/...'  # TODO


class UnhandledResponseTypeError(FastTypeError):
    code = 'response.unhandled_type'
    msg_template = 'cannot return "{method_response_type}" from handler'
    doc_url = 'https://github.com/fastaio/...'  # TODO


class CannotSerializeResponseError(FastTypeError):
    code = 'response.serialize_error'
    msg_template = 'cannot serialize handler response schema: {exc}'
    doc_url = 'https://github.com/fastaio/...'  # TODO


class WrongAnnotatedWebResponseError(FastTypeError):
    code = 'response.wrong_response_annotate'
    msg_template = 'unable to process request: "{attr_name}" attr is specified but it is not "exp_response_type"'
    doc_url = 'https://github.com/fastaio/...'  # TODO
