from __future__ import annotations
from typing import List, Optional, Tuple
import os
import io
import json
import requests
import tarfile
import mimetypes
from google.resumable_media import DataCorruption
from google.resumable_media.requests import ResumableUpload

from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.events import EventManager
from continual.rpc.management.v1 import (
    management_pb2,
    types as management_types_py,
)

CHUNK_SIZE = 117440512  # 112 MB in bytes, chosen arbitrarily


class ArtifactsManager(Manager):
    """Manages artifact resources."""

    # the name pattern for artifacts depends on the resource it was created for
    name_pattern: str = ""

    def create(
        self,
        path: str = "",
        external: bool = True,
        type: str = "",
        url: str = None,
        metadata: dict = None,
        upload: bool = True,
    ) -> Artifact:
        """Create an artifact"""
        if external or not upload:
            req = management_pb2.CreateArtifactRequest(
                parent=self.parent,
                artifact=Artifact(
                    path=path,
                    type=type,
                    external=True,
                    url=url,
                    metadata=metadata,
                    run_name=self.run_name,
                ).to_proto(),
            )
            res = self.client._management.CreateArtifact(req)
            return Artifact.from_proto(res, client=self.client)

        elif upload:
            artifact_name = ""
            try:
                file_to_upload = path
                if os.path.isdir(path):
                    tarfile_name = os.path.basename(path) + ".tar.gz"
                    with tarfile.open(tarfile_name, "w:gz") as tar:
                        tar.add(
                            path,
                            recursive=True,
                            arcname=os.path.basename(tarfile_name).split(".")[0],
                        )
                    file_to_upload = tarfile_name

                mime_type, _ = mimetypes.guess_type(file_to_upload)

                payload = ""
                with open(file_to_upload, "rb") as f:
                    payload = f.read()

                total_bytes = len(payload)
                exceeds_chunk_size = total_bytes >= CHUNK_SIZE

                req = management_pb2.GenerateArtifactUploadURLRequest(
                    resource=self.parent,
                    path=path,
                    type=type,
                    mime_type=mime_type or "",
                    metadata=json.dumps(metadata or dict()),
                    resumable=exceeds_chunk_size,
                    run_name=self.run_name,
                )
                res = self.client._management.GenerateArtifactUploadURL(req)

                upload_url = res.url
                artifact_name = res.artifact.name

                headers = dict()
                if mime_type:
                    headers["Content-Type"] = mime_type

                if exceeds_chunk_size:
                    transport = requests.Session()

                    stream = io.BytesIO(payload)

                    upload = ResumableUpload(upload_url, CHUNK_SIZE)
                    upload._resumable_url = upload_url
                    upload._total_bytes = total_bytes
                    upload._stream = stream

                    while not upload.finished:
                        try:
                            print("Writing chunk ... ")
                            response = upload.transmit_next_chunk(transport, timeout=60)
                            print(f"Chunk response: {response}")
                        except DataCorruption:
                            raise
                else:
                    upload_res = requests.put(
                        upload_url, data=payload, headers={"Content-Type": mime_type}
                    )
                    upload_res.raise_for_status()

                return Artifact.from_proto(res.artifact, client=self.client)
            except:
                if artifact_name:
                    req = management_pb2.DeleteArtifactRequest(name=artifact_name)
                    res = self.client._management.DeleteArtifact(req)
                raise

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
    ) -> List[Artifact]:
        """List artifact.

        Arguments:
            page_size: Number of items to return.

        Returns:
            A list of artifacts.
        """
        req = management_pb2.ListArtifactsRequest(
            parent=self.parent,
            page_size=page_size,
            filters=filters,
        )
        resp = self.client._management.ListArtifacts(req)
        return [Artifact.from_proto(x, client=self.client) for x in resp.artifacts]

    def get(self, name: str) -> Artifact:
        if not self.client:
            print(f"Cannot fetch artifact without client")
            return

        req = management_pb2.GetArtifactRequest(name=name)
        res = self.client._management.GetArtifact(req)
        return Artifact.from_proto(res, client=self.client)

    def delete(self, name: str):
        if not self.client:
            print(f"Cannot delete artifact without client")
            return

        req = management_pb2.DeleteArtifactRequest(name=name)
        self.client._management.DeleteArtifact(req)

    def download(
        self,
        id: str,
        download_dir: str = "./artifacts",
    ) -> Tuple[Artifact, str]:

        artifact = self.get(id)
        downloaded_to = ""
        if not artifact.url:
            raise ValueError(
                f"Artifact cannot be downloaded - no URL was found: {artifact.url}"
            )
        elif artifact.external:
            raise ValueError(f"Cannot download an external artifact - {artifact.url}")

        try:
            res = requests.get(artifact.url, stream=True)
            with tarfile.open(fileobj=res.raw, mode="r") as f:
                f.extractall(download_dir)

            root_dir = os.path.basename(artifact.path or "").split(".")[0]
            downloaded_to = os.path.join(download_dir, root_dir)
        except:
            res = requests.get(artifact.url)
            downloaded_to = os.path.join(
                download_dir,
                os.path.basename(artifact.path or artifact.name.split("/")[-1]),
            )
            with open(downloaded_to, "wb") as f:
                f.write(res.content)
        return artifact, downloaded_to

    # def upload_artifacts(
    #     self, paths: List[str], type: str = "", metadata: dict = None
    # ) -> List[str]:
    #     artifact_names = []
    #     for path in paths:
    #         try:
    #             name = self.upload_artifact(path=path, type=type, metadata=metadata)
    #             artifact_names.append(name)
    #         except:
    #             artifact_names.append("")
    #     return artifact_names


class Artifact(Resource, management_types_py.Artifact):
    """Artifact resource."""

    # the name pattern for artifacts depends on the resource it was created for
    name_pattern: str = ""
    manager: ArtifactsManager

    events: EventManager
    """Event manager."""

    def _init(self):
        self.manager = ArtifactsManager(parent=self.parent, client=self.client)

    def download(self, dest_dir: str = "./artifacts") -> Tuple[Artifact, str]:
        """
        Arguments
        ----------
        dest_dir: str
            directory into which to download the artifact payload

        Returns
        -------
        Artifact, str
            The artifact handle as well as the path to which the artifact's payload
            was downloaded.
        """
        return self.manager.download(id=self.name, download_dir=dest_dir)
