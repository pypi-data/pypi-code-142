from __future__ import annotations
from typing import List, Optional
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.dataset_versions import DatasetVersionManager
from continual.python.sdk.promotions import PromotionManager
from continual.python.sdk.events import EventManager
from continual.python.sdk.tags import TagsManager
from continual.python.sdk.metadata import MetadataManager


from continual.python.sdk.batchpredictions import (
    BatchPredictionManager,
)


class DatasetManager(Manager):
    """Manages dataset resources."""

    name_pattern: str = "projects/{project}/datasets/{dataset}"

    def create(
        self,
        display_name: str,
        description: Optional[str] = "",
        if_not_exists: bool = True,
    ) -> Dataset:
        """Create dataset.

        Arguments:
            id: Dataset name or id.

        Returns
            An experiment.
        """
        req = management_pb2.CreateDatasetRequest(
            name=self.name(display_name),
            description=description,
            if_not_exists=if_not_exists,
        )
        resp = self.client._management.CreateDataset(req)
        return Dataset.from_proto(resp, client=self.client, parent_run=self.run_name)

    def get(self, id: str) -> Dataset:
        """Get dataset.

        Arguments:
            id: Dataset name or id.

        Returns
            An experiment.
        """
        req = management_pb2.GetDatasetRequest(name=self.name(id))
        resp = self.client._management.GetDataset(req)
        return Dataset.from_proto(resp, client=self.client, parent_run=self.run_name)

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
        all_projects: bool = False,
    ) -> List[Dataset]:
        """List dataset.

        Arguments:
            page_size: Number of items to return.

        Returns:
            A list of datasets.
        """
        req = management_pb2.ListDatasetsRequest(
            parent=self.parent,
            page_size=page_size,
            filters=filters,
            all_projects=all_projects,
        )
        resp = self.client._management.ListDatasets(req)
        return [
            Dataset.from_proto(x, client=self.client, parent_run=self.run_name)
            for x in resp.datasets
        ]

    def list_all(self) -> Pager[Dataset]:
        """List all dataset.

        Pages through all dataset using an iterator.

        Returns:
            A iterator of all dataset.
        """

        def next_page(next_page_token):
            req = management_pb2.ListDatasetsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListDatasets(req)
            return (
                [
                    Dataset.from_proto(x, client=self.client, parent_run=self.run_name)
                    for x in resp.datasets
                ],
                resp.next_page_token,
            )

        return Pager(next_page)


class Dataset(Resource, types.Dataset):
    """Dataset resource."""

    name_pattern: str = "projects/{project}/datasets/{dataset}"
    manager: DatasetManager

    dataset_versions: DatasetVersionManager
    """Dataset version manager."""

    promotions: PromotionManager
    """Promotion manager."""

    batch_predictions: BatchPredictionManager
    """Batch Prediction  manager."""

    events: EventManager
    """Event manager."""

    tags: TagsManager
    """Tags Manager"""

    metadata: MetadataManager
    """Metadata Manager"""

    def _init(self):
        self.manager = DatasetManager(
            parent=self.parent, client=self.client, run_name=self.parent_run
        )
        self.dataset_versions = DatasetVersionManager(
            parent=self.name, client=self.client, run_name=self.parent_run
        )
        self.promotions = PromotionManager(
            parent=self.name, client=self.client, run_name=self.parent_run
        )
        self.batch_predictions = BatchPredictionManager(
            parent=self.name, client=self.client
        )
        self.events = EventManager(client=self.client, parent=self.name)
        self.tags = TagsManager(
            parent=self.name, client=self.client, run_name=self.parent_run
        )
        self.metadata = MetadataManager(
            parent=self.name, client=self.client, run_name=self.parent_run
        )
