# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Access base run artifacts client"""
import logging
import os

from azureml.mlflow._common.async_utils.task_queue import TaskQueue

module_logger = logging.getLogger(__name__)

ARTIFACTS_BATCH_SIZE = os.environ.get("AZUREML_ARTIFACT_BATCH_SIZE", 50)
AZUREML_ARTIFACTS_TIMEOUT_ENV_VAR = "AZUREML_ARTIFACTS_DEFAULT_TIMEOUT"
AZUREML_ARTIFACTS_MIN_TIMEOUT = 300


class BaseArtifactsClient(object):

    def _upload_files(self, local_paths, remote_paths):
        batch_size = ARTIFACTS_BATCH_SIZE
        results = []
        timeout_seconds = int(
            os.environ.get(AZUREML_ARTIFACTS_TIMEOUT_ENV_VAR, AZUREML_ARTIFACTS_MIN_TIMEOUT))

        for i in range(0, len(local_paths), batch_size):
            with TaskQueue(_ident="upload_files", flush_timeout_seconds=timeout_seconds) as task_queue:
                batch_local_paths = local_paths[i:i + batch_size]
                batch_remote_paths = remote_paths[i:i + batch_size]

                for local_path, remote_path in zip(batch_local_paths, batch_remote_paths):
                    task = task_queue.add(self.upload_artifact, local_path, remote_path)
                    results.append(task)

        return map(lambda result: result.wait(), results)
