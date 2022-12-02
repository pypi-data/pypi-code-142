import json
import os
import uuid
import requests

from quantagonia.cloud.specs_enums import *
from quantagonia.enums import HybridSolverServers
from quantagonia.errors import SolverError


class SpecsHTTPSClient():
    """ client class for qqvm server """
    def __init__(self, api_key: str, target_server: HybridSolverServers = HybridSolverServers.PROD) -> None:
        """ """
        self.api_key = api_key
        self.server = target_server.value

    def _jsonArrayToPythonArray(self, arr : dict) -> list:

        res = []
        ix = 0

        while str(ix) in arr.keys():
            res.append(arr[str(ix)])
            ix += 1

        return res

    def _submitJob(self, problem_files: list, specs: list) -> uuid:

        # build a single JSON array with specs
        spec_arr = {}
        for ix in range(0, len(specs)):
            spec_arr[str(ix)] = specs[ix]

        files = [("files", (os.path.basename(prob), open(prob, "rb"))) for prob in problem_files]
        response = requests.post(self.server + SpecsEndpoints.submitjob, files=files, data=[("specs", json.dumps(spec_arr))], headers={"X-api-key" : self.api_key})

        # close all file handles
        for f in files:
            f[1][1].close()

        if not response.ok:
            error_report = response.json()
            raise RuntimeError(error_report)
        return response.json()['jobid']

    def _checkJob(self, jobid: uuid) -> str:
        params = {'jobid': str(jobid)}
        response = requests.get(self.server + SpecsEndpoints.checkjob, params=params, headers={"X-api-key": self.api_key})
        if response.ok:
            return response.json()['status']
        elif response.status_code > 499:
            log = self._getCurrentLog(jobid)
            error_report = response.json()
            error_report["details"] = log[0]
            raise SolverError(error_report)
        elif response.status_code < 499:
            error_report = response.json()
            raise RuntimeError(error_report)

    def _getCurrentStatus(self, jobid: uuid) -> str:
        params = {'jobid': str(jobid)}
        response = requests.get(self.server + SpecsEndpoints.getcurstatus, params=params, headers={"X-api-key" : self.api_key})

        return self._jsonArrayToPythonArray(json.loads(response.text))

    def _getCurrentSolution(self, jobid: uuid) -> str:
        params = {'jobid': str(jobid)}
        response = requests.get(self.server + SpecsEndpoints.getcursolution, params=params, headers={"X-api-key" : self.api_key})

        return self._jsonArrayToPythonArray(json.loads(response.text))

    def _getCurrentLog(self, jobid: uuid) -> str:
        params = {'jobid': str(jobid)}
        response = requests.get(self.server + SpecsEndpoints.getcurlog, params=params, headers={"X-api-key" : self.api_key})
        if not response.ok:
            error_report = response.json()
            raise RuntimeError(error_report)
        return self._jsonArrayToPythonArray(json.loads(response.text))

    def _getResults(self, jobid: uuid) -> dict:
        params = {'jobid': str(jobid)}
        response = requests.get(self.server + SpecsEndpoints.getresults, params=params, headers={"X-api-key" : self.api_key})
        
        if not response.ok:
            error_report = response.json()
            raise RuntimeError(error_report)

        return self._jsonArrayToPythonArray(json.loads(response.text))

    def _interruptJob(self, jobid: uuid):
        response = requests.delete(self.server + SpecsEndpoints.interruptjob + "/" + str(jobid),
                                headers={"X-api-key": self.api_key})

        if not response.ok:
            error_report = response.json()
            raise RuntimeError(error_report)

        return response.json()

    ### blocking interface
    def submitJob(self, problem_files: list, specs: list) -> uuid:
        return self._submitJob(problem_files, specs)

    def checkJob(self, jobid: uuid) -> str:
        return self._checkJob(jobid)

    def getCurrentStatus(self, jobid: uuid) -> str:
        return self._getCurrentStatus(jobid)

    def getCurrentSolution(self, jobid: uuid) -> str:
        return self._getCurrentSolution(jobid)

    def getCurrentLog(self, jobid: uuid) -> str:
        return self._getCurrentLog(jobid)

    def getResults(self, jobid: uuid) -> dict:
        return self._getResults(jobid)

    def interruptJob(self, jobid: uuid) -> dict:
        return self._interruptJob(jobid)

    ### non-blocking interface
    async def submitJobAsync(self, problem_files: list, specs: list) -> uuid:
        return self._submitJob(problem_files, specs)

    async def checkJobAsync(self, jobid: uuid) -> str:
        return self._checkJob(jobid)

    async def getCurrentStatusAsync(self, jobid: uuid) -> str:
        return self._getCurrentStatus(jobid)

    async def getCurrentSolutionAsync(self, jobid: uuid) -> str:
        return self._getCurrentSolution(jobid)

    async def getCurrentLogAsync(self, jobid: uuid) -> str:
        return self._getCurrentLog(jobid)

    async def getResultsAsync(self, jobid: uuid) -> dict:
        return self._getResults(jobid)

    async def interruptJobAsync(self, jobid: uuid) -> dict:
        return self._interrupt_job(jobid)
