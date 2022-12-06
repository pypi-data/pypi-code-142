import os

# TODO: move async solution `asyncpg`
import psycopg
from psycopg import Connection

def get_pg_client() -> Connection:
    pg_host = os.environ.get("PG_HOST", "localhost")
    pg_port = int(os.environ.get("PG_PORT", 5432))
    pg_dbname = os.environ.get("PG_DBNAME", "test")
    pg_dbuser = os.environ.get("PG_USER", "pguser")
    pg_dbpass = os.environ.get("PG_PASS", "pass")

    return psycopg.connect(
        dbname=pg_dbname,
        user=pg_dbuser,
        password=pg_dbpass,
        host=pg_host,
        port=pg_port,
    )
