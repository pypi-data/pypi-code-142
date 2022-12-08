
import requests


def alarm_list_api(SERVER_HOST,filter,order,page,size):

    res = requests.get(f"{SERVER_HOST}/alarm/list", json={"filter": filter,'order':order,'page':page, 'size':size}, verify=False).json()

    return res



def user_list_api(SERVER_HOST,creator):

    res = requests.get(f"{SERVER_HOST}/user/list", json={'creator' : creator},verify=False).json()

    return res
