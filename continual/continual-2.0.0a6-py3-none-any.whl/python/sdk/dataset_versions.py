from __future__ import annotations
from typing import List, Optional, Union
from continual.python.sdk.batchpredictions import (
    BatchPredictionManager,
)
from continual.python.sdk.data_checks import DataCheck, DataChecksManager
from continual.python.sdk.data_profiles import DataProfilesManager
from continual.python.sdk.metrics import MetricsManager, Metric
from continual.rpc.management.v1 import management_pb2, management_types_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.events import EventManager
from continual.python.sdk.artifacts import ArtifactsManager
from continual.python.sdk.tags import TagsManager
from continual.python.sdk.metadata import MetadataManager
from continual.python.sdk.dataset_version_assignments import (
    DatasetVersionAssignmentManager,
)
from google.protobuf.json_format import ParseDict


class DatasetVersionManager(Manager):
    """Manages Dataset Version resources."""

    name_pattern: str = "projects/{project}/datasets/{dataset}/versions/{version}"

    def create(self) -> DatasetVersion:
        """Create a dataset version for local development

        Returns
            A Dataset Version.
        """
        req = management_pb2.CreateDatasetVersionRequest(
            parent=self.parent, run_name=self.run_name
        )
        resp = self.client._management.CreateDatasetVersion(req)
        return DatasetVersion.from_proto(resp, client=self.client)

    def get(self, id: str) -> DatasetVersion:
        """Get dataset version.

        Arguments:
            id: Dataset name or id.

        Returns
            An Dataset Version.
        """
        req = management_pb2.GetDatasetVersionRequest(name=self.name(id))
        resp = self.client._management.GetDatasetVersion(req)
        return DatasetVersion.from_proto(resp, client=self.client)

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
        all_projects: bool = False,
    ) -> List[DatasetVersion]:
        """List dataset versions.

        Arguments:
            page_size: Number of items to return.

            filter: List of filters to apply to batch prediction job. Can be:
            - state  (i.e. state:FAILED)

        Returns:
            A list of dataset versions.
        """
        req = management_pb2.ListDatasetVersionsRequest(
            parent=self.parent,
            page_size=page_size,
            filters=filters,
            all_projects=all_projects,
        )
        resp = self.client._management.ListDatasetVersions(req)
        return [
            DatasetVersion.from_proto(x, client=self.client)
            for x in resp.dataset_versions
        ]

    def list_all(self) -> Pager[DatasetVersion]:
        """List all dataset versions.

        Pages through all dataset versions using an iterator.

        Returns:
            A iterator of all dataset versions.
        """

        def next_page(next_page_token):
            req = management_pb2.ListDatasetVersionsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListDatasetVersions(req)
            return (
                [
                    DatasetVersion.from_proto(x, client=self.client)
                    for x in resp.dataset_versions
                ],
                resp.next_page_token,
            )

        return Pager(next_page)


class DatasetVersion(Resource, types.DatasetVersion):
    """Dataset version resource."""

    name_pattern: str = "projects/{project}/datasets/{dataset}/versions/{version}"
    manager: DatasetVersionManager

    data_checks: DataChecksManager
    """Data Checks Manager"""

    data_profiles: DataProfilesManager
    """Data Profiles Manager"""

    assignments: DatasetVersionAssignmentManager
    """Dataset Version Assignment Manager"""

    metrics: MetricsManager
    """Metrics Manager"""

    events: EventManager
    """Event manager."""

    artifacts: ArtifactsManager
    """Artifacts Manager"""

    tags: TagsManager
    """Tags Manager"""

    metadata: MetadataManager
    """Metadata Manager"""

    def _init(self):
        self.manager = DatasetVersionManager(
            parent=self.parent, client=self.client, run_name=self.run_name
        )
        self.events = EventManager(parent=self.name, client=self.client)

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
        self.batch_predictions = BatchPredictionManager(
            parent=self.parent, client=self.client, run_name=self.run_name
        )
        self.metrics = MetricsManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )
        self.assignments = DatasetVersionAssignmentManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )

    def create_data_checks(self, data_checks: List[Union[DataCheck, dict]]):
        """Logs data checks from a list of dictionaries"""
        for data_check in data_checks:
            self.create_data_check(data_check=data_check)

    def create_data_check(self, data_check: Union[DataCheck, dict]):
        """Logs data check"""
        if isinstance(data_check, dict):
            data_check["run_name"] = self.run_name
            self.data_checks.create(DataCheck(**data_check))
        elif isinstance(data_check, DataCheck):
            self.create_data_check(data_check=data_check.to_dict())

    def list_data_checks(
        self, page_size: Optional[int] = None, filters: List[str] = None
    ) -> List[DataCheck]:
        """List data checks added to this model version

        Arguments:
            page_size: Number of items to return.
            filters: filters on metrics

        Returns:
            A list of datachecks.
        """
        return self.data_checks.list(page_size=page_size, filters=filters)

    def create_data_profile(self, stats_entries: List[dict]):
        """Create and log data profile from a list of dataset stats entry"""
        self.data_profiles.create(
            types.DataProfile(dataset_stats=stats_entries, resource_name=self.name)
        )

    def create_data_profile_from_dict(self, data_profile_dict: dict):
        """
        Construct and log a DataProfile from a dict or JSON dict
        """
        self.create_data_profile(
            types.DataProfile.from_proto(
                ParseDict(data_profile_dict, management_types_pb2.DataProfile())
            )
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
