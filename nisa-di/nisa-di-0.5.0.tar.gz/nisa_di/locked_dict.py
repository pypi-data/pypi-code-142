import threading


class LockedDict(dict):
    _lock: threading.Lock
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._lock = threading.Lock()
        
    def __enter__(self):
        self._lock.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock.release()
        
    
        
        
        
if __name__ == "__main__":
    cc = LockedDict()
    with cc:
        cc['test'] = "asdasdasd"
    
    print(cc)

