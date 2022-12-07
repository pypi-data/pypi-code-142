from qiskit.providers import JobV1 as Job
from qiskit.providers.jobstatus import JobStatus


class SyncJob(Job):
    _async = False

    def __init__(self, backend, job_id, result):
        super().__init__(backend, job_id)
        self._result = result

    def submit(self):
        pass

    def result(self):
        return self._result

    def status(self):
        return JobStatus.DONE
