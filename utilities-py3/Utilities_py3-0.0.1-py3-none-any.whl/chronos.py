from time import strftime, strptime, time
from datetime import datetime,time, timedelta
from timeit import timeit
def time_now():
    now = datetime.now()
    return now

def time_func(func):
    start = datetime.now()
    func()
    finish = datetime.now()
    dif = finish-start
    return dif