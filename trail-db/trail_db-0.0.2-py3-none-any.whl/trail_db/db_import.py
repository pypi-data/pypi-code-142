import pymongo
import os
import json
from mlflow.tracking import MlflowClient

class DB_import:
    def __init__(self, URI, database):
        URI = URI
        client = pymongo.MongoClient(URI)
        self.db = client[database]

    def JSON_to_db(self, data):
        self.db.experiments.insert_one(data)
        return(data)

    def MLflow_to_db(self, mlflowrun):
        tags = {k: v for k, v in mlflowrun.data.tags.items() if not k.startswith("mlflow.")}
        artifacts = [f.path for f in MlflowClient().list_artifacts(mlflowrun.info.run_id, "model")]
        d = {}
        d['run_id'] = mlflowrun.info.run_id
        d['artifacts'] = artifacts
        d['params'] = mlflowrun.data.params
        d['metrics'] = mlflowrun.data.metrics
        d['tags'] = tags

        #with open('data.json', 'w') as fp:
        #    json.dump(d, fp)
        DB_import.JSON_to_db(d)

    def get_run_info(self):
        pass