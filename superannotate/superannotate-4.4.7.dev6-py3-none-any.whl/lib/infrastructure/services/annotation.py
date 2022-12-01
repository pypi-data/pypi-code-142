import asyncio
import copy
import io
import json
from pathlib import Path
from typing import Callable
from typing import Dict
from typing import List
from urllib.parse import urljoin

import aiohttp
import lib.core as constants
from lib.core import entities
from lib.core.exceptions import AppException
from lib.core.reporter import Reporter
from lib.core.service_types import UploadAnnotations
from lib.core.service_types import UploadAnnotationsResponse
from lib.core.serviceproviders import BaseAnnotationService
from lib.infrastructure.stream_data_handler import StreamedAnnotations
from pydantic import parse_obj_as
from superannotate.logger import get_default_logger

logger = get_default_logger()


class AnnotationService(BaseAnnotationService):
    ASSETS_PROVIDER_VERSION = "v2"
    DEFAULT_CHUNK_SIZE = 5000

    URL_GET_ANNOTATIONS = "items/annotations/download"
    URL_UPLOAD_ANNOTATIONS = "items/annotations/upload"
    URL_LARGE_ANNOTATION = "items/{item_id}/annotations/download"
    URL_SYNC_LARGE_ANNOTATION = "items/{item_id}/annotations/sync"
    URL_SYNC_LARGE_ANNOTATION_STATUS = "items/{item_id}/annotations/sync/status"
    URL_CLASSIFY_ITEM_SIZE = "items/annotations/download/method"
    URL_DOWNLOAD_LARGE_ANNOTATION = "items/{item_id}/annotations/download"
    URL_START_FILE_UPLOAD_PROCESS = "items/{item_id}/annotations/upload/multipart/start"
    URL_START_FILE_SEND_FINISH = "items/{item_id}/annotations/upload/multipart/finish"
    URL_START_FILE_SYNC_STATUS = "items/{item_id}/annotations/sync/status"
    URL_START_FILE_SYNC = "items/{item_id}/annotations/sync"
    URL_START_FILE_SEND_PART = "items/{item_id}/annotations/upload/multipart/part"
    URL_DELETE_ANNOTATIONS = "annotations/remove"
    URL_DELETE_ANNOTATIONS_PROGRESS = "annotations/getRemoveStatus"
    URL_ANNOTATION_SCHEMAS = "items/annotations/schema"

    @property
    def assets_provider_url(self):
        if self.client.api_url != constants.BACKEND_URL:
            return f"https://assets-provider.devsuperannotate.com/api/{self.ASSETS_PROVIDER_VERSION}/"
        return f"https://assets-provider.superannotate.com/api/{self.ASSETS_PROVIDER_VERSION}/"

    def get_schema(self, project_type: int, version: str):
        return self.client.request(
            urljoin(self.assets_provider_url, self.URL_ANNOTATION_SCHEMAS),
            "get",
            params={
                "project_type": project_type,
                "version": version,
            },
        )

    async def _sync_large_annotation(self, team_id, project_id, item_id):
        sync_params = {
            "team_id": team_id,
            "project_id": project_id,
            "desired_transform_version": "export",
            "desired_version": "V1.00",
            "current_transform_version": "V1.00",
            "current_source": "main",
            "desired_source": "secondary",
        }
        sync_url = urljoin(
            self.assets_provider_url,
            self.URL_SYNC_LARGE_ANNOTATION.format(item_id=item_id),
        )
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False),
            headers=self.client.default_headers,
            raise_for_status=True,
        ) as session:
            await session.post(sync_url, params=sync_params)

            sync_params.pop("current_source")
            sync_params.pop("desired_source")

            synced = False
            sync_status_url = urljoin(
                self.assets_provider_url,
                self.URL_SYNC_LARGE_ANNOTATION_STATUS.format(item_id=item_id),
            )
            while synced != "SUCCESS":
                synced = await session.get(sync_status_url, params=sync_params)
                synced = await synced.json()
                synced = synced["status"]
                await asyncio.sleep(1)
        return synced

    async def get_big_annotation(
        self, project: entities.ProjectEntity, item: dict, reporter: Reporter
    ) -> dict:
        url = urljoin(
            self.assets_provider_url,
            self.URL_LARGE_ANNOTATION.format(item_id=item["id"]),
        )

        query_params = {
            "team_id": project.team_id,
            "project_id": project.id,
            "annotation_type": "MAIN",
            "version": "V1.00",
        }

        await self._sync_large_annotation(
            team_id=project.team_id, project_id=project.id, item_id=item["id"]
        )

        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False),
            headers=self.client.default_headers,
            raise_for_status=True,
        ) as session:
            start_response = await session.post(url, params=query_params)
            large_annotation = await start_response.json()

        reporter.update_progress()
        return large_annotation

    async def get_small_annotations(
        self,
        project: entities.ProjectEntity,
        folder: entities.FolderEntity,
        items: List[str],
        reporter: Reporter,
        callback: Callable = None,
    ) -> List[dict]:
        query_params = {
            "team_id": project.team_id,
            "project_id": project.id,
            "folder_id": folder.id,
        }

        handler = StreamedAnnotations(
            self.client.default_headers,
            reporter,
            map_function=lambda x: {"image_names": x},
            callback=callback,
        )

        loop = asyncio.new_event_loop()

        return loop.run_until_complete(
            handler.get_data(
                url=urljoin(self.assets_provider_url, self.URL_GET_ANNOTATIONS),
                data=items,
                params=query_params,
                chunk_size=self.DEFAULT_CHUNK_SIZE,
            )
        )

    def sort_items_by_size(
        self,
        project: entities.ProjectEntity,
        folder: entities.FolderEntity,
        item_names: List[str],
    ) -> Dict[str, List]:
        chunk_size = 2000
        query_params = {
            "project_id": project.id,
            "folder_id": folder.id,
        }

        response_data = {"small": [], "large": []}
        for i in range(0, len(item_names), chunk_size):
            body = {
                "item_names": item_names[i : i + chunk_size],  # noqa
                "folder_id": folder.id,
            }  # noqa
            response = self.client.request(
                url=urljoin(self.assets_provider_url, self.URL_CLASSIFY_ITEM_SIZE),
                method="POST",
                params=query_params,
                data=body,
            )
            if not response.ok:
                raise AppException(response.error)
            response_data["small"].extend(response.data.get("small", []))
            response_data["large"].extend(response.data.get("large", []))
        return response_data

    async def download_big_annotation(
        self,
        project: entities.ProjectEntity,
        download_path: str,
        postfix: str,
        item: dict,
        callback: Callable = None,
    ):
        item_id = item["id"]
        item_name = item["name"]
        query_params = {
            "team_id": project.team_id,
            "project_id": project.id,
            "annotation_type": "MAIN",
            "version": "V1.00",
        }

        url = urljoin(
            self.assets_provider_url,
            self.URL_DOWNLOAD_LARGE_ANNOTATION.format(item_id=item_id),
        )

        await self._sync_large_annotation(
            team_id=project.team_id, project_id=project.id, item_id=item_id
        )

        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False),
            headers=self.client.default_headers,
            raise_for_status=True,
        ) as session:
            start_response = await session.post(url, params=query_params)
            res = await start_response.json()
            Path(download_path).mkdir(exist_ok=True, parents=True)

            dest_path = Path(download_path) / (item_name + postfix)
            with open(dest_path, "w") as fp:
                if callback:
                    res = callback(res)
                json.dump(res, fp)

    async def download_small_annotations(
        self,
        project: entities.ProjectEntity,
        folder: entities.FolderEntity,
        reporter: Reporter,
        download_path: str,
        postfix: str,
        items: List[str] = None,
        callback: Callable = None,
    ):
        query_params = {
            "team_id": project.team_id,
            "project_id": project.id,
            "folder_id": folder.id,
        }
        handler = StreamedAnnotations(
            headers=self.client.default_headers,
            reporter=reporter,
            map_function=lambda x: {"image_names": x},
            callback=callback,
        )

        return await handler.download_data(
            url=urljoin(self.assets_provider_url, self.URL_GET_ANNOTATIONS),
            data=items,
            params=query_params,
            chunk_size=self.DEFAULT_CHUNK_SIZE,
            download_path=download_path,
            postfix=postfix,
        )

    async def upload_small_annotations(
        self,
        project: entities.ProjectEntity,
        folder: entities.FolderEntity,
        items_name_file_map: Dict[str, io.StringIO],
    ) -> UploadAnnotationsResponse:
        url = urljoin(
            self.assets_provider_url,
            (
                f"{self.URL_UPLOAD_ANNOTATIONS}?{'&'.join(f'image_names[]={item_name}' for item_name in items_name_file_map.keys())}"
            ),
        )

        headers = copy.copy(self.client.default_headers)
        del headers["Content-Type"]
        async with aiohttp.ClientSession(
            headers=headers,
            connector=aiohttp.TCPConnector(ssl=False),
            raise_for_status=True,
        ) as session:
            data = aiohttp.FormData(quote_fields=False)
            for key, file in items_name_file_map.items():
                file.seek(0)
                data.add_field(
                    key,
                    bytes(file.read(), "ascii"),
                    filename=key,
                    content_type="application/json",
                )

            _response = await session.post(
                url,
                params={
                    "team_id": project.team_id,
                    "project_id": project.id,
                    "folder_id": folder.id,
                },
                data=data,
            )
            if not _response.ok:
                logger.debug(await _response.text())
                raise AppException("Can't upload annotations.")
            data_json = await _response.json()
            response = UploadAnnotationsResponse()
            response.status = _response.status
            response._content = await _response.text()
            response.data = parse_obj_as(UploadAnnotations, data_json)
            return response

    async def upload_big_annotation(
        self,
        project: entities.ProjectEntity,
        folder: entities.FolderEntity,
        item_id: int,
        data: io.StringIO,
        chunk_size: int,
    ) -> bool:
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False),
            headers=self.client.default_headers,
            raise_for_status=True,
        ) as session:
            params = {
                "team_id": project.team_id,
                "project_id": project.id,
                "folder_id": folder.id,
            }
            start_response = await session.post(
                urljoin(
                    self.assets_provider_url,
                    self.URL_START_FILE_UPLOAD_PROCESS.format(item_id=item_id),
                ),
                params=params,
            )
            if not start_response.ok:
                raise AppException(str(await start_response.text()))
            process_info = await start_response.json()
            params["path"] = process_info["path"]
            headers = copy.copy(self.client.default_headers)
            headers["upload_id"] = process_info["upload_id"]
            chunk_id = 1
            data_sent = False
            while True:
                chunk = data.read(chunk_size)
                params["chunk_id"] = chunk_id
                if chunk:
                    data_sent = True
                    response = await session.post(
                        urljoin(
                            self.assets_provider_url,
                            self.URL_START_FILE_SEND_PART.format(item_id=item_id),
                        ),
                        params=params,
                        headers=headers,
                        data=json.dumps({"data_chunk": chunk}),
                    )
                    if not response.ok:
                        raise AppException(str(await response.text()))
                    chunk_id += 1
                if not chunk and not data_sent:
                    return False
                if len(chunk) < chunk_size:
                    break
            del params["chunk_id"]
            response = await session.post(
                urljoin(
                    self.assets_provider_url,
                    self.URL_START_FILE_SEND_FINISH.format(item_id=item_id),
                ),
                headers=headers,
                params=params,
            )
            if not response.ok:
                raise AppException(str(await response.text()))
            del params["path"]
            response = await session.post(
                urljoin(
                    self.assets_provider_url,
                    self.URL_START_FILE_SYNC.format(item_id=item_id),
                ),
                params=params,
                headers=headers,
            )
            if not response.ok:
                raise AppException(str(await response.text()))
            while True:
                response = await session.get(
                    urljoin(
                        self.assets_provider_url,
                        self.URL_START_FILE_SYNC_STATUS.format(item_id=item_id),
                    ),
                    params=params,
                    headers=headers,
                )
                if response.ok:
                    data = await response.json()
                    status = data.get("status")
                    if status == "SUCCESS":
                        return True
                    elif status.startswith("FAILED"):
                        return False
                    await asyncio.sleep(15)
                else:
                    raise AppException(str(await response.text()))

    def delete(
        self,
        project: entities.ProjectEntity,
        folder: entities.FolderEntity = None,
        item_names: List[str] = None,
    ):
        data = {}
        params = {"project_id": project.id}
        if folder:
            params["folder_id"] = folder.id
        if item_names:
            data["image_names"] = item_names
        return self.client.request(
            self.URL_DELETE_ANNOTATIONS, "post", params=params, data=data
        )

    def get_delete_progress(self, project: entities.ProjectEntity, poll_id: int):
        return self.client.request(
            self.URL_DELETE_ANNOTATIONS_PROGRESS,
            "get",
            params={"project_id": project.id, "poll_id": poll_id},
        )
