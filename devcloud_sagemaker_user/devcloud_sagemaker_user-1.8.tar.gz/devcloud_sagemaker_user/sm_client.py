import uuid
import sys
import requests
import json
import enum
import zipfile
import tarfile
import os
from multiprocessing import  Process, Pool
import urllib.parse as path_encoder
import time
import datetime


HELLO_WORLD_MESSAGE = 'Hello world! PyOhio Demo - 3! CLEpy'

API_GW = "https://j3j738idh5.execute-api.cn-north-1.amazonaws.com.cn/api"

def login(username,password):
    headers = {
        'Content-Type': 'application/json'
    }
    
    account_info = {
        "username": username,
        "password": password,
    }
    payload = json.dumps(account_info)
    
    response = requests.request("POST", f"{API_GW}/login", headers=headers, data=payload)
    

    
    if json.loads(response.text)['Code'] == "InternalServerError":
        print("Incorrect Account or Password! Please login again!")
        return 0
    if json.loads(response.text)['Code'] == "201":
        print("Incorrect Password! Please login again!")
        return 0
    
    if json.loads(response.text)['Code']== "200":
        response_body = json.loads(response.text)
        print("\n login successfully \n your account info:",json.loads(response.text))
        
        #print(response_body)
        token = response_body["data"]["token"]        
        file = open('.token','w')
        print("\n token ‘.token’ recorded in current folder!!")
        file.write(token)
        file.close()
        return 1

def platform_charge_to_account(target_account_name,recharge_credits):
    headers = {
        'Content-Type': 'application/json'
    }

    file=open('.token','r')#read token from "token.txt"
    token=file.read()
# 进行充值操作前 需要登录拿到token
# token是平台账号intel登录生成的
    info = {
        "target_account_name": target_account_name,
        "token": token,
        "recharge_credits": recharge_credits,
    }   
    payload = json.dumps(info)
    #print(f"payload {payload}")
    response = requests.request("POST", f"{API_GW}/account/recharge", headers=headers, data=payload)
    response_body = json.loads(response.text)

    print("Account:",target_account_name,"has been charged",recharge_credits,"points!")

def query_device_list():
    url = f"{API_GW}/device/query"
    response = requests.request("GET", url)
    #print(response)

    response_body = json.loads(response.text)
    
    total_device =len(response_body['list'])
   
    for i in range(total_device):
        print(response_body['list'][i])
    #print(len(response_body['Items']))

def __upload_one_folder(task_id, type, dir_name: str):
    file_list = __list_files(dir_name)
    list_len = len(file_list)
    workers = 100
    worker_num = min(workers, 512)
    worker_num = 1 if list_len < workers else worker_num
    po = Pool(worker_num)
    for f in file_list:
        po.apply_async(func=__upload_one_file, args=(task_id, type, f))
    po.close()
    po.join()


def __list_files(dir_name):
    r = []
    subdirs = [x[0] for x in os.walk(dir_name)]
    for subdir in subdirs:
        files = os.walk(subdir).__next__()[2]
        if (len(files) > 0):
            for file in files:
                r.append(os.path.join(subdir, file))
    # print(r)
    return r



def __upload_one_file(task_id, type, object_name):
    # request a s3 presigned URL
    object_name_encoded = path_encoder.quote(object_name, safe="")  # by default / is recognized as safe
    url = f"{API_GW}/s3url/{task_id}/{type}/{object_name_encoded}"
    # print(f"getting {url}")
    response = requests.request("GET", url)
    # print(f"response {response}")
    response_body = json.loads(response.text)

    with open(object_name, 'rb') as f:
        files = {'file': (object_name, f)}
        http_response = requests.post(response_body['url'], data=response_body['fields'], files=files)
    # If successful, returns HTTP status code 204
    # print(f'File upload HTTP status code: {http_response.status_code}')


