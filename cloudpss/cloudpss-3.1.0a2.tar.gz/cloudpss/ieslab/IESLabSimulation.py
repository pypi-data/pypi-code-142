import json
from ..utils import request
from ..model.model import Model
from .DataManageModel import IESSimulationDataManageModel


class IESLabSimulation(object):
    def __init__(self, project={}):
        self.id = project.get('id', None)
        self.name = project.get('name', None)
        self.__modelRid = project.get('model', None)
        self.project_group = project.get('project_group', None)
        if self.__modelRid is not None:
            self.model = Model.fetch(self.__modelRid)
        self.dataManageModel = IESSimulationDataManageModel(self.id)

    @staticmethod
    def fetch(simulationId):
        try:
            r = request(
                'GET', 'api/ieslab-simulation/rest/simu/{0}/'.format(simulationId))
            project = json.loads(r.text)
            return IESLabSimulation(project)
        except:
            raise Exception('未查询到当前算例')

    def run(self, job=None, name=None):
        if job is None:
            currentJob = self.model.context['currentJob']
            job = self.model.jobs[currentJob]

        job['args']['simulationId'] = self.id
        return self.model.run(job, name=name)

