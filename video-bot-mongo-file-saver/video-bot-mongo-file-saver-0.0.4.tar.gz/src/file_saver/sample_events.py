from aws_lambda_sample_events import SampleEvent

def generate_event(service_name):
    event = SampleEvent(service_name)
    return event