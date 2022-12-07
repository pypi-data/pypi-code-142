import aiofiles
import os
import hashlib
import boto3
import base64
import shutil
from uuid import uuid4, UUID
from fastapi import status, Response
from typing import Optional

from etiket.app.crud.db import (
    get_scope_from_db_by_name,
    get_file_from_db_by_scope_uuid,
    get_upload_from_db_by_uuid,
    commit_to_db,
)
from etiket.core.types import (
    FileStatus,
    UploadConcat,
)
from etiket.app.models import (
    Upload,
)
from etiket.core.config import settings
from etiket.core.exceptions import (
    UserNotInScopeException,
    FileIsImmutableException,
    NewVersionFileForbiddenException,
    UploadStillInProgressException,
    NotAllUploadsCompletedYetException,
    UploadGoneException,
    UnsupportedTusVersionException,
    UnsupportedTusExtensionException,
    ContentTypeException,
    UploadOffsetMismatchException,
    UploadAlreadyCompletedException,
    ContentLengthLargerThanUploadLengthException,
    UploadTerminationFailedException,
    UploadFailedException,
    UploadLengthException,
    DeferUploadLengthException,
    UploadChecksumHeaderException,
    UnsupportedChecksumAlgorithmException,
    UploadUUIDInConcatHeaderException,
    UploadConcatHeaderException,
    UploadLengthInFinalConcatHeaderException,
    UploadMetadataHeaderException,
    MissingScopeUploadMetadataHeaderException,
    MissingFileUUIDUploadMetadataHeaderException,
    InvalidFileUUIDUploadMetadataHeaderException,
)


