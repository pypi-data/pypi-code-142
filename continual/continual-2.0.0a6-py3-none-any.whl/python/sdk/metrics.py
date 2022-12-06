from __future__ import annotations
from typing import List, Optional

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.events import EventManager


class MetricsManager(Manager):
    """Manages metric resources."""

    name_pattern: str = (
        "projects/{project}/models/{model}/model_versions/{version}/metrics/{metric}"
    )

    def get(self, id: str) -> Metric:
        """Get metric.

        Arguments:
            id: Metric name or id.

        Returns
            A metric.
        """

        req = management_pb2.GetMetricRequest(name=self.name(id))
        metric = self.client._management.GetMetric(req)
        return Metric.from_proto(metric, client=self.client)

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
    ) -> List[Metric]:
        """List metrics.

        Arguments:
            page_size: Number of items to return.

        Returns:
            A list of metrics.
        """
        req = management_pb2.ListMetricsRequest(
            parent=self.parent, page_size=page_size, filters=filters
        )
        resp = self.client._management.ListMetrics(req)
        return [Metric.from_proto(x, client=self.client) for x in resp.metrics]

    def list_all(self) -> Pager[Metric]:
        """List all metrics.

        Pages through all metrics using an iterator.

        Returns:
            A iterator of all metrics.
        """

        def next_page(next_page_token):
            req = management_pb2.ListMetricsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListMetrics(req)
            return (
                [Metric.from_proto(x, client=self.client) for x in resp.metrics],
                resp.next_page_token,
            )

        return Pager(next_page)

    def create(self, metric: Metric):
        """Create an metric.

        Arguments:
            metric: User-defined metric

        Returns:
            A new metric.
        """
        req = management_pb2.CreateMetricRequest(
            parent=self.parent,
            metric=metric.to_proto(),
        )

        resp = self.client._management.CreateMetric(req)
        return Metric.from_proto(resp, client=self.client)

    def delete(self, id: str) -> None:
        """Delete a metric.

        Arguments:
            id: Metric name or id.
        """

        req = management_pb2.DeleteMetricRequest(name=self.name(id))
        self.client._management.DeleteMetric(req)


class Metric(Resource, types.Metric):
    """Metric resource."""

    name_pattern: str = (
        "projects/{project}/models/{model}/model_versions/{version}/metrics/{metric}"
    )
    manager: MetricsManager

    events: EventManager
    """Event manager."""

    def _init(self):
        self.manager = MetricsManager(parent=self.parent, client=self.client)
