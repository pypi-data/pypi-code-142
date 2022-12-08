import boto3

def snsemail(self):
    topic_arn = 'arn:aws:sns:us-east-1:124904646737:MySNS'
    message = 'This is a test message on topic.'
    subject = 'This is a message subject on topic.'
    
    AWS_REGION = 'us-east-1'
    sns_client = boto3.client('sns', region_name=AWS_REGION)
    response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject,
            )['MessageId']