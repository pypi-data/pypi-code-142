from __future__ import annotations
from typing import List, Optional, Iterator, Union
from continual.python.sdk.metrics import Metric, MetricsManager

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.events import EventManager
from continual.python.sdk.artifacts import ArtifactsManager
from continual.python.sdk.tags import TagsManager
from continual.python.sdk.metadata import MetadataManager

import requests


class BatchPredictionManager(Manager):
    """Manages Batch Prediction resources."""

    name_pattern: str = (
        "projects/{project}/models/{model}/batchPredictions/{batch_prediction_job}"
    )

    def create(self, model_version_name: str) -> BatchPrediction:
        """Get batch prediction job.

        Arguments:
            model_version_name: Name of the model version to use for prediction

        Returns
            A Batch prediction .
        """
        req = management_pb2.CreateBatchPredictionRequest(
            parent=self.parent,
            run_name=self.run_name,
            trained_model_version_name=model_version_name,
        )
        resp = self.client._management.CreateBatchPrediction(req)
        return BatchPrediction.from_proto(resp, client=self.client)

    def get(self, id: str) -> BatchPrediction:
        """Get batch prediction job.

        Arguments:
            id: Batch Prediction  name or id.

        Returns
            A Batch prediction .
        """
        req = management_pb2.BatchPredictionRequest(name=self.name(id))
        resp = self.client._management.GetBatchPrediction(req)
        return BatchPrediction.from_proto(resp, client=self.client)

    def get_batch_prediction_config(self, batch_prediction_name: str):
        req = management_pb2.GetBatchPredictionJobConfigRequest(
            batch_prediction_name=batch_prediction_name
        )
        resp = self.client._management.GetBatchPredictionJobConfig(req)

        return types.BatchPredictionJobConfig.from_proto(resp, client=self.client)

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
        all_projects: bool = False,
    ) -> List[BatchPrediction]:
        """List batch prediction jobs.

        Arguments:
            page_size: Number of items to return.

            filter: List of filters to apply to batch prediction job. Can be:
            - state  (i.e. state:FAILED)
            - incremental (i.e. incremental:True)
            - dest type (i.e. dest_type:STORE)

        Returns:
            A list of batch prediction jobs.
        """
        req = management_pb2.ListBatchPredictionsRequest(
            parent=self.parent,
            page_size=page_size,
            filters=filters,
            all_projects=all_projects,
        )
        resp = self.client._management.ListBatchPredictions(req)
        return [
            BatchPrediction.from_proto(u, client=self.client)
            for u in resp.batch_predictions
        ]

    def list_all(self) -> Iterator[BatchPrediction]:
        """List all batch prediction jobs.

        Pages through all batch prediction jobs using an iterator.

        Returns:
            A iterator of all batch prediction jobs.
        """

        def next_page(next_page_token):
            req = management_pb2.ListBatchPredictionsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListBatchPredictions(req)
            return (
                [
                    BatchPrediction.from_proto(u, client=self.client)
                    for u in resp.batch_predictions
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def cancel(self, id: str) -> None:
        """Cancel a Batch Prediction.

        Arugments:
            id: Name or id of Batch Predictin

        """
        req = management_pb2.BatchPredictionRequest(name=self.name(id))
        self.client._management.CancelBatchPrediction(req)

    def download(self, id: str, file: str) -> None:
        """Download csv file created by batch prediction.

        Arguments:
            id: Batch Prediction  name or id.
            file: the path to a file, relative to the current working directory or absolute

        """
        batch_prediction_job = self.get(id)
        with requests.get(
            batch_prediction_job.csv_file_path, allow_redirects=True
        ) as fd:
            open(file, "xb").write(fd.content)
        return


class BatchPrediction(Resource, types.BatchPrediction):
    """BatchPrediction resource."""

    name_pattern: str = (
        "projects/{project}/models/{model}/batchPredictions/{batch_prediction_job}"
    )
    manager: BatchPredictionManager

    events: EventManager
    """Event manager."""

    metrics: MetricsManager
    """Metrics Manager"""

    artifacts: ArtifactsManager
    """Artifacts Manager"""

    tags: TagsManager
    """Tags Manager"""

    metadata: MetadataManager
    """Metadata Manager"""

    def _init(self):
        self.manager = BatchPredictionManager(parent=self.parent, client=self.client)
        self.events = EventManager(parent=self.name, client=self.client)
        self.artifacts = ArtifactsManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )
        self.tags = TagsManager(parent=self.name, client=self.client)
        self.metadata = MetadataManager(parent=self.name, client=self.client)
        self.metrics = MetricsManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )

    def create_metrics(self, metrics: List[Union[Metric, dict]]):
        """Logs metrics from a list of dictionaries"""
        for metric in metrics:
            self.create_metric(metric=metric)

    def create_metric(self, metric: Union[Metric, dict]):
        """Logs metric"""
        if isinstance(metric, dict):
            metric["run_name"] = self.run_name
            if isinstance(metric["value"], int):
                metric["value"] = float(metric["value"])
            self.metrics.create(Metric(**metric))
        elif isinstance(metric, Metric):
            self.create_metric(metric=metric.to_dict())

    def list_metrics(
        self, page_size: Optional[int] = None, filters: List[str] = None
    ) -> List[Metric]:
        """List metrics added to this model version

        Arguments:
            page_size: Number of items to return.
            filters: filters on metrics

        Returns:
            A list of metrics.
        """
        return self.metrics.list(page_size=page_size, filters=filters)
