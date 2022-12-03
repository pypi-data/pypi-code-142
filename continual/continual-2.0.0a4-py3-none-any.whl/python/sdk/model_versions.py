from __future__ import annotations
import numpy as np
from sklearn.metrics import confusion_matrix

from typing import List, Optional, Union
from continual.python.sdk.batchpredictions import (
    BatchPrediction,
    BatchPredictionManager,
)
from continual.python.sdk.data_checks import DataChecksManager
from continual.python.sdk.data_profiles import DataProfilesManager
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.experiments import ExperimentManager
from continual.python.sdk.promotions import Promotion, PromotionManager
from continual.python.sdk.events import EventManager
from continual.python.sdk.metrics import MetricsManager, Metric
from continual.python.sdk.artifacts import ArtifactsManager
from continual.python.sdk.tags import TagsManager
from continual.python.sdk.metadata import MetadataManager


class ModelVersionManager(Manager):
    """Manages Model Version resources."""

    name_pattern: str = "projects/{project}/models/{model}/versions/{version}"

    def create(self) -> ModelVersion:
        """Create a model version for local development

        Returns
            A Model Version.
        """
        req = management_pb2.CreateModelVersionRequest(
            parent=self.parent, run_name=self.run_name
        )
        resp = self.client._management.CreateModelVersion(req)
        return ModelVersion.from_proto(resp, client=self.client)

    def get(self, id: str) -> ModelVersion:
        """Get model version.

        Arguments:
            id: Model name or id.

        Returns
            An Model Version.
        """
        req = management_pb2.GetModelVersionRequest(name=self.name(id))
        resp = self.client._management.GetModelVersion(req)
        return ModelVersion.from_proto(resp, client=self.client)

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
        all_projects: bool = False,
    ) -> List[ModelVersion]:
        """List model versions.

        Arguments:
            page_size: Number of items to return.

            filter: List of filters to apply to batch prediction job. Can be:
            - state  (i.e. state:FAILED)

        Returns:
            A list of model versions.
        """
        req = management_pb2.ListModelVersionsRequest(
            parent=self.parent,
            page_size=page_size,
            filters=filters,
            all_projects=all_projects,
        )
        resp = self.client._management.ListModelVersions(req)
        return [
            ModelVersion.from_proto(x, client=self.client) for x in resp.model_versions
        ]

    def list_all(self) -> Pager[ModelVersion]:
        """List all model versions.

        Pages through all model versions using an iterator.

        Returns:
            A iterator of all model versions.
        """

        def next_page(next_page_token):
            req = management_pb2.ListModelVersionsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListModelVersions(req)
            return (
                [
                    ModelVersion.from_proto(x, client=self.client)
                    for x in resp.model_versions
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def cancel(self, id: str) -> None:
        """Cancel model training run."""
        req = management_pb2.CancelTrainingRequest(name=self.name(id))
        self.client._management.CancelTraining(req)


class ModelVersion(Resource, types.ModelVersion):
    """Model version resource."""

    name_pattern: str = "projects/{project}/models/{model}/versions/{version}"
    manager: ModelVersionManager

    experiments: ExperimentManager
    """Experiment manager."""

    promotions: PromotionManager
    """Promotion manager."""

    batch_predictions: BatchPredictionManager
    """Batch Prediction  manager."""

    metrics: MetricsManager
    """Metrics Manager"""

    data_checks: DataChecksManager
    """Data Checks Manager"""

    data_profiles: DataProfilesManager
    """Data Profiles Manager"""

    events: EventManager
    """Event manager."""

    artifacts: ArtifactsManager
    """Artifacts Manager"""

    tags: TagsManager
    """Tags Manager"""

    metadata: MetadataManager
    """Metadata Manager"""

    def _init(self):
        self.manager = ModelVersionManager(
            parent=self.parent, client=self.client, run_name=self.run_name
        )
        self.promotions = PromotionManager(
            parent=self.parent, client=self.client, run_name=self.run_name
        )
        self.batch_predictions = BatchPredictionManager(
            parent=self.parent, client=self.client, run_name=self.run_name
        )
        self.experiments = ExperimentManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )
        self.events = EventManager(parent=self.name, client=self.client)
        self.metrics = MetricsManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )
        self.artifacts = ArtifactsManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )
        self.tags = TagsManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )
        self.metadata = MetadataManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )
        self.data_checks = DataChecksManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )
        self.data_profiles = DataProfilesManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )

    def create_batch_prediction(self) -> BatchPrediction:
        """Creates a batchprediciton using the current model version

        Returns:
            A new batch prediction.
        """
        return self.batch_predictions.create(model_version_name=self.name)

    def create_promotion(self, reason: str) -> Promotion:
        """Promote current model version.

        Arguments:
            reason : string reason for promotion

        Returns:
            A new promotion.
        """
        return self.promotions.create(
            model_version_name=self.name,
            reason=reason,
        )

    def log(self, items: dict):
        """Logs to fields in model version"""
        raise NotImplementedError

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

    def create_sklearn_confusion_matrix(
        self,
        display_name: str,
        group_name: str,
        y_true: list,
        y_pred: list,
        labels: None,
        sample_weight=None,
        normalize=None,
    ):
        """
        Creates confusion matrix metadata on this model version

        Arguments:
            display_name: The display name of the confusion matrix
            matrix: np.nadarray of example counts
            group_name: A label associated with the group of the confusion matrix

        Return:
            Metadata
                Type confusion matrix
        """
        matrix = confusion_matrix(
            y_true=y_true,
            y_pred=y_pred,
            labels=labels,
            sample_weight=sample_weight,
            normalize=normalize,
        )
        return self.metadata.create(
            type="CONFUSION_MATRIX",
            data=dict(display_name=display_name, rows=matrix.astype(np.uint).tolist()),
            group_name=group_name,
        )
