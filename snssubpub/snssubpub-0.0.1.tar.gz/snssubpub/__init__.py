import boto3

def subscribe(PROTOCOL, ENDPOINT):
    sns = boto3.client('sns', region_name='us-east-1')
    topic = 'arn:aws:sns:us-east-1:637877259020:Consultant-Topic'
    subscription = sns.subscribe(TopicArn=topic, Protocol=PROTOCOL, Endpoint=ENDPOINT, ReturnSubscriptionArn=True)
    return subscription
            
def publish(MESSAGE, SUBJECT):
    sns = boto3.client('sns', region_name='us-east-1')
    topic = 'arn:aws:sns:us-east-1:637877259020:Consultant-Topic'
    publish = sns.publish(TopicArn=topic, Message=MESSAGE, Subject=SUBJECT,)['MessageId']
    return publish