def submit_a_task(local_data, source_code, weights, hyper_param):
    devcloud_login()
    file = open('.token', 'r')  # read token from "token.txt"
    token = file.read()
    # create task id

    task_id = str(uuid.uuid4())
    print(f"task id is: {task_id}")

    # upload data and code to s3
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
    if local_data is not None:
        if local_data.startswith('s3://'):
            with open("s3_public_dataset.txt", 'w') as f:
                f.write(local_data)
            __upload_one_file(task_id, "Traindata", "s3_public_dataset.txt")
            print(f"use s3 public datasets  {local_data}")
        else:
            datasets_start_time = datetime.datetime.now()
            __upload_one_folder(task_id, "Traindata", local_data)
            datasets_end_time = datetime.datetime.now()
            print(f"uploaded {local_data}")
            print("datasets upload time: %s Seconds"%(datasets_end_time-datasets_start_time))

    if source_code is not None:
        code_start_time = datetime.datetime.now()
        __upload_one_file(task_id, "Code", source_code)
        code_end_time = datetime.datetime.now()
        print(f"uploaded {source_code}")
        print("code upload time: %s Seconds"%(code_end_time-code_start_time))

    if weights is not None:
        weights_start_time = datetime.datetime.now()
        __upload_one_file(task_id, "Weights", weights)
        weights_end_time = datetime.datetime.now()
        print(f"uploaded {weights}")
        print("weights upload time: %s Seconds"%(weights_end_time-weights_start_time))

    # put hyper param to Dynamodb through API Gateway
    headers = {
        'Content-Type': 'application/json'
    }
    hyper_param.update({"token": token, "task_id": task_id})
    payload = json.dumps(hyper_param)
    print(f"payload {payload}")
    response = requests.request("POST", f"{API_GW}/task/submit", headers=headers, data=payload)

    print(response)
    return task_id



def get_task_status(task_id):
    #task_id = "a403f523-79e8-4c31-919a-8cc6e7eb1748"    
    url = f"{API_GW}/task/status/{task_id}"
    response = requests.request("GET", url)

    response_body = json.loads(response.text)

    #print(response)
    print("Training Job status is:",response_body[task_id])
    response = requests.request("GET", url)
    response_body = json.loads(response.text)
    print("Training Job status now is:",response_body[task_id])

   
    return response_body[task_id]


# 打印task_id任务最近的n行
def query_task_log(task_id, n):
    log_url = f"{API_GW}/task/log/{task_id}"

    headers = {
        'Content-Type': 'application/json'
    }

    len_c = 0

    status_url = f"{API_GW}/task/status/{task_id}"
    response = requests.request("GET", status_url)
    response_body = json.loads(response.text)
    job_status = response_body[task_id]
    print(job_status)

    response = requests.request("POST", log_url, headers=headers)
    contents = json.loads(response.text)
    len_cc = len(contents)

    if len_cc > len_c and len_cc != 2:
        if len_cc > n:
            contents = contents[-n:len_cc]
            for content in contents:
                print(content['message'])
        else:
            contents = contents[len_c:len_cc]
            for content in contents:
                print(content['message'])
    else:
        print("Waiting log output, Please try it again in 10 seconds...")


def download_trained_model(task_id):
    #task_id = "a403f523-79e8-4c31-919a-8cc6e7eb1748"
    
    url = f"{API_GW}/trainedmodel/url/{task_id}"

    response = requests.request("GET", url)
    print(response)

    response_body = json.loads(response.text)

    print("Download trained model from:",response_body["url"])
    # 下载训练好的模型
    r = requests.get(response_body["url"])
    with open(r"./model.tar.gz", "wb") as f:
        f.write(r.content)
    f.close()
    print("Download completed!")


def query_task_info(task_id):
    url = f"{API_GW}/task/query/{task_id}"
    response = requests.request("GET", url)
    response_body = json.loads(response.text)
    print(response)
    print("Task Id:",task_id,"\nTask info:",response_body)

