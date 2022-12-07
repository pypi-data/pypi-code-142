import asyncio
import logging
import os
import shutil
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import boto3
import hashlib
import aiofiles
import aiofiles.os as aios
from aiobotocore.session import get_session as get_aioboto_session

from etiket.app.crud.db import get_session
from etiket.app.models import File
from etiket.core.config import settings
from etiket.core.s3utils import get_s3_key
from etiket.core.types import FileStatus


logger = logging.getLogger(__name__)
logging.basicConfig(filename='secure_files.log', encoding='utf-8',level=logging.INFO)
logging.getLogger('apscheduler').setLevel(logging.WARNING)
logging.getLogger('botocore').setLevel(logging.WARNING)
logging.getLogger('aiobotocore').setLevel(logging.WARNING)


async def calculate_etag_file(file_entry):
    filehash = hashlib.md5()
    try:
        async with aiofiles.open(file_entry.path, mode="rb") as f:
            chunksize = settings.ETIKET_CHUNK_SIZE
            while chunk:= await f.read(chunksize):
                filehash.update(chunk)
        return filehash.hexdigest()
    except Exception as e:
        logger.error(e)
        logger.error(f"Something went wrong while calculating ETag {file_entry.path}")
        return None


def copy_file_to_s3(file_entry, file_dict):
    bucket = settings.S3_BUCKET
    scope = file_dict.get('scope')
    file_uuid = file_dict.get('uuid')
    key = get_s3_key(scope,file_uuid)
    session = boto3.Session(profile_name = 'default')
    client = session.client(
            "s3",
            endpoint_url=settings.S3_ENDPOINT,
            use_ssl=True,
            verify=True
            )
    try:
        client.upload_file(
                file_entry.path,
                bucket,
                key,
                ExtraArgs = {
                    "Metadata": file_dict
                    }
                )
    except ClientError as e:
        logging.error(e)
        return False
    return True


async def remove_local_copy_file(file_entry,file_dict):
    bucket = settings.S3_BUCKET
    scope = file_dict.get('scope')
    file_uuid = file_dict.get('uuid')
    key = get_s3_key(scope,file_uuid)
    session = get_aioboto_session()
    async with session.create_client(
            "s3",
            endpoint_url=settings.S3_ENDPOINT,
            use_ssl=True,
            verify=True,
            ) as s3:
        try:
            s3_object = await s3.head_object(Bucket=bucket,Key=key)
            s3_size = int(s3_object['ContentLength'])
            if s3_size != int(file_dict['size']):
                logger.warning(f"File size in db {file_dict['size']} does not correspond to S3 object {s3_size}")
                return False
            etag = s3_object['Metadata']['etag']
            if etag != file_dict['etag']:
                logger.warning(f"ETag in db {file_dict['etag']} does not correspond to S3 object ETag {etag}")
                return False
        except ClientError as e:
            logging.error(e)
            return False
    try:
        await aios.remove(file_entry.path)
    except Exception as e:
        logging.error(e)
        return False


async def secure_file(queue, session = get_session):
    while True:
        file_entry = await queue.get()
        filename = os.path.basename(file_entry.path)
        scope, file_uuid = filename.split('::')
        try:
            db_file = get_file_from_db_by_scope_uuid(scope, file_uuid, session)
        except:
            logger.error(f"Could not get file from db")
            queue.task_done()
        etag = await calculate_etag_file(file_entry)
        if etag is None:
            logger.error(f"ETag {file_entry.path} was None")
            queue.task_done()
        try:
            db_file.etag = etag
            db_file = commit_to_db(db_file, session)
            file_dict=db_file.dict()
        except:
            logger.error(f"Could not commit etag to file {scope}/{file_uuid} to db")
            queue.task_done()
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, copy_file_to_s3, file_entry, file_dict)
        try:
            db_file.s3_bucket = settings.S3_BUCKET
            db_file.s3_key = get_s3_key(scope,file_uuid)
            db_file.status = FileStatus.secured
            db_file = commit_to_db(db_file, session)
            file_dict=db_file.dict()
        except:
            logger.error(f"Could not commit s3 location to file {scope}/{file_uuid} to db")
            queue.task_done()
        await remove_local_copy_file(file_entry,file_dict)
        logger.info(f"Secured {file_entry.path}: {scope} {file_uuid} {etag}")
        queue.task_done()


def scantree(path):
    """Recursively yield DirEntry objects for files storage path."""
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)
        else:
            yield entry


class SecureFilesFlow:
    async def scan_files(self):
        for entry in scantree(settings.ETIKET_FILESTORAGE_PATH):
            logger.info(f"Queueing {entry.path}")
            self.queue.put_nowait(entry)
        tasks = []
        for i in range(3):
            task = asyncio.create_task(secure_file(self.queue))
            tasks.append(task)
        await self.queue.join()
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)

    def start(self):
        self.queue = asyncio.Queue()
        self.sch = AsyncIOScheduler()
        self.sch.start()
        self.sch.add_job(self.scan_files, 'interval', seconds=4, max_instances=1)
    

if __name__ == '__main__':
    flow = SecureFilesFlow()
    flow.start()
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass


