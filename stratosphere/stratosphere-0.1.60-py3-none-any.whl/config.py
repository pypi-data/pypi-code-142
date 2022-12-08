import logging


class db:
    """Parameters affecting the database management."""

    # The default URL can be used for all database operations.
    default_url = "sqlite:///:memory:"

    # Rads and writes are executed in chunks, that enable
    # r/w progress bars.
    query_read_chunk_size = 1000
    query_write_chunk_size = 1000

    experiments_table = "experiments"
    experiment_table_prefix = "e_"


class serialization:
    enable_compression = False
    store_pickle = True


class tqdm:
    """Parameters controlling how tqdm is used/not used."""

    enable = True


class log:
    """Parameters controlling the built-in logging capabilities."""

    level = logging.INFO

    # If enabled, exceptions are reported in a compact way.
    catch_exceptions = True


class dask:
    """Parameters to handle dask execution backends."""

    scheduler_address = "tcp://127.0.0.1:8786"
    dashboard_address = ":8787"
    scheduler_port = 8786
    client_timeout = "5s"
