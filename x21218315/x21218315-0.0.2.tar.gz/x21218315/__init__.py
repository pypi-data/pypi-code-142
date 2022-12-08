import boto3

def SNSpublish(TOPIC_arn):
    message = 'Task has been successfully added'
    subject = 'New task added'
    AWS_REGION = 'us-east-1'
    sns_client = boto3.client('sns', region_name=AWS_REGION)
    response = sns_client.publish(TopicArn=TOPIC_arn, Message=message,
                        Subject=subject,)['MessageId']