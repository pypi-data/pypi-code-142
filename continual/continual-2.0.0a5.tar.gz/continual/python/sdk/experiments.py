from __future__ import annotations
from typing import List, Optional, Union
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


class ExperimentManager(Manager):
    """Manages experiment resources."""

    name_pattern: str = (
        "projects/{project}/models/{model}/versions/{version}/experiments/{experiment}"
    )

    def create(self) -> Experiment:
        """Create experiment.

        Returns
            An experiment.
        """
        req = management_pb2.CreateExperimentRequest(
            parent=self.parent, run_name=self.run_name
        )
        resp = self.client._management.CreateExperiment(req)
        return Experiment.from_proto(resp, client=self.client)

    def get(self, id: str) -> Experiment:
        """Get experiment.

        Arguments:
            id: Experiment name or id.

        Returns
            An experiment.
        """
        req = management_pb2.GetExperimentRequest(name=self.name(id))
        resp = self.client._management.GetExperiment(req)
        return Experiment.from_proto(resp, client=self.client)

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
        all_projects=False,
    ) -> List[Experiment]:
        """List experiments.

        Arguments:
            page_size: Number of items to return.

            filters: List of filters to apply to experiment. Can be:
            - state  (i.e. state:FAILED)


        Returns:
            A list of experiments.
        """
        req = management_pb2.ListExperimentsRequest(
            parent=self.parent,
            page_size=page_size,
            filters=filters,
            all_projects=all_projects,
        )
        resp = self.client._management.ListExperiments(req)
        return [Experiment.from_proto(x, client=self.client) for x in resp.experiments]

    def list_all(self) -> Pager[Experiment]:
        """List all experiments.

        Pages through all experiments using an iterator.

        Returns:
            A iterator of all experiments.
        """

        def next_page(next_page_token):
            req = management_pb2.ListExperimentsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListExperiments(req)
            return (
                [
                    Experiment.from_proto(x, client=self.client)
                    for x in resp.experiments
                ],
                resp.next_page_token,
            )

        return Pager(next_page)


class Experiment(Resource, types.Experiment):
    """Experiment resource."""

    manager: ExperimentManager
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

    name_pattern: str = (
        "projects/{project}/models/{model}/versions/{version}/experiments/{experiment}"
    )

    def _init(self):
        self.manager = ExperimentManager(parent=self.parent, client=self.client)
        self.events = EventManager(parent=self.name, client=self.client)
        self.metrics = MetricsManager(parent=self.name, client=self.client)
        self.artifacts = ArtifactsManager(
            parent=self.name, client=self.client, run_name=self.run_name
        )
        self.tags = TagsManager(parent=self.name, client=self.client)
        self.metadata = MetadataManager(parent=self.name, client=self.client)

    def cancel(self) -> None:
        """Cancel experiment."""
        raise NotImplementedError("Not yet implemented.")

    def wait(self) -> None:
        """Wait for experiment to complete."""
        raise NotImplementedError("Not yet implemented.")

    def create_metrics(self, metrics: List[Union[Metric, dict]]):
        """Logs metrics from a list of dictionaries"""
        for metric in metrics:
            self.create_metric(metric=metric)

    def create_metric(self, metric: Union[Metric, dict]):
        """Log a single metrics"""
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
