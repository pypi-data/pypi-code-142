import os
from datetime import datetime
import math
from pymongo.database import Database


class Distributor(object):
    def __init__(self,
                 length,
                 db: Database):
        self.length = length
        self.db = db

    def next_job(self):
        raise NotImplementedError()

    def assign_job(self, job, user_id):
        if job["user_id"] is not None:
            raise RuntimeError("Can't assign already assigned job, please create new")
        if self.db.job.find_one({"user_id": user_id, "ended_at": None}) is not None:
            raise RuntimeError("Can't assign job for user, that already have a job")
        self.db.job.update_one({"_id": job["_id"]},
                               {"$set": {"user_id": user_id, "started_at": datetime.now()}},
                               upsert=False)

    def create_job(self,
                   indices):
        indices = list(indices)
        if not (0 <= min(indices) < max(indices) < self.length):
            raise RuntimeError("Bad job configuration")

        result = self.db.job.insert_one({
            "indices": indices,
            "created_at": datetime.now(),
            "started_at": None,
            "ended_at": None,
            "user_id": None,
            "submit_count": [0 for _ in range(len(indices))],
            "submit_at": [[] for _ in range(len(indices))]
        })
        return self.db.job.find_one({"_id": result.inserted_id})

    def get_job(self, user_id):
        job = self.db.job.find_one({"user_id": user_id, "ended_at": None})
        if job is None:
            job = self.next_job()
            if job is not None:
                self.assign_job(job, user_id)
        return job

    def finish_job(self, job):
        ended_at = datetime.now()
        self.db.job.update_one({"_id": job["_id"]},
                               {"$set": {"ended_at": ended_at}})

    def submit(self, job, obj_id):
        submit_at = datetime.now()
        if not (0 <= obj_id < len(job['indices'])):
            raise RuntimeError("obj id missing range")

        self.db.job.update_one({"_id": job["_id"]},
                               {"$inc": {f"submit_count.{obj_id}": 1},
                                "$push": {f"submit_at.{obj_id}": submit_at}},
                               upsert=False)

    def missing_index(self):
        created = set()
        for job in self.db.job.find():
            created.update(list(job['indices']))
        return sorted(list(set(range(self.length)).difference(created)))


class SimpleDistributor(Distributor):
    def __init__(self, length, db, n_per_batch):
        super(SimpleDistributor, self).__init__(length, db)
        self.n_per_batch = n_per_batch

    def next_job(self):
        indices = self.missing_index()[:self.n_per_batch]
        print("Indices:", indices)
        if len(indices) == 0:
            return None
        job = self.create_job(indices)
        print("Created job: ", job)
        return job