class TusService:
    def __init__(self):
        self.tus_resumable = settings.ETIKET_TUS_RESUMABLE
        self.tus_versions = [settings.ETIKET_TUS_RESUMABLE]
        self.tus_max_size = str(settings.ETIKET_MAX_FILE_SIZE)
        self.tus_min_size_partial = str(settings.ETIKET_MIN_PARTIAL_FILE_SIZE)
        self.tus_extensions = settings.ETIKET_TUS_EXTENSIONS
        self.tus_checksum_algorithms = settings.ETIKET_TUS_CHECKSUM_ALGORITHMS

    def options_upload(self):
        headers = {}
        headers["Tus-Resumable"] = self.tus_resumable
        headers["Tus-Version"] = ",".join(self.tus_versions)
        headers["Tus-Max-Size"] = self.tus_max_size
        headers["Tus-Min-Size-Partial"] = self.tus_min_size_partial
        headers["Tus-Extension"] = ",".join(self.tus_extensions)
        headers["Tus-Checksum-Algorithm"] = ",".join(self.tus_checksum_algorithms)

        return Response(status_code=status.HTTP_204_NO_CONTENT, headers=headers)

    async def start_upload(
        self,
        tus_resumable: str,
        upload_length: Optional[int],
        upload_metadata: str,
        content_length: int,
        content_type: Optional[str],
        upload_concat: Optional[str],
        upload_defer_length: Optional[int],
        upload_checksum: Optional[str],
        request,
        user,
        session,
    ):

        if tus_resumable != self.tus_resumable:
            raise UnsupportedTusVersionException

        if upload_defer_length:
            raise UnsupportedTusExtensionException("creation-defer-length")

        if upload_length:
            if upload_length > settings.ETIKET_MAX_FILE_SIZE:
                raise UploadLengthException(settings.ETIKET_MAX_FILE_SIZE)

        if content_length > 0:
            with_creation = True
            if content_type != "application/offset+octet-stream":
                raise ContentTypeException
            if upload_length is None:
                raise DeferUploadLengthException
            if content_length > upload_length:
                raise ContentLengthLargerThanUploadLengthException
        else:
            with_creation = False

        with_checksum, algorithm, checksum, filehash = self._parse_upload_checksum(
            upload_checksum
        )

        concat, concat_request, concat_uuids = self._parse_upload_concat(upload_concat)
        if (
            concat
            and concat_request == UploadConcat.final
            and upload_length is not None
        ):
            raise UploadLengthInFinalConcatHeaderException

        scope, file_uuid = self._parse_upload_metadata(upload_metadata)

        db_scope = get_scope_from_db_by_name(scope, session)

        if user not in db_scope.users:
            raise UserNotInScopeException(scope)

        db_file = get_file_from_db_by_scope_uuid(scope, file_uuid, session)

        if db_file.immutable and (
            db_file.status == FileStatus.available
            or db_file.status == FileStatus.secured
        ):
            raise FileIsImmutableException

        # check if file is available. Only allow for new version if file is secured
        if db_file.status == FileStatus.available:
            raise NewVersionFileForbiddenException

        # do not allow more than one upload if not partial
        for upload in db_file.uploads:
            if not upload.completed and (
                not upload.concat or not concat
            ):  # only allow additional partial upload for a file
                raise UploadStillInProgressException(upload.uuid)

        # concatenate files if partial uploads are complete
        if concat and concat_request == UploadConcat.final:
            for upload in db_file.uploads:
                # check if upload is complete
                if not upload.completed:
                    raise NotAllUploadsCompletedYetException
                if upload.uuid not in concat_uuids:
                    raise IncompleteConcatUUIDListException
            if len(db_file.uploads) != len(concat_uuids):
                raise IncompleteConcatUUIDListException
            db_file.location = self._construct_file_location(scope, file_uuid)
            with open(db_file.location, "wb") as dest:
                for upload_uuid in concat_uuids:
                    upload_part_location = self._construct_upload_location(
                        scope, file_uuid, upload_uuid
                    )
                    if os.path.exists(upload_part_location):
                        with open(upload_part_location, "rb") as source:
                            shutil.copyfileobj(source, dest)
                    else:
                        raise UploadGoneException
            for upload_uuid in concat_uuids:
                upload_part_location = self._construct_upload_location(
                    scope, file_uuid, upload_uuid
                )
                os.unlink(upload_part_location)
            upload_length = os.path.getsize(db_file.location)
            db_file.size = upload_length
            db_file.status = FileStatus.available
            db_file = commit_to_db(db_file, session)
            headers = {}
            headers["Upload-Length"] = str(upload_length)
            headers["Upload-Concat"] = upload_concat
            return Response(
                status_code=status.HTTP_201_CREATED,
                headers=headers,
            )

        if db_file.status == FileStatus.unavailable:
            db_file.status = FileStatus.pending
            db_file = commit_to_db(db_file, session)

        upload_uuid = uuid4()
        upload_location = self._construct_upload_location(scope, file_uuid, upload_uuid)
        db_upload = Upload(
            uuid=upload_uuid,
            length=upload_length,
            offset=0,
            location=upload_location,
            concat=concat,
            file_id=db_file.id,
        )

        async with aiofiles.open(upload_location, mode="wb+") as f:
            await f.write(b"\0")

        offset = 0
        if with_creation:
            offset = await self._write_chunk(
                upload_location, content_length, filehash, checksum, request
            )

        db_upload.offset = offset
        if offset == upload_length:
            db_upload.completed = True
            if not concat:
                db_file.location = self._construct_file_location(scope, file_uuid)
                shutil.move(db_upload.location, db_file.location)
                db_file.size = os.path.getsize(db_file.location)
                db_file.status = FileStatus.available
                db_file = commit_to_db(db_file, session)
        db_upload = commit_to_db(db_upload, session)

        headers = {}
        headers["Location"] = self._construct_relative_upload_uri(
            db_upload.uuid, request.url_for("start_upload")
        )
        headers["Tus-Resumable"] = tus_resumable
        headers["Upload-Offset"] = str(offset)

        return Response(
            status_code=status.HTTP_201_CREATED,
            headers=headers,
        )

    async def continue_upload(
        self,
        upload_uuid: UUID,
        tus_resumable: str,
        upload_offset: int,
        content_length: int,
        content_type: str,
        upload_checksum: Optional[str],
        request,
        user,
        session,
    ):

        if tus_resumable != self.tus_resumable:
            raise UnsupportedTusVersionException

        if content_type != "application/offset+octet-stream":
            raise ContentTypeException

        with_checksum, algorithm, checksum, filehash = self._parse_upload_checksum(
            upload_checksum
        )
        # probably will make this into a local file and lock the file
        db_upload = get_upload_from_db_by_uuid(upload_uuid, session)

        if upload_offset != db_upload.offset:
            raise UploadOffsetMismatchException

        if db_upload.completed:
            raise UploadAlreadyCompletedException

        if content_length + upload_offset > db_upload.length:
            raise ContentLengthLargerThanUploadLengthException

        scope = db_upload.file.scope
        db_scope = get_scope_from_db_by_name(scope, session)

        if user not in db_scope.users:
            raise UserNotInScopeException(scope)

        upload_location = db_upload.location

        offset = await self._write_chunk(
            upload_location,
            content_length,
            filehash,
            checksum,
            request,
            offset=upload_offset,
        )
        db_upload.offset = offset

        if offset == db_upload.length:
            db_upload.completed = True
            if not db_upload.concat:
                file_uuid = db_upload.file.uuid
                db_file = get_file_from_db_by_scope_uuid(scope, file_uuid, session)
                db_file.location = self._construct_file_location(scope, file_uuid)
                #change to aiofiles.os.rename?
                shutil.move(db_upload.location, db_file.location)
                db_file.size = os.path.getsize(db_file.location)
                db_file.status = FileStatus.available
                db_file = commit_to_db(db_file, session)
        db_upload = commit_to_db(db_upload, session)

        headers = {}
        headers["Tus-Resumable"] = "1.0.0"
        headers["Upload-Offset"] = str(offset)
        headers["Upload-Length"] = str(db_upload.length)

        return Response(status_code=status.HTTP_204_NO_CONTENT, headers=headers)

    async def terminate_upload(self, upload_uuid, current_user, session):
        db_upload = get_upload_from_db_by_uuid(upload_uuid, session)

        # below might not be necessary...but is more secure
        scope = db_upload.file.scope
        db_scope = get_scope_from_db_by_name(scope, session)
        if not current_user.admin:
            if current_user not in db_scope.users:
                raise UserNotInScopeException(scope)

        try:
            os.unlink(db_upload.location)
        except FileNotFoundError:
            pass

        try:
            session.delete(db_upload)
            session.commit()
        except:
            raise UploadTerminationFailedException

        headers = {}
        headers["Tus-Resumable"] = self.tus_resumable

        return Response(
            status_code=status.HTTP_204_NO_CONTENT,
            headers=headers,
        )

    async def status_upload(self, tus_resumable, upload_uuid, current_user, session):
        if tus_resumable != self.tus_resumable:
            raise UnsupportedTusVersionException

        # maybe simply store upload information in local meta file to minimize database action
        db_upload = get_upload_from_db_by_uuid(upload_uuid, session)

        headers = {}
        headers["Tus-Resumable"] = self.tus_resumable
        headers["Cache-Control"] = "no-store"
        headers["Upload-Offset"] = str(db_upload.offset)
        headers["Upload-Length"] = str(db_upload.length)

        return Response(status_code=status.HTTP_200_OK, headers=headers)

    async def _write_chunk(
        self, upload_location, content_length, filehash, checksum, request, offset=0
    ):
        try:
            added_length = 0
            async with aiofiles.open(upload_location, mode="r+b") as f:
                try:
                    if offset > 0:
                        await f.seek(offset)
                    async for chunk in request.stream():
                        disconnected = await request.is_disconnected()
                        if disconnected:
                            break
                        added_length += len(chunk)
                        if added_length > content_length:
                            added_length -= len(chunk)
                            break
                        if filehash:
                            filehash.update(chunk)
                        await f.write(chunk)
                except ClientDisconnect:
                    pass  # need to finish
            offset += added_length
            if filehash:
                if checksum != filehash.hexdigest():
                    raise ChecksumMismatchException
            return offset
        except Exception as e:
            raise UploadFailedException

    def _construct_file_location(self, scope, file_uuid):
        return f"{settings.ETIKET_FILESTORAGE_PATH}/{scope}::{file_uuid}"

    def _construct_relative_upload_uri(self, upload_uuid, upload_url):
        return f"{upload_url}{upload_uuid}"

    def _construct_upload_location(self, scope, file_uuid, upload_uuid):
        return f"{settings.ETIKET_UPLOADS_PATH}/{scope}::{file_uuid}.{upload_uuid}"

    def _parse_upload_checksum(self, upload_checksum):
        """
        Header should be of form:
        Upload-Checksum: md5 lkjlk09sdf09sdf09ds
        Upload-Checksum: sha1 090klsdf00fs0df
        """
        if upload_checksum is None:
            with_checksum = False
            algorithm = checksum = filehash = None
            return with_checksum, algorithm, checksum, filehash
        try:
            algorithm, checksum_encoded = upload_checksum.split()
        except KeyError:
            raise UploadChecksumHeaderException
        if algorithm not in ["sha1", "md5"]:
            raise UnsupportedChecksumAlgorithmException
        checksum = str(base64.b64decode(checksum_encoded).decode())
        filehash = hashlib.md5() if algorithm == "md5" else hashlib.sha1()
        with_checksum = True
        return with_checksum, algorithm, checksum, filehash

    def _parse_upload_concat(self, upload_concat):
        """
        Header upload_concat should be of form:
        Upload-Concat: partial
        Upload-Concat: final;/uploads/uuid1 /uploads/uuid2 ...
        """
        if upload_concat is None:
            concat = False
            concat_request = concat_uuids = None
            return concat, concat_request, concat_uuids
        upload_concat_split = upload_concat.split(";")
        if (
            upload_concat_split[0] == UploadConcat.partial
            and len(upload_concat_split) == 1
        ):
            concat_request = UploadConcat.partial
            concat_uuids = None
        elif upload_concat_split[0] == UploadConcat.final:
            concat_request = UploadConcat.final
            try:
                concat_uuids = [
                    UUID(x.split("/")[-1]) for x in upload_concat_split[1].split()
                ]
            except ValueError:
                raise UploadUUIDInConcatHeaderException
            except Exception as e:
                raise UploadConcatHeaderException
        else:
            raise UploadConcatHeaderException
        concat = True
        return concat, concat_request, concat_uuids

    def _parse_upload_metadata(self, upload_metadata):
        """
        Header should be of form:
        Upload-Metadata: scope str(base64.encode(scopename)),file_uuid str(base64.encode(file_uuid), ...
        """
        try:
            upload_metadata_dict = {
                x[0]: str(base64.b64decode(x[1]).decode())
                for x in [y.split() for y in upload_metadata.split(",")]
            }
        except Exception as e:
            raise UploadMetadataHeaderException

        scope = upload_metadata_dict.get("scope")  # validate that is needs to be
        if not scope:
            raise MissingScopeUploadMetadataHeaderException

        file_uuid = upload_metadata_dict.get("uuid")
        if not file_uuid:
            raise MissingFileUUIDUploadMetadataHeaderException
        try:
            file_uuid = UUID(file_uuid)
        except ValueError:
            raise InvalidFileUUIDUploadMetadataHeaderException

        return scope, file_uuid
