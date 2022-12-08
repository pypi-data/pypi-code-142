from file_transfer.utils.lambda_helpers import *

class Request:
    
    def get_param(self, params, name):
        try:
            return params[name]
        except KeyError as err:
            raise (f'Information required on path: {err}')
        except Exception as general_error:
            raise(general_error)     

    def get_from_body(self, payload, name):
        try:
            return payload[name]    
        except KeyError as err:
            raise (f'Information required on body: {err}')
        except Exception as general_error:
            raise(general_error) 

    def get_event_type(self, event):
        if ('Records' in event):
            if (len(event['Records']) > 0):
                if (len(event['Records']) == 1):
                    return event['Records']['eventSource']
                else:   
                    return 'invalid - more than one record'
            else:
                return 'invalid - no records'
        else:
            return 'direct'            
    
    def get_request_direct_call(self, event):
        body = from_body(event)
        route = get_route(event)
        params = get_path_params(event)
        header = from_header(event)
        user = get_user(event)
        return {'body': body, 'route': route, 'params': params, 'header': header, 'user': user}

    def get_request_s3_call(self, event):
        body = from_body(event)
        route = get_route(event)
        params = get_path_params(event)
        header = from_header(event)
        user = get_user(event)
        return {'body': body, 'route': route, 'params': params, 'header': header, 'user': user}

    def get_request_sqs_call(self, event):
        body = from_body(event)
        route = get_route(event)
        params = get_path_params(event)
        header = from_header(event)
        user = get_user(event)
        return {'body': body, 'route': route, 'params': params, 'header': header, 'user': user}

    def __init__(self, event):

        event_type = self.get_event_type(event)

        if (event_type == 'direct'):
            request = self.get_request_direct_call(event)
        elif  (event_type == 'aws:s3'):  
            request = self.get_request_s3_call(event)
        elif (event_type == 'aws:sqs'):   
            request = self.get_request_sqs_call(event)
        else:
            raise Exception(f'Invalid event - {event_type}')       

        self.route = request['route']
        self.params = request['params']
        self.body = request['body']
        self.header = request['header']
        self.user = request['user']