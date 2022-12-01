import time
from queue import Empty


def getn_from_queue(queue, n, sleep_seconds=0.0001):
    """
    通用的在queue里面批量取n个值再返回，方便后续的批量操作
    """
    results = []
    try:
        while len(results) < n:
            results.append(queue.get(block=False))
    except Empty:
        time.sleep(sleep_seconds)
    return results
