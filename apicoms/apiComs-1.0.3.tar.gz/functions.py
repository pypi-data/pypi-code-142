import requests, json


def get_api(endpoint, header):
    """please pass headers as {} if no headers"""
    response = requests.get(url=endpoint, headers=header, verify=False)
    return response      


def post_api(endpoint, request_payload, header):
    """Please specify the parameters in the following order. endpoint, request and header"""
    if type(request_payload) == str:
        request = request_payload
    else:
        request = json.dumps(request_payload)        
    response = requests.post(url=endpoint, data=request, headers=header, verify=False)
    return response


def put_api(endpoint, request_payload, header):
    """Please specify the parameters in the following order. endpoint, request and header"""
    if type(request_payload) == str:
        request = request_payload
    else:
        request = json.dumps(request_payload)
    response = requests.put(url=endpoint, data=request, headers=header, verify=False)
    return response


def patch_api(endpoint, request_payload, header):
    """Please specify the parameters in the following order. endpoint, request and header"""
    if type(request_payload) == str:
        request = request_payload
    else:
        request = json.dumps(request_payload)
    response = requests.put(url=endpoint, data=request, headers=header, verify=False)
    return response


def delete_api(endpoint, request_payload, header):
    """Please specify the parameters in the following order. endpoint, request and header"""
    if type(request_payload) == str:
        request = request_payload
    else:
        request = json.dumps(request_payload)
    response = requests.delete(url=endpoint, params=request, headers=header, verify=False)
    return response
