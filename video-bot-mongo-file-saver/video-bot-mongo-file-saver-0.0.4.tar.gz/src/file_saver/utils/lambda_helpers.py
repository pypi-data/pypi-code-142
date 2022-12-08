import json

def get_json(obj):
  return json.loads(
    json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
  )

def get_user(event):
  if 'headers' in event:
    if 'user' in event['headers']:
      return event['headers']['user']
    else:
      return ''
  else:
    return event['requestContext']['authorizer']['iam']['userId']      
  
def from_body(event):
  body = event['body']
  if (type(body).__name__ == 'str'):
    body = json.loads(body)
  return body  

def get_path_params(event):
  if 'pathParameters' in event:
    return event['pathParameters']

def get_route(event):
  if 'path' in event:
    return event['path']  
  else:  
    return event['requestContext']['http']['path']

  
def from_header(event):
  return event['headers']