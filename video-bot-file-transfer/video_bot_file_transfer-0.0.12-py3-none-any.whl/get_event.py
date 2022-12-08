
from file_transfer.utils.json import from_json

def get_event():

        event = from_json('event_call.json')
        #event = from_json('event_s3.json')
        #event = from_json('event_sqs.json')
        return event
