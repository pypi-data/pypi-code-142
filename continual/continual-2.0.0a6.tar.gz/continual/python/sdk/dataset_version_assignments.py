from __future__ import annotations
from typing import List, Optional

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.events import EventManager


class DatasetVersionAssignmentManager(Manager):
    """Manages Dataset Version resources."""

    name_pattern: str = "projects/{project}/datasets/{dataset}/versions/{version}"

    def create(self, resource_name: str) -> DatasetVersionAssignment:
        """Create a dataset version assignemnt

        Returns
            A Dataset Version Assignment.
        """
        req = management_pb2.CreateDatasetVersionAssignmentRequest(
            dataset_version_name=self.parent,
            resource_name=resource_name,
        )
        resp = self.client._management.CreateDatasetVersionAssignment(req)
        return DatasetVersionAssignment.from_proto(resp, client=self.client)

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
        all_projects: bool = False,
    ) -> List[DatasetVersionAssignment]:
        """List dataset version assignments.

        Arguments:
            page_size: Number of items to return.

            filter: List of filters to apply to batch prediction job. Can be:
            - state  (i.e. state:FAILED)

        Returns:
            A list of dataset versions.
        """
        req = management_pb2.ListDatasetVersionAssignmentsRequest(
            parent=self.parent,
            page_size=page_size,
        )
        resp = self.client._management.ListDatasetVersionAssignments(req)
        return [
            DatasetVersionAssignment.from_proto(x, client=self.client)
            for x in resp.assignments
        ]

    def list_all(self) -> Pager[DatasetVersionAssignment]:
        """List all dataset version assignments.

        Pages through all dataset versions using an iterator.

        Returns:
            A iterator of all dataset versions.
        """

        def next_page(next_page_token):
            req = management_pb2.ListDatasetVersionAssignmentsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListDatasetVersionAssignments(req)
            return (
                [
                    DatasetVersionAssignment.from_proto(x, client=self.client)
                    for x in resp.dataset_versions
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def delete(self, id: str) -> None:
        """Delete an assignment.

        Arguments:
            id: DatasetVersionAssignment name or id.
        """

        req = management_pb2.DeleteDatasetVersionAssignmentRequest(name=self.name(id))
        self.client._management.DeleteDatasetVersionAssignment(req)


class DatasetVersionAssignment(Resource, types.DatasetVersionAssignment):
    """Dataset version resource."""

    name_pattern: str = "projects/{project}/datasets/{dataset}/versions/{version}"
    manager: DatasetVersionAssignmentManager

    events: EventManager
    """Event manager."""

    def _init(self):
        self.manager = DatasetVersionAssignmentManager(
            parent=self.parent, client=self.client
        )
        self.events = EventManager(parent=self.name, client=self.client)
