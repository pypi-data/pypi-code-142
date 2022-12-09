import json

from cloudpss.ieslab.DataManageModel import IESPlanDataManageModel
from cloudpss.ieslab.EvaluationModel import IESLabEvaluationModel
from cloudpss.ieslab.PlanModel import IESLabPlanModel
from cloudpss.runner.IESLabTypicalDayResult import IESLabTypicalDayResult
from ..utils import request
from ..model.model import Model
from cloudpss.runner.runner import  Runner

class IESLabPlan(object):
    def __init__(self, project={}):
        self.id = project.get('id', None)
        self.name = project.get('name', None)
        self.__modelRid = project.get('model', None)
        self.project_group = project.get('project_group', None)
        if self.__modelRid is not None:
            self.model = Model.fetch(self.__modelRid)
        self.dataManageModel = IESPlanDataManageModel(self.id)
        self.planModel = IESLabPlanModel(self.id)
        self.evaluationModel = IESLabEvaluationModel(self.id)

    @staticmethod
    def fetch(simulationId):
        try:
            r = request('GET',
                        'api/ieslab-plan/rest/simu/{0}/'.format(simulationId))
            project = json.loads(r.text)
            return IESLabPlan(project)
        except:
            raise Exception('未查询到当前算例')

    def __run(self, job=None, name=None):
        if job is None:
            currentJob = self.model.context['currentJob']
            job = self.model.jobs[currentJob]

        job['args']['simulationId'] = self.id
        return self.model.run(job, name=name)

    def iesLabTypicalDayRun(self, job=None, name=None, **kwargs)->Runner[IESLabTypicalDayResult]:

        if job is None:
            currentJob = self.model.context['currentJob']
            job = self.model.jobs[currentJob]
            if job['rid'] != 'job-definition/ies/ies-gmm':
                for j in self.model.jobs:
                    if j['rid'] == 'job-definition/ies/ies-gmm':
                        job = j
        if job is None:
            raise Exception("找不到默认的综合能源系统规划典型日生成算法的计算方案")
        if job['rid'] != 'job-definition/ies/ies-gmm':
            raise Exception("不是综合能源系统规划典型日生成算法的计算方案")
        return self.__run(job=job, name=name)

    def iesLabEvaluationRun(self, planId):
        return self.evaluationModel.run(planId)

    def iesLabEnergyEvaluationRun(self, planId):
        return self.evaluationModel.EnergyEvaluationRun(planId)

    def iesLabEnvironmentalEvaluationRun(self, planId):
        return self.evaluationModel.EnvironmentalEvaluationRun(planId)

    def iesLabPlanRun(self):
        return self.planModel.run()
