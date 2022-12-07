from uuid import UUID
from fastapi.responses import StreamingResponse
from fastapi import status
from sqlmodel import Session
import aiofiles
from aiobotocore.session import get_session as get_aioboto_session
import os
import mimetypes

from etiket.core.config import settings
from etiket.core.exceptions import (
    UserNotInScopeException,
    FileAlreadyExistsException,
    FileNotAvailableException,
    InvalidRangeException,
    DownloadFailedException,
)
from etiket.app.models import (
    File,
    FileCreate,
    FileUpdate,
    FileRead,
)
from etiket.app.crud.db import (
    get_dataset_from_db_by_scope_uuid,
    get_file_from_db_by_scope_uuid,
    commit_to_db,
)


class FileService:
    def __init__(self):
        pass

    async def add_file(self, file: FileCreate, user, session: Session) -> FileRead:
        dataset = get_dataset_from_db_by_scope_uuid(
            file.scope, file.dataset_uuid, session
        )
        if user not in dataset.scopes.users:
            raise UserNotInScopeException(file.scope)
        for ifile in dataset.files:
            if ifile.name == file.name and ifile.immutable:
                raise FileAlreadyExistsException
        db_file = File.from_orm(file)
        mimetype,encoding = mimetypes.guess_type(file.name)
        db_file.mimetype = mimetype if mimetype else 'application/octet-stream'
        db_file.dataset_id = dataset.id
        db_file = commit_to_db(db_file, session)
        return db_file


    async def update_file(
        self, scope: str, file_uuid: UUID, file: FileUpdate, user, session: Session
    ) -> FileRead:
        db_file = get_file_from_db_by_scope_uuid(scope, file_uuid, session)
        if current_user not in db_file.dataset.scopes.users:
            raise UserNotInScopeException(scope)
        file_data = file.dict(exclude_unset=True)
        for key, value in file_data.items():
            if value is None:
                continue
            setattr(db_file, key, value)
        db_file = commit_to_db(db_file, session)
        return db_file

    async def get_file(
        self, scope: str, file_uuid: UUID, Range: str, user, session: Session
    ) -> StreamingResponse:
        db_file = get_file_from_db_by_scope_uuid(scope, file_uuid, session)
        if db_file.status != ("available" or "secured"):
            raise FileNotAvailableException
        if Range:
            try:
                start_finish = Range.replace("bytes=", "").split("-")
                start = int(start_finish[0]) if start_finish[0] != "" else 0
                end = (
                    int(start_finish[1]) if start_finish[1] != "" else db_file.size - 1
                )
            except ValueError:
                raise InvalidRangeException(Range)
        else:
            start = 0
            end = db_file.size
        total_length = end - start
        if total_length <= 0:
            raise InvalidRangeException(Range)

        async def stream_file():
            exists = os.path.exists(db_file.location)
            if exists:
                #DO WE NEED A FILE LOCK? PROBABLY YES
                async with aiofiles.open(db_file.location, mode="rb") as f:
                    if start > 0:
                        await f.seek(start)
                    chunksize = (
                        settings.ETIKET_CHUNK_SIZE
                        if settings.ETIKET_CHUNK_SIZE < total_length
                        else total_length
                    )
                    length_read = 0
                    while chunk := await f.read(chunksize):
                        if Range:
                            length_read += len(chunk)
                            if length_read == total_length:
                                yield chunk
                                break
                            if length_read + chunksize > total_length:
                                chunksize = total_length - length_read
                        yield chunk
            else:
                try:
                    session = get_aioboto_session()
                    async with session.create_client(
                            "s3",
                            endpoint_url=settings.S3_ENDPOINT,
                            use_ssl=True,
                            verify=True,
                            ) as s3:
                        object = await s3.get_object(
                            Bucket=db_file.s3_bucket,
                            Key=db_file.s3_key,
                            Range=Range,
                        )
                        async for chunk in object["Body"]:
                            yield chunk
                except ClientError as e:
                    print(e)
                    yield DownloadFailedException

        mimetype = db_file.mimetype if db_file.mimetype else "application/octet-stream"
        headers = {}
        headers["Content-Length"] = str(total_length)
        if Range:
            headers["Content-Range"] = f"bytes {start}-{end}/{db_file.size}"
            status_code = status.HTTP_206_PARTIAL_CONTENT
        else:
            headers["Accept-Ranges"] = "bytes"
            status_code = status.HTTP_200_OK
        return StreamingResponse(
            stream_file(), status_code=status_code, headers=headers, media_type=mimetype
        )
