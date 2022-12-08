from typing import Any
import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta
from decimal import Decimal

from .constants import REGION_NAME, logger


def get_secret(session: boto3.Session, secretId: str, regionName=REGION_NAME) -> str:
    """Returns secret string from SecretsManager in region."""
    client = session.client(
        service_name="secretsmanager",
        region_name=regionName
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secretId
        )
    except ClientError as e:
        raise e
    secret = get_secret_value_response['SecretString']

    return secret


def get_report_times(expire_days=1) -> dict[str, Any]:
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


def putDataToDB(
    session: boto3.Session,
    tableName: str,
    data: list[Any],
    add_time=True,
    expire_days=1
) -> bool:
    ddb_resource = session.resource('dynamodb')
    table = ddb_resource.Table(tableName)  # type: ignore
    logger.info(f"putting {len(data)} objects to {tableName}")
    with table.batch_writer() as batch:
        for item in data:
            if type(item) != dict:
                try:
                    item = item.json()
                except:
                    logger.error(f"wrong type of item ({type(item)}. Skipped)")
                    logger.debug(f"errored item: {item}")
                    continue
            if add_time:
                times = get_report_times(expire_days=expire_days)
                item['expireTime'] = times['expireTime']
                item['reportTime'] = times['reportTime']
            batch.put_item(Item=item)
    return True


def scanDataFromDDB(
    session: boto3.Session,
    tableName: str,
    scan_kwargs: dict = {}
) -> list[dict]:
    logger.info(f"scan data from {tableName}: {scan_kwargs}")
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table(tableName)  # type: ignore
    data = table.scan(**scan_kwargs)
    items = data['Items']
    while data.get('LastEvaluatedKey'):
        scan_kwargs['ExclusiveStartKey'] = data['LastEvaluatedKey']
        data = table.scan(**scan_kwargs)
        items.extend(data['Items'])
    return items
