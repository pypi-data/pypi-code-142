import urllib3
from urllib3 import Retry
import logging

api_call_times_logger = None
http_pool_manager = None


def setup_logging():
    global api_call_times_logger
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M:%S',
                        filename='myapp.log',
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s %(name)-12s\t\t %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger().addHandler(console)

    api_call_times_logger = logging.getLogger("api_call_times")


def setup_http_pool():
    global http_pool_manager

    retries = Retry(total=1000, connect=5, read=2, redirect=5)

    http_pool_manager = urllib3.PoolManager(num_pools=500,
                                            maxsize=10000,
                                            retries=retries,
                                            block=True)
    urllib3.util.make_headers(keep_alive=True)


setup_logging()
setup_http_pool()
