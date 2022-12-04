import datetime
import traceback
import shortuuid
import hashlib
from clickhouse_driver import Client as ClickHouseClient
from clickhouse_driver import connect
from clickhouse_driver.dbapi.extras import DictCursor
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_HOST
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_PORT
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_USER
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_PASSWORD
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_REQUEST_EXTRA
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_TTL_DAY


def capture_exception(error: BaseException, message: str = "") -> None:

    assert DJANGO_CLICKHOUSE_LOGGER_HOST, "Please specify DJANGO_CLICKHOUSE_LOGGER_HOST in your settings.py file"
    clickhouse_connect = connect(host=DJANGO_CLICKHOUSE_LOGGER_HOST, port=DJANGO_CLICKHOUSE_LOGGER_PORT, user=DJANGO_CLICKHOUSE_LOGGER_USER, password=DJANGO_CLICKHOUSE_LOGGER_PASSWORD)
    
    exc_info = traceback.format_exception(error)
    exc_info = "\n".join(exc_info)
    
    clickhouse_dict = {}
    clickhouse_dict["uuid"] = shortuuid.uuid()
    clickhouse_dict["asctime"] = datetime.datetime.now()
    clickhouse_dict["exc_info"] = exc_info 
    clickhouse_dict["exc_hash"] = hashlib.md5(exc_info.encode()).hexdigest()
    clickhouse_dict["user"] = "capture_exception"
    clickhouse_dict["user_id"] = 0
    clickhouse_dict["request_extra"] = message
    clickhouse_dict["site"] = ""
    clickhouse_dict["scheme"] = ""
    clickhouse_dict["body"] = ""
    clickhouse_dict["path"] = ""
    clickhouse_dict["method"] = "" 
    clickhouse_dict["GET"] = "" 
    clickhouse_dict["POST"] = "" 
    clickhouse_dict["headers"] = "" 
    clickhouse_dict["args"] = "" 
    clickhouse_dict["kwargs"] = ""  
    clickhouse_dict["pathname"] = "" 
    clickhouse_dict["funcName"] = "" 
    clickhouse_dict["lineno"] = 0 
    clickhouse_dict["message"] = "" 
    clickhouse_dict["exc_text"] = "" 
    clickhouse_dict["created"] = 0
    clickhouse_dict["filename"] = "" 
    clickhouse_dict["levelname"] = ""  
    clickhouse_dict["levelno"] = ""  
    clickhouse_dict["module"] = ""
    clickhouse_dict["msecs"] = 0
    clickhouse_dict["msg"] = "" 
    clickhouse_dict["name"] = "" 
    clickhouse_dict["process"] = ""
    clickhouse_dict["processName"] = ""
    clickhouse_dict["relativeCreated"] = "" 
    clickhouse_dict["stack_info"] = ""
    clickhouse_dict["thread"] = ""
    clickhouse_dict["threadName"] = ""

    with clickhouse_connect.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute(
            """INSERT INTO django_clickhouse_logger.records (*)  VALUES""",
            [clickhouse_dict],
        )

