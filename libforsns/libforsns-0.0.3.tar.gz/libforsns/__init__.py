import boto3

def subscribe(PROTOCOL, ENDPOINT):
    sns = boto3.client('sns', region_name='us-east-1')
    topic = 'arn:aws:sns:us-east-1:672168469627:Consultant-SNS-Topic'
    subscription = sns.subscribe(TopicArn=topic, Protocol=PROTOCOL, Endpoint=ENDPOINT, ReturnSubscriptionArn=True)
    return subscription
            
def publish(MESSAGE, SUBJECT):
    sns = boto3.client('sns', region_name='us-east-1')
    topic = 'arn:aws:sns:us-east-1:672168469627:Consultant-SNS-Topic'
    publish = sns.publish(TopicArn=topic, Message=MESSAGE, Subject=SUBJECT,)['MessageId']
    return publish
