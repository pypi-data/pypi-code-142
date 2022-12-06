import json
import os
import threading
import time
from copy import copy, deepcopy
from threading import BoundedSemaphore, Thread
from typing import Callable, Optional, Type

from pyrhd.utility.cprint import aprint, deleteLines, printInfo
from pyrhd.utility.utils import Utils

SAVING_INTERVAL = 10
CN = 105  # [i] normal-text -> purple-magenta
CC = (78, 201, 176)  # Class name -> Greenish (vscode-clr)
CU = "magenta"  # URL -> magenta
CA = 99  # contrast of CB -> light magenta
CB = 201  # contrast of CA -> pink
CT = (167, 206, 155)  # time, numbers -> light green (vscode-clr)

CS = (22, 198, 12)  # success -> green
CW = (252, 225, 0)  # warning -> yellow
CE = "red"  # error -> red

TMP_I = ["i", CB, CA]
TMP_E = ["!", CA, "red"]


class BaseHarvester:
    def __init__(
        self, ultimatum_path, saving_interval: int = None, default_ultimatum: dict = {}
    ) -> None:
        self.ultimatum_path = ultimatum_path
        # custom saving interval if given, else defaults to global variable SAVING_INTERVAL
        self.save_int = saving_interval or SAVING_INTERVAL
        self.ultimatum = {}
        self.save_flag = True
        self.getFileData(default_ultimatum)
        self.life_saver_thr = Thread(target=self.lifeSaver, daemon=True)
        self.life_saver_thr.start()

    def getFileData(self, default_ultimatum):
        aprint("[BaseHarvester]", "cyan", "Reading cached ultimatum.json", "magenta")
        try:
            if os.path.exists(self.ultimatum_path):
                with open(self.ultimatum_path, "r") as f:
                    buffer = f.read()
                    for i in range(3):
                        last = "}" * i
                        try:
                            content = buffer + last
                            self.ultimatum = json.loads(content)
                            break
                        except:
                            ...
            else:
                raise Exception
        except:
            p = os.path.dirname(self.ultimatum_path)
            os.makedirs(p, exist_ok=True)
        if self.ultimatum == {}:
            self.ultimatum = default_ultimatum
        self.saveUltimatum()
        deleteLines()

    def saveUltimatum(self):
        try:
            with open(self.ultimatum_path, "w") as f:
                # use copy() to avoid "RuntimeError: dictionary changed size during iteration"
                json.dump(self.ultimatum, f, indent=4)
                return True
        except Exception as e:
            aprint(f"[BaseHarvester.saveUltimatum] {e}", "red")
            # if there are any errors in saving the json file, then save the str format
            with open(
                self.ultimatum_path.replace(".json", "_str.txt"), "w", encoding="utf-8"
            ) as f:
                f.write(str(self.ultimatum))
            return False

    def lifeSaver(self):
        while self.save_flag:
            self.saveUltimatum()
            time.sleep(self.save_int)

    def quitSaver(self):
        try:
            self.save_flag = False
            for tries in range(1, 6):
                aprint(
                    f"[BaseHarvester] (try:{tries})",
                    "cyan",
                    "Final save of ultimatum.json",
                    "magenta",
                )
                if self.saveUltimatum():
                    break
                time.sleep(3)
        except KeyboardInterrupt:
            self.quitSaver()


def hello_harvester(globals):
    def decorator(harvest):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            aprint("\n>>>", CA, "Harvester\n", CB)
            msg = ["Harvester", CC, "for", CN, globals["ROOT_URL"], CU]
            printInfo(*TMP_I, *msg, "has been instantiated", CN)
            harvest(*args, **kwargs)
            aprint("\n>>>", CA, "Harvester-End\n", CB)
            tmp_s = ["Time taken for", CN, "Harvester", CC, "class to complete is", CN]
            time_taken = round(time.time() - start_time, 6)
            printInfo(*TMP_I, *tmp_s, time_taken, CT, "seconds", CN)
            # globals["Harvester"].quitSaver()

        return wrapper

    return decorator


def iter_harvester(iter_cls, unit_cls, ultimatum: dict, sema4_count: int):
    unit_name = unit_cls.__name__
    thr: list[Thread] = []
    sema4 = BoundedSemaphore(sema4_count)
    try:
        iterator = iter_cls()
    except:
        iterator = iter_cls(ultimatum)
    index = 0
    for items in iterator:
        index, *items = items
        sema4.acquire()
        unit_args = [*items, ultimatum, sema4]
        Utils.threading.createThread(unit_cls, unit_args, thr)

        msg = [f"{{threads#={threading.active_count()}}} ", "cyan"]
        msg += [unit_name, CC, f" : Processed ", CN]
        msg += [index, CT, " out of ", CN, iterator.total, CT]
        printInfo(*TMP_I, *msg, same_line=True, sep="")
    msg = [f"Processing recently spawned of ", CN, index, CT, f" {unit_name}", CC]
    printInfo(*TMP_I, *msg, same_line=True, sep="")

    Utils.threading.joinThreads(thr)  # Waiting the threads to terminate

    tmp_s = [f"Harvesting of ", CN, index, CT, f" {unit_name} "]
    tmp_s += [CC, "is done :)", CN]
    printInfo(*TMP_I, *tmp_s, sep="")
