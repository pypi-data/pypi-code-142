import copy
import os
from pathlib import Path
from pprint import pprint
import numpy as np

import pandas as pd
from pymongo import MongoClient
from pymongo.database import Database
from ..cache import try_int
from ..fields.grid import Stack, VStack, HStack
from ..fields.inputs.hidden import InputHiddenField
from ..fields.inputs.text import InputTextField
from ..fields.outputs.json import OutputJSONField
from ..fields.outputs.table import OutputTableField
from ..fields.redirect import SubmitButton
from ..web import Web
from ..page import Page


class LoginPage(Page):
    def __init__(self, db):
        super(LoginPage, self).__init__()
        self.fields = VStack([
            InputTextField("user_id")
        ])
        self.db = db

    def get_content(self, **kwargs):
        return self.fields.generate()

    def process(self, **data):
        user_id = data['user_id']
        return "/job?user_id=%s&obj_id=0" % user_id


class JobStatusPage(Page):
    def __init__(self, distributor):
        super(JobStatusPage, self).__init__()
        self.error_fields = OutputJSONField("Error")
        self.distributor = distributor

        self.fields = HStack([
            OutputTableField("job"),
            OutputJSONField("progress")
        ])

    def get_content(self, **kwargs):
        user_id = kwargs.get('user_id')
        if user_id is None:
            error_fields = copy.deepcopy(self.error_fields)
            error_fields.set_output({"Error": "Login to setup user_id"})
            return error_fields.generate()

        job = self.distributor.get_job(user_id)
        length = len(job['indices'])
        df = pd.DataFrame({"indices": list(range(length)),
                           "submit_count": list(job['submit_count'])},
                          dtype=np.int64)
        return self.fill(self.fields, {
            "job": df,
            "progress": f"{100 * sum([1 for c in job['submit_count'] if c > 0]) / length} %"
        })

    def process(self, **data):
        if "user_id" not in data:
            return "/login"
        user_id = data['user_id']
        return f'/job/status?user_id={user_id}'


class JobPage(Page):
    def __init__(self,
                 fields,
                 db: Database,
                 dataset,
                 saver,
                 distributor,
                 hook=lambda a, b: None):
        super(JobPage, self).__init__()
        self.fields = VStack([
            HStack([
                SubmitButton("Prev", url=None),
                SubmitButton("Next", url=None),
                SubmitButton("JobStatus", url=None)
            ]),
            fields,
            InputHiddenField("user_id", None),
            InputHiddenField("obj_id", None),
        ])

        self.error_fields = OutputJSONField("Error")

        self.db = db
        self.distributor = distributor
        self.dataset = dataset
        self.saver = saver
        self.hook = hook

        pprint(list(self.db.job.find()))

    def get_content(self, **kwargs):
        user_id = kwargs.get('user_id')
        obj_id = try_int(kwargs.get('obj_id', 0), 0)
        if user_id is None:
            error_fields = copy.deepcopy(self.error_fields)
            error_fields.set_output({"Error": "Login to setup user_id"})
            return error_fields.generate()
        fields = copy.deepcopy(self.fields)
        fields["user_id"].set_output(user_id)
        fields["obj_id"].set_output(obj_id)
        job = self.distributor.get_job(user_id)
        print("Job: ", job)
        idx = job['indices'][obj_id]
        length = len(job['indices'])
        fields[0]["Prev"].set_output(f"/job?user_id={user_id}&obj_id={max(0, obj_id - 1)}")
        fields[0]["Next"].set_output(f"/job?user_id={user_id}&obj_id={min(length, obj_id + 1)}")
        fields[0]["JobStatus"].set_output(f"/job/status?user_id={user_id}")
        self.fill(fields[1], self.dataset[idx], inplace=True, generate=False,
                  hook=self.hook)
        return fields.generate()

    def process(self, **data):
        if "user_id" not in data:
            return "/login"
        data = self.parse(self.fields, data)
        user_id = data.pop('user_id')
        obj_id = int(data.pop('obj_id'))
        job = self.distributor.get_job(user_id)
        self.distributor.submit(job, obj_id)
        idx = job['indices'][obj_id]
        length = len(job['indices'])
        self.saver.save(idx, data)
        return f"/job?user_id={user_id}&obj_id={min(length, obj_id + 1)}"


class StatsPage(Page):
    def __init__(self):
        super(StatsPage, self).__init__()

    def get_content(self, **kwargs):
        user_id = kwargs.pop('user_id')

    def process(self, **data):
        pass


class Labelling(Web):
    def __init__(self,
                 name,
                 fields,
                 dataset,
                 saver,
                 distributor_fn,
                 db_name=None,
                 hook=lambda a, b: None):
        if db_name is None:
            db_name = name
        client = MongoClient()
        client.drop_database(db_name)
        db = client[db_name]
        self.dataset = dataset
        self.distributor = distributor_fn(db)
        self.fields = fields
        self.saver = saver

        super(Labelling, self).__init__({
            "stats": StatsPage(),
            "job": JobPage(db=db,
                           dataset=dataset,
                           distributor=self.distributor,
                           fields=fields,
                           saver=saver,
                           hook=hook),
            "login": LoginPage(db),
            "job/status": JobStatusPage(self.distributor)
        }, name=name)
