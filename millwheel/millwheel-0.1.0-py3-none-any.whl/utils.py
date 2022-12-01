import logging
from functools import wraps
from subprocess import PIPE, STDOUT, Popen

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def locked(lock):
    def wrapper(function):
        @wraps(function)
        def inner(*a, **kw):
            name = function.__qualname__
            logger.info(f"{name:15s} - acquire lock")
            lock.acquire()
            logger.info(f"{name:15s} - acquired lock")
            try:
                return function(*a, **kw)
            finally:
                lock.release()
                logger.info(f"{name:15s} - released lock")

        return inner

    return wrapper


def syscaller(print):
    def system(w):
        print(w)
        p = Popen(w, shell=True, stdout=PIPE, stderr=STDOUT, text=True)
        for line in iter(p.stdout.readline, ""):
            line = line.rstrip()
            print(line)
        p.wait()
        p.stdout.close()
        if p.returncode:
            logger.error("task failed")

    return system
