from functools import partial
import threading
import queue
import time
import sys

threads = int(sys.argv[1])

start_time = time.time()

filtering_queue = queue.Queue(maxsize=100000)
writing_queue = queue.Queue(maxsize=100000)

def filtering_worker(age=2):
    while True:
        time.sleep(0.1)
        item = filtering_queue.get()
        print(item)
        filtering_queue.task_done()
        writing_queue.put(item)

def writing_worker(age=1):
    while True:
        _ = writing_queue.get()
        writing_queue.task_done()

for i in range(threads):
    threading.Thread(target=partial(filtering_worker, age=2), daemon=True).start()
threading.Thread(target=partial(writing_worker, age=2), daemon=True).start()

for item in range(100):
    filtering_queue.put(item)

filtering_queue.join()
writing_queue.join()

end_time = time.time()

print("%.2f"%(100/(end_time - start_time)))