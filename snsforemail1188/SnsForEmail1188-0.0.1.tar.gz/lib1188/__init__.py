import boto3

def subscribe(protocol, endpoint):
    sns = boto3.client('sns', region_name='us-east-1')
    topic = 'arn:aws:sns:us-east-1:672168469627:Consultant-SNS-Topic'
    subscription = sns.subscribe(TopicArn=topic, Protocol=protocol, Endpoint=endpoint, ReturnSubscriptionArn=True)
    return subscription
            
def publish(self, message, subject):
    sns = boto3.client('sns', region_name='us-east-1')
    topic = 'arn:aws:sns:us-east-1:672168469627:Consultant-SNS-Topic'
    publish = sns.publish(TopicArn=topic, Message=message, Subject=subject,)['MessageId']
    return publish