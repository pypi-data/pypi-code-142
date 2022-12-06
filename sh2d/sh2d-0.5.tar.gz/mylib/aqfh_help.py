#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import base64
import requests
import ddddocr
import hashlib
import random
from requests.adapters import HTTPAdapter
requests.packages.urllib3.disable_warnings()
# 添加自动重试
requests = requests.Session()
requests.mount('http://', HTTPAdapter(max_retries=3))
requests.mount('https://', HTTPAdapter(max_retries=3))


class AQFHClient:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.headers = {
            "Referer": url,
            "Accept": "application/json, text/plain, */*",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.38 (KHTML, like Gecko) Chrome/105.0.5195.54 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.91"
        }
        self.data = {}

    def connect(self, method, resource, data=None):

        r = getattr(requests, method.lower())('{0}{1}'.format(
            self.url, resource), json=data, headers=self.headers, verify=False, allow_redirects=False)
        r.encoding = r.apparent_encoding
        time.sleep(random.randint(10,30)/10)
        print('[{}]'.format(r.status_code), method, resource)
        if r.status_code == 200:
            try:
                return r.status_code, r.json()
            except:
                return r.status_code, r.text
        else:
            self.connect(method, resource, data)
    # 自动登录

    def login(self):
        '''自动登录'''
        _, rj1 = self.connect('GET', '/api/api/code')
        ocr = ddddocr.DdddOcr(show_ad=False)
        code = ocr.classification(base64.b64decode(
            rj1['data']['img'].replace('data:image/png;base64,', '')))
        data = {"account": self.username, "password": hashlib.new('sha1', self.password.encode(
            'utf-8')).hexdigest(), "code": code, "key": rj1['data']['key']}
        _, rj2 = self.connect('POST', '/api/api/login', data)
        if rj2['message'] == "Success":
            self.headers['Authorization'] = 'Bearer {}'.format(
                rj2['data']['access_token'])
            print('[+] 登录成功')
            return True
        elif rj2['message'] == "验证码有误":
            print('[*] 验证码有误,重试中')
            self.login()
        else:
            print('[-] 登录失败,', rj2['message'])
            return False
    # 定级对象列表

    def getObjectList(self, name="", neteid="", rank=[], status=[], creator_name=""):
        '''定级对象列表'''
        page = 1
        while True:
            data = {"name": name, "neteid": neteid, "rank": rank, "status": status, "time": "", "reviewer_name": "", "review_status": "", "apply_back_status": "",
                    "creator_name": creator_name, "company_name": "", "updated_at": "", "comment_time_start": "", "comment_time_end": "", "page": page, "companytype": "3"}
            _, rj = self.connect('POST', '/api/api/getObjectList', data)
            for item in rj['data']['data']:
                _id = item['id']
                self.data.setdefault('ObjectList', {})
                self.data['ObjectList'][_id] = item
            print('[+] 当前第{}页，系统数为：{}'.format(page, rj['data']['total']))
            if page * 10 > rj['data']['total']:
                break
            page += 1
    # 定级对象信息

    def getObjectInfo(self, _id):
        '''定级对象信息'''
        data = {"id": _id, "companytype": "3"}
        _, rj = self.connect('POST', '/api/api/getObjectInfo', data)
        self.data['ObjectList'][_id]['ObjectInfo'] = rj['data']
    # 符合性评测

    def getObjectAttachmentReviewProve(self, _id):
        '''符合性评测'''
        data = {"id": _id}
        _, rj = self.connect(
            'POST', '/api/api/getObjectAttachmentReviewProve', data)
        self.data['ObjectList'][_id]['ObjectAttachmentReviewProve'] = rj['data']
    # 符合性评测表

    def getTitleList(self, _id, nete_id):
        '''符合性评测表'''
        data = {"id": _id, "neteid": nete_id, "companytype": "3"}
        _, rj = self.connect(
            'POST', '/api/api/getTitleList', data)
        self.data['ObjectList'][_id]['TitleList'] = rj['data']
    # 风险评估

    def getObjectAttachmentRisk(self, _id):
        '''风险评估'''
        data = {"id": _id}
        _, rj = self.connect(
            'POST', '/api/api/reviewGetObjectAttachmentRisk', data)
        self.data['ObjectList'][_id]['ObjectAttachmentRisk'] = rj['data']
    # IP列表

    def getIpList(self, _id):
        '''IP列表'''
        page = 1
        while True:
            data = {"id": _id, "current_page": 1, "per_page": 10}
            _, rj = self.connect('POST', '/api/api/getIpList', data=data)
            self.data['ObjectList'][_id].setdefault('IpList', [])
            self.data['ObjectList'][_id]['IpList'] += rj['data']['data']
            if page*10 > rj['data']['total']:
                break
            page += 1
    # 用户id列表

    def getAllAssistant(self):
        '''用户id列表'''
        _, rj = self.connect('POST', '/api/api/getAllAssistant')
        self.data['AllAssistant'] = rj['data']
    # 网络id列表

    def getNetType(self):
        '''网络id列表'''
        _, rj = self.connect('GET', '/api/api/common/getNetType')
        self.data['NetType'] = rj['data']
    # 统计

    def getcountObject(self):
        '''统计'''
        _, rj = self.connect('POST', '/api/api/countObject')
        self.data['countObject'] = rj['data']
    # 导出对象下载地址

    def getexportObjectURL(self):
        '''导出对象下载地址'''
        data = {"apply_back_status": "", "comment_time_end": "", "comment_time_start": "", "company_name": "", "companytype": "3", "creator_name": "", "expire_status": "",
                "name": "", "neteid": "", "page": 1, "public_ip": "", "rank": [], "review_status": [], "reviewer_name": "", "software_ip": "", "status": [], "time": "", "updated_at": ""}
        _, rj = self.connect('POST', '/api/api/exportObjectList', data=data)
        self.data['exportObjectURL'] = rj['data']['url']
    # 下载文件

    def download(self, path, url):
        '''下载文件'''
        print('[+] download', path)
        with open(path, 'wb') as f:
            f.write(requests.get(url, headers=self.headers,
                    verify=False, allow_redirects=False).content)