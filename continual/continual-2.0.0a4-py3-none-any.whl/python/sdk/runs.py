from __future__ import annotations
import time
from threading import Thread
from typing import List, Optional
from continual.python.sdk.artifacts import ArtifactsManager
from continual.python.sdk.models import ModelManager
from continual.python.sdk.datasets import DatasetManager

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.events import EventManager
from continual.python.sdk.tags import TagsManager
from continual.python.sdk.metadata import MetadataManager
from google.protobuf.timestamp_pb2 import Timestamp


class RunManager(Manager):
    """Manages run resources."""

    name_pattern: str = "projects/{project}/runs/{run}"

    def get(self, id: str) -> Run:
        """Get run.

        Arguments:
            id: Run name or id.

        Returns
            A run.
        """

        req = management_pb2.GetRunRequest(name=self.name(id))
        run = self.client._management.GetRun(req)
        return Run.from_proto(run, client=self.client)

    def heartbeat(self, run_name: str) -> Timestamp:
        """Send heartbeat for a given run name

        Arguments:
            run_name: string name of run
        """
        req = management_pb2.LogRunHeartbeatRequest(name=run_name)
        return self.client._management.LogRunHeartbeat(req)

    def list(
        self, page_size: Optional[int] = None, filters: List[str] = None
    ) -> List[Run]:
        """List runs.

        Arguments:
            page_size: Number of items to return.

        Returns:
            A list of runs.
        """
        req = management_pb2.ListRunsRequest(
            parent=self.parent, page_size=page_size, filters=filters
        )
        resp = self.client._management.ListRuns(req)
        return [Run.from_proto(x, client=self.client) for x in resp.runs]

    def list_all(self) -> Pager[Run]:
        """List all runs.

        Pages through all runs using an iterator.

        Returns:
            A iterator of all runs.
        """

        def next_page(next_page_token):
            req = management_pb2.ListRunsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListRuns(req)
            return (
                [Run.from_proto(x, client=self.client) for x in resp.runs],
                resp.next_page_token,
            )

        return Pager(next_page)

    def create(
        self,
        run_id: Optional[str] = None,
        description: Optional[str] = None,
        heartbeat_interval: Optional[int] = 5,
    ) -> Run:
        """Create an run.

        New runs are identified by a unique run id that is
        generated from the display name.  To set a run id explicitly,
        you can pass `run_id`.  However run ids are globally unique across
        all projects.

        Arguments:
            run_id: User-defined run id.
            description: A string description of the run
            heartbeat_interval: integer number of seconds to wait between run heartbeats to
                Continual endpoint

        Returns:
            A new run.
        """
        req = management_pb2.CreateRunRequest(
            run_id=run_id,
            parent=self.parent,
            description=description,
            heartbeat_interval=heartbeat_interval,
        )

        resp = self.client._management.CreateRun(req)
        return Run.from_proto(resp, client=self.client)

    def delete(self, id: str) -> None:
        """Delete a run.

        Arguments:
            id: Run name or id.
        """

        req = management_pb2.DeleteRunRequest(name=self.name(id))
        self.client._management.DeleteRun(req)

    def update(self, run: Run, paths: List[str]):
        """
        Arguments:
            run : Updated run object
            paths: list of actual fields to update
        """

        req = management_pb2.UpdateRunRequest(run=run.to_proto(), update_paths=paths)
        self.client._management.UpdateRun(req)


class Run(Resource, types.Run, Thread):
    """Run resource."""

    name_pattern: str = "runs/{run}"
    manager: RunManager

    models: ModelManager
    """Models manager"""

    datasets: DatasetManager
    """Datasets manager"""

    artifacts: ArtifactsManager
    """Artifacts manager."""

    events: EventManager
    """Event manager."""

    tags: TagsManager
    """Tags Manager"""

    metadata: MetadataManager
    """Metadata Manager"""

    def _init(self):
        Thread.__init__(self, daemon=True)
        self.manager = RunManager(parent=self.parent, client=self.client)
        self.events = EventManager(parent=self.parent, client=self.client)
        self.models = ModelManager(
            parent=self.parent, client=self.client, run_name=self.name
        )
        self.datasets = DatasetManager(
            parent=self.parent, client=self.client, run_name=self.name
        )
        self.artifacts = ArtifactsManager(
            parent=self.name, client=self.client, run_name=self.name
        )

        self.tags = TagsManager(
            parent=self.name, client=self.client, run_name=self.name
        )
        self.metadata = MetadataManager(
            parent=self.name, client=self.client, run_name=self.name
        )

        # Thread variables
        self.running = True
        self.start()

    def complete(self):
        """Cleanup Run"""
        self.set_state("COMPLETED")
        self.running = False
        self.join()

    def _heartbeat(self):
        """Sends a heartbeat to the server from this run"""
        self.last_heartbeat = self.manager.heartbeat(run_name=self.name).ToDatetime()

    def set_state(self, state: str):
        self.state = state
        self.manager.update(self, paths=["state"])

    def run(self):
        while True:
            if not self.running:
                break
            self._heartbeat()
            time.sleep(self.heartbeat_interval)
