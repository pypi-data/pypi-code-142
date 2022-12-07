import logging
import boto3
from botocore.exceptions import ClientError
import os
import random
import json

def login_valid(topicOfArn1, subjectToSend1, messageToSend1):
    topicOfArn = topicOfArn1
    subjectToSend = subjectToSend1
    messageToSend = messageToSend1
    AWS_REGION = 'us-east-1'
    sns_client = boto3.client('sns', region_name=AWS_REGION)
    response = sns_client.publish(
        TopicArn=topicOfArn,
        Message=messageToSend,
        Subject=subjectToSend,
        )['MessageId']
    print("Inside Lib")
    print(response)
    return "success"