from simple_print import sprint
from clickhouse_driver import Client as ClickHouseClient
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_HOST
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_PORT
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_USER
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_PASSWORD
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_TTL_DAY


def create_logger_table() -> None:
    # python manage.py shell --command="from django_clickhouse_logger.db import create_logger_table; create_logger_table();"

    assert DJANGO_CLICKHOUSE_LOGGER_HOST, "Please specify DJANGO_CLICKHOUSE_LOGGER_HOST in your settings.py file"
    assert isinstance(DJANGO_CLICKHOUSE_LOGGER_TTL_DAY, int), "DJANGO_CLICKHOUSE_LOGGER_TTL_DAY must be positive integer"

    client = ClickHouseClient(host=DJANGO_CLICKHOUSE_LOGGER_HOST, port=DJANGO_CLICKHOUSE_LOGGER_PORT, user=DJANGO_CLICKHOUSE_LOGGER_USER, password=DJANGO_CLICKHOUSE_LOGGER_PASSWORD)
    client.execute("CREATE DATABASE IF NOT EXISTS django_clickhouse_logger")
    client.execute("DROP TABLE IF EXISTS django_clickhouse_logger.logger")
    client.execute(f"""
    CREATE TABLE django_clickhouse_logger.logger (
    `uuid` String,
    `asctime` DateTime,     
    `exc_info` Nullable(String),
    `exc_hash` Nullable(String),
    `user` Nullable(String),
    `user_id` Nullable(UInt16),
    `request_extra` Nullable(String),
    `site` Nullable(String),   
    `scheme` Nullable(String),  
    `body` Nullable(String),  
    `path` Nullable(String),  
    `method` Nullable(String), 
    `GET` Nullable(String),
    `POST` Nullable(String),
    `headers` Nullable(String),
    `args` Nullable(String),
    `kwargs` Nullable(String),    
    `pathname` Nullable(String),   
    `funcName` Nullable(String),   
    `lineno` Nullable(Int32),  
    `message` Nullable(String),  
    `exc_text` Nullable(String),      
    `created` Nullable(Float64),
    `filename` Nullable(String),  
    `levelname` Nullable(String),
    `levelno` Nullable(String),
    `module` Nullable(String),
    `msecs` Nullable(Float64),
    `msg` Nullable(String),
    `name` Nullable(String),
    `process` Nullable(String),
    `processName` Nullable(String),
    `relativeCreated` Nullable(String),
    `stack_info` Nullable(String),
    `thread` Nullable(String),  
    `threadName` Nullable(String)    
    ) 
    ENGINE = MergeTree() 
    PARTITION BY toDate(asctime)
    ORDER BY (asctime) 
    TTL asctime + INTERVAL {DJANGO_CLICKHOUSE_LOGGER_TTL_DAY} DAY
    SETTINGS min_bytes_for_wide_part = 0
    """)
    sprint(f"Success create table django_clickhouse_logger.logger; log rotation {DJANGO_CLICKHOUSE_LOGGER_TTL_DAY} day", c="green", f=1)


def truncate_logger_table() -> None:
    # python manage.py shell --command="from django_clickhouse_logger.db import truncate_logger_table; truncate_logger_table();"
    
    assert DJANGO_CLICKHOUSE_LOGGER_HOST, "Please specify DJANGO_CLICKHOUSE_LOGGER_HOST in your settings.py file"
    assert isinstance(DJANGO_CLICKHOUSE_LOGGER_TTL_DAY, int), "DJANGO_CLICKHOUSE_LOGGER_TTL_DAY must be positive integer"

    client = ClickHouseClient(host=DJANGO_CLICKHOUSE_LOGGER_HOST, port=DJANGO_CLICKHOUSE_LOGGER_PORT, user=DJANGO_CLICKHOUSE_LOGGER_USER, password=DJANGO_CLICKHOUSE_LOGGER_PASSWORD)
    client.execute("TRUNCATE TABLE IF EXISTS django_clickhouse_logger.logger")
    sprint(f"Success truncate table django_clickhouse_logger.logger", c="green", f=1)


def create_capture_exception_table() -> None:
    # python manage.py shell --command="from django_clickhouse_logger.db import create_capture_exception_table; create_capture_exception_table();"

    assert DJANGO_CLICKHOUSE_LOGGER_HOST, "Please specify DJANGO_CLICKHOUSE_LOGGER_HOST in your settings.py file"
    assert isinstance(DJANGO_CLICKHOUSE_LOGGER_TTL_DAY, int), "DJANGO_CLICKHOUSE_LOGGER_TTL_DAY must be positive integer"

    client = ClickHouseClient(host=DJANGO_CLICKHOUSE_LOGGER_HOST, port=DJANGO_CLICKHOUSE_LOGGER_PORT, user=DJANGO_CLICKHOUSE_LOGGER_USER, password=DJANGO_CLICKHOUSE_LOGGER_PASSWORD)
    client.execute("CREATE DATABASE IF NOT EXISTS django_clickhouse_logger")
    client.execute("DROP TABLE IF EXISTS django_clickhouse_logger.capture_exception")

    client.execute(f"""
    CREATE TABLE django_clickhouse_logger.capture_exception (
    `uuid` String,
    `asctime` DateTime,     
    `exc_info` Nullable(String),
    `exc_hash` Nullable(String),
    `message` Nullable(String) 
    ) 
    ENGINE = MergeTree() 
    PARTITION BY toDate(asctime)
    ORDER BY (asctime) 
    TTL asctime + INTERVAL {DJANGO_CLICKHOUSE_LOGGER_TTL_DAY} DAY
    SETTINGS min_bytes_for_wide_part = 0
    """)
    sprint(f"Success create table django_clickhouse_logger.capture_exception; log rotation {DJANGO_CLICKHOUSE_LOGGER_TTL_DAY} day", c="green", f=1)


def truncate_capture_exception_table() -> None:
    # python manage.py shell --command="from django_clickhouse_logger.db import truncate_capture_exception_table; truncate_capture_exception_table();"
    
    assert DJANGO_CLICKHOUSE_LOGGER_HOST, "Please specify DJANGO_CLICKHOUSE_LOGGER_HOST in your settings.py file"
    assert isinstance(DJANGO_CLICKHOUSE_LOGGER_TTL_DAY, int), "DJANGO_CLICKHOUSE_LOGGER_TTL_DAY must be positive integer"

    client = ClickHouseClient(host=DJANGO_CLICKHOUSE_LOGGER_HOST, port=DJANGO_CLICKHOUSE_LOGGER_PORT, user=DJANGO_CLICKHOUSE_LOGGER_USER, password=DJANGO_CLICKHOUSE_LOGGER_PASSWORD)
    client.execute("TRUNCATE TABLE IF EXISTS django_clickhouse_logger.capture_exception")
    sprint(f"Success truncate table django_clickhouse_logger.capture_exception", c="green", f=1)



