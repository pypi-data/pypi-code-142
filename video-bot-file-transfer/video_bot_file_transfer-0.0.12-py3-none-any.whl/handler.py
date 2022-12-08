from file_transfer.utils.lambda_helpers  import * 
from file_transfer.models.request import Request
from file_transfer.factories.factory import Factory

def handler(event, context):

    request = Request(event)
    factory = Factory(request)
    controller = factory.make_controller()
    result = controller.handle()

    json_str = get_json(result)
    
    print(json_str)
    
    return json_str