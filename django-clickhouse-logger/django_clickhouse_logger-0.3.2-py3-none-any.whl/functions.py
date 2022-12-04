import datetime
import io
import logging
import traceback
import shortuuid
import hashlib
from clickhouse_driver import connect
from clickhouse_driver.dbapi.extras import DictCursor
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_HOST
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_PORT
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_USER
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_PASSWORD
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_REQUEST_EXTRA


def format_exception(ei) -> str:
    sio = io.StringIO()
    tb = ei[2]
    traceback.print_exception(ei[0], ei[1], tb, None, sio)
    s = sio.getvalue()
    sio.close()
    if s[-1:] == "\n":
        s = s[:-1]
    return s


def logger(record: logging.LogRecord = "") -> None:

    assert DJANGO_CLICKHOUSE_LOGGER_HOST, "Please specify DJANGO_CLICKHOUSE_LOGGER_HOST in your settings.py file"
    clickhouse_connect = connect(host=DJANGO_CLICKHOUSE_LOGGER_HOST, port=DJANGO_CLICKHOUSE_LOGGER_PORT, user=DJANGO_CLICKHOUSE_LOGGER_USER, password=DJANGO_CLICKHOUSE_LOGGER_PASSWORD)

    request = record.request
    exc_info = getattr(record, "exc_info", "")

    if exc_info:
        exc_info = format_exception(exc_info)   

    data = {}
    data["uuid"] = shortuuid.uuid()
    data["asctime"] = datetime.datetime.now()
    data["exc_info"] = exc_info 
    data["exc_hash"] = hashlib.md5(exc_info.encode()).hexdigest()
    data["user"] = str(request.user)
    data["user_id"] = request.user.id
    data["request_extra"] = str(getattr(request, DJANGO_CLICKHOUSE_LOGGER_REQUEST_EXTRA, ""))
    data["site"] = f"{request.get_host()}:{request.get_port()}"
    data["scheme"] = str(request.scheme) 
    data["body"] = str(request.body) 
    data["path"] = str(request.path) 
    data["method"] = str(request.method)  
    data["GET"] = str(request.GET)  
    data["POST"] = str(request.POST)  
    data["headers"] = str(request.headers) 
    data["args"] = str(request.resolver_match.args)
    data["kwargs"] = str(request.resolver_match.kwargs)  
    data["pathname"] = str(getattr(record, "pathname", ""))
    data["funcName"] = str(getattr(record, "funcName", ""))
    data["lineno"] = getattr(record, "lineno", 0)
    data["message"] = record.getMessage() 
    data["exc_text"] = str(getattr(record, "exc_text", ""))   
    data["created"] = getattr(record, "lineno", 0)
    data["filename"] = str(getattr(record, "filename", ""))  
    data["levelname"] = str(getattr(record, "levelname", ""))  
    data["levelno"] = str(getattr(record, "levelno", ""))  
    data["module"] = str(getattr(record, "module", ""))  
    data["msecs"] = getattr(record, "msecs", 0)  
    data["msg"] = str(getattr(record, "msg", ""))  
    data["name"] = str(getattr(record, "name", ""))  
    data["process"] = str(getattr(record, "process", ""))  
    data["processName"] = str(getattr(record, "processName", ""))  
    data["relativeCreated"] = str(getattr(record, "relativeCreated", ""))  
    data["stack_info"] = str(getattr(record, "stack_info", ""))  
    data["thread"] = str(getattr(record, "thread", ""))  
    data["threadName"] = str(getattr(record, "threadName", ""))  

    with clickhouse_connect.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute(
            """INSERT INTO django_clickhouse_logger.logger (*) VALUES""",
            [data],
        )


def capture_exception(error: BaseException, message: str = "") -> None:

    assert DJANGO_CLICKHOUSE_LOGGER_HOST, "Please specify DJANGO_CLICKHOUSE_LOGGER_HOST in your settings.py file"
    clickhouse_connect = connect(host=DJANGO_CLICKHOUSE_LOGGER_HOST, port=DJANGO_CLICKHOUSE_LOGGER_PORT, user=DJANGO_CLICKHOUSE_LOGGER_USER, password=DJANGO_CLICKHOUSE_LOGGER_PASSWORD)
    
    exc_info = traceback.format_exception(error)
    exc_info = "\n".join(exc_info)
    
    data = {}
    data["uuid"] = shortuuid.uuid()
    data["asctime"] = datetime.datetime.now()
    data["exc_info"] = exc_info 
    data["exc_hash"] = hashlib.md5(exc_info.encode()).hexdigest()
    data["message"] = message

    with clickhouse_connect.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute(
            """INSERT INTO django_clickhouse_logger.capture_exception (*) VALUES""",
            [data],
        )


