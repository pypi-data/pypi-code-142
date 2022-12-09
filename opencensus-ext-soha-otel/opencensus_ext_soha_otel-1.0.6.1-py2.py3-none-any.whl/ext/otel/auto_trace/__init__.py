import json
import sys
import traceback

from opencensus.trace import execution_context
from opencensus.trace.status import Status
from qualname import qualname


def _get_function_name(func):
    module = func.__module__
    name = qualname(func)
    if hasattr(func, "__qualname__") and func.__qualname__:
        name = func.__qualname__
    return "{}.{}".format(module, name)


def soha_auto_trace(name=None, soha_tracer=None, method=None, is_capture_result=False, is_capture_except=True):
    if soha_tracer is None:
        raise Exception('args soha_trace is None')

    def decorator(func):
        def wrapper(*args, **kwargs):
            name_span = _get_function_name(func)
            if name is not None:
                name_span = name

            if not execution_context.get_current_span():
                with soha_tracer.start_span(name=name_span):
                    try:
                        rs = func(*args, **kwargs)
                        if method is not None and isinstance(method, str):
                            soha_tracer.current_span().add_attribute("soha_open_telemetry_method", method)

                        if is_capture_result:
                            json_serial = json.dumps(rs)
                            soha_tracer.current_span().add_attribute("soha_open_telemetry_result", json_serial)
                            # set status
                            soha_tracer.current_span().set_status(Status(
                                code=1
                            ))

                        return rs
                    except Exception as e:
                        if is_capture_except:
                            ex_type, ex_value, ex_traceback = sys.exc_info()
                            # Extract un formatter stack traces as tuples
                            trace_back = traceback.extract_tb(ex_traceback)
                            soha_tracer.current_span().add_attribute("exception.message",
                                                                     getattr(e, 'message', e))
                            soha_tracer.current_span().add_attribute("exception.stacktrace",
                                                                     json.dumps(trace_back))
                            soha_tracer.current_span().add_attribute("exception.type", "Error")
                            soha_tracer.current_span().set_status(Status(
                                code=2,
                                message=getattr(e, 'message', e)
                            ))
                        raise e
            else:
                with soha_tracer.span(name=name_span):
                    try:
                        rs = func(*args, **kwargs)
                        if method is not None and isinstance(method, str):
                            soha_tracer.current_span().add_attribute("soha_open_telemetry_method", method)

                        if is_capture_result:
                            json_serial = json.dumps(rs)
                            soha_tracer.current_span().add_attribute("soha_open_telemetry_result", json_serial)
                            # set status
                            soha_tracer.current_span().set_status(Status(
                                code=1
                            ))

                        return rs
                    except Exception as e:
                        if is_capture_except:
                            ex_type, ex_value, ex_traceback = sys.exc_info()
                            # Extract un formatter stack traces as tuples
                            trace_back = traceback.extract_tb(ex_traceback)
                            soha_tracer.current_span().add_attribute("exception.message",
                                                                     getattr(e, 'message', e))
                            soha_tracer.current_span().add_attribute("exception.stacktrace",
                                                                     json.dumps(trace_back))
                            soha_tracer.current_span().add_attribute("exception.type", "Error")
                            soha_tracer.current_span().set_status(Status(
                                code=2,
                                message=getattr(e, 'message', e)
                            ))
                        raise e

        return wrapper

    return decorator
