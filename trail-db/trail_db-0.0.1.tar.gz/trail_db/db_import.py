import pymongo
import os
import json

class DB_import:
    def __init__(self, URI, database):
        URI = URI
        client = pymongo.MongoClient(URI)
        self.db = client[database]

    def add_db(self, data):
        self.db.experiments.insert_one(data)
        return(data)
    #add_experiment_to_db("Test2", 456)