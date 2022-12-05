from threading import Thread
import math
def run_threads(thd: list[Thread]):
    for t in thd:
        t.start()
    for t in thd:
        t.join()

def get_intervals(lst,cof):
    div = math.ceil(len(lst)/cof)
    intervals = [[i*div,((i+1)*div) if i < cof-1 else len(lst)] for i in range(cof)]
    intervals = [i for i in intervals if i[1] <= len(lst)]
    if(intervals[-1][0] > intervals[-2][1]):
        intervals[-1][0] = intervals[-2][1]
    if(intervals[-1][0] == intervals[-1][1]):
        intervals.pop()
    intervals = [[lst[i[0]:i[1]]] for i in intervals]
    return intervals