from __future__ import annotations
from typing import List, Optional

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.events import EventManager


class DataChecksManager(Manager):
    """Manages data_check resources."""

    name_pattern: str = "projects/{project}/datasets/{dataset}/dataset_versions/{version}/data_checks/{data_check}"

    def get(self, id: str) -> DataCheck:
        """Get data_check.

        Arguments:
            id: DataCheck name or id.

        Returns
            A data_check.
        """

        req = management_pb2.GetDataCheckRequest(name=self.name(id))
        data_check = self.client._management.GetDataCheck(req)
        return DataCheck.from_proto(data_check, client=self.client)

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
    ) -> List[DataCheck]:
        """List data_checks.

        Arguments:
            page_size: Number of items to return.

        Returns:
            A list of data_checks.
        """
        req = management_pb2.ListDataChecksRequest(
            parent=self.parent, page_size=page_size, filters=filters
        )
        resp = self.client._management.ListDataChecks(req)
        return [DataCheck.from_proto(x, client=self.client) for x in resp.data_checks]

    def list_all(self) -> Pager[DataCheck]:
        """List all data_checks.

        Pages through all data_checks using an iterator.

        Returns:
            A iterator of all data_checks.
        """

        def next_page(next_page_token):
            req = management_pb2.ListDataChecksRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListDataChecks(req)
            return (
                [DataCheck.from_proto(x, client=self.client) for x in resp.data_checks],
                resp.next_page_token,
            )

        return Pager(next_page)

    def create(self, data_check: DataCheck):
        """Create an data_check.

        Arguments:
            data_check

        Returns:
            A new data_check.
        """
        req = management_pb2.CreateDataCheckRequest(
            parent=self.parent,
            data_check=data_check.to_proto(),
        )
        resp = self.client._management.CreateDataCheck(req)
        return DataCheck.from_proto(resp, client=self.client)


class DataCheck(Resource, types.DataCheck):
    """DataCheck resource."""

    name_pattern: str = "projects/{project}/datasets/{dataset}/dataset_versions/{version}/data_checks/{data_check}"
    manager: DataChecksManager

    events: EventManager
    """Event manager."""

    def _init(self):
        self.manager = DataChecksManager(parent=self.parent, client=self.client)
