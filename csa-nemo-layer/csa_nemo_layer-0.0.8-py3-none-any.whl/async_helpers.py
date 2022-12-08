from typing import Any
import aioboto3
from datetime import datetime, timedelta
from decimal import Decimal
import simplejson as json

from .constants import REGION_NAME, logger


async def get_secret(
    session: aioboto3.Session,
    secretId: str,
    region_name=REGION_NAME
) -> str:
    """Returns secret sctring from SecretsManager in region."""
    async with session.client(service_name="secretsmanager", region_name=region_name) as client:
        try:
            get_secret_value_response = await client.get_secret_value(
                SecretId=secretId
            )
        except Exception as e:
            raise e
    secret = get_secret_value_response['SecretString']

    return secret


def get_report_times(expire_days=3) -> dict[str, Any]:
    """Returns dict with human-readable reportTime and expireTime(POSIX) as a keys."""
    now = datetime.utcnow()
    return {
        'reportTime': now.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'expireTime': int((now + timedelta(days=expire_days)).timestamp())
    }


def serializeDDB(ddb_item: dict) -> dict:
    result = {}
    if type(ddb_item) is dict:
        for k, v in ddb_item.items():
            if type(v) is Decimal:
                try:
                    result[k] = int(v)
                except:
                    result[k] = str(v)
            elif type(v) is dict:
                result[k] = serializeDDB(v)
            else:
                result[k] = v
    return result


async def putDataToDDB(
    session: aioboto3.Session,
    tableName: str,
    data: list,
    add_time=True,
    expire_days=1
) -> bool:
    l = len(data)
    if l < 1:
        return False
    logger.info(f"putting {l} records to {tableName}")
    async with session.resource('dynamodb') as dynamo_resource:
        table = await dynamo_resource.Table(tableName)
        async with table.batch_writer() as batch:
            for item in data:
                if type(item) != dict:
                    try:
                        item = item.json()
                    except:
                        logger.error(
                            f"wrong type of item ({type(item)}. Skipped)")
                        logger.debug(f"errored item: {item}")
                        continue
                if add_time:
                    times = get_report_times(expire_days=expire_days)
                    item['expireTime'] = times['expireTime']
                    item['reportTime'] = times['reportTime']
                try:
                    await batch.put_item(Item=item)
                except Exception as e:
                    logger.error(
                        f"error while putting {item} to {tableName}: {e}")
    return True


async def scanDataFromDDB(
    session: aioboto3.Session,
    tableName: str,
    scan_kwargs: dict = {},
    region_name=REGION_NAME
) -> list[dict]:
    logger.info(f"scan data from {tableName}: {scan_kwargs}")
    async with session.resource('dynamodb', region_name=region_name) as dynamo_resource:
        table = await dynamo_resource.Table(tableName)
        data = await table.scan(**scan_kwargs)
        items = data['Items']
        while data.get('LastEvaluatedKey'):
            scan_kwargs['ExclusiveStartKey'] = data['LastEvaluatedKey']
            data = await table.scan(**scan_kwargs)
            items.extend(data['Items'])
    return items


async def queryDataFromDDB(
    session: aioboto3.Session,
    tableName: str,
    query_kwargs: dict = {},
    region_name=REGION_NAME
) -> list[dict]:
    logger.debug(f"query data from {tableName}: {query_kwargs}")
    async with session.resource('dynamodb', region_name=region_name) as dynamo_resource:
        table = await dynamo_resource.Table(tableName)
        data = await table.query(**query_kwargs)
        items = data['Items']
        while data.get('LastEvaluatedKey'):
            query_kwargs['ExclusiveStartKey'] = data['LastEvaluatedKey']
            data = await table.query(**query_kwargs)
            items.extend(data['Items'])
    return items


async def getItemFromDDB(
    session: aioboto3.Session,
    tableName: str,
    get_kwargs: dict = {},
    region_name=REGION_NAME
) -> dict:
    """Gets item from DDB table. For main index get kwargs would be {'Key':<key_index>}"""
    logger.debug(f"get item from {tableName}: {get_kwargs}")
    async with session.resource('dynamodb', region_name=region_name) as dynamo_resource:
        table = await dynamo_resource.Table(tableName)
        data = await table.get_item(**get_kwargs)
        item = data['Item']
    return item


async def loadJSONFromS3(
    session: aioboto3.Session,
    bucket: str,
    key: str
) -> dict:
    result = {}
    async with session.client("s3") as s3_client:
        try:
            s3_ob = await s3_client.get_object(Bucket=bucket, Key=key)
            async with s3_ob["Body"] as stream:
                file_data = await stream.read()
            result = json.loads(file_data.decode('utf-8'))
        except Exception as e:
            if e.response['Error']['Code'] == 'NoSuchKey':  # type: ignore
                logger.warning(f"No object {key} found - returning empty")
            else:
                logger.error(
                    f"Error reading {key} from {bucket}: {e}")
    return result


async def listS3Objects(
    session: aioboto3.Session,
    bucket: str,
    prefix=""
) -> list:
    objects = []
    async with session.resource("s3") as s3:

        s3_bucket = await s3.Bucket(bucket)
        if len(prefix) == 0:
            async for s3_object in s3_bucket.objects.all():
                objects.append(s3_object)
        else:
            async for s3_object in s3_bucket.objects.filter(Prefix=prefix):
                objects.append(s3_object)
    return objects


async def putJsonToS3(
    session: aioboto3.Session,
    bucket: str,
    key: str,
    json_object: dict
) -> dict:
    result = {}
    async with session.client("s3") as s3_client:
        try:
            body = json.dumps(json_object)
            result = await s3_client.put_object(
                Body=body,
                Bucket=bucket,
                Key=key
            )
        except Exception as e:
            logger.error(
                f"Error putting {key} to {bucket}: {e}")
    return result


async def getObjectFromS3(
    session: aioboto3.Session,
    bucket_name: str,
    key: str
):
    async with session.client("s3") as s3:
        s3_ob = await s3.get_object(Bucket=bucket_name, Key=key)
        async with s3_ob["Body"] as body:
            content = await body.read()
    return content