def query_account_info(account_name):
    #account_name = "yaru"
    url = f"{API_GW}/account/query/{account_name}"
    response = requests.request("GET", url)
    response_body = json.loads(response.text)
   # print(response)
    print("Query completed, account:",account_name,"info",response_body)


def cancel_task(task_id):
    url = f"{API_GW}/task/cancel/{task_id}"
    response = requests.request("GET", url)
    print(json.loads(response.text))
    print("Task",task_id," canceled",response)


def devcloud_login():
    envX = os.environ
    username = envX.get('JUPYTERHUB_USER')
    hostname = envX.get('HOSTNAME')
    if username and username.startswith("u") and hostname and hostname.endswith("devcloud-edge"):
        # 查询账号是否存在
        url = f"{API_GW}/account/is_exist/{username}"
        response = requests.request("GET", url)
        response_body = json.loads(response.text)
        if response_body["isexist"]:
            # 账户存在，登录账户
            headers = {
                'Content-Type': 'application/json'
            }
            account_info = {
                "username": username,
                "password": "intel123",
            }
            payload = json.dumps(account_info)

            response = requests.request("POST", f"{API_GW}/login", headers=headers, data=payload)
            response_body = json.loads(response.text)

            token = response_body["data"]["token"]
            file = open('.token', 'w')
            print("\n token ‘.token’ recorded in current folder!!")
            file.write(token)
            file.close()

            # 查询可用积分
            url = f"{API_GW}/account/query/{username}"
            response = requests.request("GET", url)
            response_body = json.loads(response.text)
            credits = response_body["credits"]

            print(username+" 登录成功, 账户可用积分: ", credits)
        else:
            # 账户不存在
            headers = {'Content-Type': 'application/json'}
            account_info = {
                "account_name": username,
                "account_email": username+"@intel.com",
                "account_password": "intel123",
                "account_type": 0,
                "corresponding_platform_name": "devcloud"
            }
            payload = json.dumps(account_info)
            # 创建username账号
            response = requests.request("POST", f"{API_GW}/account/create", headers=headers, data=payload)

            # devcloud账号给username充值20积分
            info = {
                "tag": "devcloud",
                "target_account_name": username,
            }
            payload = json.dumps(info)
            response = requests.request("POST", f"{API_GW}/account/recharge", headers=headers, data=payload)

            account_info = {
                "username": username,
                "password": "intel123",
            }
            payload = json.dumps(account_info)
            #username登录
            response = requests.request("POST", f"{API_GW}/login", headers=headers, data=payload)
            response_body = json.loads(response.text)
            token = response_body["data"]["token"]
            file = open('.token', 'w')
            print("\n token ‘.token’ recorded in current folder!!")
            file.write(token)
            file.close()
            print(username + " 创建登录成功, 账户可用积分: 20.0")


if __name__ == "__main__":
   	#create_account("platform_account","pa@intel.com","123","register_platform")#platform account
	#create_account("coresponding_platform_account_2","cpa_2@intel.com","123","platform_account")#realted platfrom account create
    	#create_account("abc","abc@132.com","password")#normal account  
   	#login("coresponding_platform_account_2","123")
    	#platform_charge_to_account("coresponding_platform_account_2",1)
	query_device_list()
	#submit_a_task("train.tar","mnist","ml.m5.xlarge","5")
        #get_task_status("bd15ebb6-a683-4b83-b2f9-3d8d36616a03")
   	#query_task_log("bd15ebb6-a683-4b83-b2f9-3d8d36616a03")
   	#download_trained_model("bd15ebb6-a683-4b83-b2f9-3d8d36616a03")
    	#platform_query_account("platform_account") #show accounts' info in "intel" platform
    	#query_task_info("bd15ebb6-a683-4b83-b2f9-3d8d36616a03")
   	#query_account_info("coresponding_platform_account_2")
	#update_account("test","intelpass","token_4","1234","666@intel.com")
 	#cancel_task("bd15ebb6-a683-4b83-b2f9-3d8d36616a03")



   
