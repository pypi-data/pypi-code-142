from google.cloud.workflows.executions_v1beta.services.executions import ExecutionsClient

SYNCHRONIZER_NAME = "synchronizer_workflow"
DASHBORD_ORCH_NAME = "dashboard_orch"


class Client(ExecutionsClient):
    def __init__(self, credentials=None):
        super().__init__(credentials=credentials)


