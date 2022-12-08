import os

from aws_lambda_powertools import Logger

logger = Logger()
logger.remove_keys(keys=['service'])

REGION_NAME = os.getenv("AWS_REGION", 'eu-west-1')
