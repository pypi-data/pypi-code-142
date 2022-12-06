import copy
import hashlib
import os
import time
from threading import Thread

from pyrhd.utility.cprint import aprint
from pyrhd.utility.utils import Utils


class Dupy:
    def __init__(self, root_path) -> None:
        self.root_path = root_path
        self.dups = []
        self.hm = {}
        self.saverthread = Thread(target=self.saveDeamon)
        self.saveflag = True
        self.saverthread.start()

        self.main()
        self.saveflag = False
        self.saverthread.join()
        cache_path = os.path.join(self.root_path, "dupy.json")
        Utils.json.saveDict(copy.deepcopy(self.hm), cache_path)

    def getHash(self, file_path, first_chunk_only=True) -> str:
        with open(file_path, "rb") as f:
            file_data = f.read(1024 if first_chunk_only else None)
            hashed = hashlib.sha1(file_data).digest().hex()
        return hashed

    def main(self):
        self.hm = dict()
        # size based hashmap
        tot_len = 0
        for i in Utils.os.getAllFiles(self.root_path):
            if i.endswith(".part"):
                continue
            try:
                file_size = os.path.getsize(i)
            except:
                continue
            self.hm[file_size] = self.hm.get(file_size, {0: [], 1: {}, 2: {}})
            self.hm[file_size][0].append(i)
            tot_len += 1
        aprint("0. Collisions based on size:", "cyan", tot_len - len(self.hm), "green")

        # first 1024 bytes based hashmap
        for i, j in ((i, j) for (i, j) in self.hm.items() if len(j[0]) > 1):
            for file_path in j[0]:
                try:
                    hashed = self.getHash(file_path)
                except:
                    continue
                self.hm[i][1][hashed] = self.hm[i][1].get(hashed, [])
                self.hm[i][1][hashed].append(file_path)
        tmp = sum(len(j) - 1 for i1, i2 in self.hm.items() for j in i2[1].values())
        aprint("1. Collisions based on first 1024 bytes:", "cyan", tmp, "green")

        # full-file based hashmap
        for i, j in self.hm.items():
            for a, b in j[1].items():
                if len(b) > 1:
                    for file_path in b:
                        hashed = self.getHash(file_path, False)
                        self.hm[i][2][hashed] = self.hm[i][2].get(hashed, [])
                        self.hm[i][2][hashed].append(file_path)
        tmp = sum(
            max(len(j) - 1, 0) for i1, i2 in self.hm.items() for j in i2[2].values()
        )
        aprint("2. Collisions based on entire file:", "cyan", tmp, "green")

        # analysis
        count = 0
        for size, size_based in self.hm.items():
            for file, file_based in size_based[2].items():
                count += 1
                if len(file_based) > 1:
                    self.dups.append(file_based)

    def saveDeamon(self):
        cache_path = os.path.join(self.root_path, "dupy.json")
        while self.saveflag:
            try:
                Utils.json.saveDict(copy.deepcopy(self.hm), cache_path)
            except:
                ...
            time.sleep(5)

    def getDups(self):
        return self.dups
