"""
ZLOGIN Module is for auto-login for Zerodha and storage of the access token to dynamoDB.
This works in conjunction with store_access module which creates a Lambda container handling re-direct url from zerodha
"""
import os
import sys
from datetime import datetime
from logging import getLogger, INFO, StreamHandler
import boto3
from kiteconnect import KiteConnect, KiteTicker

logger = getLogger("Zlogin")
logger.addHandler(StreamHandler(sys.stdout))
logger.setLevel(INFO)


def add_env_vars_from_file():
    """Read env vars stored in ~/.zerodha, basically ZAPI (zerodha api key)"""
    path = os.path.expanduser('~/.zerodha')
    with open(path, 'r', encoding='utf-8') as file:
        env_vars = dict(tuple(line.replace('\n', '').split('=')) for line
                        in file.readlines() if not line.startswith('#'))
    os.environ.update(env_vars)


def get_env_vars():
    """Get env vars of the setup - basically to get the Zerodha API key"""
    add_env_vars_from_file()
    return dict(
        api_key=os.getenv('ZAPI'),
        api_secret=os.getenv('ZSECRET'),
        api_auth=os.getenv('ZAPI_AUTH'),
        user_id=os.getenv('ZUSER'),
        pw=os.getenv('ZPASS'),
        totp_key=os.getenv('ZTOTP'),
    )


def fetch_access_token():
    """
    This function fetches access token either from Dynamodb - if the token exists for today - or generates request_token
    and passes to the Lambda function to get access_token and save to DynamoDB
    Args:
        None
    Requirements:
        A '.zerodha' file in the home directory with values for ZAPI, ZSECRET, ZAPI_AUTH, ZUSER, ZPASS, ZTOTP
        Sample in the repo
    """
    dynamodb = boto3.resource('dynamodb')
    access_store = dynamodb.Table('access_store')
    today = datetime.utcnow().date().strftime('%Y-%m-%d')
    date_rows = access_store.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key(
            'date').eq(today),
        ScanIndexForward=False
    )['Items']
    try:
        logger.info("Access Token Returned!")
        return date_rows[0]['access_token']
    except Exception as exp:
        logger.error(
            'Access token not generated - Neither does one exist for today')
        raise exp


def fetch_kiteconnect_instance():
    """Returns KiteConnect instance for further analysis"""
    access_token = fetch_access_token()
    return KiteConnect(get_env_vars()['api_key'], access_token)


def fetch_kiteticker_instance():
    """
    Returns a KiteTicker Object (WebSocket) - that can be used by defining:
        kws.on_ticks = on_ticks
        kws.on_connect = on_connect
        kws.on_close = on_close
    """
    access_token = fetch_access_token()
    return KiteTicker(get_env_vars()['api_key'], access_token)


if __name__ == "__main__":
    print(fetch_access_token())
    print(fetch_kiteconnect_instance())
    print(fetch_kiteticker_instance())
