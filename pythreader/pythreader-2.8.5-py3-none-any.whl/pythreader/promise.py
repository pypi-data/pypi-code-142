from .core import Primitive, synchronized, Timeout
from threading import get_ident, RLock

class DebugLock(object):
    
    def __init__(self):
        self.R = RLock()
        
    def acquire(self, *params, **args):
        print(self, "acquire by ", get_ident(), "...")
        self.R.acquire(*params, **args)
        print(self, "acquired by ", get_ident())
        
    def release(self):
        print(self, "released by ", get_ident())
        self.R.release()
        
    def __enter__(self):
        return self.acquire()
        
    def __exit__(self, *params):
        return self.release()
    

class Promise(Primitive):
    
    class Callback(Primitive):
        def __init__(self, oncomplete=None, onexception=None):
            self.CompleteCB = oncomplete
            self.ExceptionCB = onexception
        
        def promiseComplete(self, promise, result):
            if self.CompleteCB is not None:
                self.CompleteCB(promise, result)
        
        def promiseException(self, promise, exc_info):
            if self.ExceptionCB is not None:
                self.ExceptionCB(promise, *exc_info)

    def __init__(self, data=None, callbacks = [], name=None):
        Primitive.__init__(self, name=name)    #, lock=DebugLock())
        self.Data = data
        self.Callbacks = callbacks[:]
        self.Complete = False
        self.Canceled = False
        self.Result = None
        self.ExceptionInfo = None     # or tuple (exc_type, exc_value, exc_traceback)
        self.OnDone = self.OnCancel = self.OnException = None
        self.Chained = []
        self.Name = name

    @synchronized
    def add_callback(self, cb=None, oncomplete=None, onexception=None):
        if not self.Cancelled:
            if cb is None:
                cb = self.Callback(oncomplete, onexception)
            if self.ExceptionInfo and hasattr(cb, "promiseException"):
                cb.promiseException(self, *self.ExceptionInfo)
            elif self.Complete and hasattr(cb, "promiseComplete"):
                cb.promiseComplete(self, self.Result)
            else:
                self.Callbacks.append(cb)
        self.wakeup()

    @synchronized
    def chain(self, *promises):
        if self.ExceptionInfo:
            exc_type, exc_value, exc_traceback = self.ExceptionInfo
            for p in promises:
                p.exception(exc_type, exc_value, exc_traceback)
        elif self.Complete:
            for p in promises:
                p.complete(self.Result)
        elif self.Canceled:
            for p in promises:
                p.complete(None)
        else:
            self.Chained += list(promises)
        return self
        
    @synchronized
    def cancel(self, cancel_chained=True):
        self.Cancelled = True
        self.Callbacks = []
        if cancel_chained:
            for p in self.Chained:
                p.cancel(cancel_chained)
        self.wakeup()
        self._cleanup()

    @synchronized
    def complete(self, result=None):
        self.Result = result
        self.Complete = True
        if not self.Canceled:
            for cb in self.Callbacks:
                if hasattr(cb, "promiseComplete") and cb.promiseComplete(self, self.Result) == "stop":
                    break
        for p in self.Chained:
            #print("%s: complete(%s) ..." % (self, p))
            p.complete(result)
            #print("%s: complete(%s) done" % (self, p))
        self.wakeup()
        self._cleanup()
    
    def is_complete(self):
        return self.Complete

    def exception(self):
        return self.ExceptionInfo
        
    def is_cancelled(self):
        return self.Cancelled

    @synchronized
    def exception(self, exc_type, exc_value, exc_traceback):
        self.ExceptionInfo = (exc_type, exc_value, exc_traceback)
        if self.OnException is not None:
            self.OnExceptipn(self)
        for p in self.Chained:
            p.exception(exc_type, exc_value, exc_traceback)
        self.wakeup()
        self._cleanup()
        
    @synchronized
    def wait(self, timeout=None):
        #print("thread %s: wait(%s)..." % (get_ident(), self))
        pred = lambda x: x.Complete or x.Canceled or self.ExceptionInfo is not None
        self.sleep_until(pred, self, timeout=timeout)
        try:
            if self.Complete:
                return self.Result
            elif self.Canceled:
                return None
            elif self.ExceptionInfo:
                _, e, _ = self.ExceptionInfo
                raise e 
            else:
                raise Timeout()
        finally:
            self._cleanup()

    def _cleanup(self):
        self.Chained = []
        self.Callbacks = []
        self.Callbacks = []
    
    def __or__(self, other):
        if isinstance(other, Promise):
            return ORPromise([self, other])
        else:
            return other | self

    def __and__(self, other):
        if isinstance(other, Promise):
            return ANDPromise([self, other])
        else:
            return other & self

class ORPromise(Promise):
    
    def __init__(self, promises):
        Promise.__init__(self)
        self.Fulfilled = None
        self.Promises = promises
        for p in promises:
            p.addCallback(self)
            
    @synchronized
    def promiseComplete(self, promise, result):
        self.Fulfilled = promise
        return self.complete(promise.Result)
    
    @synchronized
    def wait(self, timeout = None):
        while self.Fulfilled is None:
            self.sleep(timeout)
        return sef.Result

    def __or__(self, other):
        if isinstance(other, ORPromise):
            return ORPromise(other.Promises+self.Promises)
        elif isinstance(other, (ANDPromise, Promise)):
            return ORPromise([other]+self.Promises)
        else:
            raise ValueError("Can not apply '|' operation to", type(self), "and", type(other))

    def __and__(self, other):
        if isinstance(other, ANDPromise):
            return ANDPromise(other.Promises + [self])
        else:
            return ANDPromise([self, other])

class ANDPromise(Promise):
    
    def __init__(self, promises):
        Promise.__init__(self)
        self.Promises = promises
        
    def wait(self, timeout=None):
        [p.wait(timeout) for p in self.Promises]
        return self.complete([p.Result for p in self.Promises])

    def __and__(self, other):
        if isinstance(other, ANDPromise):
            return ORPromise(other.Promises+self.Promises)
        elif isinstance(other, (ORPromise, Promise)):
            return ORPromise([other]+self.Promises)
        else:
            raise ValueError("Can not apply '&' operation to", type(self), "and", type(other))

    def __or__(self, other):
        if isinstance(other, ORPromise):
            return ORPromise(other.Promises + [self])
        else:
            return ORPromise([self, other])
